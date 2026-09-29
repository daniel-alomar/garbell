#!/usr/bin/env python3
"""Read-only inventory/link checks and explicit acceptance of completed sources."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile


def digest(path):
    before = path.stat()
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    after = path.stat()
    if (before.st_size, before.st_mtime_ns, before.st_ino) != (
            after.st_size, after.st_mtime_ns, after.st_ino):
        raise ValueError(f'Fitxer canviant durant la lectura: {path}')
    return h.hexdigest()


def safe(root, rel, area):
    p = Path(rel)
    if p.is_absolute() or '..' in p.parts or not p.parts or p.parts[0] != area:
        raise ValueError(f'Camí fora de {area}: {rel}')
    candidate = root / p
    if any(part.is_symlink() for part in [candidate, *candidate.parents] if part != root.parent):
        raise ValueError(f'Enllaç simbòlic no admès: {rel}')
    candidate.resolve().relative_to(root)
    return candidate


def files(root, area):
    base = safe(root, area, area)
    for folder, dirs, names in os.walk(base, followlinks=False):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.') and not (Path(folder) / d).is_symlink())
        for name in sorted(names):
            p = Path(folder) / name
            if not name.startswith('.') and not p.is_symlink() and p.is_file():
                yield p


def state_path(root):
    safe(root, '.wiki', '.wiki')
    return safe(root, '.wiki/state.json', '.wiki')


def read_state(root):
    p = state_path(root)
    data = json.loads(p.read_text()) if p.exists() else {'version': 1, 'sources': {}, 'outputs': {}}
    if data.get('version') != 1 or not isinstance(data.get('sources'), dict) or not isinstance(data.get('outputs'), dict):
        raise ValueError('Inventari invàlid; no se sobreescriurà.')
    return data


def scan(root):
    state = read_state(root)
    current, errors = {}, []
    for p in files(root, 'raw'):
        rel = p.relative_to(root).as_posix()
        try:
            current[rel] = digest(p)
        except (OSError, ValueError) as e:
            errors.append({'path': rel, 'error': str(e)})
    old = state['sources']
    failed = {e['path'] for e in errors}
    groups = defaultdict(list)
    for rel, sha in current.items():
        groups[sha].append(rel)
    changed_outputs, missing_outputs = [], []
    for rel, sha in state['outputs'].items():
        p = safe(root, rel, 'wiki')
        if not p.exists():
            missing_outputs.append(rel)
        elif digest(p) != sha:
            changed_outputs.append(rel)
    affected = set(changed_outputs + missing_outputs)
    return {
        'new': {p: h for p, h in current.items() if p not in old},
        'modified': {p: h for p, h in current.items() if p in old and old[p]['sha256'] != h},
        'missing': sorted(set(old) - set(current) - failed),
        'unchanged': sum(p in old and old[p]['sha256'] == h for p, h in current.items()),
        'duplicates': [paths for paths in groups.values() if len(paths) > 1],
        'possible_renames': [{'old': p, 'new': groups[entry['sha256']]} for p, entry in old.items()
                             if p not in current and p not in failed and entry['sha256'] in groups],
        'locally_modified_notes': changed_outputs,
        'missing_notes': missing_outputs,
        'sources_with_affected_notes': [p for p, e in old.items() if affected.intersection(e['outputs'])],
        'errors': errors,
    }


def links(root):
    targets = defaultdict(set)
    for area in ('wiki', 'raw', 'notes-personals'):
        for p in files(root, area):
            rel = p.relative_to(root).as_posix()
            for key in (rel, p.name):
                targets[key].add(rel)
            if p.suffix.lower() == '.md':
                targets[rel[:-3]].add(rel)
                targets[p.stem].add(rel)
    issues, total = [], 0
    for p in files(root, 'wiki'):
        if p.suffix.lower() != '.md':
            continue
        body = p.read_text(encoding='utf-8')
        body = re.sub(r'\A---\s*\n.*?\n---\s*\n', '', body, flags=re.S)
        body = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', body, flags=re.S | re.M)
        body = re.sub(r'`[^`\n]*`', '', body)
        for match in re.finditer(r'\[\[([^\]\n]+)\]\]', body):
            target = match.group(1).split('|')[0].split('#')[0].strip()
            if not target:
                continue
            total += 1
            found = targets.get(target, set())
            if len(found) != 1:
                issues.append({'note': p.relative_to(root).as_posix(), 'target': target,
                               'reason': 'missing' if not found else 'ambiguous'})
    return {'checked_links': total, 'issues': issues, 'anchors_checked': False}


def accept(root, source, sha, outputs):
    if not re.fullmatch('[a-f0-9]{64}', sha):
        raise ValueError('Cal una empremta SHA-256 real de la font llegida.')
    source_file = safe(root, source, 'raw')
    if digest(source_file) != sha:
        raise ValueError('La font ha canviat; torna-la a llegir abans d’acceptar.')
    hashes = {}
    for rel in outputs:
        p = safe(root, rel, 'wiki')
        if p.suffix != '.md' or not p.is_file():
            raise ValueError(f'Nota Markdown inexistent: {rel}')
        hashes[rel] = digest(p)
    if not any(p.startswith('wiki/fonts/') for p in outputs):
        raise ValueError('Cal almenys una fitxa a wiki/fonts/.')
    path = state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = safe(root, '.wiki/state.lock', '.wiki')
    with lock.open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        data = read_state(root)
        data['sources'][source] = {'sha256': sha, 'outputs': sorted(set(outputs)),
                                  'accepted_at': datetime.now(timezone.utc).isoformat()}
        data['outputs'].update(hashes)
        fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='state-', suffix='.tmp')
        try:
            with os.fdopen(fd, 'w') as stream:
                json.dump(data, stream, ensure_ascii=False, indent=2)
                stream.write('\n')
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(tmp, path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
    return {'accepted': source, 'outputs': sorted(hashes)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['scan', 'links', 'accept'])
    parser.add_argument('vault', type=Path)
    parser.add_argument('--source')
    parser.add_argument('--sha256')
    parser.add_argument('--outputs', nargs='+')
    args = parser.parse_args()
    root = args.vault.resolve()
    if not root.is_dir() or not (root / 'raw').is_dir() or not (root / 'wiki').is_dir():
        parser.error('La volta ha de contenir raw/ i wiki/.')
    try:
        if args.command == 'accept':
            if not all((args.source, args.sha256, args.outputs)):
                parser.error('accept necessita --source, --sha256 i --outputs')
            result = accept(root, args.source, args.sha256, args.outputs)
        else:
            result = scan(root) if args.command == 'scan' else links(root)
    except (OSError, ValueError, KeyError, TypeError) as e:
        parser.exit(2, f'Error: {e}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get('issues') or result.get('errors') else 0


if __name__ == '__main__':
    raise SystemExit(main())

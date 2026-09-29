#!/usr/bin/env python3
"""Build a self-contained package; examples can be omitted entirely."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
ROOT = Path(__file__).resolve().parents[1]
NAME = next((ROOT/'skills').iterdir()).name
ALLOWED = {'README.md','AGENTS.md','.gitignore','skills','context','agents','scripts','tests','examples'}

def manifest(root=ROOT, examples=True):
    data = {}
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if rel.parts[0] not in ALLOWED or (not examples and rel.parts[0]=='examples'):
            continue
        if rel.as_posix() != '.gitignore' and any(x.startswith('.') or x=='__pycache__' for x in rel.parts):
            continue
        if p.is_symlink() or any(q.is_symlink() for q in p.parents):
            raise ValueError(f'Symlink excluded: {p}')
        if p.is_file() and (p.suffix in {'.md','.py','.yaml','.toml'} or rel.as_posix()=='.gitignore'):
            data[rel.as_posix()] = p.read_text(encoding='utf-8')
    return data

def build(examples=True):
    data = manifest(examples=examples)
    out = ROOT/'dist'
    out.mkdir(exist_ok=True)
    suffix = '' if examples else '-without-examples'
    (out/f'{NAME}{suffix}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with ZipFile(out/f'{NAME}{suffix}.zip','w',ZIP_DEFLATED) as archive:
        for rel,content in data.items():
            archive.writestr(f'{NAME}/{rel}',content)
    print(f'{NAME}: {len(data)} files; {out}')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--without-examples',action='store_true')
    args=parser.parse_args()
    build(not args.without_examples)

import hashlib
import json
import importlib.util
from pathlib import Path
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    spec=importlib.util.spec_from_file_location(path.stem,path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
STATE=load(ROOT/'skills/garbell/scripts/vault_state.py')
DIST=load(ROOT/'scripts/distribute.py')
class ProjectTests(unittest.TestCase):
    def test_incremental_and_human_edits(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d); (r/'raw').mkdir(); (r/'wiki/fonts').mkdir(parents=True)
            src=r/'raw/demo.md'; src.write_text('Fictici')
            note=r/'wiki/fonts/demo.md'; note.write_text('[[raw/demo]]')
            sha=hashlib.sha256(src.read_bytes()).hexdigest()
            self.assertIn('raw/demo.md',STATE.scan(r)['new'])
            STATE.accept(r,'raw/demo.md',sha,['wiki/fonts/demo.md'])
            self.assertEqual(STATE.scan(r)['unchanged'],1)
            note.write_text('Edicio humana [[raw/demo]]')
            self.assertTrue(STATE.scan(r)['locally_modified_notes'])
            src.write_text('Canvi')
            with self.assertRaises(ValueError):STATE.accept(r,'raw/demo.md',sha,['wiki/fonts/demo.md'])
    def test_examples_links(self):
        example=ROOT/'examples/demo'
        if not example.exists(): self.skipTest('Exemples opcionals eliminats')
        self.assertEqual(STATE.links(example)['issues'],[])
    def test_demo_graph_only_configuration_distributed(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)
            graph='examples/demo/.obsidian/graph.json'
            for path in (graph, 'examples/demo/.obsidian/workspace.json',
                         'examples/demo/.obsidian/plugins/private/data.json',
                         'examples/other/.obsidian/graph.json'):
                f=r/path; f.parent.mkdir(parents=True,exist_ok=True); f.write_text('{}')
            self.assertEqual(set(DIST.manifest(r)), {graph})
            self.assertEqual(DIST.manifest(r, examples=False), {})
        example=ROOT/'examples/demo/.obsidian/graph.json'
        if example.exists():
            config=json.loads(example.read_text())
            self.assertTrue(config['colorGroups'])
            for group in config['colorGroups']:
                self.assertTrue(group['query'])
                self.assertIsInstance(group['color']['rgb'],int)
                self.assertTrue(0 <= group['color']['rgb'] <= 0xffffff)

    def test_examples_optional_and_private_excluded(self):
        data=DIST.manifest(examples=False)
        self.assertTrue('skills/garbell/SKILL.md' in data)
        self.assertFalse(any(p.startswith(('examples/','memory/','vault/','dist/')) for p in data))
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)
            for p in ('README.md','README.ca.md','memory/chat.md','vault/raw/font.md','.env'):
                f=r/p; f.parent.mkdir(parents=True,exist_ok=True); f.write_text('fixture')
            self.assertEqual(set(DIST.manifest(r)),{'README.md','README.ca.md'})
if __name__=='__main__':unittest.main()

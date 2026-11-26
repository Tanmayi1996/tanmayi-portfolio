import json
import tempfile
import unittest
from pathlib import Path
from generate import load_changes, render

class ReleaseNotesTests(unittest.TestCase):
    def test_groups_changes_by_type(self):
        data = {"product":"Demo","version":"1.0","changes":[
            {"type":"fix","title":"Fix A","description":"Fixed A"},
            {"type":"feature","title":"Feature B","description":"Added B"}]}
        output = render(data)
        self.assertLess(output.index("## New features"), output.index("## Bug fixes"))
        self.assertIn("Feature B", output)

    def test_rejects_missing_description(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"changes":[{"type":"feature","title":"Oops"}]}))
            with self.assertRaises(ValueError):
                load_changes(path)

if __name__ == "__main__":
    unittest.main()
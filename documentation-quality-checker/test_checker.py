import tempfile
import unittest
from pathlib import Path
from check_docs import check_file

class CheckerTests(unittest.TestCase):
    def test_detects_placeholder_and_broken_link(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "guide.md"
            path.write_text("# Guide\n\nTODO: add details.\n\n[Missing](nope.md)\n")
            messages = [message for _, message in check_file(path)]
            self.assertTrue(any("Placeholder" in item for item in messages))
            self.assertTrue(any("Broken local link" in item for item in messages))

    def test_clean_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "guide.md"
            path.write_text("# Guide\n\nShort, clear instructions.\n")
            self.assertEqual(check_file(path), [])

if __name__ == "__main__":
    unittest.main()
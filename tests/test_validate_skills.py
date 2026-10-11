import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_skill


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.skill = Path(self.temporary.name) / "sample-workflow"
        self.skill.mkdir()

    def write(self, metadata=None, body="Inspect the relevant source before editing."):
        if metadata is None:
            metadata = (
                "name: sample-workflow\ndescription: Review shared settings changes."
            )
        (self.skill / "SKILL.md").write_text(
            f"---\n{metadata}\n---\n\n{body}\n", encoding="utf-8"
        )

    def test_valid_skill_with_local_and_remote_references(self):
        (self.skill / "references").mkdir()
        (self.skill / "references" / "guide.md").write_text("# Guide\n")
        self.write(
            body="Read [guide](references/guide.md) and [web](https://example.com)."
        )
        self.assertEqual(validate_skill(self.skill), [])

    def test_missing_entry_point(self):
        self.assertEqual(validate_skill(self.skill), ["missing SKILL.md"])

    def test_rejects_invalid_metadata(self):
        for metadata in [
            "name: Wrong\ndescription: Review changes.",
            "name: other-name\ndescription: Review changes.",
            "name: sample-workflow\ndescription: ''",
            "name: sample-workflow\ndescription: [not, a, string]",
            "name: [unclosed",
            "- not-a-mapping",
            "name: sample-workflow\ndescription: Review.\nmetadata: {version: 1}",
            "name: sample-workflow\ndescription: Review.\nunsupported: value",
        ]:
            with self.subTest(metadata=metadata):
                self.write(metadata=metadata)
                self.assertTrue(validate_skill(self.skill))

    def test_rejects_empty_instructions(self):
        self.write(body="")
        self.assertIn("instructions must not be empty", validate_skill(self.skill))

    def test_rejects_missing_or_external_local_references(self):
        for target in ["references/missing.md", "../outside.md"]:
            with self.subTest(target=target):
                self.write(body=f"Read [guide]({target}).")
                self.assertTrue(validate_skill(self.skill))

    def test_supports_multiline_descriptions(self):
        self.write(
            metadata=(
                "name: sample-workflow\ndescription: >\n"
                "  Review changes\n  to shared UI."
            )
        )
        self.assertEqual(validate_skill(self.skill), [])


if __name__ == "__main__":
    unittest.main()

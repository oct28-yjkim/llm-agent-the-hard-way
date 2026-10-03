from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hardway.raw_responses import extract_output_text  # noqa: E402


class ExtractOutputTextTests(unittest.TestCase):
    def test_collects_text_from_message_items(self) -> None:
        payload = {
            "output": [
                {"type": "reasoning", "summary": []},
                {
                    "type": "message",
                    "content": [
                        {"type": "output_text", "text": "hello "},
                        {"type": "output_text", "text": "world"},
                    ],
                },
            ]
        }
        self.assertEqual(extract_output_text(payload), "hello world")

    def test_returns_empty_string_for_missing_output(self) -> None:
        self.assertEqual(extract_output_text({}), "")


if __name__ == "__main__":
    unittest.main()

"""Minimal Responses API client using only the Python standard library.

This intentionally avoids the OpenAI SDK so Lab 01 can expose the HTTP boundary.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any


def extract_output_text(response: dict[str, Any]) -> str:
    """Collect output_text parts from a Responses API response payload."""
    chunks: list[str] = []
    for item in response.get("output", []):
        if item.get("type") != "message":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text" and isinstance(part.get("text"), str):
                chunks.append(part["text"])
    return "".join(chunks)


def create_response(prompt: str, *, timeout: float = 30.0) -> dict[str, Any]:
    """Send one non-streaming request and return the decoded JSON body."""
    api_key = os.environ["OPENAI_API_KEY"]
    model = os.environ["OPENAI_MODEL"]
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    payload = json.dumps({"model": model, "input": prompt}).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/responses",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as result:
            return json.loads(result.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API returned HTTP {error.code}: {body}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Network error while calling the OpenAI API: {error.reason}") from error


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m hardway.raw_responses <prompt>", file=sys.stderr)
        return 2
    try:
        response = create_response(" ".join(sys.argv[1:]))
    except KeyError as error:
        print(f"Missing environment variable: {error.args[0]}", file=sys.stderr)
        return 2
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1
    print(extract_output_text(response))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Repository Instructions

## Scope

- This repository teaches how to build LLM agents from low-level primitives.
- Keep model pretraining, transformer implementation, and fine-tuning out of this repository.
- Do not introduce LangChain, LlamaIndex, or the OpenAI Agents SDK before Lab 13.

## Safety

- Never commit API keys, credentials, private documents, production data, or raw user conversations.
- Mock external side effects in tests.
- Require explicit approval before examples perform writes, sends, purchases, deletion, or permission changes.

## Verification

- Run `python scripts/verify_curriculum.py` and `python -m unittest discover -s tests` after structural or code changes.
- Live API tests are opt-in and must be skipped when `OPENAI_API_KEY` or `OPENAI_MODEL` is absent.

## Git Workflow

- Work in a `codex/` branch for substantive changes.
- Commit only coherent, verified changes with a descriptive message.
- Push the current branch to `origin` after verification succeeds.
- Never force-push or rewrite shared history.

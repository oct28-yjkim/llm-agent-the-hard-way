# Lab 09 — Approvals and Security

## 목표

도구의 위험도를 분류하고 외부 영향이 있는 작업에 승인 게이트를 적용합니다.

## 구현

- read-only, reversible write, irreversible/high-impact 작업을 분류합니다.
- 승인 화면에 대상, 변경 내용, 예상 영향을 표시합니다.
- 도구 입력과 검색 문서를 신뢰 경계 밖 데이터로 취급합니다.
- 최소 권한과 allowlist를 적용합니다.

## 실패 주입

문서 속 prompt injection, 경로 traversal, 과도한 권한, 승인 후 인자 변경을 재현합니다.

## Done Check

- 승인된 내용과 실제 실행 인자가 동일합니다.
- 검색된 문서가 시스템 지시를 덮어쓸 수 없습니다.
- 민감정보가 로그와 모델 입력에서 제거됩니다.

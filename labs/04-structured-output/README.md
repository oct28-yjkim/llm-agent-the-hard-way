# Lab 04 — Structured Output

## 목표

자연어와 프로그램 제어 데이터를 분리하고, 모델 출력을 스키마로 검증합니다.

## 구현

- 한 가지 업무 결과를 JSON Schema로 표현합니다.
- required, enum, additionalProperties를 명시합니다.
- 파싱 오류와 의미 오류를 구분합니다.
- 제한된 횟수의 repair loop를 구현합니다.

## 실패 주입

필드 누락, 잘못된 enum, 추가 필드, Markdown으로 감싼 JSON을 재현합니다.

## Done Check

- 잘못된 결과가 다음 시스템으로 전달되지 않습니다.
- 재시도 횟수와 마지막 오류가 관측 가능합니다.
- 스키마 변경의 호환성 정책이 문서화되어 있습니다.

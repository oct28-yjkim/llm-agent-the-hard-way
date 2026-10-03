# Lab 05 — Tool Calling Loop

## 목표

모델 요청 → tool call → 애플리케이션 실행 → tool output → 다음 모델 요청의 전체 루프를 직접 구현합니다.

## 구현

- JSON Schema로 두 개의 read-only 도구를 정의합니다.
- 이름, 인자, `call_id`를 검증합니다.
- 허용 목록에 없는 도구는 거부합니다.
- 최대 반복 횟수와 도구별 timeout을 둡니다.

## 실패 주입

존재하지 않는 도구, 잘못된 인자, 도구 예외, 무한 호출을 재현합니다.

## Done Check

- 같은 `call_id`가 중복 실행되지 않습니다.
- 도구 오류가 모델과 사용자에게 다른 수준으로 전달됩니다.
- 모든 호출과 결과가 trace에 연결됩니다.

참고: [Function calling](https://developers.openai.com/api/docs/guides/function-calling)

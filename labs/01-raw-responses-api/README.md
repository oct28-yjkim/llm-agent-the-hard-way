# Lab 01 — Raw Responses API

## 목표

SDK 없이 HTTP 요청을 만들고 Responses API의 입력과 출력 구조를 관찰합니다.

## 구현

- `src/hardway/raw_responses.py`를 실행합니다.
- 요청 ID, HTTP 상태, 지연시간을 기록하도록 확장합니다.
- 출력에서 `output_text`를 안전하게 추출합니다.
- 키와 모델 이름은 환경변수에서만 읽습니다.

## 실패 주입

키 누락, 잘못된 모델, 401, 429, timeout, 깨진 JSON을 재현합니다.

## Done Check

- HTTP 요청과 모델 응답의 경계를 설명할 수 있습니다.
- 오류 본문을 비밀정보 없이 로그에 남길 수 있습니다.
- API 키가 저장소에 포함되지 않습니다.

참고: [Using tools](https://developers.openai.com/api/docs/guides/tools)

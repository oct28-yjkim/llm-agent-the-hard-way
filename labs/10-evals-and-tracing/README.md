# Lab 10 — Evals and Tracing

## 목표

대표 데이터셋과 trace를 사용해 변경 전후 품질을 반복 측정합니다.

## 구현

- Lab 00의 입력을 JSONL 데이터셋으로 만듭니다.
- 정답성, 형식, 도구 선택, 근거성 grader를 구분합니다.
- 모델 호출, 도구 호출, 승인, latency, token usage를 trace로 연결합니다.
- 변경 전후 결과를 같은 데이터셋에서 비교합니다.

## 실패 주입

점수는 높지만 위험한 결과, 정답이 여러 개인 입력, 불안정한 grader를 포함합니다.

## Done Check

- 평균 점수만이 아니라 실패 사례를 직접 검토합니다.
- 품질 향상과 비용·지연시간 악화를 함께 보고합니다.
- 회귀 기준을 CI에서 자동 검사할 수 있습니다.

참고: [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)

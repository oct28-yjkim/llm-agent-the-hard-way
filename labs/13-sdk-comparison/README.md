# Lab 13 — SDK Comparison

## 목표

직접 만든 런타임을 Agents SDK로 일부 교체하고 추상화의 비용과 이득을 비교합니다.

## 구현

- 단일 에이전트와 하나의 도구부터 SDK로 옮깁니다.
- state, handoff, tracing, guardrail 코드를 비교합니다.
- SDK가 해결한 문제와 여전히 애플리케이션이 책임질 문제를 표로 정리합니다.
- 이전 eval 데이터셋을 그대로 실행합니다.

## Done Check

- migration 전후 기능과 실패 동작이 동일합니다.
- 줄어든 코드량만 아니라 디버깅 가능성도 평가합니다.
- 프레임워크 교체가 비즈니스 규칙을 바꾸지 않습니다.

참고: [Agents SDK quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart?lang=python)

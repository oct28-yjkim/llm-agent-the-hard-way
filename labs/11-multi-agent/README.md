# Lab 11 — Multi-Agent

## 목표

같은 업무를 단일 에이전트와 router/specialist 구조로 구현해 실제 이득을 측정합니다.

## 구현

- router와 두 개의 specialist를 만듭니다.
- handoff 입력과 반환 상태를 명시합니다.
- 한 에이전트를 도구로 사용하는 방식과 완전 handoff를 비교합니다.
- 단일 에이전트 기준선과 품질, 비용, latency를 비교합니다.

## 실패 주입

잘못된 routing, ping-pong handoff, 상태 유실, specialist 실패를 재현합니다.

## Done Check

- 멀티 에이전트가 필요한 근거가 측정값으로 존재합니다.
- 최대 handoff 횟수가 제한됩니다.
- 최종 책임 에이전트가 명확합니다.

# Lab 08 — Agent Runtime

## 목표

에이전트 루프를 명시적인 상태 머신으로 바꾸고 중단·재개 가능한 실행기를 만듭니다.

## 구현

- 상태를 `THINKING`, `WAITING_FOR_TOOL`, `WAITING_FOR_APPROVAL`, `DONE`, `FAILED`로 표현합니다.
- 실행 budget, deadline, 최대 step을 둡니다.
- 각 step 후 체크포인트를 저장합니다.
- 취소와 재개가 같은 결과를 반복하지 않도록 합니다.

## 실패 주입

프로세스 종료, 체크포인트 손상, timeout, 승인 대기를 재현합니다.

## Done Check

- 실행이 왜 멈췄는지 상태만 보고 알 수 있습니다.
- 중단 후 재개해도 완료된 side effect가 반복되지 않습니다.
- budget 초과가 명확한 실패로 종료됩니다.

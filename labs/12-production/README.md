# Lab 12 — Production

## 목표

실험 코드를 운영 가능한 서비스로 바꾸는 신뢰성 장치를 추가합니다.

## 구현

- rate limit과 exponential backoff를 구현합니다.
- 요청별 idempotency key와 correlation ID를 둡니다.
- 모델·도구별 비용과 latency budget을 설정합니다.
- 로그 보존, 비밀 관리, 데이터 삭제 절차를 문서화합니다.

## 실패 주입

부분 장애, 느린 도구, 중복 요청, 모델 변경, 비용 급증을 재현합니다.

## Done Check

- rollback과 kill switch가 있습니다.
- 장애 시 안전한 축소 모드로 전환됩니다.
- 배포 전 회귀 평가와 보안 체크가 자동 실행됩니다.

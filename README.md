# LLM Agent the Hard Way

Kubernetes the Hard Way처럼, 에이전트 프레임워크가 가려주는 핵심 부품을 직접 조립하며 배우는 실습형 커리큘럼입니다.

이 과정의 목표는 GPT 모델을 처음부터 학습하는 것이 아닙니다. 이미 제공되는 모델 API 위에서 요청, 스트리밍, 상태, 도구 호출, 검색, 메모리, 승인, 평가, 운영을 직접 구현해 **에이전트 런타임이 실제로 어떻게 움직이는지** 이해하는 것이 목표입니다.

## Hard Way 규칙

1. Lab 00~12에서는 LangChain, LlamaIndex, Agents SDK를 사용하지 않습니다.
2. 처음에는 Python 표준 라이브러리와 HTTP만 사용합니다.
3. 정상 동작만 확인하지 않고 타임아웃, 잘못된 JSON, 중복 실행, 도구 실패를 일부러 재현합니다.
4. 프롬프트 감상평 대신 테스트 데이터와 측정값으로 개선 여부를 판단합니다.
5. Lab 13에서만 SDK로 교체하고, 직접 만든 코드와 무엇이 달라지는지 비교합니다.

## 완성할 시스템

최종 프로젝트는 다음 능력을 갖춘 근거 기반 리서치 에이전트입니다.

- 스트리밍 응답과 다중 턴 상태
- 구조화된 출력과 직접 만든 tool-calling loop
- 로컬 문서 검색과 출처 표시
- 단기·장기 메모리 분리
- 위험한 작업 전 사용자 승인
- 재시도, 타임아웃, 중복 실행 방지
- trace, 회귀 테스트, 비용·지연시간 기록
- 단일 에이전트와 멀티 에이전트 설계 비교

## 커리큘럼

| Lab | 주제 | 핵심 산출물 |
|---:|---|---|
| 00 | 기준선과 안전 경계 | 요구사항, 위협 모델, 성공 기준 |
| 01 | Raw Responses API | SDK 없는 HTTP 클라이언트 |
| 02 | 스트리밍과 오류 | SSE 파서, timeout/retry |
| 03 | 대화 상태 | 히스토리, 요약, 컨텍스트 예산 |
| 04 | 구조화된 출력 | 스키마 검증과 재시도 |
| 05 | Tool calling | 직접 만든 도구 실행 루프 |
| 06 | Retrieval | chunk, 검색, 인용을 직접 구현 |
| 07 | 메모리 | 단기·장기 메모리 정책 |
| 08 | Agent runtime | 상태 머신, 중단, 재개 |
| 09 | 승인과 보안 | side-effect 분류, 승인 게이트 |
| 10 | Evals와 tracing | 데이터셋, grader, 회귀 테스트 |
| 11 | Multi-agent | router, specialist, handoff 비교 |
| 12 | 운영 | 비용, rate limit, idempotency, 배포 |
| 13 | SDK 비교 | Agents SDK로 교체 후 차이 분석 |
| 14 | Capstone | 리서치 에이전트 완성 |

세부 진행 방식은 [CURRICULUM.md](CURRICULUM.md)를 참고하세요.

## 빠른 시작

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .

$env:OPENAI_API_KEY = "your-key"
$env:OPENAI_MODEL = "a-model-available-to-your-project"

python -m hardway.raw_responses "Explain tool calling in one paragraph."
```

API 키 없이 저장소 구조와 오프라인 테스트만 검증할 수도 있습니다.

```powershell
python scripts/verify_curriculum.py
python -m unittest discover -s tests
```

## 공식 참고 자료

- [Responses API와 도구 사용](https://developers.openai.com/api/docs/guides/tools)
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [File search](https://developers.openai.com/api/docs/guides/tools-file-search)
- [Agents SDK quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart?lang=python)
- [Agent workflow evaluation](https://developers.openai.com/api/docs/guides/agent-evals)

API와 모델은 바뀔 수 있으므로 각 Lab을 시작할 때 공식 문서를 다시 확인하세요.

# Lab 06 — Retrieval from Scratch

## 목표

프레임워크 없이 작은 문서 집합의 분할, 색인, 검색, 인용을 구현합니다.

## 구현

- 문단 또는 토큰 기준 chunker를 작성합니다.
- 먼저 TF-IDF/BM25 수준의 로컬 검색을 구현합니다.
- 검색 결과와 답변에 문서 ID·구간을 연결합니다.
- 이후 임베딩 또는 hosted file search와 결과를 비교합니다.

## 실패 주입

관련 문서 없음, 오래된 문서, 충돌하는 문서, injection 문구가 있는 문서를 넣습니다.

## Done Check

- 근거 없는 답변을 보류할 수 있습니다.
- 인용이 실제 문서 구간과 일치합니다.
- retrieval recall과 최종 answer quality를 따로 측정합니다.

참고: [File search](https://developers.openai.com/api/docs/guides/tools-file-search)

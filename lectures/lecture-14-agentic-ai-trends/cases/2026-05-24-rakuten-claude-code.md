---
name: Rakuten × Claude Code — 피처 출시 24일→5일로 단축 (79%)
description: 라쿠텐이 Claude Code로 피처 타임-투-마켓을 79% 단축하고 12.5M 라인 오픈소스 코드베이스(vLLM)에서 7시간 자율 코딩을 달성한 사례
type: semantics-source
url: https://www.anthropic.com/customers/rakuten
source: blog
discovered: 2026-05-24
category: dev-tool
tags: [claude-code, rakuten, agentic-coding, TDD, parallel-agents, time-to-market, enterprise, japan, vLLM]
relevance: high
---

# Rakuten × Claude Code — 피처 출시 24일→5일로 단축 (79%)

## 한 줄 요약

일본 이커머스 대기업 라쿠텐이 Claude Code를 도입해 피처 타임-투-마켓을 24일에서 5일로 단축(79%)하고, 1,250만 라인 오픈소스 코드베이스(vLLM)에서 7시간 자율 코딩을 달성했다.

## 핵심 사실

- **회사**: Rakuten Group (일본, 이커머스·핀테크·통신 복합 그룹, 수백만 고객 대상 AI 기능 운영)
- **AI 도구**: Claude Code (Anthropic)
- **주요 수치**:
  - 피처 타임-투-마켓: 평균 **24 working days → 5 days (79% 단축)**
  - **7시간 연속 자율 코딩**: vLLM 오픈소스 라이브러리 (1,250만 라인 코드베이스) 내 activation-vector 추출 작업 — 단일 실행에서 완료, 참조 방법 대비 **99.9% 수치 정확도** 달성
- **사용 방식**:
  - **TDD(테스트 주도 개발)**: Claude Code가 종합 테스트를 먼저 생성하고, 그 테스트를 통과하는 기능을 구현
  - **병렬 세션**: 복수의 Claude Code 세션을 동시에 실행해 병목을 제거하고 피처 딜리버리 가속
  - **AI 코드 리뷰**: PR에 즉각적 피드백을 제공해 코드 품질 향상 및 개발 속도 제고
- **개발자 인터뷰**: Diego Mateos (Rakuten Senior ML Engineer) — "Claude Code가 내 개발 방식을 완전히 바꿨다. 포괄적인 테스트를 즉각 생성하고 그 테스트를 통과하는 기능을 만든다. 덕분에 훨씬 더 효율적인 엔지니어가 됐다."
- **1차 출처**: anthropic.com/customers/rakuten (Anthropic 공식 고객 사례) + rakuten.today/blog

## 핵심 인사이트

1. **TDD + Agentic Coding의 시너지**: 테스트를 먼저 작성하면 에이전트에게 명확한 완료 기준이 생겨 자율 실행 품질이 높아진다. 99.9% 정확도는 TDD 기반 검증 루프의 결과.
2. **7시간 자율 실행의 조건은 "컨텍스트"**: 1,250만 라인 코드베이스에서 7시간 단독 작업이 가능했던 것은 작업 범위와 코드베이스 컨텍스트가 잘 구조화된 덕분. 컨텍스트 설계가 전제.
3. **병렬화는 또 다른 가속 레버**: 단일 agent에서 복수 병렬 세션으로 전환함으로써 시간 단축과는 별개로 처리량(throughput) 자체를 늘릴 수 있음.
4. **79% 개선은 대기업에서도 검증됨**: 복잡한 레거시 시스템을 보유한 대기업 규모에서의 결과 — 스타트업이 아니므로 보수적 참고값으로 활용 가능.
5. **정량 지표의 선명함**: "79%", "7시간", "99.9%" — 검증 가능한 구체적 수치로 강의·발표 자료에 직접 인용 가능.

## 강의 활용 메모

- **"AI coding agent를 쓰면 실제로 얼마나 빠른가?"** 질문에 대한 가장 설득력 있는 데이터 포인트.
- **TDD 파트 연결**: "왜 테스트를 먼저 작성해야 하는가?" → AI와 협업할 때 더욱 중요해진 이유를 자연스럽게 연결.
- **병렬 agent 실행** 개념 소개 시 실제 대기업 사례로 활용.
- **아시아 기업 사례**로 국내 청중에게 친숙하게 접근 가능 ("일본 No.1 이커머스 라쿠텐도 하는데").
- Anthropic 2026 Agentic Coding Trends Report에서도 별도 인용됨 — 업계 벤치마크로 권위 부여.

## 원본 메모 / 인용

- 공식 고객 사례 페이지: https://www.anthropic.com/customers/rakuten
- Rakuten 공식 블로그: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code.html
- Anthropic 2026 Agentic Coding Trends Report에서 별도 사례로 인용
- LinkedIn Anthropic Research 포스트: 7시간 자율 코딩 + 79% 개선 수치 확인

## 참고 링크

- https://www.anthropic.com/customers/rakuten (Anthropic 공식)
- https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html (Rakuten 블로그)
- https://www.linkedin.com/posts/anthropicresearch_rakuten-accelerates-development-with-claude-activity-7359266984833736705-HDWF

## 후속 모니터링 포인트

- Rakuten Claude Code 도입 범위 확대 여부 (팀/프로젝트 추가 보고)
- vLLM 프로젝트에 Rakuten의 기여가 실제로 병합됐는지 확인
- 유사한 대규모 자율 코딩 성과를 보고하는 다른 기업 사례 추가 발굴

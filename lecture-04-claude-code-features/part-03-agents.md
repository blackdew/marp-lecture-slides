# Part 03: Sub-process & Agents

---

# Part 3: Sub-process & Agents

복잡한 작업을 위임하는 전문가 시스템

---

## Agent란 무엇인가?

독립적으로 실행되는 전문화된 작업 수행자

**Agent의 특징**

- 복잡한 다단계 작업을 자율적으로 수행
- 메인 세션과 독립적으로 실행
- 작업 완료 후 결과를 최종 보고서로 전달
- 병렬 실행 가능

---

## Agent가 필요한 이유

| 시나리오 | Agent 없이 | Agent 사용 |
|---------|----------|----------|
| 대규모 코드베이스 탐색 | 여러 번의 검색과 읽기 | Explore Agent 한 번 |
| 여러 파일 리팩토링 | 파일마다 수동 작업 | General-purpose Agent |
| 동시 다발적 조사 | 순차적 처리 | 병렬 Agent 실행 |

**핵심 이점**

- 컨텍스트 사용량 절약
- 작업 병렬화로 시간 단축
- 복잡한 워크플로우 자동화

---

## 사용 가능한 Agent 유형

| Agent | 용도 | 주요 도구 |
|-------|------|---------|
| general-purpose | 복잡한 다단계 작업 | 모든 도구 (*) |
| Explore | 코드베이스 빠른 탐색 | Glob, Grep, Read, Bash |
| statusline-setup | 상태바 설정 | Read, Edit |
| output-style-setup | 출력 스타일 생성 | Read, Write, Edit, Glob, Grep |

---

## General-purpose Agent

가장 범용적인 Agent

**사용 시나리오**

- 여러 파일에 걸친 리팩토링
- 복잡한 버그 수정
- 기능 구현 (여러 단계 필요)
- 문서 생성 및 업데이트

**특징**

- 모든 도구에 접근 가능
- 자율적인 의사결정
- 상세한 최종 보고서 제공

---

## Explore Agent

코드베이스 탐색 전문 Agent

**thoroughness 레벨**

- `quick`: 기본 검색
- `medium`: 적당한 탐색
- `very thorough`: 포괄적 분석

**사용 예시**

```
"API endpoints가 어떻게 동작하는지 찾아줘"
→ Explore Agent 자동 실행
```

---

## Agent 사용 시점

**Agent를 사용해야 할 때**

- 여러 위치를 탐색해야 하는 검색
- 복잡한 다단계 작업
- 병렬로 처리할 수 있는 독립적 작업들
- 대규모 코드베이스 분석

**Agent를 사용하지 말아야 할 때**

- 특정 파일 경로를 알고 있을 때 → Read 도구 사용
- 특정 클래스 정의 검색 → Glob 도구 사용
- 2-3개 파일 내 검색 → Read 도구 사용

---

## Agent 호출 방법

**Task 도구 사용**

```
Use the Task tool with:
- subagent_type: "general-purpose" | "Explore" | ...
- prompt: "상세한 작업 지시"
- description: "작업 요약 (3-5 단어)"
```

**자동 호출**

Claude Code가 필요 시 자동으로 Agent 실행

---

## Agent 실행 흐름

**1. Agent 시작**

```
<command-message>The "{name}" agent is loading</command-message>
```

**2. 백그라운드 실행**

Agent가 독립적으로 작업 수행

**3. 결과 전달**

작업 완료 후 최종 보고서 반환

**4. 사용자에게 요약**

보고서 내용을 사용자에게 전달

---

## 병렬 Agent 실행

여러 Agent를 동시에 실행하여 시간 단축

**예시: 프로젝트 분석**

```
동시에 3개 Agent 실행:
1. Frontend 구조 분석 (Explore)
2. Backend API 분석 (Explore)
3. 테스트 코드 분석 (Explore)
```

**방법**

단일 메시지에 여러 Task 도구 호출

---

## Agent 프롬프트 작성 팁

| 팁 | 설명 | 예시 |
|----|------|------|
| 명확한 목표 | 무엇을 찾거나 할지 구체적으로 | "인증 관련 코드 찾기" |
| 예상 결과 명시 | 어떤 형식으로 보고할지 | "파일 경로와 함수명 리스트" |
| 범위 제한 | 탐색 범위 지정 | "src/ 디렉토리만" |
| 우선순위 | 중요한 것부터 | "먼저 에러 찾고, 그 다음 경고" |

---

## Agent 실습 (1/2)

**시나리오: 에러 처리 패턴 찾기**

```
사용자 요청:
"이 프로젝트에서 에러를 어떻게 처리하는지 찾아줘"

Claude Code 실행:
1. Explore Agent 자동 실행
2. thoroughness: "medium"
3. 에러 처리 코드 탐색
4. 패턴 분석 및 보고
```

---

## Agent 실습 (2/2)

**결과 예시**

```
보고서:
1. 에러 처리 방식
   - try/catch 사용 (80%)
   - Error boundary (React)

2. 주요 파일
   - src/utils/errorHandler.ts
   - src/components/ErrorBoundary.tsx

3. 패턴
   - 커스텀 에러 클래스 사용
   - 중앙화된 로깅
```

---

## Agent 활용 고급 팁

**컨텍스트 절약**

- 큰 탐색 작업은 Agent에게 위임
- 메인 세션의 컨텍스트 윈도우 보존

**작업 분할**

- 독립적인 작업들을 여러 Agent로 분할
- 병렬 실행으로 시간 단축

**명확한 지시**

- Agent는 사용자와 추가 소통 불가
- 첫 프롬프트에 모든 정보 포함

---

## Agent 주의사항

| 주의사항 | 이유 |
|---------|------|
| Agent는 상태 없음 | 각 호출은 독립적 |
| 추가 메시지 불가 | 첫 프롬프트가 전부 |
| 결과 신뢰 | Agent 결과는 일반적으로 신뢰 가능 |
| 명확한 범위 | 범위가 모호하면 불필요한 탐색 |

---

## Agent 활용 정리

**언제 사용하나**

- 복잡한 탐색이 필요할 때
- 여러 작업을 병렬 처리할 때
- 컨텍스트를 절약하고 싶을 때

**어떻게 사용하나**

- 명확하고 상세한 프롬프트 작성
- 적절한 Agent 유형 선택
- 필요시 병렬 실행

**무엇을 기대하나**

- 자율적인 작업 수행
- 최종 보고서 형태의 결과
- 시간과 컨텍스트 절약

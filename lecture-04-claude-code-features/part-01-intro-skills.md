# Part 01: 소개 및 Skills

---

# Claude Code 기능 완전 정복

초보자를 위한 핵심 기능 가이드

---

## Claude Code란?

터미널에서 사용하는 AI 코딩 어시스턴트

**주요 특징**

- 코드 읽기, 편집, 실행을 한 번에
- 파일 탐색과 검색 자동화
- Git, npm, docker 등 개발 도구 통합
- 프로젝트 전체를 이해하고 작업

---

## 강의 목표

이 강의에서 배울 내용

| 핵심 기능 | 추가 기능 | 실전 활용 |
|----------|----------|---------|
| Skills | MCP | Best Practices |
| Commands | Hooks | 실제 사용 사례 |
| Sub-process/Agents | | 효과적인 프롬프트 |

---

## 오늘의 주요 내용

**3가지 핵심 기능**

1. **Skills** - 전문화된 작업 수행
2. **Commands** - 반복 작업 자동화
3. **Agents** - 복잡한 작업 위임

**추가로 배울 것**

- MCP (Model Context Protocol)
- Hooks (이벤트 기반 자동화)
- 실전 팁과 주의사항

---

# Part 1: Skills

전문화된 작업 도구

---

## Skills란 무엇인가?

특정 작업에 특화된 전문 도구

**Skills의 특징**

- 각 Skill은 하나의 전문 영역에 집중
- 사용자가 요청하지 않아도 자동으로 실행 가능
- 복잡한 작업을 간단한 명령으로 처리
- 확장 가능한 플러그인 시스템

---

## Skills 사용 시나리오

| 시나리오 | 기존 방식 | Skills 활용 |
|---------|---------|----------|
| PDF 분석 | 파일 열기 → 복사 → 붙여넣기 | 자동 텍스트 추출 |
| Excel 처리 | 수동 데이터 확인 | 자동 파싱 및 분석 |
| 이미지 분석 | 별도 도구 사용 | 직접 이미지 읽기 |

---

## Skills 호출 방법

**방법 1: Skill 도구 사용**

```
Use the Skill tool with:
- command: "pdf" (skill 이름만)
```

**방법 2: 자동 호출**

Skills는 필요시 자동으로 실행됩니다

- PDF 파일 분석 요청 시 → pdf skill 자동 실행
- Excel 파일 처리 요청 시 → xlsx skill 자동 실행

---

## 현재 사용 가능한 Skills

**참고: 실제 사용 가능한 Skills 확인 방법**

```bash
# Claude Code 실행 후
/help
```

시스템 메시지의 `<available_skills>` 섹션 확인

**일반적인 Skills 예시**

- `pdf` - PDF 파일 처리
- `xlsx` - Excel 파일 처리

---

## Skills 실습: PDF 분석

**시나리오**

프로젝트 요구사항이 담긴 PDF 파일 분석

**실행 방법**

1. PDF 파일을 프로젝트에 추가
2. Claude Code에게 요청:
   ```
   requirements.pdf 파일을 분석하고
   주요 기능 목록을 정리해줘
   ```
3. pdf skill이 자동으로 실행되어 내용 추출
4. 분석 결과를 마크다운으로 정리

---

## Skills 활용 팁

| 팁 | 설명 |
|----|------|
| 자동 실행 신뢰 | Skills는 필요시 자동 실행되므로 명시적 호출 불필요 |
| 파일 형식 명시 | 파일 확장자를 명확히 하면 적절한 Skill 선택 |
| 복합 작업 | 여러 Skills를 조합하여 복잡한 작업 수행 가능 |

**주의사항**

- 현재 시스템에 설치된 Skills만 사용 가능
- 새 Skills는 확장을 통해 추가 가능

# Lecture 09: Just Plan It!

**프로젝트 시작일**: 2025-11-16
**현재 상태**: ✅ 완료 (5시간 강의)
**최종 업데이트**: 2025-11-20

---

## 🎯 프로젝트 목표

### 강의 목적

**Just Plan It! - AI Agent와 함께하는 업무 자동화 실습**

- **대상**: 일반 업무 사용자 (엑셀, 워드는 가능하지만 터미널은 낯선 사람)
- **시간**: 5시간 (300분, 하루 완성)
- **형식**: 이론 30% + 실습 60% + 개인 해커톤 10%

### 3가지 핵심 목표

1. **업무 자동화 실행력**: CSV 정리, 문서 요약, 메일 작성 등 즉시 적용 가능한 자동화 경험
2. **AI 시대 관점 장착**: LLM, Agent, 프롬프트, 컨텍스트 등 핵심 개념 이해를 통한 관점 전환
3. **미래 업무 체험**: CLI Agent로 변화될 일하는 방식 직접 경험

### 설계 철학

- **쉬운 언어, 가벼지 않은 깊이**: 기술 용어는 필요하지만 쉽게 풀어서 설명
- **체험 우선**: 이론보다 실습을 먼저 (체험 → 이론 → 심화)
- **심리적 안전감**: "실패해도 괜찮아" 메시지 반복, Agent의 한계 명확히 제시
- **즉시 적용 가능**: 실무 직결 예제, 다음 날부터 써먹을 수 있는 내용

---

## 📚 참고한 기존 강의 (Lecture 03-08)

### Lecture 03: AI Agent 처음 만나기

**대상**: 초보자, 어르신
**핵심 내용**:

- AI Agent = 디지털 비서 개념
- 음성 비서 체험 (시리, 빅스비 등)
- 구체적 부탁 방법: "누구에게, 무엇을, 어떻게"

**재사용 부분**: Part 1-2 (AI Agent 소개, 비유 활용)

### Lecture 04-1: Claude CLI 워크플로우

**대상**: 비개발자 포함
**핵심 내용**:

- 문서 중심 개발 워크플로우
- Plan 모드와 실행 모드 구분
- 6단계 워크플로우 (문서 → Plan → 실행 → 확인 → 문서 업데이트)

**재사용 부분**: Plan 모드 개념

### Lecture 04-2: Claude Code 기능 완전 정복

**대상**: 개발자
**핵심 내용**:

- Skills, Commands, Agents, MCP, Hooks 심화
- PDF Skill 자동 실행
- 병렬 Agent 활용

**재사용 부분**: PDF Skill 자동 실행 개념

### Lecture 05: 문서작업 실전

**대상**: 작가, 연구자, 강사
**핵심 내용**:

- 소설, 논문, 강의 자료, 개인 문서 제작
- Marp 프레젠테이션 자동 생성
- 톤 조절 (대상별 문서 작성)

**재사용 부분**: Part 4-3 (메일 톤 조절 개념)

### Lecture 06: Claude Code 고급 활용법

**대상**: 전문 개발자
**핵심 내용**:

- CLAUDE.md 작성법
- 컨텍스트 관리 전략
- "Shoot and Forget" 철학
- MCP 최소 책임 원칙

**재사용 부분**: 컨텍스트 개념 (Part 3)

### Lecture 07: AI 에이전트 자동화 기초

**대상**: 비개발자 포함
**핵심 내용**:

- **선택, 계획, 문서화** 3가지 키워드 ← 핵심!
- LLM 작동 원리 (확률 기반 예측)
- Agent 구조 (LLM + Memory + Planning + Tools)
- Plan 모드 실습
- "선택은 당신의 몫" 메시지

**재사용 부분**: Part 3 전체 (선택/계획/문서화 철학)

### Lecture 08: 해커톤 실습

**대상**: 전체
**핵심 내용**:

- CSV 데이터 정리 (3개월치 매출 통합)
- PDF 문서 요약 (3개 보고서)
- 메일 자동 생성 (톤 조절)
- 파일 정리 및 리네이밍

**재사용 부분**: Part 4-1, 4-2 (CSV, PDF 실습)

---

## 📋 완료된 작업

### 기획 및 설계
- [x] 기존 강의 분석 (Lecture 03-08)
- [x] 4명 전문가 패널 리뷰 (교육, 실무, UX, 기술)
- [x] 5대 개선 과제 도출
- [x] 최종 강의 개요 확정 (outline.md)
- [x] 회의록 작성 (회의록.md)

### 강의 자료 제작
- [x] 완전한 Marp 슬라이드 제작 (lecture.md)
- [x] Part 1-6 모든 섹션 완성
- [x] 5시간(300분) 타임라인 확정
- [x] QR 코드 및 슬라이드 링크 추가 (https://bit.ly/3JXLGZ0)
- [x] Agent 프로젝트 실제 사례 7가지 추가
- [x] Part 4 샘플 파일 다운로드 링크 제공
- [x] Git 초기화 가이드 추가
- [x] IDE 도구 목록 업데이트 (AntiGravity 포함)
- [x] HTML 프레젠테이션 생성 완료

### 강의 구조 (총 5시간, 300분)

| Part | 제목 | 시간 | 내용 |
|------|------|------|------|
| Part 1 | 시작하기 | 30분 | 환경 확인 및 AI Agent 첫 만남 |
| Part 2 | 첫 실습 | 45분 | "안녕, Agent!" - 간단한 대화와 첫 작업 |
| 휴식 1 | | 15분 | |
| Part 3 | AI 시대 3가지 키워드 | 40분 | LLM 작동 원리, 선택/계획/문서화 |
| Part 4 | 업무 자동화 실습 | 95분 | CSV 정리, PDF 요약, 메일 작성, 즉석 도구 (4개 실습, 각 10+10분) |
| 휴식 2 | | 15분 | |
| Part 5 | 개인 해커톤 | 40분 | 하고 싶은 것 자유롭게 만들기 |
| Part 6 | 회고 및 다음 단계 | 20분 | Agent의 한계, 심화 학습 방향 |

### 주요 특징

1. **실습 우선 구조**: Part 2에서 바로 실습 시작 (이론은 Part 3에서)
2. **10+10 구조**: 모든 Part 4 실습 = 기본 과제(10분) + 도전 과제(10분)
3. **실전 프로젝트 사례**: 7가지 실제 Agent 활용 프로젝트 소개
4. **심리적 안전감**: "실패해도 괜찮아" 메시지 반복
5. **Agent 한계 명시**: Part 6에서 현실적인 기대치 설정

### 파일 구조

```
lectures/lecture-09-agent-hackathon/
├── README.md                   # 프로젝트 개요 및 컨텍스트
├── lecture.md                  # 완성된 Marp 프레젠테이션
├── lecture.html                # 생성된 HTML 프레젠테이션
├── outline.md                  # 최초 강의 개요
├── 회의록.md                    # 전문가 패널 토론 내용
├── part-01.md ~ part-06.md    # Part별 상세 스크립트
├── images/
│   ├── qr_slide_link.svg       # QR 코드 이미지
│   └── [기타 시각 자료]
└── samples/
    └── part4/
        └── part4-samples.zip   # Part 4 실습 파일
```

---

## 🎓 강의 사용 가이드

### 프레젠테이션 실행

**브라우저에서 보기**:
```bash
# HTML 파일 직접 열기
open lectures/lecture-09-agent-hackathon/lecture.html
```

**온라인 링크**: https://bit.ly/3JXLGZ0

**PDF 생성**:
1. 브라우저에서 lecture.html 열기
2. Cmd+P (Mac) / Ctrl+P (Windows)
3. "배경 그래픽" 옵션 활성화
4. "PDF로 저장" 선택

### 프레젠테이션 재생성

강의 내용을 수정한 경우:

```bash
./generate-presentation.sh lecture-09-agent-hackathon lecture.md
```

### 실습 파일 준비

**Part 4 샘플 파일 다운로드**:
- 링크: https://github.com/blackdew/marp-lecture-slides/raw/refs/heads/main/lectures/lecture-09-agent-hackathon/samples/part4/part4-samples.zip
- 강의 전에 미리 다운로드하여 수강생에게 공유

### 강의 진행 팁

**사전 준비**:
1. 모든 수강생이 Claude Code CLI 또는 대체 도구(Gemini CLI, Codex) 설치 완료 확인
2. Part 4 샘플 파일 배포
3. 슬라이드 QR 코드 또는 bit.ly 링크 공유

**진행 중**:
1. Part 2에서 첫 실습으로 분위기 조성
2. Part 4 실습은 10+10 구조 엄수 (기본→도전)
3. 각 Part 마무리 시 핵심 메시지 강조
4. Part 5 개인 해커톤에서 적극적인 질문 유도

**주의사항**:
- "실패해도 괜찮아" 메시지 반복 전달
- Agent의 한계를 솔직하게 설명 (Part 6)
- 시간 배분 엄수 (총 300분)

### 관련 리소스

**Agent 프로젝트 사례**:
- 슬라이드: https://docs.google.com/presentation/d/1_525QEweDZZS5LJC0roWzQaAkrp54Yn6XBI1-d9IWNQ/edit?usp=sharing
- 7가지 실전 프로젝트 (음악, 강의, 생산성, 데이터, 연구 등)

**설치 가이드**:
- Claude Code: https://getclaudecode.com/
- Gemini CLI: https://github.com/google/generative-ai-python
- Codex: https://platform.openai.com/docs/guides/code
- AntiGravity IDE: https://antigravity.google/download

---

## 📝 향후 개선 아이디어

**1. 추가 지원 자료**:
- 용어집 (glossary.md): LLM, Agent, Context, Prompt 등 주요 용어 정리
- 프롬프트 가이드북 (prompt-guide.md): 좋은 프롬프트 작성 패턴 10가지
- 치트 시트 (cheatsheet.md): 자주 쓰는 명령어 및 팁

**2. 시각 자료 추가**:
- LLM 작동 원리 설명 다이어그램
- Agent 구조 시각화
- 좋은/나쁜 프롬프트 비교 예시

**3. 실전 사례 확장**:
- 수강생 성공 사례 수집 및 공유
- 산업별 Agent 활용 사례 추가 (마케팅, 재무, HR 등)

**4. 설치 가이드**:
- Windows/Mac 단계별 설치 동영상
- 트러블슈팅 FAQ 문서
- 오프라인 설치 가이드

**5. 후속 강의**:
- 심화 과정: MCP 서버 구축, Custom Skills 개발
- 실무 적용 워크숍: 팀별 프로젝트 진행

---

## 📞 연락처 및 피드백

**강의 관련 문의**:
- GitHub: https://github.com/blackdew
- 이메일: blackdew7@gmail.com

**참고 문서**:
- 프로젝트 컨텍스트: `lectures/CLAUDE.md`
- 강의 개요: `outline.md`
- 전문가 패널 회의록: `회의록.md`

---

**최종 업데이트**: 2025-11-20
**프로젝트 상태**: ✅ 완료
**강의 제목**: Just Plan It!
**강의 시간**: 5시간 (300분)

# Cowork 프로젝트 지침 (제안)

이 문서는 Claude 데스크톱 앱의 **Cowork 프로젝트 설정 → 프로젝트 지침** 칸에 들어갈
지침의 제안본입니다. 현재 지침은 `오픈 강의용 슬라이드` 한 줄로만 되어 있어,
프로젝트의 실제 구조·워크플로우를 반영하도록 아래 내용으로 교체할 것을 권장합니다.

---

## 1. 프로젝트 지침에 붙여넣을 텍스트

아래 코드블록 안의 내용을 그대로 복사해 Cowork 프로젝트 지침 칸에 붙여넣으세요.

```markdown
# 오픈 강의용 슬라이드 (Marp)

Marp 마크다운으로 비개발자·일반인 대상 AI 에이전트 오픈 강의 슬라이드를
제작·관리하는 저장소입니다. 모든 작업·소통·문서는 한국어로 합니다.

세부 컨벤션(폴더 구조, 디자인 패턴, 빌드 명령 등)은 루트의 CLAUDE.md
(= docs/AGENTS_CONTEXT.md)에 정리되어 있습니다. 작업 전 반드시 참고하고,
충돌 시 그 문서를 우선합니다.

## 공통 규칙

- 강의는 lectures/lecture-XX-주제명/ 폴더에 독립 보관.
  진행 순서: requirements.md → outline.md → 슬라이드 원본 → 빌드 → 검증.
- 빌드 경로는 두 가지. 폴더에 _build/ 가 있으면 생성기 경로이고 원본은
  _build/wN.py 다. 없으면 Marp 경로이고 원본은 lecture.md 다.
  생성기 경로에서 lecture.md 와 outline.md 는 생성물이므로 직접 고치지 않는다.
- Marp 경로의 lecture.md 에는 Marp 프런트매터(marp: true, size: 16:9,
  paginate: true)와 section { padding: 60px 80px; } CSS를 포함.
- 이미지는 강의 폴더 images/에 SVG로 직접 생성 — 콘텐츠는 viewBox 중앙 배치,
  배경 이미지는 35% 크기.
- 한글은 슬라이드 오버플로우가 잦음: 슬라이드당 불릿 5개·테이블 5행 이내,
  볼드 강조 최소화, 긴 문장은 분할.

## 작업 모드별

- 새 강의 제작: requirements.md(대상·시간·목표) 확정 → outline.md(분 단위
  타임라인) → lecture.md 순으로 진행. /create-lecture 슬래시 커맨드는 Claude
  Code 전용이라 Cowork에서는 호출되지 않으므로, 단계를 수동으로 밟되
  .claude/agents/의 분석→설계→제작→검증→회고 흐름을 지침으로 삼는다.
- 기존 강의 수정·개선: Marp 경로는 ./generate-presentation.sh <폴더명>
  <파일.md>로 재빌드(폴더명에 lectures/ 접두사 제외). 생성기 경로는
  _build/ 안에서 python3 build.py N 을 실행. 빌드 후 슬라이드 오버플로우·
  여백·한글 줄바꿈을 스크린샷으로 육안 검증.
- 리뷰·회고: 회고 문서는 docs/retrospectives/에, 재발방지 교훈은
  .claude/learnings/create-lecture.md(Git 추적)에 누적.

## 빌드·커밋

- 빌드 산출물(lecture.html)은 소스와 같은 폴더에 생성. PDF/PPTX는 브라우저에서
  HTML을 열어 인쇄(배경 그래픽 ON)로 추출하는 것을 권장.
- 커밋·PR 설명은 한국어로, 커밋 메시지는 접두사(feat:/fix:/docs: 등)와 함께
  72자 이내로 작성.
```

---

## 2. 프로젝트 세팅 점검 결과

Cowork 환경(격리된 Linux 샌드박스 + 워크스페이스 마운트)에서 이 프로젝트를
다룰 때 확인된 사항입니다.

### 2.1 Marp CLI 설치

- 샌드박스에 Marp CLI가 기본 설치되어 있지 않습니다(Node v22는 있음).
- 기본 `npm install -g`는 `/usr` 권한 문제로 실패합니다. 사용자 prefix로
  설치하면 약 3초 만에 성공합니다:

  ```bash
  npm config set prefix ~/.npm-global
  PUPPETEER_SKIP_DOWNLOAD=1 npm install -g @marp-team/marp-cli
  export PATH=~/.npm-global/bin:$PATH
  ```

- 이 설치는 세션마다 필요하지만 Claude가 빌드 시 자동으로 처리하므로,
  사용자가 직접 할 일은 없습니다(참고용).

### 2.2 generate-presentation.sh의 stdin 대기 (해결됨)

- Marp v4는 비대화형 환경에서 stdin 입력을 기다리며 멈춥니다.
- `generate-presentation.sh`의 marp 호출에 `--no-stdin`이 적용되어 있습니다.
  Cowork 샌드박스에서도 그대로 실행됩니다.

### 2.3 한글 폰트

- 샌드박스에는 한글 폰트가 없습니다. 단, HTML 결과물은 사용자 브라우저에서
  시스템 폰트로 렌더링되므로 문제가 없습니다.
- 샌드박스 내부에서 PDF/이미지를 직접 렌더링하면 한글이 깨질 수 있으므로,
  PDF는 기존 방침대로 브라우저 인쇄로 추출하는 것이 안전합니다.

### 2.4 시각 검증 방법

- Cowork 데스크톱 앱의 computer use(스크린샷·화면 제어)는 현재 비활성입니다.
- 대신 브라우저 자동화 도구로 HTML을 렌더링하고 스크린샷을 찍어 슬라이드
  오버플로우·여백을 육안 검증할 수 있습니다. CLAUDE.md의 "검수 및 테스트
  절차"는 Cowork에서도 이 방식으로 수행 가능합니다.

### 2.5 /create-lecture 자동화 파이프라인

- `.claude/commands/`의 `/create-lecture` 등 슬래시 커맨드와 `.claude/agents/`의
  전문 에이전트는 Claude Code(터미널) 전용입니다. Cowork에서는 슬래시로
  호출되지 않습니다.
- Cowork에서 새 강의를 만들 때는 파이프라인의 6단계(분석→설계→제작→검증→회고)를
  대화로 수동 진행하게 됩니다. 위 지침에 이 점을 명시해 두었습니다.

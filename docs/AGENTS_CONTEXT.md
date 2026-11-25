# AI 코딩 어시스턴트 작업 컨텍스트

## 디렉토리 개요

이 저장소는 마크다운 기반 프레젠테이션을 사용하여 강의 자료를 생성하고 관리합니다. 모든 강의는 `lectures/` 디렉토리 아래에 위치하며 일관된 구조를 따릅니다.

### 저장소 구조

```text
.
├── generate-presentation.sh          # Marp 마크다운 → HTML
├── generate-lecture-pages.sh         # 강의 상세 페이지 + 포털 카드 생성
├── index.html                        # 강의 목록 포털 (카드는 위 스크립트가 생성)
├── assets/css/                       # 공통 CSS (Giscus 댓글 테마)
├── CLAUDE.md · AGENTS.md · GEMINI.md # 모두 docs/AGENTS_CONTEXT.md 심볼릭 링크
├── .claude/
│   ├── agents/                       # 강의 제작 에이전트 7개
│   ├── commands/                     # 슬래시 커맨드 3개
│   └── learnings/                    # 강의 제작 교훈 누적 (Git 추적)
├── docs/
│   ├── AGENTS_CONTEXT.md             # 이 문서. 작업 규칙의 단일 출처
│   ├── 00-review-summary.md          # 강의 리뷰 종합
│   ├── review-lecture-09-agent-hackathon.md
│   ├── cowork-project-instructions.md
│   └── retrospectives/               # 작업 회고
└── lectures/
    ├── lecture-09-agent-hackathon/
    ├── lecture-10-antigravity-gemini/
    ├── lecture-11-agent-life-transition/
    ├── lecture-12-agent-life-transition/
    ├── lecture-15-codex-4weeks/      # Codex 4주 과정 1강
    └── lecture-16-codex-week2/       # Codex 4주 과정 2강
```

### 강의 폴더 구성

강의 폴더는 두 형태입니다. 어느 쪽인지는 `_build/` 유무로 구분합니다.

#### Marp 경로 (9·10·11·12강)

```text
lecture-XX-<주제명>/
├── requirements.md    # 대상 · 시간 · 목표
├── outline.md         # 분 단위 타임라인
├── lecture.md         # 슬라이드 원본. 직접 편집
├── part-XX.md         # 모듈 초안 (선택)
├── images/img_*.svg   # 손으로 만든 SVG
├── .work/             # 중간 산출물 (gitignore 대상)
└── lecture.html       # 빌드 결과
```

#### 생성기 경로 (15·16강)

```text
lecture-XX-<주제명>/
├── requirements.md
├── _build/
│   ├── wN.py          # 슬라이드 원본. 여기만 편집
│   ├── svg*.py        # SVG 그림 정의
│   ├── build.py       # → weekN.html
│   ├── build_marp.py  # → lecture.md + images/
│   └── outline.py     # → outline.md
├── images/img_*.svg   # build_marp.py 가 생성
├── outline.md         # 생성물
├── lecture.md         # 생성물
├── weekN.html         # 발표용 본 슬라이드
└── lecture.html       # Marp 결과
```

생성기 경로에서 `lecture.md` 와 `outline.md` 는 생성물입니다. 직접 고치면 다음 빌드에서 사라집니다.

## 작업 흐름

### 자동화 파이프라인 (권장)

`/create-lecture` 스킬을 사용하면 `requirements.md`로부터 완성된 프레젠테이션까지 자동 생성됩니다:

```
/create-lecture lectures/lecture-XX-주제명 [--plan-only] [--no-images] [--rebuild]
```

| 옵션 | 설명 |
|------|------|
| (없음) | 전체 파이프라인 실행 (학습 → 분석 → 설계 → 제작 → 검증 → 회고) |
| `--plan-only` | 분석/설계까지만 실행 (outline.md 생성) |
| `--no-images` | SVG 이미지 생성 건너뛰기 (기존 이미지 재활용) |
| `--rebuild` | 제작/검증만 재실행 (기존 분석/설계 결과 재활용) |

**전제 조건**: 강의 폴더에 `requirements.md`가 있어야 합니다.

**파이프라인 흐름** (6개 전문 에이전트가 6-Phase로 협업):

0. **학습 주입**: `learnings/create-lecture.md`를 읽어 모든 에이전트에 과거 교훈 주입
1. **분석**: 수강생 페르소나, 주제 리서치, 기존 자료 분석 (병렬 3개 에이전트)
2. **설계**: 분 단위 타임라인, 학습 목표, 비주얼 에셋 목록이 포함된 `outline.md` 생성
3. **제작**: `lecture.md` 슬라이드 작성, SVG 이미지 생성, 실습 섹션 설계
4. **검증**: 품질 리뷰 (근본원인 분석 포함) 후 `generate-presentation.sh`로 HTML 빌드
5. **회고**: 리뷰 리포트에서 교훈 추출 → learnings 파일 업데이트 + 스냅샷 저장

중간 산출물은 `.work/` 디렉토리에 저장되며, `--rebuild`로 재활용할 수 있습니다.

#### 자기 개선 루프

파이프라인은 **자기 개선 루프**를 내장하고 있어, 매 실행마다 과거 실수를 학습합니다:

- **Phase 0 (학습 주입)**: `.claude/learnings/create-lecture.md`의 교훈을 모든 에이전트 프롬프트에 주입
- **Phase 5 (회고)**: 리뷰 리포트의 근본원인 분석에서 새로운 교훈을 추출하여 learnings 파일 업데이트
- **Reflect**: 사용자가 결과물을 수정한 뒤 `/create-lecture-reflect`를 실행하면 diff 기반 교훈 추출

learnings 파일은 Git 추적 대상으로, 팀원 간에 공유됩니다.

#### 피드백 캡처 (`/create-lecture-reflect`)

```
/create-lecture-reflect lectures/lecture-XX-주제명
```

생성된 `lecture.md`를 사용자가 수정한 뒤 실행하면:
1. 자동 생성본 스냅샷(`.work/generated-lecture.md.snapshot`)과 현재 파일을 비교
2. 삭제/추가/수정/레이아웃 변경에서 일반화 가능한 교훈 추출
3. `learnings/create-lecture.md`에 교훈 추가
4. 3회 이상 반복된 교훈은 "반복 패턴"으로 승격 → `create-lecture-templates.md`에 반영 제안

### 수동 작업 흐름

자동화 파이프라인 대신 수동으로 진행하는 경우:

1. **기획 (Planning):** `requirements.md`에 요구사항 정의, `outline.md`에 강의 개요 작성
2. **초안 작성 (Drafting):** 모듈화된 `part-0x.md` 파일로 콘텐츠 개발
3. **검토 (Review):** 대화와 피드백을 통해 콘텐츠 반복 개선
4. **통합 (Consolidation):** 완성된 파트를 메인 `lecture.md` 파일로 병합
5. **빌드 (Build):** `generate-presentation.sh`를 사용하여 프레젠테이션 출력물 생성
6. **검증 (Validation):** 브라우저에서 HTML 출력물 테스트
7. **배포 (Distribution):** HTML/PDF/PPTX 파일 공유

## 핵심 목표

강의 슬라이드를 HTML·PDF·PPTX 로 생성하고, 강의별 산출물을 일관된 구조로 보존합니다. 원본은 강의마다 하나뿐이며, 나머지는 모두 생성물입니다.

## 빌드 경로 두 가지

슬라이드 원본이 강의마다 다릅니다. 고치기 전에 어느 경로인지 확인하십시오.

| 항목 | Marp 경로 | 생성기 경로 |
|------|-----------|-------------|
| 해당 강의 | 09 · 10 · 11 · 12 | 15 · 16 |
| 원본 파일 | `lecture.md` | `_build/wN.py` |
| 발표용 산출물 | `lecture.html` | `weekN.html` |
| 빌드 명령 | `./generate-presentation.sh` | `python3 build.py N` |
| 발표자 노트 | 없음 | 있음 (N 키) |

### Marp 경로

마크다운을 직접 씁니다. 슬라이드는 `---` 로 나눕니다.

```markdown
---
marp: true
size: 16:9
---

# 1강: 시작하기

첫 번째 슬라이드입니다.

---

# 목차

- 소개
- 설치
```

### 생성기 경로

파이썬 자료구조 하나에서 두 형식을 뽑습니다.

- `build.py` → `weekN.html` — 발표용. 발표자 노트 토글, 16:9 자동 맞춤, 휴대폰 문서 모드
- `build_marp.py` → `lecture.md` — Marp 변환용. PDF·PPTX 출력과 포털 등재에 씁니다
- 16강은 생성기를 복사하지 않고 15강 것을 `_build/_shared.py` 로 참조합니다

### Marp 설치

Node.js 와 npm 이 필요합니다. 두 경로 모두 Marp 산출물을 뽑을 때 씁니다.

```bash
npm install -g @marp-team/marp-cli
```

## 마크다운 작성 규칙

마크다운 파일 생성 시 다음 규칙을 준수합니다.

- **헤딩(Headings):** 제목이나 섹션 구분 시 `**` 대신 `#`, `##`, `###` 등을 사용합니다. (MD036)
- **목록 들여쓰기(List Indentation):** 중첩된 목록은 상위 목록보다 2칸 들여쓰기합니다. (MD007)
- **목록 마커 공백(List Marker Space):** 목록 마커 뒤에는 항상 1칸의 공백만 사용합니다. (MD030)
- **헤딩 주변 공백(Blanks around headings):** 헤딩 위아래에는 한 줄씩 비워둡니다. (MD022)
- **목록 주변 공백(Blanks around lists):** 목록 위아래에는 한 줄씩 비워둡니다. (MD032)
- **중복 헤딩 금지(No duplicate headings):** 한 문서 내 동일 제목을 반복하지 않습니다. (MD024)
- **레이아웃 규칙:** 모든 슬라이드는 Marp 프런트매터(`marp: true`, `size: 16:9`)를 포함하고 `---`로 슬라이드를 구분합니다.
- **이름 규칙:** 디렉터리는 소문자 케밥 케이스(`lecture-xx-topic`), 이미지 파일은 `img_1_1_daily_losses.svg`처럼 snake_case와 순번 조합을 사용합니다. 주제어는 폴더만 보고 강의를 구분할 수 있어야 합니다. 같은 주제를 대상이나 시간만 바꿔 다시 할 때는 `codex-week2`처럼 구분자를 붙입니다.
- **스크립트 스타일:** 셸 스크립트는 POSIX 호환 문법과 두 칸 들여쓰기를 유지하며, 필요한 경우에만 한글·영문 병기 주석을 추가합니다.

## 언어 및 작성 규칙

- **한글 원칙**: 구현 계획, 저장소 문서, 커밋 메시지, PR 설명을 모두 한글로 씁니다.
- **적용 범위**: 아래 문장 규칙과 용어 규칙은 슬라이드와 저장소 문서에 똑같이 적용합니다.

### 문장: 한눈에 읽히는 길이로 쓴다

- 한 문장에 한 가지만 담습니다.
- 수식어를 겹치지 않습니다.
- 목록 항목은 명사형으로 끝냅니다.
- 설명이 길어지면 문장을 나누거나 표로 바꿉니다.
- 같은 내용을 두 곳에 쓰지 않습니다. 한 곳에 두고 나머지는 링크합니다.

### 용어: 표준 기술 용어를 쓰고 비유로 덮지 않는다

`LLM`, `Memory`, `Planning`, `Tools`, `컨텍스트`, `프롬프트` 같은 표준 기술 용어를 그대로 씁니다. `학습 목표`, `타임라인`, `실습`, `수강생`, `루브릭` 같은 표준 교육 용어도 그대로 씁니다. 필요하면 **기능 설명**을 덧붙입니다. 그 위에 비유를 한 겹 더 얹지 않습니다.

| 쓰지 않음 | 대신 |
|-----------|------|
| Agent = 도구를 쓸 줄 아는 똑똑한 동료 | Agent = 도구를 사용해 실제 작업을 수행하는 AI |
| LLM (두뇌) / 똑똑한 두뇌 | LLM (추론) / 언어 이해 및 생성 |
| Tools = 손과 발 / 칼, 불, 냄비 | Tools = 파일 조작, 명령 실행 |
| 요리사에게 레시피만 vs 재료와 도구까지 | 챗봇은 방법을 설명하고, Agent는 그 작업을 직접 수행 |
| AI 조수 / AI 비서 | 에이전트 / Agent |
| 명확한 지시가 성공의 열쇠 | 명확한 지시가 결과를 좌우함 |

표에 `비유` 열이나 `비유` 행을 만들지 않습니다. 왼쪽에 표준 용어가 있고 가운데에 기능 설명이 있으면 비유 열은 더할 것이 없습니다.

**예외 — 의도적 비유는 허용합니다.** 명시적으로 도입하고(`### 게임에 비유하면` 같은 제목), 대조표나 전환 문장으로 전개하며, 표준 용어로는 전달하기 어려운 감각을 전달할 때만 씁니다. 호칭 한 줄로 끝나는 비유는 의도적 비유가 아닙니다.

## 이미지 에셋 가이드

강의안에 사용되는 이미지는 각 강의 폴더 내의 `images` 디렉토리에 로컬로 저장하는 것을 원칙으로 합니다.

### 이미지 생성 규칙

외부 이미지 다운로드는 실패하기 쉽습니다. 강의 내용에 맞는 **SVG 이미지를 직접 생성**하십시오.

SVG 이미지 생성 시 다음 규칙을 반드시 준수해야 합니다.

1. **콘텐츠는 항상 중앙에 배치:**
   Marp의 `![bg left]` 나 `![bg right]` 같은 배경 이미지 지시어는 이미지를 자르는 것이 아니라, 이미지 전체를 해당 방향으로 **정렬**합니다. 따라서 SVG 내부의 그래픽이나 텍스트가 특정 방향으로 치우쳐 있으면, 최종 결과물에서 의도치 않게 잘려 보이게 됩니다. **모든 SVG 콘텐츠는 `viewBox`의 중앙에 위치하도록 설계해야 합니다.**

2. **단순하고 명확한 디자인:**
   복잡한 일러스트레이션보다는, 슬라이드의 핵심 메시지를 전달하는 단순한 아이콘, 도형, 텍스트의 조합을 사용합니다. 이는 다른 강의와의 통일성을 유지하고, 파일 용량을 작게 유지하는 데 도움이 됩니다.

3. **대체 텍스트 제공:**
   만약 내용에 맞는 이미지를 생성하기 어려운 경우, 해당 이미지의 내용을 설명하는 텍스트를 담은 SVG 플레이스홀더를 생성합니다.

### 이미지 참조 방법

마크다운에서 이미지를 참조할 때는 상대 경로를 사용합니다:

```markdown
![설명](./images/img_2_1_footprints.svg)
![bg left:35%](images/img_p1_1.svg)
```

### 배경 이미지 전용 가이드

Marp의 배경 이미지(`![bg left]`, `![bg right]`)는 인라인 이미지와 다른 특성을 가집니다:

1. **권장 크기 비율:**
   - 배경 이미지는 **35%** 크기를 사용합니다 (40% 이상은 여백이 부족함)
   - SVG viewBox는 세로로 긴 비율 권장: `viewBox="0 -80 600 960"` ~ `viewBox="0 -80 600 1160"`

2. **중요한 제약사항:**
   - SVG의 viewBox 크기를 변경해도 Marp의 배경 이미지 렌더링에는 영향을 주지 않습니다
   - CSS 스타일로 배경 이미지의 여백을 조정할 수 없습니다
   - **유일한 여백 조정 방법은 마크다운에서 퍼센티지를 낮추는 것입니다**

3. **배경 이미지 SVG 디자인:**
   - 콘텐츠는 반드시 viewBox 중앙에 배치
   - 내부 여백을 충분히 확보 (상하 80px, 좌우 100px 권장)
   - 세로 방향으로 긴 디자인 (aspect ratio 약 1:1.5 ~ 1:1.8)

## Marp 디자인 패턴

모든 새 강의 생성 시 다음 디자인 패턴을 적용합니다.

### 필수 CSS 템플릿

모든 `lecture.md` 파일의 프런트매터에 다음 CSS를 포함해야 합니다:

```markdown
---
marp: true
theme: default
size: 16:9
paginate: true
---

<style>
section {
  padding: 60px 80px;
}

section.lead {
  padding: 60px 80px;
}
</style>
```

이 패딩은 슬라이드 콘텐츠가 가장자리에 붙는 것을 방지합니다.

### 배경 이미지 사용법

```markdown
![bg left:35%](images/img_example.svg)

# 슬라이드 제목

- 콘텐츠는 오른쪽 65% 영역에 표시됩니다
```

크기와 viewBox 규칙은 위 "배경 이미지 전용 가이드" 에 있습니다.

### 공간 절약 패턴

슬라이드에 세로 공간이 부족할 때:

1. **테이블 사용:** 체크리스트나 단계별 설명은 불릿 리스트 대신 테이블로 작성

```markdown
## 체크리스트 (비추천)

**시작 전**
- 문서 준비
- Plan 모드

**진행 중**
- 한 번에 한 가지
- 자주 확인

## 체크리스트 (권장)

| 시작 전 | 진행 중 | 완료 후 |
|---------|---------|---------|
| 문서 준비 | 한 번에 한 가지 | 문서 업데이트 |
| Plan 모드 | 자주 확인 | git commit |
```

테이블은 수평 공간을 효율적으로 사용하여 세로 길이를 약 40-50% 줄일 수 있습니다.

2. **슬라이드 분할:** 여전히 공간이 부족하면 내용을 2개 슬라이드로 나눕니다

### PDF 생성 방법

Marp CLI의 `--pdf` 옵션은 Puppeteer 오류로 실패할 수 있습니다. 다음 수동 방법을 권장합니다:

1. 브라우저에서 생성된 HTML 파일 열기
1. Cmd+P (Mac) 또는 Ctrl+P (Windows)로 인쇄 대화상자 열기
1. "배경 그래픽" 또는 "Background graphics" 옵션 활성화
1. "PDF로 저장" 선택

## 빌드 · 테스트 · 개발 명령

### 주요 빌드 스크립트

```bash
./generate-presentation.sh <폴더명> <마크다운파일명>
```

예시:

```bash
./generate-presentation.sh lecture-09-agent-hackathon lecture.md
```

**주의**: 첫 번째 인자에 `lectures/` 접두사를 포함하지 않습니다. 스크립트가 자동으로 `lectures/`를 붙입니다.

이 스크립트는:
- 마크다운을 Marp로 HTML로 변환
- `images/` 폴더를 출력 위치로 복사
- 소스 파일과 동일한 디렉토리에 출력

### 생성기 경로 빌드

15·16강은 `_build/` 안에서 실행합니다.

```bash
cd lectures/lecture-16-codex-week2/_build
python3 build.py 2        # → ../week2.html  (발표용)
python3 build_marp.py 2   # → ../lecture.md + ../images/
python3 outline.py 2      # → ../outline.md
python3 ../../lecture-15-codex-4weeks/_build/check.py ../week2.html   # 태그 검사
```

그다음 Marp 산출물을 뽑습니다.

```bash
./generate-presentation.sh lecture-16-codex-week2 lecture.md
```

### 라이브 프리뷰

Marp 경로에서 편집 중 자동 새로고침:

```bash
marp lectures/<폴더>/<파일.md> --watch
```

### 수동 변환 명령

```bash
marp lectures/<폴더>/<파일.md> -o lectures/<폴더>/<파일.html> --html --allow-local-files
marp lectures/<폴더>/<파일.md> --pdf       # Puppeteer 의존성 필요
marp lectures/<폴더>/<파일.md> --pptx      # 직접 PPTX 생성
```

## 검수 및 테스트 절차

콘텐츠 수정 후 다음 순서로 확인합니다.

1. 재빌드
   - Marp 경로: `./generate-presentation.sh <폴더> <파일.md>`
   - 생성기 경로: `_build/` 에서 `python3 build.py N` 실행 후 `check.py` 로 태그 검사
2. 브라우저에서 결과물을 열어 확인
   - 줄바꿈 및 텍스트 흐름 — 한국어는 오버플로우가 잦습니다
   - 폰트 렌더링
   - 이미지 경로 및 렌더링
   - 배경 이미지 여백 — 슬라이드 가장자리에 닿지 않는지
   - 콘텐츠 여백 — 텍스트가 상하좌우 끝에 닿지 않는지
   - 슬라이드 오버플로우 — 하단이 잘리지 않는지
3. `images/` 폴더가 결과물과 함께 복사됐는지 확인
4. 다이어그램이나 외부 자산을 추가하면 `marp --watch` 로 깨진 링크를 조기에 확인

`check.py` 는 HTML 태그 중첩만 검사합니다. 레이아웃 깨짐은 잡지 못하므로 브라우저 확인을 건너뛰지 않습니다.

### 일반적인 디자인 문제 해결

#### 문제: 배경 이미지가 슬라이드 끝에 붙어있음

- 해결: `![bg left:40%]` 를 `![bg left:35%]` 로 변경

#### 문제: 텍스트가 슬라이드 끝에 붙어있음

- 해결: 프런트매터에 `section { padding: 60px 80px; }` CSS 추가

#### 문제: 슬라이드 하단 콘텐츠가 잘림

- 해결 1: 불릿 리스트를 테이블로 변환하여 세로 공간 절약
- 해결 2: 콘텐츠를 2개 슬라이드로 분할

주의사항:

- 한국어 텍스트는 줄바꿈이 쉽게 어긋날 수 있으므로 긴 문장은 불릿으로 분할하고, 강조 표현은 최소화합니다.
- 마크다운 프리뷰와 실제 Marp 렌더링 결과가 다를 수 있으므로 반드시 HTML 출력물을 브라우저에서 확인합니다.

## 커밋 및 PR 가이드

### 커밋 메시지 규칙

- 짧고 구체적으로 작성 (72자 이내)
- 설명적 접두사 사용: `fix:`, `docs:`, `feat:` 등
- 여러 강의 모듈에 걸친 변경 시 모듈명 포함
- 예시: `fix: 강의안 이미지 문제 해결 및 디자인 개선`

### Pull Request 가이드

PR 설명에 포함할 항목:
- 변경된 강의 모듈 목록
- 생성된 결과물 목록 (HTML/PDF/PPTX)
- 관련 이슈 또는 강의 계획 문서
- 시각적 변경이 있을 경우 전후 비교 스크린샷

리뷰 요청 전:
- `generate-presentation.sh`를 실행하여 프레젠테이션 결과물을 최신 상태로 갱신

## 일반적인 작업 패턴

### 새 강의 만들기 (자동화)

1. 새 디렉토리 생성: `lectures/lecture-XX-주제명`
2. `requirements.md` 작성 (대상, 시간, 목표, 고려사항, 성공 기준)
3. 자동 파이프라인 실행:

```
/create-lecture lectures/lecture-XX-주제명
```

단계별로 진행하려면:

```
# 1단계: 분석/설계만 먼저 실행하여 outline.md 검토
/create-lecture lectures/lecture-XX-주제명 --plan-only

# 2단계: outline.md 확인/수정 후 제작/빌드 실행
/create-lecture lectures/lecture-XX-주제명 --rebuild
```

### 새 강의 만들기 (수동)

1. 빌드 경로를 먼저 정합니다. 발표자 노트가 필요하면 생성기 경로, 아니면 Marp 경로입니다.
2. 새 디렉토리 생성: `lectures/lecture-XX-주제명`
3. `requirements.md` 에 대상·시간·목표를 적습니다.
4. Marp 경로: `images/` 를 만들고 Marp 프런트매터가 들어간 `lecture.md` 를 작성한 뒤
   `./generate-presentation.sh lecture-XX-주제명 lecture.md` 로 빌드합니다.
5. 생성기 경로: `_build/` 에 `_shared.py` · `build.py` · `build_marp.py` · `outline.py` · `wN.py` 를 두고
   `python3 build.py N` 으로 빌드합니다. 공용 생성기(`deck.py` 등)는 15강 `_build/` 를 참조합니다.

### 강의 등재 (포털 + 상세 페이지)

강의 폴더를 만든 뒤 포털과 상세 페이지에 올리려면 **`generate-lecture-pages.sh`의 `LECTURES` 배열 한 곳만** 고치고 스크립트를 실행합니다.

```bash
./generate-lecture-pages.sh
```

배열 한 줄의 형식은 파이프로 구분한 13개 필드입니다.

```text
폴더명|제목|부제|대상|시간|구성|평가|설명|메인파일|카드제목|카드부제|카드태그|카드뱃지
```

| 구간 | 쓰이는 곳 | 비우면 |
|------|-----------|--------|
| 1~8 | 강의 상세 페이지 메타 정보 | 필수 |
| 9 메인파일 | 상세 페이지 iframe과 포털 링크 | `lecture.html` |
| 10 카드제목 | 포털 카드 제목 | 제목에서 `Lecture NN: ` 제거 |
| 11 카드부제 | 포털 카드 부제 | 부제 필드 사용 |
| 12 카드태그 | 포털 카드 태그 (쉼표 구분) | 태그 영역 생략 |
| 13 카드뱃지 | `Lecture NN · 값` 형태 강조 | 번호만 표시 |

루트 `index.html`은 `<!-- LECTURE_CARDS:START -->` ~ `<!-- LECTURE_CARDS:END -->` 사이만 교체됩니다. 소개 문구·푸터·CSS는 직접 고치면 되고, 카드 목록은 직접 고치지 마십시오.

강의를 내릴 때도 배열에서 해당 줄을 지우고 스크립트를 실행하면 포털 카드가 사라집니다.

### 콘텐츠 반복 작업

라이브 리로드를 위해 `marp --watch` 사용:

```bash
cd lectures/lecture-XX-주제명
marp lecture.md --watch
```

### 커밋 전 생성 파일 확인

```bash
git status
# HTML 출력물이 최신인지 확인
./generate-presentation.sh <폴더> <파일.md>
# 브라우저에서 변경사항 검토
```

## Imported Claude Cowork project instructions

오픈 강의용 슬라이드

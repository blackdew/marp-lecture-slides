# Marp Lecture Slides

AI 에이전트 오픈 강의 슬라이드 저장소입니다. 마크다운과 파이썬 생성기로 HTML·PDF·PPTX 슬라이드를 만듭니다.

공개 포털: <https://blackdew.github.io/marp-lecture-slides/>

## 강의 목록

| 폴더 | 주제 | 대상 | 시간 | 빌드 경로 |
|------|------|------|------|-----------|
| `lecture-09-agent-hackathon` | Just Plan It! AI 에이전트 해커톤 | 모든 레벨 | 6시간 | Marp |
| `lecture-10-antigravity-gemini` | AI 에이전트 활용 (Do-See-Ask-Learn) | 비개발자 | 6시간 | Marp |
| `lecture-11-agent-life-transition` | Just Plan It!! AI Agent로 일과 삶의 전환 | 대학생·교직원 | 2시간 | Marp |
| `lecture-12-agent-life-transition` | AI Agent 활용 생활·업무 전환 | 대학생·교직원 | 2시간 | Marp |
| `lecture-15-codex-4weeks` | 에이전트와 함께하는 삶의 전환: Codex 4주 과정 1강 | 비전공자 30~60대 | 2시간 | 생성기 |
| `lecture-16-codex-week2` | 에이전트, 더 잘 쓰는 방법: Codex 4주 과정 2강 | 비전공자 30~60대 | 2시간 | 생성기 |

포털에는 09·10·11·12·15강이 등재되어 있습니다.

## 설치

Node.js 와 npm 이 필요합니다.

```bash
npm install -g @marp-team/marp-cli
```

생성기 경로 강의는 Python 3 을 추가로 씁니다. 외부 패키지는 필요하지 않습니다.

## 빌드

빌드 경로는 두 가지입니다. 폴더에 `_build/` 가 있으면 생성기 경로입니다.

### Marp 경로 (09·10·11·12강)

원본은 `lecture.md` 입니다.

```bash
./generate-presentation.sh lecture-09-agent-hackathon lecture.md
```

첫 번째 인자에 `lectures/` 를 붙이지 않습니다. 스크립트가 자동으로 붙입니다.

### 생성기 경로 (15·16강)

원본은 `_build/wN.py` 하나입니다. `lecture.md` 와 `outline.md` 는 생성물이므로 직접 고치지 않습니다.

```bash
cd lectures/lecture-16-codex-week2/_build
python3 build.py 2         # → ../week2.html  (발표용 슬라이드)
python3 build_marp.py 2    # → ../lecture.md + ../images/
python3 outline.py 2       # → ../outline.md
```

Marp 산출물이 필요하면 이어서 실행합니다.

```bash
cd ../../.. && ./generate-presentation.sh lecture-16-codex-week2 lecture.md
```

### 라이브 프리뷰

Marp 경로에서 편집 중 자동 새로고침:

```bash
marp lectures/<폴더>/<파일.md> --watch
```

## 포털 등재

`generate-lecture-pages.sh` 의 `LECTURES` 배열에 한 줄을 추가하고 실행합니다.

```bash
./generate-lecture-pages.sh
```

강의 상세 페이지와 루트 `index.html` 의 카드가 함께 생성됩니다. 배열 형식은 [CLAUDE.md](docs/AGENTS_CONTEXT.md) 의 "강의 등재" 절에 있습니다.

## 저장소 구조

```text
.
├── generate-presentation.sh    # Marp 마크다운 → HTML
├── generate-lecture-pages.sh   # 강의 상세 페이지 + 포털 카드 생성
├── index.html                  # 강의 목록 포털
├── docs/                       # 작업 컨텍스트 · 리뷰 · 회고
├── .claude/                    # 강의 제작 에이전트 · 슬래시 커맨드 · 학습 메모리
└── lectures/                   # 강의 폴더
```

## PDF · PPTX 출력

HTML 을 브라우저에서 열고 인쇄 대화상자에서 "배경 그래픽" 을 켠 뒤 PDF 로 저장합니다. Marp CLI 의 `--pdf` 는 Puppeteer 의존성 때문에 실패할 수 있습니다.

## 작성 규칙

슬라이드 작성 규칙, 디자인 패턴, 이미지 가이드, 검수 절차는 [CLAUDE.md](docs/AGENTS_CONTEXT.md) 에 있습니다. 이 저장소의 작업 규칙은 모두 그 문서 하나에 모읍니다.

## 라이선스

MIT

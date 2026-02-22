# Marp Lecture Slides

마크다운 기반 프레젠테이션 제작 시스템입니다. [Marp](https://marp.app/)를 활용하여 마크다운 파일을 HTML, PDF, PPTX 형식의 슬라이드로 변환합니다.

## 주요 기능

- 마크다운으로 프레젠테이션 작성
- 모듈화된 콘텐츠 관리 (part-XX.md)
- 강의별 독립된 디렉토리 구조
- HTML/PDF/PPTX 출력 지원
- SVG 기반 시각 자료 관리
- 자동 빌드 스크립트

## 필수 요구사항

- Node.js (npm 포함)
- Marp CLI

## 설치

```bash
npm install -g @marp-team/marp-cli
```

## 사용 방법

### 1. 프레젠테이션 빌드

```bash
./generate-presentation.sh <강의폴더명> <마크다운파일명>
```

예시:

```bash
./generate-presentation.sh lecture-09-agent-hackathon lecture.md
```

### 2. 라이브 프리뷰

편집 중 자동 새로고침을 원할 경우:

```bash
marp lectures/<폴더>/<파일.md> --watch
```

### 3. 수동 변환

```bash
marp lectures/<폴더>/<파일.md> -o lectures/<폴더>/<파일.html> --html --allow-local-files
marp lectures/<폴더>/<파일.md> --pdf
marp lectures/<폴더>/<파일.md> --pptx
```

## 프로젝트 구조

```text
.
├── generate-presentation.sh      # 메인 빌드 스크립트
├── generate-lecture-pages.sh     # 강의별 index.html 생성 스크립트
├── index.html                    # 강의 목록 포탈 페이지
├── assets/css/                   # 공통 CSS (Giscus 댓글 테마 등)
├── docs/
│   ├── AGENTS_CONTEXT.md         # AI 에이전트용 작업 컨텍스트
│   ├── 00-review-summary.md      # 강의 리뷰 종합 요약
│   └── retrospectives/           # 작업 회고
├── .claude/
│   ├── agents/                   # 강의 제작 전문 에이전트 (7개)
│   ├── commands/                 # Claude Code 스킬
│   └── learnings/                # 자기 개선 루프 학습 메모리
└── lectures/                     # 강의 자료 루트 디렉토리
    └── lecture-XX-<주제명>/      # 개별 강의 폴더 (패턴)
        ├── requirements.md       # 강의 요구사항 정의서
        ├── outline.md            # 강의 개요 및 타임라인
        ├── lecture.md            # 메인 프레젠테이션 파일
        ├── part-XX.md            # 모듈화된 콘텐츠 (선택)
        ├── images/               # 시각 자료
        │   └── img_*.svg         # SVG 이미지 파일
        ├── .work/                # 파이프라인 중간 산출물
        └── lecture.html          # 생성된 결과물
```

## 작업 흐름

1. **기획**: 강의 개요 작성
2. **초안**: 모듈화된 `part-XX.md` 파일로 콘텐츠 개발
3. **검토**: 피드백을 통한 반복 개선
4. **통합**: 완성된 파트를 `lecture.md`로 병합
5. **빌드**: `generate-presentation.sh`로 출력물 생성
6. **검증**: 브라우저에서 HTML 결과물 확인

## 마크다운 작성 규칙

- 슬라이드는 `---`로 구분
- 프런트매터에 `marp: true`, `size: 16:9` 필수
- 배경 이미지: `![bg left:35%](images/example.svg)`
- 헤딩 주변 공백 확보 (MD022)
- 목록 들여쓰기 2칸 (MD007)

## 디자인 가이드

### 필수 CSS

모든 `lecture.md`에 다음 CSS 포함:

```markdown
<style>
section {
  padding: 60px 80px;
}
</style>
```

### 이미지 생성 규칙

- SVG 형식 우선 사용
- 콘텐츠는 viewBox 중앙 배치
- 배경 이미지는 35% 크기 권장

### PDF 생성

Marp CLI의 `--pdf` 옵션 대신 다음 방법 권장:

1. HTML 파일을 브라우저에서 열기
2. Cmd+P (Mac) / Ctrl+P (Windows)
3. "배경 그래픽" 옵션 활성화
4. "PDF로 저장"

## 현재 강의 목록

현재 `lectures/` 디렉토리에는 다음 강의가 포함되어 있습니다:

| 강의 | 주제 | 대상 | 시간 |
|------|------|------|------|
| lecture-09-agent-hackathon | Just Plan It! AI 에이전트 해커톤 | 모든 레벨 | 6시간 |
| lecture-10-antigravity-gemini | AI 에이전트 활용 (Do-See-Ask-Learn) | 비개발자 | 6시간 |
| lecture-11-agent-life-transition | Just Plan It!! AI Agent로 일과 삶의 전환 | 대학생/교직원 | 2시간 |
| lecture-12-agent-life-transition | AI Agent 활용 생활/업무 전환 | 대학생/교직원 | 2시간 |

## 라이선스

MIT

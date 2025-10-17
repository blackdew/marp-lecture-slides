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
./generate-presentation.sh lecture-01-ai-data-coding lecture.md
```

### 2. 라이브 프리뷰

편집 중 자동 새로고침을 원할 경우:

```bash
marp <폴더>/<파일.md> --watch
```

### 3. 수동 변환

```bash
marp <폴더>/<파일.md> -o <폴더>/<파일.html> --html --allow-local-files
marp <폴더>/<파일.md> --pdf
marp <폴더>/<파일.md> --pptx
```

## 프로젝트 구조

```text
.
├── generate-presentation.sh    # 메인 빌드 스크립트
├── docs/
│   ├── AGENTS_CONTEXT.md       # AI 에이전트용 작업 컨텍스트
│   └── retrospectives/         # 작업 회고
├── lecture-XX-주제명/
│   ├── lecture.md              # 메인 프레젠테이션 파일
│   ├── part-01.md ~ part-XX.md # 모듈화된 콘텐츠
│   ├── images/                 # 시각 자료
│   └── lecture.html            # 생성된 결과물
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

## 샘플 강의 목록

- lecture-01-ai-data-coding
- lecture-02-프로젝트공유
- lecture-03-ai-agent-intro
- lecture-04-claude-cli-workflow

## 라이선스

MIT

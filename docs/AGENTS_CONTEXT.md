# AI 코딩 어시스턴트 작업 컨텍스트

## 디렉토리 개요

이 저장소는 마크다운 기반 프레젠테이션을 사용하여 강의 자료를 생성하고 관리합니다. 각 강의는 독립된 디렉토리에 위치하며(`lecture-01-ai-data-coding`, `lecture-02-프로젝트공유`, `lecture-03-ai-agent-intro` 등) 일관된 구조를 따릅니다.

### 저장소 구조

```
.
├── generate-presentation.sh          # 메인 빌드 스크립트
├── CLAUDE.md -> docs/AGENTS_CONTEXT.md   # Claude Code용 심볼릭 링크
├── AGENTS.md -> docs/AGENTS_CONTEXT.md   # 범용 Agents용 심볼릭 링크
├── GEMINI.md -> docs/AGENTS_CONTEXT.md   # Gemini용 심볼릭 링크
├── docs/
│   ├── AGENTS_CONTEXT.md              # 마스터 작업 컨텍스트 파일
│   └── retrospectives/                # 작업 회고 및 학습 내용
├── lecture-01-ai-data-coding/
│   ├── lecture.md                     # 메인 프레젠테이션 파일
│   ├── part-01.md ~ part-05.md        # 모듈화된 콘텐츠 섹션
│   ├── images/                        # 시각 자료
│   └── lecture.html                   # 생성된 결과물
├── lecture-02-프로젝트공유/
│   ├── project_sharing_presentation.md
│   ├── PROJECT_*.md                   # 문서 파일들
│   └── images/
└── lecture-03-ai-agent-intro/
    ├── lecture.md
    ├── part-01.md ~ part-04.md
    └── images/
```

각 강의 폴더의 구성:
- `lecture.md` 또는 유사한 메인 프레젠테이션 파일
- `part-0x.md` 초안/모듈화된 콘텐츠 파일
- `images/` 시각 자료 디렉토리
- 생성된 출력 파일 (`.html`, `.pdf`, `.pptx`)

## 작업 흐름

각 강의는 다음 단계를 따라 진행됩니다:

1. **기획 (Planning):** `outline.md` 또는 유사한 파일에 강의 개요 작성
2. **초안 작성 (Drafting):** 모듈화된 `part-0x.md` 파일로 콘텐츠 개발
3. **검토 (Review):** 대화와 피드백을 통해 콘텐츠 반복 개선
4. **통합 (Consolidation):** 완성된 파트를 메인 `lecture.md` 파일로 병합
5. **빌드 (Build):** `generate-presentation.sh`를 사용하여 프레젠테이션 출력물 생성
6. **검증 (Validation):** 브라우저에서 HTML 출력물 테스트
7. **배포 (Distribution):** HTML/PDF/PPTX 파일 공유

## 핵심 목표

마크다운 파일을 사용하여 프레젠테이션 슬라이드(PPT/HTML/PDF)를 생성하고, 강의별 산출물을 일관된 구조로 보존하는 것이 핵심입니다.

## 권장 도구: Marp

`Marp`는 마크다운으로 프레젠테이션을 제작할 때 사용하는 표준 도구입니다. 모든 프레젠테이션은 Marp (Markdown Presentation Ecosystem)를 사용하여 빌드됩니다.

### 설치

Node.js와 npm이 설치되어 있어야 합니다:

```bash
npm install -g @marp-team/marp-cli
```

### 기본 사용법

슬라이드는 `---` 구분자로 나눕니다:

```markdown
---
marp: true
size: 16:9
---

# 1강: 시작하기

이것은 첫 번째 슬라이드입니다.

---

# 목차

- 소개
- 설치
- 사용법
```

## 마크다운 작성 규칙

마크다운 파일 생성 시 다음 규칙을 준수합니다.

* **헤딩(Headings):** 제목이나 섹션 구분 시 `**` 대신 `#`, `##`, `###` 등을 사용합니다. (MD036)
* **목록 들여쓰기(List Indentation):** 중첩된 목록은 상위 목록보다 2칸 들여쓰기합니다. (MD007)
* **목록 마커 공백(List Marker Space):** 목록 마커 뒤에는 항상 1칸의 공백만 사용합니다. (MD030)
* **헤딩 주변 공백(Blanks around headings):** 헤딩 위아래에는 한 줄씩 비워둡니다. (MD022)
* **목록 주변 공백(Blanks around lists):** 목록 위아래에는 한 줄씩 비워둡니다. (MD032)
* **중복 헤딩 금지(No duplicate headings):** 한 문서 내 동일 제목을 반복하지 않습니다. (MD024)
* **레이아웃 규칙:** 모든 슬라이드는 Marp 프런트매터(`marp: true`, `size: 16:9`)를 포함하고 `---`로 슬라이드를 구분합니다.
* **이름 규칙:** 디렉터리는 소문자 케밥 케이스(`lecture-xx-topic`), 이미지 파일은 `img_1_1_daily_losses.svg`처럼 snake_case와 순번 조합을 사용합니다.
* **스크립트 스타일:** 셸 스크립트는 POSIX 호환 문법과 두 칸 들여쓰기를 유지하며, 필요한 경우에만 한글·영문 병기 주석을 추가합니다.

## 이미지 에셋 가이드

강의안에 사용되는 이미지는 각 강의 폴더 내의 `images` 디렉토리에 로컬로 저장하는 것을 원칙으로 합니다.

### 이미지 생성 규칙

외부 이미지를 다운로드하는 것은 불안정하고 실패할 확률이 높으므로, 강의 내용에 맞는 간단한 **SVG 형식의 이미지를 직접 생성**하는 것을 최우선으로 권장합니다.

SVG 이미지 생성 시 다음 규칙을 반드시 준수해야 합니다.

1.  **콘텐츠는 항상 중앙에 배치:**
    Marp의 `![bg left]` 나 `![bg right]` 같은 배경 이미지 지시어는 이미지를 자르는 것이 아니라, 이미지 전체를 해당 방향으로 **정렬**합니다. 따라서 SVG 내부의 그래픽이나 텍스트가 특정 방향으로 치우쳐 있으면, 최종 결과물에서 의도치 않게 잘려 보이게 됩니다. **모든 SVG 콘텐츠는 `viewBox`의 중앙에 위치하도록 설계해야 합니다.**

2.  **단순하고 명확한 디자인:**
    복잡한 일러스트레이션보다는, 슬라이드의 핵심 메시지를 전달하는 단순한 아이콘, 도형, 텍스트의 조합을 사용합니다. 이는 다른 강의와의 통일성을 유지하고, 파일 용량을 작게 유지하는 데 도움이 됩니다.

3.  **대체 텍스트 제공:**
    만약 내용에 맞는 이미지를 생성하기 어려운 경우, 해당 이미지의 내용을 설명하는 텍스트를 담은 SVG 플레이스홀더를 생성합니다.

### 이미지 참조 방법

마크다운에서 이미지를 참조할 때는 상대 경로를 사용합니다:

```markdown
![설명](./images/img_2_1_footprints.svg)
![bg left:40%](images/img_p1_1.svg)
```

## 빌드 · 테스트 · 개발 명령

### 주요 빌드 스크립트

```bash
./generate-presentation.sh <폴더명> <마크다운파일명>
```

예시:

```bash
./generate-presentation.sh lecture-01-ai-data-coding lecture.md
```

이 스크립트는:
- 마크다운을 Marp로 HTML로 변환
- `images/` 폴더를 출력 위치로 복사
- 소스 파일과 동일한 디렉토리에 출력

### 라이브 프리뷰

편집 중 자동 새로고침:

```bash
marp <폴더>/<파일.md> --watch
```

### 수동 변환 명령

```bash
marp <폴더>/<파일.md> -o <폴더>/<파일.html> --html --allow-local-files
marp <폴더>/<파일.md> --pdf       # Puppeteer 의존성 필요
marp <폴더>/<파일.md> --pptx      # 직접 PPTX 생성
```

## 검수 및 테스트 절차

콘텐츠 수정 후 다음 단계를 따릅니다:

1. `./generate-presentation.sh <폴더> <파일.md>`를 실행하여 HTML 재생성
2. 브라우저에서 HTML 파일을 열어 다음 항목 확인:
   - 줄바꿈 및 텍스트 흐름 (한국어 텍스트는 오버플로우되기 쉬움)
   - 폰트 렌더링
   - 이미지 경로 및 렌더링
3. `images/` 폴더가 HTML 출력물과 함께 올바르게 복사되었는지 확인
4. 새 다이어그램이나 외부 자산 추가 시 `marp --watch`를 사용하여 깨진 링크를 조기에 발견

주의사항:
* 한국어 텍스트는 줄바꿈이 쉽게 어긋날 수 있으므로 긴 문장은 불릿으로 분할하고, 강조 표현은 최소화합니다.

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

### 새 강의 만들기

1. 새 디렉토리 생성: `lecture-XX-주제명`
2. `images/` 서브디렉토리 추가
3. Marp 프런트매터가 포함된 초기 `lecture.md` 생성
4. 빌드: `./generate-presentation.sh lecture-XX-주제명 lecture.md`

### 콘텐츠 반복 작업

라이브 리로드를 위해 `marp --watch` 사용:

```bash
cd lecture-XX-주제명
marp lecture.md --watch
```

### 커밋 전 생성 파일 확인

```bash
git status
# HTML 출력물이 최신인지 확인
./generate-presentation.sh <폴더> <파일.md>
# 브라우저에서 변경사항 검토
```

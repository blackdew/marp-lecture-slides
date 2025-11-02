# Part 02: Commands

---

# Part 2: Commands

반복 작업을 자동화하는 도구

---

## Commands란 무엇인가?

사용자 정의 명령어로 반복 작업 간소화

**Commands의 특징**

- `/`로 시작하는 슬래시 명령어
- 자주 쓰는 작업을 한 줄로 실행
- 마크다운 파일로 쉽게 작성
- 프로젝트별 또는 전역으로 설정 가능

---

## Commands vs Skills

| 구분 | Commands | Skills |
|-----|----------|--------|
| 목적 | 반복 작업 자동화 | 특정 파일 형식 처리 |
| 실행 | 사용자가 명시적 호출 | 자동 실행 가능 |
| 생성 | 마크다운 파일 작성 | 플러그인 설치 |
| 범위 | 프로젝트 맞춤형 | 범용적 |

---

## Commands 사용 예시

**기본 명령어**

```
/help       # 도움말 보기
/clear      # 대화 기록 지우기
```

**커스텀 명령어 예시**

```
/review-pr 123          # PR 리뷰
/run-tests              # 테스트 실행 및 결과 분석
/deploy staging         # 스테이징 배포
```

---

## Commands 저장 위치

**프로젝트별 Commands**

```
.claude/
└── commands/
    ├── review-pr.md
    ├── run-tests.md
    └── deploy.md
```

**전역 Commands**

```
~/.config/claude/
└── commands/
    └── my-command.md
```

---

## Command 파일 구조

**파일명**: `.claude/commands/review-pr.md`

**내용 예시**:

```markdown
# PR 리뷰 수행

주어진 PR 번호의 코드를 리뷰하고 다음을 확인:
- 코드 스타일 일관성
- 잠재적 버그
- 테스트 커버리지
- 문서화 여부

리뷰 결과를 마크다운으로 정리해줘.
```

---

## Custom Command 만들기

**Step 1: 디렉토리 생성**

```bash
mkdir -p .claude/commands
```

**Step 2: 명령어 파일 작성**

```bash
# .claude/commands/analyze-bundle.md 생성
```

**Step 3: 내용 작성**

```markdown
# 번들 크기 분석

1. package.json의 dependencies 확인
2. 큰 패키지 상위 5개 찾기
3. 대체 가능한 경량 라이브러리 제안
```

---

## Command 사용 방법

**실행**

```
/analyze-bundle
```

**인자가 있는 Command**

파일 내용에서 `{인자}` 참조 가능:

```markdown
# PR {pr_number} 리뷰

PR #{pr_number}의 변경사항을 리뷰해줘.
```

실행: `/review-pr 123`

---

## 유용한 Command 예시 (1/2)

**코드 리뷰**

```markdown
# 코드 리뷰

최근 커밋의 변경사항을 리뷰하고:
- 버그 가능성
- 성능 이슈
- 보안 문제
를 확인해줘.
```

**테스트 실행**

```markdown
# 테스트 실행 및 분석

1. npm test 실행
2. 실패한 테스트 분석
3. 수정 방법 제안
```

---

## 유용한 Command 예시 (2/2)

**문서 생성**

```markdown
# README 업데이트

프로젝트의 주요 기능을 분석하고
README.md를 최신 상태로 업데이트해줘.

포함 내용:
- 설치 방법
- 사용 예시
- API 문서
```

---

## Commands 활용 팁

| 팁 | 설명 |
|----|------|
| 명확한 이름 | 명령어 이름은 기능을 명확히 표현 |
| 단계별 지시 | 복잡한 작업은 단계별로 나누어 작성 |
| 재사용성 | 자주 쓰는 패턴을 명령어로 만들기 |
| 문서화 | 주석으로 명령어 목적 설명 |

---

## Commands 실습

**실습: 코드 품질 체크 명령어 만들기**

1. `.claude/commands` 디렉토리 생성
2. `quality-check.md` 파일 생성
3. 다음 내용 작성:
   - ESLint 실행
   - Type 체크
   - 테스트 실행
   - 결과 요약
4. `/quality-check` 명령으로 실행

---

## Command 디버깅

**확인 사항**

- 파일이 `.claude/commands/` 에 있는지 확인
- 파일 확장자가 `.md` 인지 확인
- 명령어 이름이 파일명과 일치하는지 확인

**도움말 확인**

```
/help
```

사용 가능한 모든 명령어 목록이 표시됩니다.

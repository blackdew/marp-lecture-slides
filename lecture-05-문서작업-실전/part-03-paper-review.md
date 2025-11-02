# Part 3: 논문 리뷰 및 작성

학술 연구를 위한 Claude Code 활용

---

## 논문 작업의 도전 과제

**연구자들이 겪는 어려움**

- 수십 개의 참고문헌 관리
- 논문 PDF 읽고 핵심 추출
- 관련 논문 간 비교 분석
- 인용 형식 통일
- 섹션별 일관성 유지
- 버전 관리

**Claude Code의 해결책**

PDF Skill + 구조화된 파일 관리 + 자동화

---

## 프로젝트 구조

**추천 디렉토리**

```
my-research/
├── papers/                    # 수집한 논문 PDF
│   ├── smith2023.pdf
│   ├── lee2024.pdf
│   └── ...
├── notes/                     # 논문별 노트
│   ├── smith2023-notes.md
│   ├── lee2024-notes.md
│   └── ...
├── synthesis/                 # 종합 분석
│   ├── literature-review.md
│   └── comparison-table.md
├── my-paper/                  # 내 논문 작성
│   ├── abstract.md
│   ├── introduction.md
│   ├── methodology.md
│   ├── results.md
│   └── conclusion.md
└── references.bib             # 참고문헌
```

---

## Skills: PDF 논문 분석

**시나리오**

새로운 논문 PDF 파일을 다운로드했고, 핵심 내용을 빠르게 파악하고 싶음

**Claude Code 활용**

```
"papers/smith2023.pdf를 분석해서
다음 정보를 추출해줘:

1. 연구 목적 및 질문
2. 방법론
3. 주요 결과
4. 한계점
5. 우리 연구와의 관련성

notes/smith2023-notes.md로 저장"
```

---

## PDF Skill 자동 실행

**백그라운드 처리**

1. pdf skill 자동 실행
2. PDF 텍스트 추출
3. 내용 분석 및 구조화
4. 마크다운 파일로 저장

**생성된 노트 예시**

```markdown
# Smith et al. (2023) - Deep Learning for NLP

## 연구 목적
자연어 처리에서 Transformer 모델의 효율성 개선

## 방법론
- 데이터셋: WikiText-103
- 모델: Modified Transformer
- 평가 지표: Perplexity, BLEU

## 주요 결과
- 기존 모델 대비 15% 성능 향상
- 추론 속도 2배 개선
...
```

---

## 여러 논문 일괄 분석

**시나리오**

papers/ 폴더에 10개의 PDF가 있고, 모두 요약 필요

**Agent 활용**

```
"papers/ 디렉토리의 모든 PDF 파일을 분석해서
각각에 대한 요약 노트를 notes/ 에 생성해줘.

파일명은 원본 PDF 이름을 따르되 -notes.md 추가"
```

**General-purpose Agent 자동 실행**

- 모든 PDF 파일 탐색
- 순차적으로 분석
- 노트 파일 생성

---

## Custom Command: 논문 리뷰

**`.claude/commands/review-paper.md`**

```markdown
# 논문 리뷰 생성

주어진 PDF 파일을 분석하고 다음 형식으로 리뷰 작성:

## 기본 정보
- 제목, 저자, 연도, 학술지

## 핵심 내용 (3-5 문장)

## 강점
- 3-5개 불릿

## 약점
- 3-5개 불릿

## 우리 연구와의 관련성
- 어떻게 활용할 수 있는지

## 인용 필요 여부
- Yes/No 및 이유

파일명: notes/{저자}{연도}-review.md
```

---

## Command 실행

**새 논문 리뷰 시**

```
/review-paper papers/lee2024.pdf
```

**자동 생성**

- PDF 읽기
- 구조화된 리뷰 작성
- notes/lee2024-review.md 저장

**시간 절약**

수동 요약: 30-45분 → Claude Code: 2-3분

---

## 논문 비교 분석

**시나리오**

관련 논문 5개를 비교하여 차이점과 공통점 파악

**요청**

```
"notes/ 폴더의 smith2023, lee2024, kim2023,
park2024, choi2023 노트를 읽고

다음을 비교 분석해줘:
1. 사용한 방법론
2. 데이터셋
3. 성능 지표
4. 주요 차이점

synthesis/comparison-table.md로 저장"
```

---

## 생성된 비교표

**Markdown 표 형식**

| 논문 | 방법론 | 데이터셋 | 성능 (BLEU) | 특징 |
|-----|-------|---------|------------|------|
| Smith 2023 | Transformer | WikiText | 42.5 | 속도 개선 |
| Lee 2024 | BERT | GLUE | 45.1 | 정확도 우선 |
| Kim 2023 | GPT-3 | Custom | 48.3 | Few-shot |
| Park 2024 | T5 | C4 | 46.7 | 다국어 |
| Choi 2023 | RoBERTa | BookCorpus | 44.2 | 사전학습 |

**시각적으로 차이 한눈에 파악**

---

## 문헌 리뷰 작성

**시나리오**

내 논문의 Related Work 섹션 작성

**Claude Code 활용**

```
"synthesis/comparison-table.md와
notes/ 폴더의 모든 리뷰를 바탕으로

학술 논문 형식의 Literature Review를
작성해줘.

- 시간순 또는 주제별로 구성
- 각 논문의 기여도 설명
- 우리 연구의 위치 명확히

my-paper/related-work.md로 저장"
```

---

## 생성된 Literature Review

**예시**

```markdown
# Related Work

## Transformer-based Approaches

Smith et al. (2023) proposed an efficient Transformer
variant that achieves 15% better performance while
reducing inference time by half. Their approach focuses
on architectural modifications to the attention mechanism.

Building upon this work, Lee et al. (2024) introduced
a BERT-based model that prioritizes accuracy over speed,
achieving 45.1 BLEU score on the GLUE benchmark.

## Few-shot Learning Methods

Kim et al. (2023) demonstrated that GPT-3 can...

## Our Contribution

While previous work has focused on either efficiency
or accuracy, our approach aims to balance both...
```

---

## 참고문헌 관리

**BibTeX 파일 생성**

```
"notes/ 폴더의 모든 논문 정보를 읽고
references.bib 파일을 생성해줘.

BibTeX 형식으로, 각 논문의:
- author, title, year, journal/conference
- DOI (가능한 경우)

를 포함해줘"
```

**자동 생성 references.bib**

```bibtex
@article{smith2023deep,
  author = {Smith, John and Doe, Jane},
  title = {Deep Learning for NLP},
  journal = {ACL},
  year = {2023},
  doi = {10.18653/v1/2023.acl-long.123}
}

@inproceedings{lee2024bert,
  author = {Lee, Minho},
  title = {BERT for Korean},
  booktitle = {EMNLP},
  year = {2024}
}
```

---

## 논문 작성: 섹션별 관리

**모듈화 전략**

각 섹션을 별도 파일로 작성

**작업 흐름**

```
1. abstract.md 작성
2. introduction.md 작성
3. methodology.md 작성
4. results.md 작성
5. conclusion.md 작성
```

**장점**

- 섹션별로 집중 가능
- 동료와 섹션별 공유 용이
- Git으로 섹션별 버전 관리

---

## 섹션 작성 지원

**Introduction 작성 예시**

```
"my-paper/introduction.md를 작성해줘.

다음 내용 포함:
1. 연구 배경 (2-3 문단)
2. 기존 연구의 한계 (1-2 문단)
3. 우리의 접근 방법 (1 문단)
4. 논문 구성 (1 문단)

synthesis/literature-review.md와
notes/ 폴더 내용을 참고해줘"
```

**Claude가 초안 작성**

---

## 일관성 검사

**시나리오**

여러 섹션에서 같은 개념을 다르게 표현했을 수 있음

**검사 요청**

```
"my-paper/ 폴더의 모든 섹션을 읽고

다음을 확인해줘:
1. 용어 일관성 (같은 개념을 다른 용어로 표현)
2. 약어 통일 (처음 사용 시 전체 이름 + 약어)
3. 시제 일관성 (Abstract는 현재형 등)
4. 수치 표기 일관성"
```

---

## 일관성 검사 결과

**Agent 보고서**

```
용어 일관성 문제:

1. "모델" vs "model" (한영 혼용)
   - introduction.md: "모델"
   - methodology.md: "model"
   → 통일 필요

2. 약어 정의
   - "NLP" 첫 사용 시 정의 없음
   - introduction.md:12에 추가 필요:
     "Natural Language Processing (NLP)"

3. 시제
   - abstract.md: 과거형과 현재형 혼용
   → 현재형으로 통일 권장
```

**즉시 수정 가능**

---

## 표와 그림 관리

**LaTeX 표 생성**

```
"synthesis/comparison-table.md의
마크다운 표를 LaTeX 표로 변환해줘.

\begin{table}...\end{table} 형식
캡션: 'Comparison of recent NLP models'"
```

**자동 변환**

```latex
\begin{table}[h]
\centering
\caption{Comparison of recent NLP models}
\begin{tabular}{lllll}
\hline
Paper & Method & Dataset & BLEU & Feature \\
\hline
Smith 2023 & Transformer & WikiText & 42.5 & Speed \\
Lee 2024 & BERT & GLUE & 45.1 & Accuracy \\
...
\end{tabular}
\end{table}
```

---

## 통계 분석 지원

**Excel/CSV 데이터 분석**

```
"results/experiment-data.csv를 읽고

1. 기술 통계 계산 (평균, 표준편차)
2. 각 조건별 결과 비교
3. LaTeX 표로 변환
4. 간단한 해석 추가

my-paper/results-table.md로 저장"
```

**csv Skill 또는 Read로 처리**

---

## 버전 관리: Git 활용

**논문 작성 시작 시**

```
"Git 저장소 초기화하고
현재 구조를 커밋해줘"
```

**섹션 완성 시마다**

```
"introduction.md 작성 완료했어.
Git 커밋해줘"
```

**자동 커밋**

```bash
git add my-paper/introduction.md
git commit -m "feat: Introduction 초안 완성"
```

---

## 협업: 공동 저자 피드백

**피드백 관리**

```
my-research/
└── feedback/
    ├── reviewer1-comments.md
    ├── reviewer2-comments.md
    └── response.md
```

**피드백 반영**

```
"feedback/reviewer1-comments.md를 읽고
지적된 사항을 my-paper/ 섹션에 반영해줘.

변경사항 목록을 feedback/changes.md에 기록"
```

---

## 투고 준비: 형식 변환

**학회별 형식 요구사항**

```
"my-paper/ 폴더의 모든 섹션을 통합해서
ACL 2024 형식에 맞는 단일 LaTeX 파일로
만들어줘.

- 섹션 순서: Abstract, Intro, Method, Results, Conclusion
- 참고문헌은 references.bib 사용
- 표와 그림 포함

output/paper-acl2024.tex로 저장"
```

---

## 최종 체크리스트

**Custom Command: 투고 전 검사**

**`.claude/commands/final-check.md`**

```markdown
# 투고 전 최종 검사

1. 모든 섹션 완성 확인
2. 참고문헌 형식 통일
3. 표와 그림 캡션 확인
4. 페이지 제한 준수
5. 저자 정보 및 감사의 글
6. 보충 자료 준비

체크리스트 형식으로 결과 출력
```

---

## 논문 리뷰 (심사자 입장)

**역할 전환: 내가 심사자라면**

```
"my-paper/ 폴더의 논문을 읽고
학술지 심사자 입장에서 리뷰를 작성해줘.

형식:
- 전체 평가 (Accept/Revise/Reject)
- 강점 3-5개
- 약점 3-5개
- 구체적 수정 제안
- 질문 사항

feedback/self-review.md로 저장"
```

**객관적 피드백 얻기**

---

## 연구 노트 관리

**일일 연구 기록**

```
notes/
└── daily/
    ├── 2024-01-15.md
    ├── 2024-01-16.md
    └── ...
```

**주간 요약 자동 생성**

```
"notes/daily/ 폴더의 이번 주 (1/15-1/21)
일일 노트를 읽고 주간 요약을 만들어줘.

- 주요 진행 사항
- 발견한 문제점
- 다음 주 계획

notes/weekly/2024-W03.md로 저장"
```

---

## 학회 발표 자료 준비

**논문 → 슬라이드 변환**

```
"my-paper/ 폴더의 논문을 바탕으로
15분 발표용 슬라이드를 만들어줘.

Marp 형식으로:
- 제목 슬라이드
- 연구 배경 (2 슬라이드)
- 방법론 (3 슬라이드)
- 결과 (4 슬라이드)
- 결론 (1 슬라이드)
- Q&A (1 슬라이드)

presentation/conference-talk.md로 저장"
```

---

## 연구 프로젝트 타임라인

**진행 상황 추적**

```markdown
# 연구 프로젝트 타임라인

## 2024-01 (완료)
- ☑ 문헌 조사 (20편 논문 리뷰)
- ☑ 연구 질문 정립

## 2024-02 (진행 중)
- ☑ 실험 설계
- → 데이터 수집 중
- ☐ 예비 실험

## 2024-03 (예정)
- ☐ 본 실험
- ☐ 결과 분석
- ☐ 논문 작성 시작
```

---

## 실전 팁

| 단계 | Claude Code 활용 |
|-----|-----------------|
| 문헌 조사 | PDF 일괄 분석, 노트 자동 생성 |
| 비교 분석 | 표 생성, 종합 리포트 |
| 논문 작성 | 섹션별 초안, 일관성 검사 |
| 참고문헌 | BibTeX 자동 생성 |
| 협업 | Git 버전 관리, 피드백 반영 |
| 투고 준비 | 형식 변환, 최종 검사 |

---

## 시간 절약 효과

**기존 방식**

- 문헌 조사 (10편): 20시간
- 비교 분석: 8시간
- 논문 작성: 40시간
- 형식 맞추기: 6시간
- **총: 74시간**

**Claude Code 활용**

- 문헌 조사: 5시간 (75% 절약)
- 비교 분석: 2시간 (75% 절약)
- 논문 작성: 25시간 (37% 절약)
- 형식 변환: 1시간 (83% 절약)
- **총: 33시간 (55% 절약)**

---

## 주의사항

**Claude Code의 역할**

- 구조화, 정리, 요약 지원
- 형식 변환, 일관성 유지
- 참고문헌 관리

**연구자의 역할**

- 연구 아이디어 및 질문
- 실험 설계 및 수행
- 결과 해석 및 통찰
- 최종 검토 및 책임

**절대 하지 말 것**

- 논문 내용 전체를 AI가 작성하도록 요청
- 인용 없이 AI 생성 문장 사용
- 논문 윤리 위반

---

## 논문 작업 정리

**Claude Code가 도와주는 것**

- PDF 논문 빠른 분석
- 여러 논문 비교 정리
- 섹션별 초안 작성 지원
- 일관성 및 형식 검사
- 참고문헌 자동 관리
- 버전 관리

**연구자가 얻는 것**

- 시간 절약 (55%)
- 체계적 문헌 관리
- 일관된 논문 품질
- 협업 효율 증가

**다음: 개인 문서 관리**

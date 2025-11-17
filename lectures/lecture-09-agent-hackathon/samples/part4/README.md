# Part 4 실습용 샘플 파일

이 폴더에는 Part 4 "업무 자동화 실습"에서 사용할 샘플 파일들이 들어있습니다.

---

## 📁 파일 구성

### 1. CSV 파일 (실습 4-1: CSV 데이터 정리)

- `sales_jan.csv` - 2024년 1월 매출 데이터 (36행)
- `sales_feb.csv` - 2024년 2월 매출 데이터 (33행)
- `sales_mar.csv` - 2024년 3월 매출 데이터 (35행)

**특징**:
- 날짜 포맷이 제각각 (2024-01-01, 01/03/2024, Feb 2, 2024 등)
- 금액에 특수문자 혼재 (₩1,500,000, 1500000원, 1500000 등)
- 중복 데이터 포함 (실습용)

### 2. 분기 보고서 파일 (실습 4-2: PDF 문서 요약)

- `report_q1.md` - 2024년 1분기 경영 실적 보고서
- `report_q2.md` - 2024년 2분기 경영 실적 보고서
- `report_q3.md` - 2024년 3분기 경영 실적 보고서

**⚠️ PDF 변환 필요**:
현재 마크다운 형식으로 제공됩니다. 실습 전에 PDF로 변환해주세요.

### 3. 회의록 파일 (실습 4-3: 상황별 메일 작성)

- `meeting_notes.md` - 2024년 1분기 성과 검토 회의록

**내용**: 매출 실적, 주요 이슈, 2분기 전략, 액션 아이템 등

---

## 🔄 PDF 변환 방법

마크다운 파일을 PDF로 변환하는 방법:

### 방법 1: Agent에게 요청 (권장)

```bash
# 터미널에서 samples/part4 폴더로 이동
cd samples/part4

# Agent 실행
claude

# 프롬프트 입력
3개의 마크다운 파일(report_q1.md, report_q2.md, report_q3.md)을
PDF로 변환해줘.
파일명은 report_q1.pdf, report_q2.pdf, report_q3.pdf로 해줘.
```

### 방법 2: 온라인 도구 사용

1. https://www.markdowntopdf.com/ 접속
2. 마크다운 파일 업로드
3. PDF 다운로드

### 방법 3: Pandoc 사용 (설치 필요)

```bash
# Pandoc 설치 (Mac)
brew install pandoc

# PDF 변환
pandoc report_q1.md -o report_q1.pdf
pandoc report_q2.md -o report_q2.pdf
pandoc report_q3.md -o report_q3.pdf
```

---

## 📋 실습별 사용 파일

| 실습 | 사용 파일 | 목적 |
|------|----------|------|
| **4-1** | sales_jan.csv<br>sales_feb.csv<br>sales_mar.csv | CSV 데이터 통합 및 정리 |
| **4-2** | report_q1.pdf<br>report_q2.pdf<br>report_q3.pdf | PDF 문서 요약 |
| **4-3** | meeting_notes.md | 대상별 메일 작성 (팀원용/경영진용) |
| **4-4** | (파일 없음) | 즉석 도구 만들기 (HTML 생성) |

---

## 💡 사용 팁

### CSV 파일
- 실제 매출 데이터를 시뮬레이션한 현실적인 데이터
- 날짜 포맷, 금액 표기 등 실무에서 흔히 발생하는 문제 포함
- Agent에게 데이터 정리 및 통합 요청 시 좋은 예제

### 분기 보고서
- 각 보고서는 독립적으로 사용 가능
- 요약 실습: 각 보고서를 3-5 문장으로 요약
- 통합 실습: 3개 보고서를 하나의 연간 리포트로 통합

### 회의록
- 팀원용 메일: 친근하고 상세하게
- 경영진용 메일: 간결하고 수치 중심, 격식 있게
- 같은 내용을 다른 톤으로 작성하는 연습

---

## 🚨 주의사항

1. **실습 전 백업**: 원본 파일을 복사해두세요
   ```bash
   cp -r samples/part4 samples/part4_backup
   ```

2. **PDF 변환 확인**: 실습 4-2 전에 반드시 PDF 변환 완료
3. **파일 경로**: Agent 실행 위치를 확인하세요
   - 실습 폴더: `ai-hackathon` 또는 지정한 작업 폴더
   - 샘플 파일 복사: 작업 폴더로 복사 후 사용 권장

---

**작성일**: 2024년 11월 17일
**버전**: 1.0

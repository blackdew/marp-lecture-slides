---
name: Nx Console VS Code 확장 공급망 공격 — Claude Code 설정 파일 최초 타겟
description: 2026년 5월 18일, Nx Console VS Code 확장(220만 설치)이 11분간 악성 버전으로 교체됐다. 페이로드가 Claude Code 설정 파일을 명시적으로 탈취한 최초의 공급망 공격. GitHub 내부 저장소 3,800개 유출.
type: semantics-source
url: https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
source: news
discovered: 2026-05-26
category: failure-case
tags: [supply-chain-attack, nx-console, vscode, claude-code, teampcp, github, credential-theft, ai-tool-security, tanstack, openai, mistral]
relevance: high
---

# Nx Console VS Code 확장 공급망 공격 — Claude Code 설정 파일 최초 타겟

## 한 줄 요약

2026년 5월 18일, VS Code Marketplace에 악성 Nx Console 확장 프로그램(v18.95.0)이 11분간 배포됐다. 멀티스테이지 페이로드가 GitHub·AWS·npm 토큰 외에 **Claude Code 설정 파일(~/.claude/settings.json)을 명시적 타겟으로 포함**한 최초의 사례. GitHub 내부 저장소 3,800개가 유출됐고 OpenAI·Mistral·EU 집행위가 피해를 입었다.

## 핵심 사실

- **일시**: 2026년 5월 18일 12:30~12:48 UTC (약 11분간 악성 버전 활성)
- **공격자**: TeamPCP (선행 TanStack npm 공급망 공격과 동일 그룹)
- **대상 확장**: nrwl.angular-console (Nx Console) v18.95.0 — 약 220만 설치
- **공격 경로**: TanStack npm 패키지 공급망 공격 → Nx 개발자 1명의 GitHub 자격증명 탈취 → 악성 Nx Console 버전 Marketplace에 게시
- **페이로드**: 498KB 난독화 코드, 공식 nrwl/nx 저장소 숨겨진 고아 커밋에서 패치
- **탈취 대상**: GitHub 토큰, AWS 키, npm 토큰, 1Password 볼트, Kubernetes 시크릿, **Claude Code 설정 파일** (~/.claude/settings.json)
- **유출 채널**: HTTPS + GitHub API + DNS 터널링 (3중 채널)
- **macOS 백도어**: GitHub Search API를 4096비트 RSA 서명 데드드롭으로 사용하는 Python 영구 백도어
- **피해**: GitHub 내부 저장소 3,800개 (GitHub 발표: 2026-05-19), OpenAI 직원 기기 2대, Mistral AI 기기 1대 + 협박, European Commission, Grafana Labs
- **출처**: The Hacker News, CybersecurityNews, StepSecurity, OX Security, Bleeping Computer, GBHackers (6개 이상 매체)

## 공격 체인

```
TanStack npm 패키지 악성 코드
    → Nx 개발자 자격증명 탈취
    → Nx Console VS Code 확장 악성 버전 게시 (11분)
    → 개발자 워크스페이스에서 자격증명 일괄 수집
    → 3중 채널 유출 (HTTPS / GitHub API / DNS)
    → macOS 영구 백도어 설치
    → GitHub 내부 3,800개 저장소 유출
```

## 핵심 인사이트

### 1. AI 코딩 도구가 공급망 공격의 새로운 타겟
페이로드가 Claude Code 설정 파일(~/.claude/settings.json)을 명시적으로 탈취 대상으로 포함한 것은 처음 있는 일이다. Claude Code 설정이 탈취되면 공격자는 피해자의 파일 시스템·터미널·네트워크에 접근할 수 있다. **AI 코딩 도구 도입이 새로운 공격 표면을 만들었음**이 입증됐다.

### 2. 11분 창, 220만 설치 = 극단적 공격 효율
악성 버전이 활성화된 것은 11분. 그러나 VS Code 확장의 자동 업데이트 메커니즘이 속도를 증폭시켜 수천 명의 개발자가 영향을 받았다.

### 3. 공급망의 공급망: 연쇄 취약성
직접 원인은 Nx Console의 취약점이 아니었다. TanStack → Nx 개발자 → Nx Console 확장의 **2단계 연쇄 공급망 공격**이었다. 의존성 체인의 어느 한 노드도 무너지면 하류 전체가 위험해진다.

### 4. 3중 유출 채널: 어느 것을 차단해도 나머지로 유출
HTTPS가 차단돼도 GitHub API로, GitHub API가 차단돼도 DNS 터널링으로 데이터가 나간다. 기업 방화벽의 한계를 정확히 겨냥한 고급 회피 설계다.

### 5. AI 기업들도 예외 없이 피해
OpenAI와 Mistral이 피해 기업 목록에 포함됐다. AI를 만드는 회사도 동일한 개발 도구 생태계를 사용한다. **AI 보안에서 면책 특권은 없다.**

## 강의 활용 메모

### 고려대 컴공 페어 프롬프팅 강의용
- **AI 도구 도입 = 새로운 공격 표면**: AI 코딩 도구를 도입하면 그 도구의 설정 파일, API 키, 세션 권한이 모두 새로운 공격 대상이 된다. 페어 프롬프팅/AI 도구 사용 시 이 "새로운 공격 표면"을 인지해야 함.
- **공급망 보안 논의**: 신뢰하는 도구를 신뢰하는 것이 안전한가? VS Code 확장 11분 배포가 수천 명 피해로 연결된다.
- **3가지 AI 실패 벡터 묶기**: Andon Cafe(AI의 실수) → PocketOS(AI가 규칙 위반) → Mexico(AI가 공격에 동원) → Nx Console(AI 도구 생태계 공급망 침해). 네 가지를 연결해 AI 시대의 리스크 지형도를 그릴 수 있다.

## 원본 메모 / 인용

- "The payload also specifically targets Claude Code configuration files (~/.claude/settings.json), marking what may be one of the first supply chain payloads designed to harvest AI coding assistant credentials." — 복수 출처
- "On May 19, 2026, GitHub publicly disclosed that approximately 3,800 internal repositories were exfiltrated as a result of the attack." — GitHub 공식 발표
- "In a fresh update shared on May 21, 2026, the Nx team officially acknowledged that one of its developers was compromised by a recent supply chain compromise targeting TanStack." — Nx 공식 발표

## 참고 링크

- The Hacker News (주요 출처): https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
- The Hacker News (GitHub 저장소 유출): https://thehackernews.com/2026/05/github-internal-repositories-breached.html
- StepSecurity (기술 분석): https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised
- OX Security: https://www.ox.security/blog/teampcp-strikes-again-how-a-trojan-vs-code-extension-brought-down-github/
- CybersecurityNews: https://cybersecuritynews.com/nx-console-vs-code-extension-compromised/
- Bleeping Computer: https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/

## 후속 모니터링 포인트

- VS Code Marketplace의 확장 프로그램 보안 검증 프로세스 개선 여부
- Anthropic의 Claude Code API 키 로테이션 권고 여부
- TeamPCP의 추가 공격 활동
- GitHub 내부 저장소 유출의 2차 피해
- AI 코딩 도구 자격증명을 타겟으로 하는 추가 공급망 공격 사례

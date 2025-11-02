# Part 04: MCP & Hooks

---

# Part 4: MCP & Hooks

Claude Code 확장하기

---

## MCP란 무엇인가?

Model Context Protocol - AI와 외부 도구 연결

**MCP의 역할**

- Claude Code에 새로운 도구 추가
- 외부 데이터 소스 접근
- 서드파티 서비스 통합
- 표준화된 프로토콜

---

## MCP 개념

**기본 구조**

```
Claude Code ← MCP Protocol → MCP Server ← 외부 서비스
```

**MCP Server 예시**

- 파일 시스템 접근
- 데이터베이스 쿼리
- API 호출
- 브라우저 자동화

---

## MCP vs 기본 도구

| 구분 | 기본 도구 | MCP |
|-----|---------|-----|
| 범위 | 파일, Git, Bash 등 | 무제한 확장 |
| 설치 | 기본 제공 | 별도 설치 필요 |
| 커스터마이징 | 제한적 | 완전한 자유 |
| 예시 | Read, Write, Bash | DB 쿼리, 웹 스크래핑 |

---

## MCP 서버 설치

**1. MCP 서버 찾기**

- [modelcontextprotocol.io](https://modelcontextprotocol.io)
- GitHub에서 "mcp server" 검색
- 커뮤니티 추천

**2. 설정 파일 수정**

```bash
~/.config/claude/config.json
```

**3. Claude Code 재시작**

새 MCP 도구 사용 가능

---

## 유용한 MCP 서버 (1/2)

**파일 시스템**

- `@modelcontextprotocol/server-filesystem`
- 파일 읽기/쓰기 확장 기능

**데이터베이스**

- `@modelcontextprotocol/server-postgres`
- PostgreSQL 쿼리 실행

---

## 유용한 MCP 서버 (2/2)

**웹 자동화**

- `@modelcontextprotocol/server-puppeteer`
- 브라우저 제어 및 스크래핑

**외부 API**

- 다양한 서드파티 API 서버들
- 날씨, 주식, 뉴스 등

---

## MCP 설정 예시

**config.json 구조**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

---

## MCP 활용 예시

**시나리오: 데이터베이스 마이그레이션**

```
사용자: "users 테이블 스키마를 확인하고
        새 email 필드를 추가해줘"

Claude Code:
1. MCP PostgreSQL 서버로 스키마 조회
2. 마이그레이션 SQL 생성
3. 안전성 검토
4. 실행 여부 확인
```

---

## MCP 주의사항

| 주의사항 | 설명 |
|---------|------|
| 보안 | MCP 서버에 접근 권한 부여 시 주의 |
| 성능 | 일부 MCP 서버는 느릴 수 있음 |
| 의존성 | MCP 서버 업데이트 관리 필요 |
| 호환성 | Claude Code 버전과 호환성 확인 |

---

# Hooks

이벤트 기반 자동화

---

## Hooks란 무엇인가?

특정 이벤트 발생 시 자동 실행되는 스크립트

**Hooks의 특징**

- 도구 호출 전후에 실행
- 셸 명령어로 구현
- 프로젝트별 설정 가능
- 워크플로우 자동화

---

## Hooks 종류

| Hook | 실행 시점 | 용도 |
|------|---------|------|
| user-prompt-submit | 사용자 메시지 전송 시 | 입력 검증, 로깅 |
| pre-tool-call | 도구 실행 전 | 권한 확인, 백업 |
| post-tool-call | 도구 실행 후 | 결과 검증, 알림 |

---

## Hooks 설정 방법

**설정 파일 위치**

```bash
~/.config/claude/config.json
```

**Hook 추가 예시**

```json
{
  "hooks": {
    "pre-tool-call": "echo 'Running tool...'",
    "post-tool-call": "./scripts/notify.sh"
  }
}
```

---

## Hook 실습: 자동 백업

**시나리오**

파일 편집 전 자동 백업 생성

**pre-tool-call Hook**

```bash
#!/bin/bash
# .config/claude/hooks/backup.sh

if [[ "$TOOL_NAME" == "Write" ]]; then
  FILE_PATH=$(echo "$TOOL_INPUT" | jq -r '.file_path')
  if [[ -f "$FILE_PATH" ]]; then
    cp "$FILE_PATH" "$FILE_PATH.backup"
    echo "Backup created: $FILE_PATH.backup"
  fi
fi
```

---

## Hook 활용 예시 (1/2)

**자동 포맷팅**

```bash
# post-tool-call hook
if [[ "$TOOL_NAME" == "Write" ]]; then
  FILE_PATH=$(echo "$TOOL_INPUT" | jq -r '.file_path')
  if [[ "$FILE_PATH" == *.js ]]; then
    prettier --write "$FILE_PATH"
  fi
fi
```

---

## Hook 활용 예시 (2/2)

**민감 정보 체크**

```bash
# pre-tool-call hook
if [[ "$TOOL_NAME" == "Bash" ]]; then
  COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command')
  if [[ "$COMMAND" == *"rm -rf"* ]]; then
    echo "Dangerous command blocked"
    exit 1
  fi
fi
```

---

## Hook 피드백 처리

**Hook 메시지**

Hook의 출력은 `<user-prompt-submit-hook>` 태그로 표시

**차단된 작업**

- Hook이 non-zero exit code 반환 시 작업 차단
- Claude Code는 대안 시도 가능
- 사용자에게 확인 요청 가능

---

## Hook 디버깅

**확인 사항**

- Hook 스크립트 실행 권한 (`chmod +x`)
- 환경 변수 접근 가능 여부
- 출력이 표준 출력으로 전달되는지

**로깅**

```bash
echo "Hook executed: $TOOL_NAME" >> /tmp/claude-hooks.log
```

---

## Hooks 활용 팁

| 팁 | 설명 |
|----|------|
| 최소한으로 유지 | Hook이 너무 많으면 느려짐 |
| 명확한 메시지 | Hook 실행 시 무엇을 했는지 출력 |
| 조건부 실행 | 필요한 경우에만 실행 |
| 에러 처리 | Hook 실패 시 명확한 메시지 |

---

## MCP vs Hooks 비교

| 구분 | MCP | Hooks |
|-----|-----|-------|
| 목적 | 새 도구 추가 | 기존 워크플로우 자동화 |
| 복잡도 | 높음 | 낮음 |
| 유연성 | 매우 높음 | 제한적 |
| 사용 난이도 | 어려움 | 쉬움 |

**선택 기준**

- 새 기능 필요 → MCP
- 자동화만 필요 → Hooks

---

## MCP & Hooks 정리

**MCP**

- 외부 도구와 데이터 소스 연결
- 무한한 확장 가능성
- 설정 및 유지보수 필요

**Hooks**

- 이벤트 기반 자동화
- 간단한 스크립트로 구현
- 워크플로우 개선

**함께 사용하기**

MCP로 기능 추가 + Hooks로 자동화

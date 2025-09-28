#!/bin/bash

# 이 스크립트는 강의안 마크다운 파일로부터
# HTML, PPTX와 PDF 파일을 생성합니다.
# 사용법: ./generate-presentation.sh <폴더명> <마크다운파일명>

# 인자 확인
if [ $# -ne 2 ]; then
    echo "사용법: $0 <폴더명> <마크다운파일명>"
    echo "예시: $0 lecture-01-ai-data-coding lecture.md"
    exit 1
fi

FOLDER_NAME=$1
MD_FILE=$2
INPUT_PATH="${FOLDER_NAME}/${MD_FILE}"

# 입력 파일 존재 확인
if [ ! -f "$INPUT_PATH" ]; then
    echo "오류: 파일을 찾을 수 없습니다: $INPUT_PATH"
    exit 1
fi

# 출력 파일명 생성 (확장자 제거)
OUTPUT_BASE=$(basename "$MD_FILE" .md)

echo "=== 프레젠테이션 생성 시작 ==="
echo "입력 파일: $INPUT_PATH"
echo "출력 폴더: $FOLDER_NAME"
echo ""

# HTML 생성 (Puppeteer 오류 방지를 위해 우선 HTML로 생성)
echo "HTML 프레젠테이션 생성 중 (${OUTPUT_BASE}.html)..."
marp "$INPUT_PATH" --html -o "${FOLDER_NAME}/${OUTPUT_BASE}.html" --allow-local-files

# 이미지 폴더 복사 (HTML과 같은 위치에)
if [ -d "${FOLDER_NAME}/images" ]; then
    echo "이미지 폴더 복사 중..."
    cp -r "${FOLDER_NAME}/images" "${FOLDER_NAME}/"
fi

echo ""
echo "=== 생성 완료 ==="
echo "생성된 파일:"
echo "  - ${FOLDER_NAME}/${OUTPUT_BASE}.html"
echo ""
echo "PDF나 PPTX가 필요하시면 브라우저에서 HTML을 열어 인쇄 기능을 사용하세요."


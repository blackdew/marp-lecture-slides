#!/bin/bash

# 각 강의에 대한 상세 페이지(index.html) 생성 스크립트
# 메타정보 + iframe + 댓글 시스템

# 강의 정보 배열 (폴더명|제목|부제|대상|시간|구성|평가|설명)
declare -a LECTURES=(
    "lecture-09-agent-hackathon|Lecture 09: Just Plan It!|AI 에이전트 해커톤|모든 레벨|300분|6개 Part|A (91/100)|5시간 집중 워크숍. 환경 설정부터 팀 해커톤까지, AI Agent 완전 체험."
    "lecture-10-antigravity-gemini|Lecture 10: AI 에이전트 활용|Do-See-Ask-Learn 실습|비개발자|360분|6개 Part|미평가|Do-See-Ask-Learn 사이클로 배우는 AI 에이전트. JavaScript 기초부터 파일 자동화까지."
    "lecture-11-agent-life-transition|Lecture 11: Just Plan It!!|AI Agent로 일과 삶의 전환|대학생/교직원|120분|5개 Part|미평가|동명대학교 특강. AI Agent 체험부터 업무 자동화, 팀 해커톤까지."
    "lecture-12-agent-life-transition|Lecture 12: AI Agent 활용|생활/업무 전환|대학생/교직원|120분|4개 Act|미평가|동명대학교 특강. Agent 개념 이해부터 역할별 실습, 삶의 전환 로드맵까지."
)

# 함수: index.html 생성
generate_index_html() {
    local folder=$1
    local title=$2
    local subtitle=$3
    local target=$4
    local duration=$5
    local structure=$6
    local rating=$7
    local description=$8

    # 강의 번호 추출
    local lecture_num=$(echo "$folder" | grep -oE "lecture-[0-9]+" | sed 's/lecture-//')

    # 리뷰 파일 경로 결정
    local review_file="../../docs/review-${folder}.md"

    cat > "lectures/${folder}/index.html" << EOF
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} ${subtitle}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }

        .header h1 {
            color: #2c3e50;
            font-size: 2em;
            margin-bottom: 10px;
        }

        .header .subtitle {
            font-size: 1.2em;
            color: #555;
            margin-bottom: 20px;
        }

        .meta-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }

        .meta-item {
            padding: 15px;
            background: #f8f9fa;
            border-radius: 6px;
            border-left: 4px solid #3498db;
        }

        .meta-item strong {
            display: block;
            color: #2c3e50;
            margin-bottom: 5px;
            font-size: 0.9em;
        }

        .meta-item span {
            color: #555;
            font-size: 1em;
        }

        .rating {
            display: inline-block;
            padding: 5px 12px;
            background: #28a745;
            color: white;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9em;
        }

        .description {
            margin: 20px 0;
            padding: 20px;
            background: #e3f2fd;
            border-radius: 6px;
            border-left: 4px solid #2196f3;
        }

        .description p {
            color: #1565c0;
            font-size: 1.1em;
            line-height: 1.8;
        }

        .actions {
            display: flex;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 12px 24px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
        }

        .btn-primary {
            background: #3498db;
            color: white;
        }

        .btn-primary:hover {
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(52, 152, 219, 0.3);
        }

        .btn-secondary {
            background: white;
            color: #3498db;
            border: 2px solid #3498db;
        }

        .btn-secondary:hover {
            background: #3498db;
            color: white;
        }

        .slide-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }

        .slide-container h2 {
            margin-bottom: 15px;
            color: #2c3e50;
        }

        iframe {
            width: 100%;
            height: 600px;
            border: none;
            border-radius: 6px;
        }

        .comments-section {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .comments-section h2 {
            color: #2c3e50;
            margin-bottom: 20px;
        }

        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }

            .header h1 {
                font-size: 1.5em;
            }

            .meta-info {
                grid-template-columns: 1fr;
            }

            iframe {
                height: 400px;
            }

            .actions {
                flex-direction: column;
            }

            .btn {
                width: 100%;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- 헤더 섹션 -->
        <div class="header">
            <h1>🎯 ${title}</h1>
            <p class="subtitle">${subtitle}</p>

            <!-- 메타 정보 -->
            <div class="meta-info">
                <div class="meta-item">
                    <strong>📊 대상</strong>
                    <span>${target}</span>
                </div>
                <div class="meta-item">
                    <strong>⏱️ 시간</strong>
                    <span>${duration}</span>
                </div>
                <div class="meta-item">
                    <strong>📁 구성</strong>
                    <span>${structure}</span>
                </div>
                <div class="meta-item">
                    <strong>⭐ 평가</strong>
                    <span class="rating">${rating}</span>
                </div>
            </div>

            <!-- 강의 설명 -->
            <div class="description">
                <p>${description}</p>
            </div>

            <!-- 액션 버튼 -->
            <div class="actions">
                <a href="lecture.html" target="_blank" class="btn btn-primary">
                    🖥️ 슬라이드 전체화면으로 보기
                </a>
                <a href="${review_file}" class="btn btn-secondary">
                    📝 강의 리뷰 보기
                </a>
                <a href="../../" class="btn btn-secondary">
                    🏠 전체 강의 목록
                </a>
            </div>
        </div>

        <!-- 슬라이드 미리보기 -->
        <div class="slide-container">
            <h2>📊 슬라이드 미리보기</h2>
            <p style="color: #666; margin-bottom: 15px;">
                아래에서 슬라이드를 미리 볼 수 있습니다. 전체화면으로 보려면 위의 버튼을 클릭하세요.
            </p>
            <iframe src="lecture.html" title="${title} 슬라이드"></iframe>
        </div>

        <!-- 댓글 섹션 -->
        <div class="comments-section">
            <h2>💬 강의에 대한 의견을 남겨주세요</h2>
            <p style="color: #666; margin-bottom: 20px;">
                GitHub 계정으로 로그인하여 댓글을 남길 수 있습니다.
            </p>

            <!-- Giscus 댓글 시스템 -->
            <script src="https://giscus.app/client.js"
                    data-repo="blackdew/marp-lecture-slides"
                    data-repo-id="R_kgDONgVZDg"
                    data-category="General"
                    data-category-id="DIC_kwDONgVZDs4Clel5"
                    data-mapping="pathname"
                    data-strict="0"
                    data-reactions-enabled="1"
                    data-emit-metadata="0"
                    data-input-position="bottom"
                    data-theme="preferred_color_scheme"
                    data-lang="ko"
                    crossorigin="anonymous"
                    async>
            </script>
        </div>
    </div>
</body>
</html>
EOF

    echo "✓ Generated: lectures/${folder}/index.html"
}

# 메인 실행
echo "=== 강의 상세 페이지 생성 시작 ==="
echo ""

for lecture in "${LECTURES[@]}"; do
    IFS='|' read -r folder title subtitle target duration structure rating description <<< "$lecture"

    # lecture.html이 있는지 확인
    if [ -f "lectures/${folder}/lecture.html" ]; then
        generate_index_html "$folder" "$title" "$subtitle" "$target" "$duration" "$structure" "$rating" "$description"
    else
        echo "⚠ Skipped: lectures/${folder}/lecture.html not found"
    fi
done

echo ""
echo "=== 생성 완료 ==="
echo "브라우저에서 lectures/<폴더>/index.html을 열어보세요!"

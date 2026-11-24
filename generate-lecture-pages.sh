#!/bin/bash

# 각 강의에 대한 상세 페이지(index.html) 생성 스크립트
# 메타정보 + iframe + 댓글 시스템

# 강의 정보 배열 (폴더명|제목|부제|대상|시간|구성|평가|설명|메인파일)
# 평가 필드는 "라벨:값" 형태로 쓰면 라벨을 바꿉니다 (예: 산출물:프로토타입 5개 이상)
# 메인파일을 비워 두면 lecture.html 을 씁니다. 자체 HTML 덱이 있으면 그 파일명을 적습니다.
declare -a LECTURES=(
    "lecture-09-agent-hackathon|Lecture 09: Just Plan It!|AI 에이전트 해커톤|모든 레벨|300분|6개 Part|A (91/100)|5시간 집중 워크숍. 환경 설정부터 팀 해커톤까지, AI Agent 완전 체험."
    "lecture-10-antigravity-gemini|Lecture 10: Gemini CLI|AI 에이전트 활용 마스터 클래스|비개발자 및 일반 업무 사용자|360분 (6시간)|6개 Part|산출물:프로토타입 5개 이상|비개발자를 위한 실무 자동화 + 코딩. Do-See-Ask-Learn 사이클로 배우는 AI 에이전트."
    "lecture-11-agent-life-transition|Lecture 11: Just Plan It!!|AI Agent로 일과 삶의 전환|대학생/교직원|120분|5개 Part|미평가|동명대학교 특강. AI Agent 체험부터 업무 자동화, 팀 해커톤까지."
    "lecture-12-agent-life-transition|Lecture 12: AI Agent 활용|생활/업무 전환|대학생/교직원|120분|4개 Act|미평가|동명대학교 특강. Agent 개념 이해부터 역할별 실습, 삶의 전환 로드맵까지."
    "lecture-15-codex-4weeks|Lecture 15: 에이전트와 함께하는 삶의 전환|Codex 4주 과정 (1주차)|비전공자 30~60대|120분×4주|4개 주차|미평가|비전공자 대상 4주 연속 과정. 1주차는 동기부여와 생각의 전환. 터미널 없이 ChatGPT 데스크탑의 Codex만 사용.|week1.html"
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
    local mainfile=${9:-lecture.html}

    # 강의 번호 추출
    local lecture_num=$(echo "$folder" | grep -oE "lecture-[0-9]+" | sed 's/lecture-//')

    # 네 번째 메타 항목: "라벨:값" 형태면 라벨을 바꾸고, 아니면 평가로 봅니다
    local meta4_label="평가"
    local meta4_value="$rating"
    local meta4_class=' class="rating"'
    case "$rating" in
      *:*)
        meta4_label="${rating%%:*}"
        meta4_value="${rating#*:}"
        meta4_class=""
        ;;
    esac

    # 액션 버튼: 리뷰 문서가 실제로 있을 때만 링크를 넣습니다
    local actions_html="                <a href=\"${mainfile}\" target=\"_blank\" class=\"btn btn-primary\">
                    슬라이드 전체화면으로 보기
                </a>"
    if [ -f "docs/review-${folder}.md" ]; then
      actions_html="${actions_html}
                <a href=\"../../docs/review-${folder}.md\" class=\"btn btn-secondary\">
                    강의 리뷰 보기
                </a>"
    fi
    actions_html="${actions_html}
                <a href=\"../../\" class=\"btn btn-secondary\">
                    전체 강의 목록
                </a>"

    cat > "lectures/${folder}/index.html" << EOF
<!DOCTYPE html>
<!-- 이 파일은 generate-lecture-pages.sh 가 생성합니다. 직접 고치지 마세요.
     내용을 바꾸려면 그 스크립트의 LECTURES 배열을 고치고 다시 실행하세요. -->
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} ${subtitle}</title>
    <link rel="stylesheet" href="../../assets/css/giscus-custom.css">
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
            <h1>${title}</h1>
            <p class="subtitle">${subtitle}</p>

            <!-- 메타 정보 -->
            <div class="meta-info">
                <div class="meta-item">
                    <strong>대상</strong>
                    <span>${target}</span>
                </div>
                <div class="meta-item">
                    <strong>시간</strong>
                    <span>${duration}</span>
                </div>
                <div class="meta-item">
                    <strong>구성</strong>
                    <span>${structure}</span>
                </div>
                <div class="meta-item">
                    <strong>${meta4_label}</strong>
                    <span${meta4_class}>${meta4_value}</span>
                </div>
            </div>

            <!-- 강의 설명 -->
            <div class="description">
                <p>${description}</p>
            </div>

            <!-- 액션 버튼 -->
            <div class="actions">
${actions_html}
            </div>
        </div>

        <!-- 슬라이드 미리보기 -->
        <div class="slide-container">
            <h2>슬라이드 미리보기</h2>
            <p style="color: #666; margin-bottom: 15px;">
                아래에서 슬라이드를 미리 볼 수 있습니다. 전체화면으로 보려면 위의 버튼을 클릭하세요.
            </p>
            <iframe src="${mainfile}" title="${title} 슬라이드"></iframe>
        </div>

        <!-- 댓글 섹션 -->
        <div class="comments-section">
            <h2>강의에 대한 의견을 남겨주세요</h2>
            <p>
                GitHub 계정으로 로그인하여 댓글을 남길 수 있습니다.
            </p>

            <script src="https://giscus.app/client.js"
                    data-repo="blackdew/marp-lecture-slides"
                    data-repo-id="R_kgDOQElocA"
                    data-category="General"
                    data-category-id="DIC_kwDOQElocM4CyAGd"
                    data-mapping="specific"
                    data-term="${folder}"
                    data-strict="0"
                    data-reactions-enabled="1"
                    data-emit-metadata="0"
                    data-input-position="bottom"
                    data-theme="https://blackdew.github.io/marp-lecture-slides/assets/css/giscus-theme-custom.css"
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
    IFS='|' read -r folder title subtitle target duration structure rating description mainfile <<< "$lecture"
    mainfile=${mainfile:-lecture.html}

    # 메인 슬라이드 파일이 있는지 확인
    if [ -f "lectures/${folder}/${mainfile}" ]; then
        generate_index_html "$folder" "$title" "$subtitle" "$target" "$duration" "$structure" "$rating" "$description" "$mainfile"
    else
        echo "⚠ Skipped: lectures/${folder}/${mainfile} not found"
    fi
done

echo ""
echo "=== 생성 완료 ==="
echo "브라우저에서 lectures/<폴더>/index.html을 열어보세요!"

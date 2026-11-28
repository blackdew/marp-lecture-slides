# -*- coding: utf-8 -*-
"""2주차 화면 캡처. ../captures/ 의 파일을 덱에 넣을 수 있는 data URI 로 읽습니다.

1주차 imgs.py 는 base64 문자열을 파일에 직접 적어 두었습니다. 여기서는 원본 이미지를
captures/ 에 두고 빌드할 때 읽습니다. 캡처를 바꾸려면 captures/ 의 파일만 교체합니다.
덱 생성기는 이 data URI 를 다시 ../images/ 의 파일로 저장해서 불러옵니다.
"""
import base64
import pathlib

_CAP = pathlib.Path(__file__).resolve().parent.parent / 'captures'


def _uri(name):
    return 'data:image/jpeg;base64,' + base64.b64encode((_CAP / name).read_bytes()).decode()


# 2026-11-26, Codex 에 실제로 요청해서 받은 카드. CARD_MOTHER 는 앱에 들어 있는 실행 파일의 결과이고,
# CARD_REQUEST_ONLY 를 받은 방식은 기록으로 다시 확인하지 못했습니다
CARD_REQUEST_ONLY = _uri('card-request-only.jpg')   # 요청만 적음: “연말 인사 카드를 웹페이지로 만들어줘”
CARD_MOTHER = _uri('card-mother.jpg')               # 내 상황과 확인 방법을 더함

# 2026-11-27, ChatGPT 데스크탑 앱의 Codex (Mac) 에 실제로 요청해서 받은 결과
SNOWMAN = _uri('snowman.jpg')                       # Freeform 을 조작해서 그리고 저장한 눈사람
CARD_IMAGE = _uri('card-image.jpg')                 # 이미지 생성: 눈 내린 마을 위로 해가 떠오르는 수채화
SHORTS_FRAME = _uri('shorts-frame.jpg')             # 쇼츠 영상의 한 장면 (그림 + 음성 + 자막)

# 2026-11-27, 앱에 들어 있는 Codex 실행 파일에 실제로 요청해서 받은 결과
CARD_PAGE = _uri('card-page.jpg')                   # 눈사람 그림과 눈 내린 마을 그림을 넣은 연하장 페이지
REPORT_PLAN = _uri('report-plan.jpg')               # 부모님과 가는 경주 2박 3일 여행 계획 보고서
REPORT_TOPIC = _uri('report-topic.jpg')             # AI 에이전트 최신 소식 보고서

# 2026-11-28, 앱에 들어 있는 Codex 실행 파일. 연하장을 만들고 고친 뒤 프롬프트로 정리해서 다시 쓴 결과
CARD_FIRST = _uri('card-first.jpg')                 # 요청을 여러 번 주고받아 만든 어머니 연하장
CARD_REUSE = _uri('card-reuse.jpg')                 # 저장한 프롬프트로 새 채팅에서 한 번에 만든 아버지 연하장

# 2026-11-28, 강사가 제공한 그림. 피클을 만든 회사가 공개한 소개 화면이고, 직접 써서 받은 결과가 아닙니다
PICKLE_INTRO = _uri('pickle-intro.jpg')             # 전화 대행, 쇼핑과 주문, 예약과 예매를 보여 주는 화면
# 2026-11-28, 애플의 앱 정보 조회(itunes.apple.com/lookup)가 알려 준 주소에서 받은 앱 아이콘 (512x512)
PICKLE_ICON = _uri('pickle-icon.jpg')

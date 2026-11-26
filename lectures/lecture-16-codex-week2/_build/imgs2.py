# -*- coding: utf-8 -*-
"""2주차 화면 캡처. ../captures/ 의 파일을 덱에 넣을 수 있는 data URI 로 읽습니다.

1주차 imgs.py 는 base64 문자열을 파일에 직접 적어 두었습니다. 여기서는 원본 이미지를
captures/ 에 두고 빌드할 때 읽습니다. 캡처를 바꾸려면 captures/ 의 파일만 교체합니다.
"""
import base64
import pathlib

_CAP = pathlib.Path(__file__).resolve().parent.parent / 'captures'


def _uri(name):
    return 'data:image/jpeg;base64,' + base64.b64encode((_CAP / name).read_bytes()).decode()


# 2026-11-26, ChatGPT 데스크탑 앱의 Codex 에 실제로 요청해서 받은 카드
CARD_REQUEST_ONLY = _uri('card-request-only.jpg')   # 요청만 적음: “연말 인사 카드를 웹페이지로 만들어줘”
CARD_MOTHER = _uri('card-mother.jpg')               # 내 상황과 확인 방법을 더함: 실습 1 의 요청 전체
CARDS_THREE = _uri('cards-three.jpg')               # 세 가지 방식으로 만든 카드 (어머니, 김 선생님, 영희)

# 2026-11-26, 앱에 들어 있는 Codex 실행 파일에 실제로 요청해서 받은 결과 (새 방식 시연)
CARDS_MATERIAL = _uri('cards-material.jpg')         # 폴더의 어머니 카드와, 그 카드를 읽고 만든 이모 카드
CARDS_RULES = _uri('cards-rules.jpg')               # 저장한 지침 파일의 내용과, 새 채팅에서 만든 아버지 카드

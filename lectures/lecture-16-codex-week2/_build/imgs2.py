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
CARD_WITH_CONTEXT = _uri('card-with-context.jpg')   # 내 상황과 확인 방법을 더함: 실습 1 의 요청 전체

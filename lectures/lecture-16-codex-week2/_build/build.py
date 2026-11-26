# -*- coding: utf-8 -*-
"""발표용 HTML 을 뽑습니다.  python3 build.py 2  →  ../week2.html"""
import importlib
import pathlib
import sys

import _shared                                    # noqa: F401  (sys.path 설정)
import deck
from deck import page

out = pathlib.Path(__file__).resolve().parent.parent
# deck.IMG 는 자기 파일 위치(1강 폴더) 기준입니다. 이 강의 폴더로 돌려놓지 않으면
# 그림 파일이 1강의 images/ 에 저장됩니다
deck.IMG = out / 'images'
for n in (sys.argv[1:] or ['2']):
    m = importlib.import_module('w' + n)
    html = page(m.TITLE, m.S)
    p = out / ('week' + n + '.html')
    p.write_text(html, encoding='utf-8')
    print('week%s.html  %7d bytes  %2d slides  "%s"' % (n, len(html.encode()), len(m.S), m.TITLE))

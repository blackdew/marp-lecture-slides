# -*- coding: utf-8 -*-
"""같은 원본에서 Marp 마크다운을 뽑습니다.  python3 build_marp.py 2  →  ../lecture.md"""
import importlib
import pathlib
import sys

import _shared                                    # noqa: F401  (sys.path 설정)
import marpdeck

sys.modules['deck'] = marpdeck                    # from deck import * → marpdeck

out = pathlib.Path(__file__).resolve().parent.parent

# marpdeck.IMG 는 자기 파일 위치(1강 폴더) 기준입니다. 이 강의 폴더로 돌려놓지 않으면
# 인라인 SVG 가 1강의 images/ 에 떨어집니다.
marpdeck.IMG = out / 'images'
args = sys.argv[1:] or ['2']
for n in args:
    m = importlib.import_module('w' + n)
    md = marpdeck.page(m.TITLE, m.S)
    name = 'lecture.md' if len(args) == 1 else ('week%s.md' % n)
    p = out / name
    p.write_text(md, encoding='utf-8')
    print('%-12s %7d bytes  %2d slides  "%s"' % (name, len(md.encode()), len(m.S), m.TITLE))

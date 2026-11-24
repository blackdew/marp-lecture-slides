# -*- coding: utf-8 -*-
"""같은 원본(wN.py)에서 Marp 마크다운을 뽑습니다.

    python3 build_marp.py 1          → ../lecture.md  (1주차)
    python3 build_marp.py 1 2 3 4    → ../week1.md … week4.md

deck 대신 marpdeck 을 끼워 넣는 것 말고는 build.py 와 같습니다.
"""
import importlib, pathlib, sys

sys.path.insert(0, '.')
import marpdeck
sys.modules['deck'] = marpdeck          # from deck import * → marpdeck

out = pathlib.Path('..')
args = sys.argv[1:] or ['1']
for n in args:
    m = importlib.import_module('w' + n)
    md = marpdeck.page(m.TITLE, m.S)
    name = 'lecture.md' if (n == '1' and len(args) == 1) else ('week%s.md' % n)
    p = out / name
    p.write_text(md, encoding='utf-8')
    print('%-12s %6d bytes  %2d slides  "%s"' % (name, len(md.encode()), len(m.S), m.TITLE))

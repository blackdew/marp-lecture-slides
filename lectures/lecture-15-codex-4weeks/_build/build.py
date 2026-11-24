# -*- coding: utf-8 -*-
import importlib, io, sys, pathlib
sys.path.insert(0, '.')
from deck import page
out = pathlib.Path('..')
for n in sys.argv[1:]:
    m = importlib.import_module('w' + n)
    html = page(m.TITLE, m.S)
    p = out / ('week' + n + '.html')
    p.write_text(html, encoding='utf-8')
    print('week%s.html  %6d bytes  %2d slides  "%s"' % (n, len(html.encode()), len(m.S), m.TITLE))

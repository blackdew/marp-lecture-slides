# -*- coding: utf-8 -*-
"""w2.py 에서 타임라인을 뽑아 ../outline.md 를 만듭니다.  python3 outline.py 2"""
import importlib
import pathlib
import re
import sys

import _shared                                      # noqa: F401
from deck import page                               # noqa: F401  (import 순서 고정)

n = (sys.argv[1:] or ['2'])[0]
m = importlib.import_module('w' + n)
out = pathlib.Path(__file__).resolve().parent.parent

rows = []
for html in m.S:
    title = re.search(r'data-title="([^"]*)"', html)
    part = re.search(r'data-part="([^"]*)"', html)
    if not title:
        continue
    t, p = title.group(1), (part.group(1) if part else '')
    if ' · ' in p:
        seg, tm = p.rsplit(' · ', 1)
    else:
        seg, tm = p, '·'
    rows.append((tm, seg, t))

lines = ['# 강의 개요: %s' % m.TITLE, '',
         '원본은 `_build/w%s.py` 하나입니다. 이 문서는 거기서 뽑은 목록이라 손으로 고치지 마세요.' % n,
         '슬라이드를 바꾸면 `python3 _build/outline.py %s` 로 이 파일도 다시 만드세요.' % n, '',
         '## 타임라인', '', '| # | 시각 | 구간 | 장표 |', '|---|---|---|---|']
for i, (tm, seg, t) in enumerate(rows, 1):
    lines.append('| %d | %s | %s | %s |' % (i, tm, seg, t))

lines += ['', '## 빌드', '', '```bash', 'cd _build',
          'python3 build.py %s        # → ../week%s.html  (발표용)' % (n, n),
          'python3 ../../lecture-15-codex-4weeks/_build/check.py ../week%s.html' % n,
          'python3 build_marp.py %s   # → ../lecture.md  (Marp)' % n,
          'python3 outline.py %s      # → ../outline.md' % n,
          'cd ../../.. && ./generate-presentation.sh lecture-16-codex-week2 lecture.md',
          '```', '']
(out / 'outline.md').write_text('\n'.join(lines), encoding='utf-8')
print('outline.md  %d 장표' % len(rows))

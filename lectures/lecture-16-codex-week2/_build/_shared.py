# -*- coding: utf-8 -*-
"""공용 생성기 경로를 잡습니다.

deck.py · style.py · svgw.py · svg1~3.py · marpdeck.py 는 1강 폴더에 있는 것을
그대로 씁니다. 복사하면 강의가 늘어날 때마다 갈라지기 때문입니다.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SHARED = HERE.parent.parent / 'lecture-15-codex-4weeks' / '_build'

if not SHARED.is_dir():
    raise SystemExit('공용 생성기를 찾지 못했습니다: %s' % SHARED)

for p in (str(HERE), str(SHARED)):      # 이 폴더가 먼저. 같은 이름이면 여기 것이 이깁니다
    if p in sys.path:
        sys.path.remove(p)
sys.path.insert(0, str(SHARED))
sys.path.insert(0, str(HERE))

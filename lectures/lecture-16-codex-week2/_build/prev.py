# -*- coding: utf-8 -*-
"""브라우저로 열 수 있게 발표용 조각을 문서로 감쌉니다.

    python3 prev.py 2 <출력폴더>

출력 폴더를 적지 않으면 OS 임시 폴더에 씁니다. 경로를 코드에 박지 않습니다.
"""
import pathlib
import sys
import tempfile

SK = ('<!doctype html><html><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
      '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui}'
      'img{max-width:100%}[hidden]{display:none!important}</style>')

src_dir = pathlib.Path(__file__).resolve().parent.parent
nums = [a for a in sys.argv[1:] if a.isdigit()] or ['2']
rest = [a for a in sys.argv[1:] if not a.isdigit()]
out = pathlib.Path(rest[0]) if rest else pathlib.Path(tempfile.gettempdir())
out.mkdir(parents=True, exist_ok=True)

for n in nums:
    src = (src_dir / ('week%s.html' % n)).read_text(encoding='utf-8')
    dst = out / ('prev%s.html' % n)
    dst.write_text(SK + '</head><body>' + src + '</body></html>', encoding='utf-8')
    print(dst)

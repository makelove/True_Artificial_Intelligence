# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 11:00
# @Author  : play4fun
# @File    : 将BT种子转换为磁力链代码1.py
# @Software: PyCharm

"""
将BT种子转换为磁力链代码1.py:
出错
"""

import bencode, hashlib, base64, urllib
from urllib.parse import urlencode
#bencode  ModuleNotFoundError: No module named 'BTL'

torrent = open('avator.torrent', 'rb').read()

metadata = bencode.bdecode(torrent)

hashcontents = bencode.bencode(metadata['info'])

digest = hashlib.sha1(hashcontents).digest()

b32hash = base64.b32encode(digest)

params = {'xt': 'urn:btih:%s' % b32hash,

          'dn': metadata['info']['name'],

          'tr': metadata['announce'],

          'xl': metadata['info']['length']}

paramstr = urlencode(params)

magneturi = 'magnet:?%s' % paramstr

print(magneturi)

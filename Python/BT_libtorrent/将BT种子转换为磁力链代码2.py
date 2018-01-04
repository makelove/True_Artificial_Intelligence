# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 11:03
# @Author  : play4fun
# @File    : 将BT种子转换为磁力链代码2.py
# @Software: PyCharm

"""
将BT种子转换为磁力链代码2.py:
http://www.au92.com/archives/P-y-t-h-o-n-jiang-B-T-zhong-zi-wen-jian-zhuan-huan-wei-ci-li-lian-de-liang-zhong-fang-fa.html
"""

import libtorrent as bt
info = bt.torrent_info('avator.torrent')
# info
print("magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name()))
#magnet:?xt=urn:btih:539390d341f8c18400052ed905f77e48d6ebe40e&dn=Avatar ECE (2009) [1080p]

#这样也可以
magnet="magnet:?xt=urn:btih:%s"%info.info_hash()
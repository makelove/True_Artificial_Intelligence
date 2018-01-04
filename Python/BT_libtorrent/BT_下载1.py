# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 12:04
# @Author  : play4fun
# @File    : BT_下载1.py
# @Software: PyCharm

"""
BT_下载1.py:
https://gist.github.com/codeboy/923f74b72abda9502f42
"""

'''
You should try libtorrent (rasterbar). http://libtorrent.org
If you want to write your client in python, on linux, install it with:
sudo apt-get install python-libtorrent
A very simple example of python code to use it to download a torrent:
'''

import libtorrent as lt
import time
import sys

ses = lt.session()
ses.listen_on(6881, 6891)

info = lt.torrent_info(sys.argv[1])#种子文件
h = ses.add_torrent({'ti': info, 'save_path': './'})
print 'starting', h.name()

while (not h.is_seed()):
   s = h.status()

   state_str = ['queued', 'checking', 'downloading metadata', \
      'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
   print '\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
      (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
      s.num_peers, state_str[s.state]),
   sys.stdout.flush()

   time.sleep(1)

print h.name(), 'complete'

'''
(.py3) pro:test3 play$ python2 /Users/play/github/True_Artificial_Intelligence/Python/BT_libtorrent/BT_下载1.py  ./\[zooqle.com\]\ American\ Housewife\ S02E11\ HDTV\ x264-SVA\ \[eztv\].torrent
starting American.Housewife.S02E11.HDTV.x264-SVA[eztv].mkv
99.90% complete (down: 276.0 kb/s up: 151.0 kB/s peers: 80) downloading American.Housewife.S02E11.HDTV.x264-SVA[eztv].mkv complete
'''
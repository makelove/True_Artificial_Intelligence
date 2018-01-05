# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 17:21
# @Author  : play4fun
# @File    : 新建torrent文件1.py
# @Software: PyCharm

"""
新建torrent文件1.py:
https://stackoverflow.com/questions/28041730/create-new-torrent-and-seed

阿凡达Avatar ECE (2009) [1080p]
udp://tracker.yify-torrents.com/announce
http://tracker.yify-torrents.com/announce
udp://tracker.1337x.org:80/announce
udp://exodus.desync.com:6969
udp://tracker.istole.it:80
udp://tracker.ccc.de:80/announce
http://fr33dom.h33t.com:3310/announce
udp://tracker.publicbt.com:80
udp://coppersurfer.tk:6969/announce
udp://tracker.openbittorrent.com:80/announce

????
问题已经被解决，使用不同的跟踪器，而不是“trackerList”列出。代码是正确的。
"""

import sys
import time
import libtorrent as lt

files_bt=sys.argv[1]

#Create torrent
fs = lt.file_storage()
lt.add_files(fs, files_bt)
t = lt.create_torrent(fs)

#
# trackerList = ['udp://tracker.istole.it:80/announce',
#            'udp://tracker.ccc.de:80/announce',
#            'http://tracker.torrentbay.to:6969/announce',
#            'udp://fr33domtracker.h33t.com:3310/announce',
#            'udp://tracker.publicbt.com:80/announce',
#            'udp://tracker.openbittorrent.com:80/announce',
#            'udp://11.rarbg.com/announce'
#            'udp://tracker.istole.it:80/announce']
#更换Tracker 就行了!
trackerList=["udp://tracker.coppersurfer.tk:6969",
"udp://tracker.leechers-paradise.org:6969",
"udp://tracker.opentrackr.org:1337/announce",
"udp://torrent.gresille.org:80/announce",
"udp://9.rarbg.me:2710/announce",
"udp://p4p.arenabg.com:1337",
"udp://tracker.internetwarriors.net:1337"]

for tracker in trackerList:
    t.add_tracker(tracker, 0)

# t.add_tracker("udp://tracker.openbittorrent.com:80/announce", 0)#不成功

t.set_creator('libtorrent %s' % lt.version)
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

torrent = t.generate()
f = open("mytorrent.torrent", "wb")
f.write(lt.bencode(torrent))
f.close()

#Seed torrent
ses = lt.session()
ses.listen_on(6881, 6891)
h = ses.add_torrent({'ti': lt.torrent_info('mytorrent.torrent'), 'save_path': '.', 'seed_mode': True})
print "Total size: " + str(h.status().total_wanted)
print "Name: " + h.name()
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
      'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
      (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)

'''
100.00% complete (down: 2.0 kb/s up: 90.0 kB/s peers: 1) seeding
100.00% complete (down: 4.0 kb/s up: 145.0 kB/s peers: 1) seeding
100.00% complete (down: 6.0 kb/s up: 195.0 kB/s peers: 1) seeding
100.00% complete (down: 5.0 kb/s up: 163.0 kB/s peers: 0) seeding
100.00% complete (down: 4.0 kb/s up: 130.0 kB/s peers: 0) seeding
'''
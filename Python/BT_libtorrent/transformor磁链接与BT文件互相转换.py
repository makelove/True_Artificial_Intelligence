# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:38:58 2015

@author: aneasystone

https://github.com/aneasystone/btool

"""

import libtorrent as lt
import time

'''
    transfer a torrent file to a magnet link
'''
def torrent2magnet(torrent_file):
    
    info = lt.torrent_info(torrent_file)
    link = "magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name())
    return link

'''
    transfer a magnet link to a torrent file
'''
def magnet2torrent(link, torrent_file):
    
    sess = lt.session()
    sess.add_dht_router('router.bittorrent.com', 6881)
    sess.add_dht_router('router.utorrent.com', 6881)
    sess.add_dht_router('router.bitcomet.com', 6881)
    sess.add_dht_router('dht.transmissionbt.com', 6881)
    sess.start_dht()

    params = {
        "save_path": 'D:\\Desktop',
        #"storage_mode":lt.storage_mode_t.storage_mode_sparse,
        #"paused": True,
        #"auto_managed": True,
        "duplicate_is_error": True
    }
    handle = lt.add_magnet_uri(sess, link, params)
    
    # waiting for metadata
    while (not handle.has_metadata()):
        time.sleep(5)
    
    # create a torrent
    torinfo = handle.get_torrent_info()
    torfile = lt.create_torrent(torinfo)
    torcontent = lt.bencode(torfile.generate())

    # save to file
    t = open(torrent_file, "wb")
    t.write(torcontent)
    t.close()
    
    return True
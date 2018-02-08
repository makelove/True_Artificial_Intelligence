# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 17:34
# @Author  : play4fun
# @File    : websockets-webtorrent-python.py
# @Software: PyCharm

"""
websockets-webtorrent-python.py:
"""

#!/usr/bin/env python

import asyncio
import websockets

infohash = '08ada5a7a6183aae1e09d831df6748d566095a10'
#infohash = binascii.hexlify(b"08ada5a7a6183aae1e09d831df6748d566095a10")
infohash = str(infohash)
pl = '{"numwant":10,"uploaded":0,"downloaded":0,"left":"null","event":"started","action":"announce","info_hash":"'+infohash+'","peer_id":"-WW0098-CR5i5FXgxCXl"}'

async def hello():
    async with websockets.connect('wss://tracker.btorrent.xyz') as websocket:
        await websocket.send(pl)
        print("> {}".format(pl))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())

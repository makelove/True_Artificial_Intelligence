# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 17:21
# @Author  : play4fun
# @File    : pgnparser1.py
# @Software: PyCharm

"""
pgnparser1.py:
"""

import pgn

# pgn_text = open('morphy.pgn').read()
pgn_text = open('example.pgn').read()
pgn_game = pgn.PGNGame()

x = pgn.loads(pgn_text)
print(x)  # Returns a list of PGNGame
#[<PGNGame "Fischer, Robert J." vs "Spassky, Boris V.">]
d = pgn.dumps(pgn_game)
print(d)  # Returns a string with a pgn game
'''
[<PGNGame "Fischer, Robert J." vs "Spassky, Boris V.">]
[Event "?"]
[Site "?"]
[Date "?"]
[Round "?"]
[White "?"]
[Black "?"]
[Result "?"]
'''
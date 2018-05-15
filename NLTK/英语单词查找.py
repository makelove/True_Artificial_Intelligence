# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 19:54
# @Author  : play4fun
# @File    : 英语单词查找.py
# @Software: PyCharm

"""
英语单词查找.py:
在使用Python的字典中查找单词
http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python
"""
from nltk.corpus import wordnet

synsets=wordnet.synsets( 'love' )
for synset in synsets:
  print ("-" * 10)
  print ("Name:", synset.name())
  print ("Lexical Type:", synset.lexname())
  print ("Lemmas:", synset.lemma_names())
  print ("Definition:", synset.definition())
  for example in synset.examples():
    print ("Example:", example)
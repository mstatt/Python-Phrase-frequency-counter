# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:28:51 2017

@author: MStattelman
"""
import glob
import re
import os
import nltk
import collections
from collections import Counter
from nltk import ngrams

#Use tweet tokenizer to prevent contracted words from spliting
from nltk.tokenize import TweetTokenizer

def remove_punctuation(text):
    # Removes all punctuation and conotation from the string and returns a 'plain' string
    punctuation2 = '-&'+'®©™€â´‚³©¥ã¼•ž®è±äüöž!@#Â“§$%^*()î_+€$=¿{”}[]:«;"»\â¢|<>,.?/~`0123456789'
    for sign in punctuation2:
        text = text.replace(sign, " ")
    return text

phrase_len = 4

corpus = []
path = 'YOURDIRECTORY/'

file_list = []
os.chdir(path)
for file in glob.glob("*.csv"):
    file_list.append(file)
    f = open(file)
    corpus.append(remove_punctuation(f.read()))
    f.close()


frequencies = Counter([])
for text in corpus:
    tknzr = TweetTokenizer()
    token = tknzr.tokenize(text)
    quadgrams = ngrams(token, phrase_len)
    frequencies += Counter(quadgrams)



od = collections.OrderedDict(frequencies.most_common())
import pandas as pd
df = pd.DataFrame.from_dict(od, orient='index').reset_index()
df = df.rename(columns={'index':'Phrase', 0:'Count'})

os.chdir('..')
df.to_html(open('Quad.html', 'w'))


#Write File list to File
with open ("Quad.html","a")as fp:
   fp.write("<br/>File list used in the above analysis:<br/>")
   for line in file_list:
       fp.write(line+"<br/>")
   fp.close()

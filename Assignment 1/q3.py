# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:05:13 2020

@author: Usama
"""
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text = "We are having a 'datascience' class, come join with us! ;) , InshaAllah we are moving to 'Germany' ....!! <3 <3 :D"

sentList = sent_tokenize(text)
sentence = ""
for x in sentList:
    for w in x.split():
        if w not in (';)', ':D', '<3') and w[0] != "'":
            sentence = sentence + w+" ";
            print(w)
        else:
             sentence = sentence +" ";
            
    sentence = sentence+"\n";


print(sentence.replace("  ", ""))
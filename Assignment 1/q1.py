# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:42:54 2020

@author: Usama
"""

import gensim
import numpy as np
data = [
        ("https://www.linkedin.com/in/ahmed-feroz-334409160/","Ahmed Feroz","Freelance Game Developer at Centrick Studios","Centrick Studios"),
        ("https://www.linkedin.com/in/hassan-qureshi/","Hassan Qureshi","Python Engineer at Bitrupt","Bitrupt"),
       ("https://www.linkedin.com/in/shammad/" , "Syed Hammad Ahmed" ,
        "Fulbright PhD Scholar at University of Central Florida","University of Central Florida")]




studentName = input("Enter Student Name : ")
studentInterest = input("Enter Student Interest : ")


# studentName = "Usama"
# studentInterest = "I love python engineering"
ziped_data = zip((studentName,studentInterest),data[1])


from nltk.tokenize import word_tokenize


gen_doc = [[w.lower() for w in word_tokenize(text[2])]
           for text in data
           ]

dictionary  = gensim.corpora.Dictionary(gen_doc)

corpus = [dictionary.doc2bow(x) for x in gen_doc ]

print(dictionary.token2id)

tf_idf = gensim.models.TfidfModel(corpus)
for doc in tf_idf[corpus]:
    print([[dictionary[id],np.around(freq,decimals=2)] for id,freq in doc])


sims = gensim.similarities.Similarity('sims/', tf_idf[corpus], num_features=len(dictionary))

print(sims)

query_doc = [w.lower() for w in word_tokenize(studentInterest )]

query_corpus = dictionary.doc2bow(query_doc)


query_doc_tf_idf = tf_idf[query_corpus]
sims[query_doc_tf_idf]

print('Comparing Resutls: ',sims[query_doc_tf_idf])
match_index = np.argmax(sims[query_doc_tf_idf])
if sims[query_doc_tf_idf][match_index] != 0:
    print("Student "+studentName+" will be supervised by "+data[match_index][1]+" having interests "+studentInterest)
else:
    print("No Supervisor Found For Student "+studentName+" Having Interest"+studentInterest)
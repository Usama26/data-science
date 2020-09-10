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




# studentName = input("Enter Student Name : ")
# studentInterest = input("Enter Student Interest : ")


studentName = "Usama"
studentInterest = "I love python engineering"


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


sims = gensim.similarities.Similarity('', tf_idf[corpus], num_features=len(dictionary))

print(sims)

query_doc = [w.lower() for w in word_tokenize(studentInterest )]

query_corpus = dictionary.doc2bow(query_doc)


query_doc_tf_idf = tf_idf[query_corpus]
sims[query_doc_tf_idf]
print('Comparing Resutls: ',sims[query_doc_tf_idf])












# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans
# from sklearn.metrics import adjusted_rand_score
# import numpy

# texts = ["This first text talks about houses and dogs",
#         "This is about airplanes and airlines",
#         "This is about dogs and houses too, but also about trees",
#         "Trees and dogs are main characters in this story",
#         "This story is about batman and superman fighting each other", 
#         "Nothing better than another story talking about airplanes, airlines and birds",
#         "Superman defeats batman in the last round"]

# # vectorization of the texts
# vectorizer = TfidfVectorizer(stop_words="english")
# X = vectorizer.fit_transform(texts)
# # used words (axis in our multi-dimensional space)
# words = vectorizer.get_feature_names()
# print("words", words)


# n_clusters=3
# number_of_seeds_to_try=10
# max_iter = 300
# number_of_process=2 # seads are distributed
# model = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=number_of_seeds_to_try, n_jobs=number_of_process).fit(X)

# labels = model.labels_
# # indices of preferible words in each cluster
# ordered_words = model.cluster_centers_.argsort()[:, ::-1]

# print("centers:", model.cluster_centers_)
# print("labels", labels)
# print("intertia:", model.inertia_)

# texts_per_cluster = numpy.zeros(n_clusters)
# for i_cluster in range(n_clusters):
#     for label in labels:
#         if label==i_cluster:
#             texts_per_cluster[i_cluster] +=1 

# print("Top words per cluster:")
# for i_cluster in range(n_clusters):
#     print("Cluster:", i_cluster, "texts:", int(texts_per_cluster[i_cluster])),
#     for term in ordered_words[i_cluster, :10]:
#         print("\t"+words[term])

# print("\n")
# print("Prediction")

# text_to_predict = "Why batman was defeated  by superman so easy?"
# Y = vectorizer.transform([text_to_predict])
# predicted_cluster = model.predict(Y)[0]
# texts_per_cluster[predicted_cluster]+=1

# print(text_to_predict)
# print("Cluster:", predicted_cluster, "texts:", int(texts_per_cluster[predicted_cluster])),
# for term in ordered_words[predicted_cluster, :10]:
#     print("\t"+words[term])




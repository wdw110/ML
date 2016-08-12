#encoding=utf-8

text = '''
The Neatest Little Guide to Stock Market Investing
Investing For Dummies, 4th Edition
The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns
The Little Book of Value Investing
Value Investing: From Graham to Buffett and Beyond
Rich Dad's Guide to Investing: What the Rich Invest in, That the Poor and the Middle Class Do Not!
Investing in Real Estate, 5th Edition
Stock Investing For Dummies
Rich Dad's Advisors: The ABC's of Real Estate Investing: The Secrets of Finding Hidden Profits Most Investors Miss
'''

txt = [s.split() for s in open('txtdm.txt')]

get_ipython().system('head -n 10 txtdm.txt')

txt = [s.split() for s in open('txtdm.txt')]
ignore = ",|:|!|'"
stopwords = ['and','edition','for','in','little','of','the','to']

import re
txt = [[re.sub(ignore,'',w.lower()) for w in s ] for s in txt]
txt = [[w for w in s if w not in stopwords] for s in txt]
txt = [' '.join(s) for s in txt]

from sklearn.feature_extraction.text import CountVectorizer
model = CountVectorizer() 
xvec = model.fit_transform(txt)


from sklearn.decomposition import NMF
n_topics = 2
nmf = NMF(n_components=n_topics,
                    sparseness='data', init='nndsvd', random_state=0)
nmf.fit_transform(xvec)

import numpy as np

np.round(nmf.components_,2)
feature_names = model.get_feature_names()
n_top_words=5

for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


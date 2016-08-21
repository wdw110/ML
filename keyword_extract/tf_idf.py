#encoding=utf-8

from __future__ import unicode_literals
import math

def tf_idf(fname):
	tf = []
	df = {}
	idf = {}
	tfidf = []
	if isinstance(fname, list):
		docs = fname
	else:
		docs = open(fname,'r').readlines()
	for doc in docs:
		tmp = {}
		for word in doc:
			if not word in tmp:
				tmp[word] = 0
			tmp[word] += 1
		tf.append(tmp)
		for key in tmp:
			if not key in df:
				df[key] = 0
			df[key] += 1
	for k, v in df.items():
		idf[k] = math.log(len(docs))-math.log(v)
		print k,idf[k]
	for obj in tf:
		tmp = {}
		total = sum(obj.values())
		for k, v in obj.items():
			tmp[k] = v * idf[k]
		tfidf.append(tmp)
	return tf,idf,tfidf

s = [[u'这篇', u'文章'],[u'那篇', u'论文'],[u'这个',u'那篇', u'论文',u'那篇', u'论文'],[u'那篇', u'论文',u'这个']]

tf,idf,tfidf = tf_idf(s)
print tfidf
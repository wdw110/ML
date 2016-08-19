#encoding=utf-8

from __future__ import division
import jieba
import gensim
import numpy as np

#一种提取短文本关键词的方法，文本源按行排列

def read_file(file):
	print 'Reading original data...'
	with open(file,'r') as f:
		docs = f.readlines()
	return docs

def word2vec(data,n):
	pass

def keyword(data,n,m):
	wd2vc = word2vec(data,n)
	dim = len(wd2vc)

	#生成语义邻接矩阵
	G = np.zeros((dim,dim)) #G:语义邻接矩阵
	for i in xrange(dim):
		for j in xrange(i):
			sim = np.dot(wd2vc[i][1],wd2vc[j][1])
			if sim >= m:
				G[i][j] = 1
				G[j][i] = 1

	#特征词选择过程
	error = 1 
	d = 0.85 #d in [0,1]
	P = np.zeros(dim) #P:所有词的特征度向量
	E = np.ones((dim,dim)) #E:单位矩阵
	A = np.zeros((dim,dim)) #A:特征矩阵
	for i in xrange(dim):
		tmp = G[i,:]
		n_i = len(tmp[tmp>0])
		for j in xrange(i):
			A[i][j] = G[i][j]/n_i

	while error > 10**(-6):
		tmp = P
		P = (1-d)/dim*E + d*A*tmp
		er = P - tmp
		error = math.sqrt(np.dot(er,er))

	




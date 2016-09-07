#encoding=utf-8

from __future__ import division
import re
import os
import sys
import math
import jieba
import jieba.analyse
import numpy as np 

reload(sys)
sys.setdefaultencoding('utf-8')

path = os.getcwd()
fname = os.path.join(path,'stop_words.txt')
jieba.analyse.set_stop_words(fname) #设置停用词路径

class keyword(object):
	"""docstring for keyword"""
	def __init__(self):
		self.docs = []
		self.idf = {}
		self.stop_words = []
		self.load(fname,tag='stop')

	def load(self, filename, tag):
		if tag == 'doc':
			with open(filename,'r') as f:
				for i in f.readlines():
					if not i.split():
						continue
					self.docs.append(i)
		elif tag == 'stop':
			with open(fname,'r') as f:
				for line in f.readlines():
					self.stop_words.append(line.strip())

	def save(self):
		idf_name = os.path.join(path,'idf.txt')
		f = open(idf_name, 'w')
		for k,v in self.idf.items():
			f.write(k+'\t'+str(v)+'\n')
		f.close()

	def train(self, data):
		df = {}
		for doc in data:
			tmp = {}
			word_list = list(jieba.cut(doc))
			for w in word_list:  #去除停用词
				if w in self.stop_words:
					word_list.remove(w)

			for word in word_list:
				if not word in tmp:
					tmp[word] = 0
				tmp[word] += 1
			for key in tmp:
				if not key in df:
					df[key] = 0
				df[key] += 1
		for k, v in df.items():
			self.idf[k] = math.log(len(data)+1)-math.log(v+1)

	def tf_idf(self, x, n=5):  # x为文本内容,n为关键词数量
		res = {}
		word_obj = {}
		word_list = list(jieba.cut(x))
		for w in word_list:  #去除停用词
			print type(w)
			if w in self.stop_words:
				word_list.remove(w)
			else:
				if not w in word_obj:
					word_obj[w] = 0
				word_obj[w] += 1
		size = sum(word_obj.values())
		for k, v in word_obj.items():
			tfidf = v/size * self.idf[k]
			res[k] = tfidf
		tmp = sorted(res.items(), key = lambda d:d[1], reverse=True)
		res_arr = ','.join(dict(tmp[:n]).keys())
		return res_arr

if __name__ == '__main__':
	kw = keyword()
	kw.load('data.txt','doc')
	data = kw.docs
	kw.train(data)
	kw.save()
	print kw.tf_idf('【客户误报】客户报修电力故障，经询问排查核实属于欠费。')




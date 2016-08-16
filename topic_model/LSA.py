#encoding=utf-8

#http://blog.sciencenet.cn/blog-995625-812292.html

import numpy
from scipy.linalg import svd
import math

title = [
"The Neatest Little Guide to Stock Market Investing",   
"Investing For Dummies, 4th Edition",   
"The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns",   
"The Little Book of Value Investing",   
"Value Investing: From Graham to Buffett and Beyond",   
"Rich Dad's Guide to Investing: What the Rich Invest in, That the Poor and the Middle Class Do Not!",   
"Investing in Real Estate, 5th Edition",   
"Stock Investing For Dummies",   
"Rich Dad's Advisors: The ABC's of Real Estate Investing: The Secrets of Finding Hidden Profits Most Investors Miss"   
]

stopwords = ['and', 'edition','for','in','little','of','the','to']
ignorechars = ",:'!"  

class LSA(object):
	"""docstring for LSA"""
	def __init__(self, stopwords, ignorechars):
		self.stopwords = stopwords
		self.ignorechars = ignorechars
		self.wdict = {}
		self.dcount = 0

	def parse(self, doc):
		words = doc.split()
		for w in words:
			w = w.lower().translate(None, self.ignorechars)
			if w in self.stopwords:
				continue
			elif w in self.wdict:
				self.wdict[w].append(self.dcount)
			else:
				self.wdict[w] = [self.dcount]
		self.dcount += 1

	#part1:创建计数矩阵
	def build(self):
		self.keys = [k for k in self.wdict.keys() if len(self.wdict[k]) > 1]
		self.keys.sort()
		self.A = numpy.zeros([len(self.keys), self.dcount])
		for i,k in enumerate(self.keys):
			for d in self.wdict[k]:
				self.A[i,d] += 1

	def printA(self):
		print self.A

	#part2: 计数TFIDF代替简单计数
	def TFIDF(self):
		WordsPerDoc = numpy.sum(self.A, axis=0)
		DocsPerWord = numpy.sum(numpy.asarray(self.A>0,'i'), axis=1)
		rows, cols = self.A.shape
		for i in range(rows):
			for j in range(cols):
				self.A[i,j] = (self.A[i,j]/WordsPerDoc[j]) * math.log(float(cols)/DocsPerWord[i])

	#part3: 使用奇异值分解
	def calc(self):
		self.U,self.S,self.Vt = svd(self.A)

if __name__ == '__main__':
	mylsa = LSA(stopwords, ignorechars)

	for t in title:
		mylsa.parse(t)

	mylsa.build()
	#mylsa.printA()
	mylsa.TFIDF()
#	mylsa.printA()
	mylsa.calc()

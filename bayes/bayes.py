#encoding=utf-8
from __future__ import division
import numpy as np 

######################################
#贝叶斯定理：P(A|B) = P(B|A) P(A) / P(B)
#贝叶斯分类器就是计算出概率最大的那个分类
#数据结构：原始数据为二维数组，最后一列为类别
######################################

data = '''sunny	hot	high	false	no
sunny	hot	high	true	no
overcast	hot	high	false	yes
rain	mild	high	false	yes
rain	cool	normal	false	yes
rain	cool	normal	true	no
overcast	cool	normal	true	yes
sunny	mild	high	false	no
sunny	cool	normal	false	yes
rain	mild	normal	false	yes
sunny	mild	normal	true	yes
overcast	mild	high	true	yes
overcast	hot	normal	false	yes
rain	mild	high	true	no'''


class Bayes(object):

	def __init__(self):
		self.d = {}
		self.total = 0
		self.classLabelVector = []
		self.result = []

	def save(self, fname):
		pass

	def load(self, fname):      #fname文本的数据结构：每行为一个样本，最后一列为类别，
		f = open(fname,'r')		#第一行为样本属性的连续性：连续：0，离散：1
		arrayOLines = f.readlines()
		numberOfLines = len(arrayOLines)
		row = len(arrayOLines[0])
		self.Mat = np.zeros((numberOfLines,row))
		index = 0
		for line in arrayOLines:
			arr = line.strip().split('\t')
			self.Mat[index,:] = arr[0:-1]
			self.classLabelVector.append(arr[-1])
			index += 1
		m,n = self.Mat.shape
		for i in range(m):
			



			del arr[-1]  #此时arr数组中只有样本的属性值，去掉了标签
			for j in arr:
				if not self.d.has_key(j):
					self.d[j] = {}
				self.d[j][label] = self.d[j].get(label,0) + 1
				self.d[j]['total'] = self.d[j].get('total',0) + 1
			self.total += 1



	def train(self, data):
		pass

	def prob(self, row):
		pass

	def classifty(self, x):
		pass



if __name__ == '__main__':
	bayes = Bayes()
	bayes.load('data.txt')
	print bayes.d
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
		self.data = []
		self.Label = []
		self.result = []

	def save(self, fname):
		pass

	def load(self, fname):      #fname文本的数据结构：每行为一个样本，最后一列为类别，
		f = open(fname,'r')		#第一行为样本属性的连续性：连续：0，离散：1
		arrayOLines = f.readlines()
		numberOfLines = len(arrayOLines)
		col = len(arrayOLines[0].strip().split('\t')) - 1
		self.Mat = [[0 for c in range(col)] for row in range(numberOfLines)]
		index = 0
		for line in arrayOLines:
			arr = line.strip().split('\t')
			self.Mat[index] = arr[0:-1]
			self.Label.append(arr[-1])
			index += 1
		self.Mat = np.array(self.Mat)
		
	def train(self, data):
		pass

	def prob(self, row):
		pass

	def classifty(self):
		row,col = self.Mat.shape
		label_arr = list(set(self.Label))
		label_init = np.ones(len(label_arr),dtype=int)
		label_obj = dict(zip(label_arr,label_init))
		for i in range(col):
			self.data.append({})
			arr = list(zip(self.Mat[:,i],self.Label))
			for j in range(row):
				element = arr[j][0]
				if not self.data[i].get(element):
					self.data[i][element] = dict(label_obj) # python的变量间赋值是地址引用，故应重新定义 
				self.data[i][element][arr[j][1]] += 1 


if __name__ == '__main__':
	bayes = Bayes()
	bayes.load('data.txt')
	bayes.classifty()
	print bayes.Mat
	print bayes.data
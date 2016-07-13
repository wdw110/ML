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
		self.result = []

	def save(self, fname):
		

	def load(self, fname):#fname文本的数据结构：每行为一个样本，最后一列为类别，
		f = open(fname,'r')		#第一行为样本属性的连续性：连续：0，离散：1


	def train(self, data):
		

	def prob(self, row):
		

	def classifty(self, x):
		
		


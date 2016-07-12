#encoding=utf-8

import os
import path
import math

class KNN(object):

	def __init__(self):
		self.d = []

	def save(self,fname):


	def load(self,fname):
		f = open(fname,'r')
		for i in f.readlines():
			arr = i.strip().split('\t')
			d.append(arr)

	def classify(self):


def Euclidean_distance(a,b):
	if len(a)==len(b):
		return math.sqrt(sum([(a[i]-b[i])**2 for i in range(len(a))]))
	else:
		print '两向量的长度不一致！'

#encoding=utf-8

import os
import math
import pandas
import numpy as np 

class KNN(object):

	def __init__(self):
		self.train_data = []
		self.test_data = []
		self.reslut = []

	def save(self,fname):
		f = open(fname,'w')
		for i in reslut:
			ss = '\t'.join('\t')
			f.write(ss + '\n')
		f.close()

	def load(self,fname,tp='train'):
		tmp = []
		f = open(fname,'r')
		for i in f.readlines():
			arr = i.strip().split('\t')
			tmp.append(arr)
		if tp=='train': train_data = tmp
		elif tp=='test': test_data = tmp

	def classify(self,k=3):
		d1 = np.array(train_data)
		d2 = np.array(test_data)
		labels = np.array(d1[:,-1])
		dd = d1[:,0:-1]
		for i in d2.shape[0]:
			tmp = d2[i]
			obj_k = dict([(i,100000) for i in range(k)])
			for j in d1.shape[0]:
				distance = Euclidean_distance(d2[i][0:-1],d1[j])
				arr_k = sorted(obj_k.items(), lambda x, y: cmp(x[1], y[1]))
				if distance<arr_k[-1][1]:
					del obj_k[arr_k[-1][0]]
					obj_k[j] = distance
			arr_labels = list(labels[obj_k.keys()])
			label = max(arr_labels, key=arr_labels.count)#获取数组中次数最多的元素
			tmp.append(label)
			reslut = tmp

	def autoNorm(self):
		pass

	def Euclidean_distance(self,a,b):
		if len(a)==len(b):
			return math.sqrt(sum([(a[i]-b[i])**2 for i in range(len(a))]))
		else:
			print '两向量的长度不一致！'

#encoding=utf-8

from __future__ import division
import os
import math
import pandas
import numpy as np 

class KNN(object):

	def __init__(self):
		self.reslut = []
		self.d = {'setosa':0,'versicolor':1,'virginica':2}

	def save(self,fname):
		f = open(fname,'w')
		for i in self.reslut:
			ss = '\t'.join('\t')
			f.write(ss + '\n')
		f.close()

	def load(self,fname,tp='train'):
		tmp = []
		f = open(fname,'r')
		for i in f.readlines():
			arr = [float(j) for j in i.strip().split('\t')[0:-1]]
			arr.append(self.d[i.strip().split('\t')[-1]])
			tmp.append(arr)
		if tp=='train': self.train_data = np.array(tmp)
		elif tp=='test': self.test_data = np.array(tmp)

	def classify(self,k=3):
		d1 = self.train_data
		d2 = self.test_data
		labels = d1[:,-1]
		dd = d1[:,0:-1]
		for i in range(d2.shape[0]):
			tmp = list(d2[i])
			obj_k = dict([(a,100000.0) for a in range(k)])
			for j in range(d1.shape[0]):
				distance = Euclidean_distance(d2[i][0:-1],d1[j][0:-1])
				arr_k = sorted(obj_k.items(), lambda x, y: cmp(x[1], y[1]))
				if distance<arr_k[-1][1]:
					obj_k[j] = distance
					if len(obj_k)>k:
						del obj_k[arr_k[-1][0]]
			arr_labels = list(labels[obj_k.keys()])
			label = max(arr_labels, key=arr_labels.count)#获取数组中次数最多的元素
			tmp.append(label)
			self.reslut.append(tmp)

	def autoNorm(self):
		d1 = self.train_data[:,0:-1]
		d2 = self.test_data[:,0:-1]
		rows = [self.train_data.shape[0],self.test_data.shape[0]]
		labels = [self.train_data[:,-1].reshape(rows[0],1),self.test_data[:,-1].reshape(rows[1],1)]
		n = d1.shape[1]
		minvalues = np.append(d1.min(0),d2.min(0)).reshape(2,n)
		maxvalues = np.append(d1.max(0),d2.max(0)).reshape(2,n)
		self.train_data = np.append((d1-minvalues[0,:])/(maxvalues[0,:]-minvalues[0,:]),labels[0],axis=1)
		self.test_data = np.append((d2-minvalues[1,:])/(maxvalues[1,:]-minvalues[1,:]),labels[1],axis=1)


def Euclidean_distance(a,b):
	if len(a)==len(b):
		return math.sqrt(sum([(float(a[i])-float(b[i]))**2 for i in range(len(a))]))
	else:
		print '两向量的长度不一致！'


if __name__ == '__main__':
	knn = KNN()
	knn.load('knn_train.txt','train')
	knn.load('knn_test.txt','test')
	knn.autoNorm()
	knn.classify(5)
	print knn.reslut

#encoding=utf-8

import numpy as np 

class KDNode(object):
	"""docstring for KDNode"""
	__slots__ = ("point", "split", "left", "right")

	def __init__(self,point,left,right,split):
		self.point = point
		self.left = left
		self.right = right
		self.split = split

class KDTree(object):
	
	def createKDTree(self,root,data):
		tmp_data = np.array(data)
		m,k = np.shape(tmp_data)
		split,mvar = max_var(tmp_data)

		data.sort(key=lambda x: x[split])
		

		root_y = sorted(tmp_data[:,split])[m/2]
		root = tmp_data[tmp_data[:,split]==root_y][0]
		tmp_data = np.delete(tmp_data,root).reshape(m-1,k)
		self.left = tmp_data[tmp_data[:,split]<=root_y]
		self.right = tmp_data[tmp_data[:,split]>root_y]




	def findKNN():

	def max_var(self,data):
		arr_var = np.var(data,axis=0)
		res = np.argmax(max(arr_var))
		return res,max(arr_var)
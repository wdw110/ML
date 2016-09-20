#encoding=utf-8

import numpy as np 

class KdNode(object):
	"""docstring for KDNode"""
	__slots__ = ("point", "split", "left", "right")

	def __init__(self,point=None,left=None,right=None,split=None):
		self.point = point
		self.left = left
		self.right = right
		self.split = split

class KdTree(object):

	def createKDTree(self,root,data):
		if not data:
			return None
		tmp_data = np.array(data)
		m,k = np.shape(tmp_data)
		split,mvar = self.max_var(tmp_data)

		data.sort(key=lambda x: x[split])
		point = data[m/2]
		root = KdNode(point,split)
		root.left = self.createKDTree(root.left,data[0:(m/2)])
		root.right = self.createKDTree(root.right,data[(m/2+1):m])
		return root

	def findKNN():
		pass

	def max_var(self,data):
		arr_var = np.var(data,axis=0)
		res = np.argmax(max(arr_var))
		return res,max(arr_var)	

if __name__ == '__main__':
	data = [(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)]
	root = ''
	kd = KdTree()
	tree = kd.createKDTree(root, data)
	print tree.left.point


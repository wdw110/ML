#encoding=utf-8

import re
import jieba
import numpy as np 

class keyword(object):
	"""docstring for keyword"""
	def __init__(self, arg):
		self.docs = []
		self.arg = arg

	def read_file(filename):
		with open(filename,'r') as f:
			for i in f.readlines():
				if not i.split():
					continue
				self.docs.append(i)
		



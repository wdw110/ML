#encoding=utf-8

from __future__ import division
import re
import sys
import jieba
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

addr_del = ['J','-',' ']
arr = []
res = []

with open('add.txt','r') as f:
	for line in f.readlines():
		if not line.strip(): continue
		r = '|'.join(addr_del)
		tmp = re.sub(r,'',line.strip())
		arr.append(list(jieba.cut(tmp)))

length = len(arr)
#res = np.zeros((length,length))
threshold = 0.3

res_obj = {}


for i in range(len(arr)):
	if not re.findall(ur'鼓楼|玄武|栖霞|浦口|白下|江宁|高淳|溧水|六合|下关|建邺|秦淮|雨花',''.join(arr[i])):
		for j in range(len(arr)):
			if ''.join(arr[i]) in ''.join(arr[j]) and len(arr[j])>len(arr[j]):
				arr[i] = arr[j]
				break
	if u'江苏省' not in arr[i]:
		arr[i].insert(0,u'江苏省')
	if u'南京' not in ','.join(arr[i]):
		arr[i].insert(1,u'南京市')


class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root = {}
		self.END = '/'

	def add(self, word):
		#从根节点遍历单词，char by char,如果不存在则新增，最后加上一个单词结束标志
		node = self.root
		for c in word:
			node = node.setdefault(c,{})
		node[self.END] = None

	def find(self, word):
		node = self.root
		for c in word:
			if c not in node:
				return False
			node = node[c]
		return self.END in node

t = Trie()

for word in arr:
	t.add(word)

print ','.join(t.root.keys())



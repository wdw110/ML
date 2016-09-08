#encoding=utf-8

from __future__ import division
import re
import jieba
import numpy as np

addr_del = ['J','-',' ']
arr = []
res = []

with open('add.txt','r') as f:
	for line in f.readlines():
		if not line.strip(): continue
		r = '|'.join(addr_del)
		tmp = re.sub(r,'',line)
		arr.append(list(jieba.cut(tmp)))

length = len(arr)
#res = np.zeros((length,length))
threshold = 0.3

def score(list1,list2):
	res = 0
	for word in list1:
		if word in list2: 
			res += 1
	return res/(len(list1)+len(list2)-res)

for i in range(length):
	for j in range(i+1,length):
		tmp = score(arr[i],arr[j])
		if tmp>threshold:
			if i in res and j not in res:
				res.insert(res.index(i),j)
			if j in res and i not in res:
				res.insert(res.index(j),i)
			if i not in res and j not in res:
				res.extend([i,j,-1])





print res




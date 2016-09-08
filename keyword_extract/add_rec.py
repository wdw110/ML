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

res_obj = {}

for add in arr:

	for word in add:
		if add[0] == '江苏省':
			res_obj.setdefault(word,{})




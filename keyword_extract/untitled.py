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

def score(list1,list2):
	res = 0
	for word in list1:
		if word in list2: 
			res += 1
	return res/(len(list1)+len(list2)-res)

for i in range(len(arr)):
	if not re.findall(ur'鼓楼|玄武|栖霞|浦口|白下|江宁|高淳|溧水|六合|下关|建邺|秦淮|雨花',''.join(arr[i])):
		for j in range(len(arr)):
			if arr[i][0] in arr[j] and len(arr[j])>len(arr[i]) and arr[j][0]==u'江苏省':
				if len(arr[i])>1:
					if arr[i][1] in arr[j]:
						arr[i] = arr[j]
				else: arr[i] = arr[j]
				break
	if u'江苏省' not in arr[i]:
		arr[i].insert(0,u'江苏省')
	else: 
		n = arr[i].index(u'江苏省')
		del arr[i][0:n]
	if u'南京' not in ','.join(arr[i]):
		arr[i].insert(1,u'南京市')


arr.sort()
with open('1.txt','w') as f:
	for i in arr:
		tmp = ''.join(i)
		f.write(tmp+'\n')

"""
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



"""
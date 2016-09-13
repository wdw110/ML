#encoding=utf-8

import re

add = {}

first_add = ['鼓楼','玄武','建邺','白下','秦淮','栖霞','雨花','高淳','溧水','六合','下关','浦口','江宁']

with open('add.txt','r') as f:
	for line in f.readlines():
		if not line.split(): continue
		string = re.sub('J|-| |　','',line.strip())
		ss = re.sub('\w+栋|\d+单元|\w+幢|\d+室|\d+$','',string)
		for word in first_add:
			if word in ss:
				arr = ss.split(word)
				if len(arr)>1 and len(arr[1].decode('utf-8'))>1:
					second_add = arr[1]
					second_add = re.sub('^区|^台|^县','',second_add)
					second_add = re.sub('^区','',second_add)
					key = '江苏省南京市'+word+'区'
					add.setdefault(key,{})
					if second_add: add[key][second_add]=1
					break

with open('add_new.txt','w') as f:
	for first in add:
		seconds = add[first]
		for sec in seconds:
			f.write(first+str(sec)+'\n')



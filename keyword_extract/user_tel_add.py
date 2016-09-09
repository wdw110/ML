#encoding=utf-8

import os
import re

res = {}

path = os.getcwd()

def read_file(rootDir): 
	res_d = list()
	res_f = list()
	list_dirs = os.walk(rootDir) 
	for root, dirs, files in list_dirs: 
		for d in dirs: 
			res_d.append(os.path.join(root, d))      
		for f in files:
			ff = os.path.join(root, f)
			if os.path.splitext(ff)[1] == '.txt':
				res_f.append(ff)
	return res_f

files = read_file(path) #读取数据的文件目录


for fname in files:
	if 'res' in fname:
		print fname
		with open(fname,'r') as f:
			for line in f.readlines():
				line = line.strip().split('\t')
				if 'res_history.txt' not in fname:
					uid = line[14]; add = line[15]; tel = line[17]
				else:
					uid = line[7]; add = line[10]; tel = line[11]
				add = re.sub(r'J|-','',add)
				if uid:
					res.setdefault(uid,{'tel':[],'add':''})
					if tel and tel not in res[uid]['tel']:
						res[uid]['tel'].append(tel)
					if len(add)>len(res[uid]['add']):
						res[uid]['add'] = add

with open(os.path.join(path,'uid_tel_add.txt'),'w') as f:
	for key in res:
		tmp = key +'\t'+ ';'.join(res[key]['tel'])+'\t'+res[key]['add']
		f.write(tmp+'\n')

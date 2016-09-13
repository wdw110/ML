#encoding=utf-8

from __future__ import division
import os
import re
import sys
import xlrd
import time
import jieba
import jieba.analyse

reload(sys)
sys.setdefaultencoding('utf-8')
start1 = time.time()

add_tmp = {'江苏省南京市':{}} #w文本挖掘所需字段
res = {}  #最终结果
work = {} #所有工单内容

#读取原始工单
def read_file(rootDir): 
	res_d = list()
	res_f = list()
	list_dirs = os.walk(rootDir) 
	for root, dirs, files in list_dirs: 
		for d in dirs: 
			res_d.append(os.path.join(root, d))      
		for f in files:
			ff = os.path.join(root, f)
			if os.path.splitext(ff)[1] == '.xls' and '.' not in os.path.splitext(ff)[0]:
				res_f.append(ff)
	return res_f 

#读取源文件
#文本内容：工单号，用户号，台区号，工单内容
print '读取源文件'
path = os.getcwd()
files_xls = read_file(path) #读取数据的文件目录

for f in files_xls:
	book = xlrd.open_workbook(f)
	table = book.sheet_by_index(0)
	nrows = table.nrows                 #行数  
	ncols = table.ncols                 #列数  
	for i in range(0, nrows): 
		key = (table.cell(i, 0).value).encode('utf-8')
		if key.isdigit():  ###判断该字符串是否全部为数字
			work[key]=[]
			for j in range(0, ncols):  
				data = (table.cell(i, j).value).encode('utf-8')
				work[key].append(re.sub(r'\r\n|\n|"|\'|\t','',data))

print '读取地址数据'
with open('add_new.txt','r') as f:
	for line in f.readlines():
		if not line.split(): continue
		line = re.sub('江苏省南京市','',line)
		arr = line.strip()
		key = arr[0:9] #utf-8编码一个汉字是三个字节
		value = re.sub(key,'',arr).decode('utf-8')
		add_tmp['江苏省南京市'].setdefault(key,{})
		add_tmp['江苏省南京市'][key][value]=1

print '生成底层数据'
#生成底层数据

#识别用户地址
rules = '^鼓楼|^玄武|^建邺|^白下|^秦淮|^栖霞|^雨花|^高淳|^溧水|^六合|^下关|^浦口|^江宁'
def add_rec(addr):
	addr = re.sub('J|-| |　|\w+栋|\d+单元|\w+幢|\d+室|\d+$','',addr)
	addr_fix = re.sub('^江苏省|^江苏|^南京|^南京市|南京市|南京','',addr)
	arr = re.findall(rules,addr_fix)
	area = ''
	res_add = ''
	if arr:
		area = arr[0]+'区'
		addr_fix = re.sub('^('+area+')+'+'|^('+arr[0]+')+','',addr_fix).decode('utf-8')
		addr_fix = re.sub(ur'^台区|^区|^县','',addr_fix)
		if addr_fix:	
			for house in add_tmp['江苏省南京市'][area]:
				if addr_fix in house:
					res_add = '江苏省南京市'+area+house.encode('utf-8')
					break
			if not res_add:
				add_tmp['江苏省南京市'][area][addr_fix]=1
				res_add = '江苏省南京市'+area+addr_fix.encode('utf-8')
				with open('add_new.txt','a') as f:
					f.write('江苏省南京市'+area+addr_fix.encode('utf-8')+'\n')
	return res_add

print add_rec('江苏省南京市白下区')

for wid in work:
	wc = work[wid]
	uid = wc[13]; cont = wc[9]
	addr = add_rec(wc[14])
	key_cont = list(jieba.analyse.extract_tags(cont,topK=10))   #提取关键字
	if addr and uid:
		res.setdefault(addr,{'users':{},'stat':{}})
		res[addr]['users'].setdefault(uid,{})
		res[addr]['users'][uid][wid] = [cont,key_cont]
		for word in key_cont:
			res[addr]['stat'].setdefault(word,0)
			res[addr]['stat'][word] += 1

print '输出最终结果'	
with open('addr_test.txt','w') as f:
	for addr in res:
		for uid in res[addr]['users']:
			for wid,v in res[addr]['users'][uid].items():
				tmp = addr+'\t'+uid+'\t'+wid+'\t'+v[0]+'\t'+','.join(v[1])
				f.write(tmp+'\n')
		f.write('小区地址：%s的关键词统计信息如下\n' % addr)
		tmp = [[w,c] for w,c in res[addr]['stat'].items()]
		tt = sorted(tmp,key=lambda x:x[1],reverse=True)
		tmp = '\t'.join([i+'\t'+str(j) for i,j in tt])
		f.write(tmp+'\n')

start2 = time.time()
print '******该阶段共耗时：%.2f秒*******' %round(start2-start1, 2)

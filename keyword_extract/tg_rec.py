#encoding=utf-8

from __future__ import division
import sys
import jieba
import jieba.analyse

reload(sys)
sys.setdefaultencoding('utf-8')

tg_tmp = {}
res = {}
#判断两个列表中所有元素是否相同，只要有一个不同返回False
def isequal(list1,list2):
	if lit1.sort() == list2.sort():
		return True
	else: return False

	"""
	if len(list1) == len(list2):
		for i in list1:
			if i not in list2:
				return False
		return True
	else: return False
	"""

#读取源文件
#文本内容：工单号，用户号，台区号，工单内容
#改
with open('test.txt','r') as f:
	for line in f.readlines():
		if not line.strip(): continue
		arr = line.strip('\n').split('\t')
		tg_id = arr[1]; content = arr[0]
		if tg_id:
			tg_tmp.setdefault(tg_id,[])
			tg_tmp[tg_id].append(content)


for tid in tg_tmp:
	arr = tg_tmp[tid]
	length = len(arr)
	res.setdefault(tid,{})
	arr_cont = []
	key_obj = {} #台区关键词统计
	for cont in arr:
		ll = list(jieba.analyse.extract_tags(cont,topK=10))
		arr_cont.append(ll)
		for kw in ll:
			key_obj.setdefault(kw,0)
			key_obj[ke] += 1
	tid.['key'] = key_obj

	#台区工单共性问题统计
	for i in range(length):
		key1 = arr_cont[i]
		for j in range(i+1,length):
			key2 = arr_cont[j]
			if len(set(key1)&set(key2))/len(set(key1)|set(key2))>=0.25:
				kk = tuple(set(key1)&set(key2))
				#tmp = res[tid].keys()
				res[tid].setdefault(kk,[])
				res[tid][kk].extend([arr[i],arr[j]])
	for kk in res[tid]:
		res[tid][kk] = list(set(res[tid][kk]))
				'''
				if not tmp:
					res[tid][kk] = []
					res[tid][kk].extend([arr[i],arr[j]])
				else:
					aa = [isequal(l,kk) for l in tmp]
					if True in aa:
						v = res[tid][tmp[aa.index(True)]]
						if arr[i] not in v:
							v.append(arr[i])
						if arr[j] not in v:
							v.append(arr[j])
					else:
						res[tid][kk] = []
						res[tid][kk].extend([arr[i],arr[j]])
				'''		

with open('tg_test.txt','w') as f:
	for tid in res:
		for k in res[tid]:
			tmp = tid+'\t'+'-'.join(k)+'\t'+'&&&'.join(res[tid][k])
			f.write(tmp+'\n')










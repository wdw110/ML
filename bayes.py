#encoding=utf-8

#http://www.cnblogs.com/fengfenggirl/p/bayes_classify.html

import random
import sys
import math
import collections

def shuffle():
	'''将原来的文本打乱顺序，用于得到训练集和测试集'''
	datas = [line.strip() for line in sys.stdin]
	random.shuffle(datas)
	for line in datas:
		print line

labels = ['A','B','C','D','E','F','G','H','I']

def label2id(label):
	for i in xrange(len(labels)):
		if label == labels[i]:
			return i
	raise Exception('Error label %s' % label)

def docdict():
	return [0]*len(labels)

def mutalInfo(N, Nij, Ni_, N_j):
	#print N,Nij,Ni_,N_j
	return Nij * 1.0 / N * math.log(N * (Nij+1)*1.0/(Ni_*N_j))/math.log(2)

def countForMI():
	'''基于统计每个词在每个类别出现的次数，以及每类的文档数'''
	docCount = [0] * len(labels) #每个类的词数目
	wordCount = collections.defaultdict(docdict)
	for line in sys.stdin:
		label,text = line.strip().split(' ',1)
		index = label2id(label[0])
		words = text.split(' ')
		for word in words:
			wordCount[word][index] += 1
			docCount[index] += 1

	miDict = collections.defaultdict(docdict)#互信息值
	N = sum(docCount)
	for k,vs in wordCount.items():
		for i in xrange(len(vs)):
			N11 = vs[i]
			N10 = sum(vs) - N11
			N01 = docCount[i] - N11
			N00 = N - N11 - N10 - N01
			mi = mutalInfo(N, N11, N10+N11, N01+N11) + mutalInfo(N,N10+N11,N00+N10) + mutalInfo(N,N01+N11,N01+N00) + mutalInfo(N,N00,N00+N10,N00+N01)
			miDict[k][i] = mi
	fWords = set()
	for i in xrange(len(docCount)):
		keyf = lambda x:x[1][i]
		sortedDict = sorted(miDict.items(),key=keyf,reverse=True)
		for j in xrange(100):
			fWords.add(line.strip())
	print docCount #打印各个类的文档数目
	for fword in fWords:
		print fword 

def loadFeatureWord():
	'''导入特征词'''
	f = open('feature.txt')
	docCounts = eval(f.readline())
	features = set()
	for line in f:
		features.add(line.strip())
	f.close()
	return docCounts, features

def trainBayes():
	'''训练贝叶斯模型，实际上计算每个类中特征词的出现次数'''
	docCounts, features = loadFeatureWord()
	wordCount = collections.defaultdict(docdict)
	tCount = [0] * len(docCounts) #每类文档特征词出现的次数
	for line in sys.stdin:
		label,text = line.strip().split(' ',1)
		index = label2id(label[0])
		words = text.split(' ')
		for word in words:
			if word in features:
				tCount[index] += 1
				wordCount[word][index] += 1
	for k,v in wordCount.items():
		scores = [(v[i]+1) * 1.0 / (tCount[i]+len(wordCount)) for i in xrange(len(v))] #加1平滑
		print '%s\t%s' % k,scores

def loadModel():
	'''导入贝叶斯模型'''
	f = open('model.txt')
	scores = {}
	for line in f:
		word, counts = line.strip().rs('\t',1)
		scores[word] = eval(counts)
	f.close()
	return scores

def predict():
	'''预测文档的类标，标准输入每一行为一个文档'''
	docCounts, features = loadFeatureWord()
	docscores = [math.log(count*1.0 / sum(docCounts)) for count in docCounts]
	scores = loadModel()
	rCount = 0
	docCount = 0
	for line in sys.stdin:
		label, text = line.strip().split(' ',1)
		index = label2id(label[0])
		words = text.split(' ')
		preValues = list(docscores)
		for word in words:
			if word in features:
				for i in xrange(len(preValues)):
					preValues[i] += math.log(scores[word][i])
		m = max(preValues)
		pIndex = preValues.index(m)
		if pIndex == index:
			rCount += 1
		print label, labels[pIndex], text
		docCount += 1
	print rCount, docCount, rCount*1.0/docCount


if __name__=='__main__':
	#shuffle()
	#countForMI()
	#trainBayes()
	predict()


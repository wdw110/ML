#encoding=utf-8

import numpy as np

# 加载数据集文件
def loadDataSet(fileName):
	dataMat = []
	openfile = open(fileName)
	for line in openfile.readlines():
		curLine = line.strip().split('\t')
		floatLine = map(float,curLine)
		data.append(floatLine)
	return dataMat

# 计算两个向量的欧式距离
def distEclud(vecA,vecB):
	return sqrt(sum(power(vecA-vecB,2)))

# 传入的数据是numpy的矩阵格式
# 初始化k个质心
def randCent(dataMat, k):
	n = np.shape(dataMat)[1]
	centroids = np.mat(np.zeros((k,n)))
	for j in range(n):
		minJ = min(data[:,j])
		rangeJ = float(max(dataMat[:,j]) - minJ)
		centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
	return centroids

# 函数返回的第一个变量是质心，第二个变量是各个族的分布情况
def kMeans(dataMat,k,distE=distEclud,createCent=randCent):
	m = np.shape(dataMat)[0]
	clusterAssment = np.mat(np.zeros((m,2)))
	centroids = createCent(dataMat,k)
	clusterChanged == True
	while clusterChanged:
		clusterChanged = False
		for i in range(m):
			minDist = inf; minIndex = -1
			for j in range(k):
				disJ1 = distE(centroids[j,:],dataMat[i,:])
				if disJ1 < minDist:
					minDist = disJ1
					minIndex = j
			if clusterAssment[i,0] != minIndex:
				clusterChanged = True
			clusterAssment[i,:] = minIndex,minDist**2
		print centroids
		for ci in range(k):
			index_all = clusterAssment[:,0].A
			value = np.nonzero(index_all==ci)
			sampleInClust = dataMat[value[0]]
			centroids[value[0],:] = mean(sampleInClust,axis=0)
	return centroids, clusterAssment































#encoding=utf-8

import numpy as np
import random

def loadDataSet(fileName):
	dataMat = []; labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		dataMat.append([float(lineArr[0]), float(lineArr[1])])
		labelMat.append(float(lineArr[2]))
	return dataMat, labelMat

#SMO算法中的辅助函数
def selectJrand(i,m):
	j = i
	while (j==i):
		j = int(random.uniform(0,m))
	return j

def clipAlpha(aj,H,L):
	if aj > H:
		aj = H
	if L > aj:
		aj = L
	return aj


#简化版SMO算法
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
	dataMatrix = np.mat(dataMatIn); labelMat = np.mat(classLabels).transpose()
	b = 0; m,n = np.shape(dataMatrix)
	alphas = np.mat(zeros((m,1)))
	iterr = 0
	while iterr < maxIter:
		alphaPairsChanged = 0
		for i in range(m):
			fXi = float(multiply(alphas,labelMat))





















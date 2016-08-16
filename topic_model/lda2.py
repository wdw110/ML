#encoding=utf-8

import numpy as np

#http://www.cnblogs.com/guapeng/p/4720590.html

class LDAmodel(object):
	"""docstring for LDAmodel"""
	def __init__(self, dpre):
		self.dpre = dpre #获取预处理参数

		#模型参数：
		#聚类个数: K,迭代次数: iter_times,每个特征词个数top_words_num,超参数alpha,beta

		self.K = K
		self.beta = beta
		self.alpha = alpha
		self.iter_times = iter_times
		self.top_words_num = top_words_num

		#文件变量：
		#分好词的文件: trainfile
		#词对应id文件: wordidmapfile
		#文章-主题分布文件: thetafile
		#词主题文件: phifile
		#每个主题topN词文件: topNfile
		#最后分派结果文件: tassginfile
		#模型训练选择的参数文件: paramfile
		self.wordidmapfile = wordidmapfile
		self.trainfile = trainfile
		self.thetafile = thetafile
		self.phifile = phifile
		self.topNfile = topNfile
		self.tassginfile = tassginfile
		self.paramfile = paramfile

		# p,概率向量 double类型，存储采样的临时变量
		# nw,词Word在主题topic上的分布
		# nwsum,每个topic的词的总数
		# nd,每个doc中各个topic的词的总数
		# ndsum,每个doc中词的总数
		# Z,M*doc.size(), 文档中词的主题分布
		self.p = np.zeros(self.K)
		self.nw = np.zeros((self.dpre.words_count,self.K),dtype='int')
		self.nwsum = np.zeros(self.K,dtype='int')
		self.nd = np.zeros((self.dpre.docs_count,self.K),dtype='int')
		self.ndsum = np.zeros(dpre.docs_count,dtype='int')
		self.Z = np.array([[0 for y in xrange(dpre.docs[x].length)] for x in xrange(dpre.docs_count)])

		# 随机起始分配类型
		for x in xrange(len(self.Z)):
			self.ndsum[x] = self.dpre.docs[x].length
			for y in xrange(self.dpre.docs[x].length):
				topic = random.randint(0, self.K-1)
				self.Z[x][y] = topic
				self.nw[self.dpre.docs[x].words[y]][topic] += 1
				self.nd[x][topic] += 1
				self.nwsum[topic] += 1

		self.theta = np.array([[0.0 for y in xrange(self.K)] for x in xrange(self.dpre.docs_count)])
		self.phi = np.array([[0.0 for y in xrange(self.dpre.words_count)] for x in xrange(self.K)])


# sampling抽样过程

def sampling(self,i,j):

	topic = self.Z[i][j]
	word = self.dpre.docs[i].words[j]
	self.nw[word][topic] -= 1
	self.nd[i][topic] -= 1
	self.nwsum[topic] -= 1
	self.ndsum[i] -= 1

	Vbeta = self.dpre.words_count * self.beta
	Kalpha = self.K * self.alpha
	self.p = (self.nw[word] + self.beta)/(self.nwsum + Vbeta) * \
			 (self.nd[i] + self.alpha) / (self.ndsum[i] + Kalpha)
	for k in xrange(1,self.K):
		self.p[k] += self.p[k-1]

	u = random.uniform(0,self.p[self.K-1])
	for topic in xrange(self.K):
		if self.p[topic]>u:
			break

	self.nw[word][topic] +=1
	self.nwsum[topic] +=1
	self.nd[i][topic] +=1
	self.ndsum[i] +=1

	return topic

if __name__ == '__main__':
	a = LDAmodel()




























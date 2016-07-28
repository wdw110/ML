#encoding=utf-8

import math
import numpy as np

data = [(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)]

class KD_node(object):
	def __init__(self, point=None, split=None, LL=None, RR=None):
		"""
		point:数据点
		split:划分域
		LL,RR:结点的左右子节点
		"""
		self.point = point
		self.split = split
		self.left = LL
		self.right = RR

def createKDTree(root, data_list):
	"""
	root:当前数的根节点
	data_list:数据点的集合(无序)
	return:构造的KDTree的树根
	"""
	LEN = len(data_list)
	if LEN == 0:
		return
	#数据点的维度
	dimension = len(data_list[0])
	#方差
	max_var = 0
	#最后选择的划分域
	split = 0
	for i in range(dimension):
		ll = []
		for t in data_list:
			ll.append(t[i])
		var = computeVariance(ll)
		if var > max_var:
			max_var = var
			split = i
	#根据划分域的数据对数据点进行排序
	data.sort(key=lambda x: x[split])
	#选择下标为len/2的点作为分割点
	point = data_list[LEN/2]
	root = KD_node(point, split)
	root.left = createKDTree(root.left, data_list[0:(LEN/2)])
	root.right = createKDTree(root.right, data_list[(LEN/2 + 1):LEN])
	return root

def computeVariance(arrayList):
	"""
	arrayList:存放的数据点
	return:返回数据点的方差
	"""
	for ele in arrayList:
		ele = float(ele)
	LEN = len(arrayList)
	sum1 = array.sum()
	array = np.array(arrayList)
	array2 = array * array
	sum2 = array2.sum()
	mean = sum1 / LEN
	#D[x] = E[x^2] - (E[x])^2
	variance = sum2 / LEN - mean**2
	return variance

def findNN(root, query):
    """
    root:KDTree的树根
    query:查询点
    return:返回距离data最近的点NN，同时返回最短距离min_dist
    """
    #初始化为root的节点
    NN = root.point
    min_dist = computeDist(query, NN)
    nodeList = []
    temp_root = root
    ##二分查找建立路径
    while temp_root:
        nodeList.append(temp_root)
        dd = computeDist(query, temp_root.point)
        if min_dist > dd:
            NN = temp_root.point
            min_dist = dd
        #当前节点的划分域
        ss = temp_root.split
        if query[ss] <= temp_root.point[ss]:
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right
    ##回溯查找
    while nodeList:
        #使用list模拟栈，后进先出
        ss = back_point.split
        print 'back.point = ', back_point.point
        ##判断是否需要进入父节点的子空间进行搜索
        if abs(query[ss] - back_point.point[ss]) < min_dist:
            temp_root = back_point.right
        else:
            temp_root = back_point.left

        if temp_root:
            nodeList.append(temp_root)
            curDist = computeDist(query, temp_root.point)
            if min_dist > curDist:
                min_dist = curDist
                NN = temp_root.point
    return NN, min_dist

def computeDist(pt1, pt2):
    """
    计算两个数据点的距离
    return:pt1和pt2之间的距离
    """
    sum1 = 0.0
    for i in range(len(pt1)):
        sum1 += (pt1[i] - pt2[i])**2
    return math.sqrt(sum1)




from random import seed, random
from time import clock
from operator import itemgetter
from collections import namedtuple
from math import sqrt
from copy import deepcopy
 
 
def sqd(p1, p2):
    return sum((c1 - c2) ** 2 for c1, c2 in zip(p1, p2))
 
 
class KdNode(object):
    __slots__ = ("dom_elt", "split", "left", "right")
 
    def __init__(self, dom_elt, split, left, right):
        self.dom_elt = dom_elt
        self.split = split
        self.left = left
        self.right = right
 
 
class Orthotope(object):
    __slots__ = ("min", "max")
 
    def __init__(self, mi, ma):
        self.min, self.max = mi, ma
 
 
class KdTree(object):
    __slots__ = ("n", "bounds")
 
    def __init__(self, pts, bounds):
        def nk2(split, exset):
            if not exset:
                return None
            exset.sort(key=itemgetter(split))
            m = len(exset) // 2
            d = exset[m]
            while m + 1 < len(exset) and exset[m + 1][split] == d[split]:
                m += 1
 
            s2 = (split + 1) % len(d)  # cycle coordinates
            return KdNode(d, split, nk2(s2, exset[:m]),
                                    nk2(s2, exset[m + 1:]))
        self.n = nk2(0, pts)
        self.bounds = bounds
 
T3 = namedtuple("T3", "nearest dist_sqd nodes_visited")
 
 
def find_nearest(k, t, p):
    def nn(kd, target, hr, max_dist_sqd):
        if kd is None:
            return T3([0.0] * k, float("inf"), 0)
 
        nodes_visited = 1
        s = kd.split
        pivot = kd.dom_elt
        left_hr = deepcopy(hr)
        right_hr = deepcopy(hr)
        left_hr.max[s] = pivot[s]
        right_hr.min[s] = pivot[s]
 
        if target[s] <= pivot[s]:
            nearer_kd, nearer_hr = kd.left, left_hr
            further_kd, further_hr = kd.right, right_hr
        else:
            nearer_kd, nearer_hr = kd.right, right_hr
            further_kd, further_hr = kd.left, left_hr
 
        n1 = nn(nearer_kd, target, nearer_hr, max_dist_sqd)
        nearest = n1.nearest
        dist_sqd = n1.dist_sqd
        nodes_visited += n1.nodes_visited
 
        if dist_sqd < max_dist_sqd:
            max_dist_sqd = dist_sqd
        d = (pivot[s] - target[s]) ** 2
        if d > max_dist_sqd:
            return T3(nearest, dist_sqd, nodes_visited)
        d = sqd(pivot, target)
        if d < dist_sqd:
            nearest = pivot
            dist_sqd = d
            max_dist_sqd = dist_sqd
 
        n2 = nn(further_kd, target, further_hr, max_dist_sqd)
        nodes_visited += n2.nodes_visited
        if n2.dist_sqd < dist_sqd:
            nearest = n2.nearest
            dist_sqd = n2.dist_sqd
 
        return T3(nearest, dist_sqd, nodes_visited)
 
    return nn(t.n, p, t.bounds, float("inf"))
 
 
def show_nearest(k, heading, kd, p):
    print(heading + ":")
    print("Point:           ", p)
    n = find_nearest(k, kd, p)
    print("Nearest neighbor:", n.nearest)
    print("Distance:        ", sqrt(n.dist_sqd))
    print("Nodes visited:   ", n.nodes_visited, "\n")
 
 
def random_point(k):
    return [random() for _ in range(k)]
 
 
def random_points(k, n):
    return [random_point(k) for _ in range(n)]
 
if __name__ == "__main__":
    seed(1)
    P = lambda *coords: list(coords)
    kd1 = KdTree([P(2, 3), P(5, 4), P(9, 6), P(4, 7), P(8, 1), P(7, 2)],
                  Orthotope(P(0, 0), P(10, 10)))
    show_nearest(2, "Wikipedia example data", kd1, P(9, 2))
 
    N = 400000
    t0 = clock()
    kd2 = KdTree(random_points(3, N), Orthotope(P(0, 0, 0), P(1, 1, 1)))
    t1 = clock()
    text = lambda *parts: "".join(map(str, parts))
    show_nearest(2, text("k-d tree with ", N,
                         " random 3D points (generation time: ",
                         t1-t0, "s)"),
                 kd2, random_point(3))
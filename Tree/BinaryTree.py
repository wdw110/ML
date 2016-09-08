#encoding=utf-8

def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root,newBranch):
	if len(root[1]) > 1:
		root[1][1] = [newBranch,[],[]]
	else:
		root[1] = [newBranch,[],[]]
	return root

def insertRight(root,newBranch):
	if len(root[2]) > 1:
		root[2][2] = [newBranch,[],[]]
	else:
		root[2] = [newBranch,[],[]]
	return root

def insertLeft1(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight2(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root



def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]


r = BinaryTree(3)
insertLeft1(r,4)
insertLeft1(r,5)
insertRight2(r,6)
insertRight2(r,7)
insertRight2(r,8)
print r
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft1(l,11)
print r
insertRight2(l,11)
print r
ll = getLeftChild(l)
print ll
insertRight2(ll,1)
print(r)
print(getRightChild(getRightChild(r)))


tree=BinaryTree('a')
insertLeft(tree,'b')
insertRight2(tree,'c')
insertRight2((getLeftChild(tree)),'d')
insertLeft((getRightChild(tree)),'e')
insertRight2((getRightChild(tree)),'f')
print tree


class BinaryTree(object):
    def __init__(self,item):
        self.key=item
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,item):
        if self.leftChild==None:
            self.leftChild=BinaryTree(item)
        else:
            t=BinaryTree(item)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,item):
        if self.rightChild==None:
            self.rightChild=BinaryTree(item)
        else:
            t=BinaryTree(item)
            t.rightChild=self.rightChild
            self.rightChild=t
            


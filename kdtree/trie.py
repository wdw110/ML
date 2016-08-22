#encoding=utf-8

class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root = {}
		self.END = '/'

	def add(self, word):
		#从根节点遍历单词，char by char, 如果不存在则新增，最后加上一个单词结束标志
		node = self.root
		for c in word:
			node = node.setdefault(c,{})
		node[self.END] = None

	def find(self, word):
		node = self.root
		for c in word:
			if c not in node:
				return False
			node = node[c]
		return self.END in node

if __name__ == '__main__':
	s = 'Sorry about that. Please try refreshing and contact us if the problem persists.'
	a = Trie()
	arr = s.split(' ')
	for word in arr:
		a.add(word)

	print a.find('Sorry')

	print a.root

''''
#下面的例子是为了验证python变量赋值的方式是地址引用，所以两次print的内存地址是一样的
a = {}
b = a 
c = a
for i in range(40):
	b = b.setdefault(i,{})
	c = c[i]
	print id(b)
	print id(c)
'''
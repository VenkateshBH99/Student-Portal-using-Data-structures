class Queues:
	def __init__(self):
		self.T=[]

	def enqueue(self,x):
		self.T.append(x)

	def dequeue(self):
		return self.T.pop(0)

	def isEmpty(self):
		if len(self.T)==0:
			return True
		return False

	def Remove(self,x):
		i=self.T.index(x)
		self.T.pop(i)

	def Front(self):
		if len(self.T) is not 0:
			a=self.dequeue()
			self.T.insert(0,a)
			return a
	def print(self):
		l=len(self.T)
		i=0
		while i<l:
			print(self.T[0])
			self.T.pop(0)
			i=i+1
		return

	def pr(self):
		l=len(self.T)
		i=0
		while i<l:
			self.T.pop(0)
			i=i+1
		return

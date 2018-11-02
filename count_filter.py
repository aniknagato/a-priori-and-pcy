import random

class CountPair:
	def __init__(self, m):
		self.m = m
		self.Table = [0]*m
		self.a = random.randint(2,1000)
		self.b = random.randint(2,1000)
		self.c = random.randint(2,1000)
		self.Table2 = [False]*m

	def hash(self, pair):
		return (pair[0]*self.a + pair[1]*self.b) % self.m

	def hash3(self, pair):
		return (pair[0]*self.a + pair[1]*self.b + pair[2]*self.c) % self.m

	def add(self, pair):
		i = self.hash(pair)
		# print("count value at index", i)
		self.Table[i] += 1

	def add3(self, pair):
		i = self.hash3(pair)
		# print("count value at index", i)
		self.Table[i] += 1		

	def is_candidate(self, pair, t):
		i = self.hash(pair)
		return self.Table[i] > t

	def is_candidate3(self, pair, t):
		i = self.hash3(pair)
		return self.Table[i] > t


	def compact(self, t):
		for i in range(len(self.Table2)):
			if self.Table[i] > t:
				self.Table2[i] = True

	def compact3(self, t):
		for i in range(len(self.Table2)):
			if self.Table[i] > t:
				self.Table2[i] = True

	def print(self):
		print("Count filter: ", self.m, self.a, self.b)
		for i in range(len(self.Table)):
			print(i, self.Table[i])

	def print3(self):
		print("Count filter: ", self.m, self.a, self.b,self.c)
		for i in range(len(self.Table)):
			print(i, self.Table[i])


if __name__ == '__main__':
	c = CountPair(21)
	print(c.m, c.a, c.b)
	c.add((3,10))
	print(c.Table)

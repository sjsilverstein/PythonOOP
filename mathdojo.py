class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self, value = 0):
		super(MathDojo, self).__init__()
		self.value = value
	def add(self, *arg):
		addMe = 0
		for idxArg in arg:
			if isinstance(idxArg, list):
				tempSum = 0
				for idx in range(0, len(idxArg)):
					tempSum += idxArg[idx]
				addMe += tempSum
			else:
				addMe+= idxArg
		self.value = self.value + addMe
		return self
	def subtract(self, *arg):
		removeMe = 0
		for idxArg in arg:
			if isinstance(idxArg, list):
				tempSum = 0
				for idx in range(0, len(idxArg)):
					tempSum += idxArg[idx]
				removeMe += tempSum
			else:
				removeMe+= idxArg
		self.value = self.value - removeMe
		return self
	def result(self):
		print "{}".format(self.value)
		return self

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).result()
md = MathDojo(0)
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()

class Product(object):
	"""docstring for Product"""
	def __init__(self, price, itemName, weight, brand, status = 'For Sale'):
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.status = status

	def sell(self):
		self.status = 'Sold'
		return self
	def addTax(self, tax):
		return (self.price) * (1 + tax)
	def wasReturned(self, reason):
		if reason == 'defective':
			self.status = 'Defective'
			self.price = 0
		elif reason == 'is open':
			self.status = 'Used'
			self.price = (self.price)*0.8
		elif reason == 'in box':
			self.status = 'For Sale'
		else:
			print "Unexpected reason for wasReturned: 'defective', 'is open', or 'in box'."
		return self
	def displayInfo(self):
		print "Item Price: {} Item Name: {} Item Weight: {} Item Brand: {} Item Status: {}".format(self.price, self.itemName, self.weight, self.brand, self.status)
		return self
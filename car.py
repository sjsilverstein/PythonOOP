class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self. mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print "Price: $" + str(self.price)
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel: " + self.fuel
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax: " + str(self.tax)
		return self
#Create the Car Class Above

#myCar = Car(26000, 100, 'Full Tank', '26')

listCars = []

for num in range (0, 6):
	import random
	temp = Car(random.randint(5000,100000), random.randint(50,200), 'Full Tank', random.randint(15,40))
	print ""
	listCars.append(temp)
		
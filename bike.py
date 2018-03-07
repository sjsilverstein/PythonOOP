class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = str(max_speed)+" mph"
		self.miles = miles
	def displayInfo(self):
		print "This Bike was ${}. It's max speed is {}. It has been ridden for a total of {} miles.".format(self.price, self.max_speed, self.miles)
		return self
	def ride(self):
		print "Riding 10 miles."
		self.miles = self.miles + 10
		return self
	def reverse(self):
		if self.miles > 0:
			print "Reversing 5 miles"
			self.miles = self.miles -5
		return self




#Define Bike Above
bike1 = Bike(100, 30, 50)
bike2 = Bike(1200, 40, 0)
bike3 = Bike(2000, 50, 0)

# bike1.displayInfo()
# bike2.ride()
# bike2.displayInfo()

# Have the first instance ride three times, reverse once and have it displayInfo(). 
# Have the second instance ride twice, reverse twice and have it displayInfo(). 
# Have the third instance reverse three times and displayInfo().

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
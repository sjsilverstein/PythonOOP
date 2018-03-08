class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health = self.health -1
		return self
	def run(self):
		self.health = self.health - 5
		return self
	def displayHealth(self):
		print "{}'s Health: {}".format(self.name, self.health)
		return self


class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name, health = 150):
		super(Dog, self).__init__(name, health)
	def pet(self):
		self.health = self.health + 5
		return self


class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name, health = 170):
		super(Dragon, self).__init__(name, health)
	def fly (self):
		print "I'm a Dragon and can Fly!"
		self.health = self.health -10
		return self
	def displayHealth(self):
		print "I am a Dragon!"
		super(Dragon, self).displayHealth()

class Cat(Animal):
	def __init__(self, name = 'No Name Kitty :(', health = 100):
		super(Cat, self).__init__(name, health)
	def pet(self):
		self.health = self. health + 10
		print "Petting Kitty Cat {}".format(self.name)
		return self
	def feed(self):
		self.health = self.health +15
		print "Feeding Kitty"
		return self

# testAnimal1 = Animal('Kitty', 100)
# test14 = Animal 
# testAnimal2 = Dog('Frank')
# testAnimal3 = Dog('Joe', 250)
# testAnimal2.displayHealth()
# testAnimal3.displayHealth()
# testDragon = Dragon('Draco')
# testDragon.displayHealth()
# testDragon2 = Dragon('Ugin', 2000)
# # testDragon2.run().run().fly().displayHealth()

# kitty1 = Cat('Frank')
# kitty1.displayHealth()
# kitty1.fly().displayHealth()

		
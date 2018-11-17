#BASE CLASS
class Animal():
	def __init__(self,name):
		self.name = name
		print("ANIMAL Created")

	def who_am_i(self):
		print("I AM ANIMAL")

	def eat(self):
		print("I am eating - ANIMAL FUNCTION")

	def speak(self):
		raise NotImplenetedErrpr("SubClass Must imp this method")

class Dog(Animal):
	def __init__(self,name):
		Animal.__init__(self,name)
		print("Dog Created")

	def who_am_i(self):
		print("I AM DOG")

	def bark(self):
		print("WOOF")

	def speak(self):
		return self.name + " WOOF!"
#creating Animal
myAnimal = Animal("Anni")
#example of abstract method
#myAnimal.speak()
#creating Dog
myDog = Dog("gev")
myDog.eat()
myDog.who_am_i()
print(myDog.speak())

len(myDog) 
class Dog():

	#Class object attributes
	#SAME FOR ANY INSTANCE OF CLASS
	species = 'mammal'

	#we will send self to say that is is the instance of the class
	def __init__(self,bread,name,spots):

		#Attributes
		#Take the arguments and assign in to self...
		self.bread = bread	
		self.name = name
		#Expect boolean True/False
		self.spots = spots

	def bark(self):
		print("WOOOF ! my name is {}".format(self.name))


#create instance of the class Sample
myDog = Dog(bread  = 'Lab',name = "gever",spots = True)
type(Dog)
print(myDog.species)
myDog.bark()

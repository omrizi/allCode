
class Circle ():

	#Class Object
	pi = 3.14

	def __init__(self,radi = 1):
		self.radi = radi
		self.area = Circle.pi * (radi*radi)
	#MeTHOD
	def getCircumference(self):
		print("The circumfrence is {}".format(2 * Circle.pi * self.radi))


myCircle = Circle(radi = 30)
myCircle.getCircumference()		
print(myCircle.area)
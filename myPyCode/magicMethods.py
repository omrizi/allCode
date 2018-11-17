class Book():

	def __init__(self,title,auth,pages):

		self.title = title
		self.auth = auth
		self.pages = pages

	def __str__(self):
		return f"Name of the Book :{self.title}\nWritten by: {self.auth}\n length is: {self.pages}"

	def __len__(self):
		return self.pages

	def __del__(self):
		print("Book has been deleted")
		#we can insert more code actually
		#Deleting all the arguments and etc..
b = Book("python",'oziner',200)
 
print(b)
len(b)

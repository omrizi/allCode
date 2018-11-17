class Account():

	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f"The owner is {self.owner}\nThe balance is {self.balance}"
		
	def deposit(self,money):
		self.balance += money
		print("{} dollars are added to  your account".format(money))
		return True

	def withdraw(self,money):
		if(self.balance > money):
			self.balance -= money
			print("{} dollars are withdrawed from your account".format(money))
		else:
			print("You cannot withdraw this amount of money --> {}".format(money))


acnt = Account("Omri",100)
acnt.deposit(100)
acnt.withdraw(50)
acnt.withdraw(1000)	

print(acnt)
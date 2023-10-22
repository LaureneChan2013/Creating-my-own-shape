class BankAccount:
    def __init__(self,accNumber,name,registration,balance):
       self.accNumber = accNumber
       self.name = name
       self.registration = registration
       self.balance = balance

    def checkBalance(self):
       print(self.balance)
    def withdraw(self, money):
       self.balance -= money
       print("You have withdrawn $" +str(money))
       print("Balance: $" + str(self.balance))
    def deposit(self, money):
       self.balance -= money
       print("You have deposited $" +str(money))
       print("Balance: $" + str(self.balance))

var1 = BankAccount("1234", "Laurene" , "5062013" ,1000)
var2 = BankAccount("2222", "Bob" , "120241800" , 5555)

var1.withdraw(200)
var2.deposit(1235)


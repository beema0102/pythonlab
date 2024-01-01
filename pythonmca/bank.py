class Bankaccount:
 def __init__(self,account_number,account_holder_name,account_type,balance=0):
  self.account_number=account_number
  self.account_holder_name=account_holder_name
  self.account_type=account_type
  self.balance=balance
 def deposit(self,amount):
  if amount > 0:
   self.balance=self.balance+amount
   print ("succesful deposit=",amount)
   print("new balance=",self.balance)
  else:
   print("invalid amount")
 def withdraw(self,amount):
  if 0 < amount < self.balance:
   self.balance=self.balance-amount
  elif amount>self.balance:
   print ("no possible to withdraw") 
  else:
   print("inavalid")
 def get_balance(self):
   print("current balance=",self.balance)
   
   
a=int(input("enter account number="))
b=input("enter the name=")
c=input("enter the type=")
account1 = Bankaccount(a,b,c)
print(account1.get_balance())
d=int(input("enter the amount to deposit:"))
deposit_result = account1.deposit(d)
print(deposit_result)
e=int(input("enter the amount to withdraw:"))
withdrawal_result = account1.withdraw(e)
print(withdrawal_result)
print(account1.get_balance())

  
   


"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_money, commision_money=0, hour=0, contractNumber=0):
        self.name = name
        self.salary = Salary(money=salary_money, hour=hour)
        self.commission = Commission(money=commision_money, number=contractNumber)

    def get_pay(self):
        return self.salary.getSalary() + self.commission.getCom()
    def printMoney(self):
        if self.commission.printCom():
            return self.salary.printSalary() + self.commission.printCom()
        else:
            return self.salary.printSalary()

    def __str__(self):
        return f'''{self.name} works on a{self.printMoney()}. Their total pay is {self.get_pay()}.'''
class Salary():
    def __init__(self, money=0,hour=0):
        self.money = money
        self.hour = hour
    def getSalary(self):
        if self.hour == 0:
            return self.money
        else:
            return self.money*self.hour
    def printSalary(self):
        if self.hour == 0:
            return f" monthly salary of {self.money}"
        else:
            return f" contract of {self.hour} hours at {self.money}/hour"
        
class Commission():
    def __init__(self,money,number=0):
        self.money=money
        self.numberOfContract=number
    def getCom(self):
        if self.numberOfContract == 0:
            return self.money
        else:
            return self.money*self.numberOfContract
    def printCom(self):
        if self.money == 0:
            return ""
        if self.numberOfContract == 0:
            return f" and receives a bonus commission of {self.money}"
        if self.numberOfContract != 0:
            return f" and receives a commission for {self.numberOfContract} contract(s) at {self.money}/contract"
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name='Billie',salary_money=4000)
print(billie.__str__())
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(name='Charlie',salary_money=25,hour=100)
print(charlie.__str__())
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(name='Renee',salary_money=3000, commision_money=200, contractNumber=4)
print(renee.__str__())
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(name='Jan', salary_money=25, hour=150, contractNumber=3, commision_money=220)
print(jan.__str__())
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(name='Robbie', salary_money=2000, commision_money=1500)
print(robbie.__str__())
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(name='Ariel', salary_money=30, hour=120, commision_money=600)
print(ariel.__str__())
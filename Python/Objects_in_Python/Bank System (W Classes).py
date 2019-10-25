class BankAccount:
      def __init__(self,name='Dupont', solde=1000):
            self.name = name
            self. solde = solde

      def deposit(self,money):
            self.solde = self.solde + money
      def withdraw(self,money):
            if self.solde >= money:
                  self.solde = self.solde - money
            else:
                  print('This person does not have the funds!')
      def display(self):
            print('The solde of the Bank account of ', self.name, ' is de', self.solde, ' dollars')
      def  __repr__(self):
            return (str(self.name) + ":" + str(self.solde) + "dollars")
class AccountSaving: 
      def __init__(self, name='Dupont', solde=1000, rate = 0.3):
            self.name = name
            self.solde = solde
            self.rate = rate
      def changeRate(self, newrate):
            self.rate = newrate
      def deposit(self,money):
            self.solde = self.solde + money
      def display(self):
            print('The solde of the Bank account of ', self.name, ' is de', self.solde , ' dollars')
      def Withdraw(self,money):
            if self.solde >= money:
                  self.solde = self.solde - money
            else:
                  print('This person does not have the funds!')
      def capitalisation(self, month):
            print('Capitalisation on', month, 'months, at a rate of', self.rate,'%.')
            rate = self.rate/100
            for i in range(1,month + 1):
                  interest = self.solde * rate
                  self.solde = self.solde + interest
            

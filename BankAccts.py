class BalanceException(Exception):
    pass

#Normal Chequing Account
class ChequingAccount:
    def __init__(self, InitialAmount, Acctname): #Initializes the class with a starting amount and an account name
        self.balance = InitialAmount
        self.name = Acctname
        print (f"\nAccount {self.name} created:\nBalance = ${self.balance}")
    
    def getBalance(self): #returns current balance of account
        print(f"Balance of {self.name} = ${self.balance}")
    
    def deposit(self, depAmount): #deposits money into account
        self.dep = depAmount
        print(f"\n${self.dep} has been deposited into Account {self.name}")
        self.balance = self.balance + depAmount
        self.getBalance()
    
    def checkFunds(self, amount): #Checks if there are enough funds to withdraw a certain amount, if not, returns an error
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nAccount {self.name} has insufficient funds\n"
            )
    
    def withdraw(self, withAmount): #Withdraws money from acccount (first checks if there is enough)
        try:
            self.checkFunds(withAmount)
            self.balance = self.balance - withAmount
            print(f"\n${self.balance} has been withdrawn from Account {self.name}")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Failed: {error}")
    
    def transfer(self, transAmount, recepient): #Transfers money from one account to another (first checks if there is enough)
        try:
            print("\n------------TRANSFER IN PROGRESS------------")
            self.checkFunds(transAmount)
            self.withdraw(transAmount)
            recepient.deposit(transAmount)
            print("\n------------TRANSFER WAS SUCCESSFULL------------\n")
        except BalanceException as error:
            print(f"\nTransfer Failed: {error}")

#Rewards bank account which gives a rebate of 2% on purchases from select stores
class RewardAccount(ChequingAccount):
     def purchase(self, purAmount, store):
        try:
            if store == "Food Basics" or store == "Walmart" or store == "BestBuy" or store == "No Frills":
                self.checkFunds(purAmount)
                self.cost = purAmount
                self.balance = self.balance - (purAmount)
                print(f"\nA purchase of ${self.cost} has been made")
                self.deposit(purAmount*0.02)
            else: 
                self.checkFunds(purAmount)
                self.balance = self.balance - (purAmount)
                print(f"\nA purchase of ${self.cost} has been made")
                self.getBalance()
        except BalanceException as error:
            print(f"\nPurchase Failed: {error}")

#Savings bank account which has a withdrawal fee of $5
# class SavingsAccount(CreditAccount):
#      def withdraw(self, withAmount):
#         try:
#             self.checkFunds(withAmount)
#             self.balance = self.balance - (withAmount + 5)
#             print(f"\n${self.balance} has been withdrawn from Account {self.name}")
#             self.getBalance()
#         except BalanceException as error:
#             print(f"\nWithdraw Failed: {error}")
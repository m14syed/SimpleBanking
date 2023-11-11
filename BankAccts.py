class BalanceException(Exception):
    pass

#Normal Chequing Account
class ChequingAccount:
    def __init__(self, InitialAmount, Acctname): #Initializes the class with a starting amount and an account name
        self.balance = InitialAmount
        self.name = Acctname
        print (f"\nAccount {self.name} created:\nBalance = ${self.balance:0.02f}")
    
    def getBalance(self): #returns current balance of account
        print(f"Balance of {self.name} = ${self.balance:0.02f}")
    
    def deposit(self, depAmount): #deposits money into account
        self.dep = depAmount
        print(f"\n${self.dep:0.02f} has been deposited into Account {self.name}")
        self.balance = self.balance + depAmount
        self.getBalance()
    
    def checkFunds(self, amount): #Checks if there are enough funds to withdraw a certain amount, if not, returns an error
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Account {self.name} has insufficient funds"
            )
    
    def withdraw(self, withAmount): #Withdraws money from acccount (first checks if there is enough)
        try:
            self.checkFunds(withAmount)
            self.balance = self.balance - withAmount
            print(f"\n${self.balance:0.02f} has been withdrawn from Account {self.name}")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal Failed: {error}")
    
    def transfer(self, transAmount, recepient): #Transfers money from one account to another (first checks if there is enough)
        try:
            print("\n------------TRANSFER IN PROGRESS------------")
            self.checkFunds(transAmount)
            self.withdraw(transAmount)
            recepient.deposit(transAmount)
            print("\n------------TRANSFER WAS SUCCESSFULL------------\n")
        except BalanceException as error:
            print(f"\n------------!!TRANSFER FAILED!!-------------\n***{error}***")


#Credit bank account which gives a rebate of 2% on purchases from select stores
class CreditAccount(ChequingAccount):
    def __init__(self, creditlimit, Acctname): #Initializes the class with a credit limit and an account name
        self.balance = 0
        self.name = Acctname
        self.climit = creditlimit
        print (f"\nAccount {self.name} created:\nCredit Limit = ${self.climit:0.02f}")

    def checkFunds(self, amount): #Checks if the purchase amount is within the credit limit, if not, returns an error
        if self.balance + amount <= self.climit: 
            return
        else:
            raise BalanceException(
                f"Account {self.name} has insufficient funds"
            )

    def deposit(self, depAmount, from_purchase=False): #deposits money into account (if not from a purchase, it will not print the rebate)
        self.dep = depAmount 
        self.balance = self.balance - depAmount
        if not from_purchase:
            print(f"\nYou have payed ${self.dep:0.02f} towards your Credit Card balance.\nUpdated Credit Card Balance: ${self.balance:0.02f} \n")

    def purchase(self, purAmount, store): #Makes a purchase from a store and gives a rebate of 2% if the store is eligible
        purAmount
        try:
            if store == "Food Basics" or store == "Walmart" or store == "BestBuy" or store == "No Frills":
                self.checkFunds(purAmount)
                self.balance = self.balance + (purAmount)
                print(f"\nA purchase of ${self.cost:0.02f} has been made\nYou have recieved a rebate of ${purAmount*0.02:0.02f}")
                self.deposit(purAmount*0.02, from_purchase=True)
                self.getBalance()
            else: 
                self.checkFunds(purAmount)
                self.balance = self.balance + (purAmount)
                print(f"\nA purchase of ${purAmount:0.02f} has been made")
                self.getBalance()
        except BalanceException as error:
            print(f"\nPurchase Failed: {error}")


#Savings bank account which has a withdrawal fee of $5
class SavingsAccount(ChequingAccount): 
    def __init__(self, InitialAmount, Acctname): #Initializes the class with a starting amount and an account name
        super().__init__(InitialAmount, Acctname)
        self.fee = 5
    
    def withdraw(self, withAmount): #Withdraws money from acccount (first checks if there is enough)
        try:
            self.checkFunds(withAmount + self.fee)
            self.balance = self.balance - (withAmount + self.fee)
            print(f"\n${withAmount:0.02f} has been withdrawn from Account {self.name}\n***A fee of ${self.fee:0.02f} has been charged***")
            self.getBalance()
        except BalanceException as error:
            print(f"\n***Withdrawal Failed: {error}***")
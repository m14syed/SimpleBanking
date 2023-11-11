from BankAccts import *

JakeCredit = CreditAccount(5000, "JakeCredit")

JakeDebit = ChequingAccount(5000, "Jake")

JakeDebit.transfer(500, JakeCredit)
from BankAccts import *

def create_account():
    print("\nChoose the type of account to create:")
    print("1. Chequing Account")
    print("2. Credit Account")
    print("3. Savings Account")
    account_type = input("Enter choice (1-3): ")

    acct_name = input("Enter account name: ")
    if account_type == "1":
        initial_amount = float(input("Enter initial amount for Chequing Account: "))
        return ChequingAccount(initial_amount, acct_name)
    elif account_type == "2":
        credit_limit = float(input("Enter credit limit for Credit Account: "))
        return CreditAccount(credit_limit, acct_name)
    elif account_type == "3":
        initial_amount = float(input("Enter initial amount for Savings Account: "))
        return SavingsAccount(initial_amount, acct_name)
    else:
        print("Invalid choice.")
        return None

def account_operations(account, accounts): 
    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Funds")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.getBalance()
        elif choice == "4":
            transfer_amount = float(input("Enter transfer amount: "))
            recipient_name = input("Enter recipient account name: ")
            if recipient_name in accounts and accounts[recipient_name] != account: #Check if recipient account exists and is not the same as the sender
                account.transfer(transfer_amount, accounts[recipient_name])
            else:
                print("Invalid recipient.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main():
    accounts = {} #Dictionary to store accounts

    while True:
        print("\n1. Create a new account")
        print("2. Access existing account")
        print("3. Exit")
        main_choice = input("Enter choice (1-3): ")

        if main_choice == "1":
            account = create_account() #Create account 
            if account:
                accounts[account.name] = account #Add account to dictionary
                print(f"Account {account.name} created.")
        elif main_choice == "2":
            if accounts:
                acct_name = input("Enter account name to access: ")
                if acct_name in accounts: #Check if account exists
                    account_operations(accounts[acct_name], accounts)
                else:
                    print("Account not found.")
            else:
                print("No accounts available.")
        elif main_choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
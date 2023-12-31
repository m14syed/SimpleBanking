import tkinter as tk
from tkinter import messagebox
from BankAccts import *

# Global dictionary to store accounts
accounts = {}

def create_account(acct_type, acct_name, initial_amount):
    if acct_type == "Chequing":
        account = ChequingAccount(initial_amount, acct_name)
    elif acct_type == "Savings":
        account = SavingsAccount(initial_amount, acct_name)
    elif acct_type == "Credit":
        account = CreditAccount(initial_amount, acct_name)  # Assuming initial_amount is used as credit limit
    else:
        messagebox.showerror("Error", "Invalid Account Type")
        return
    accounts[acct_name] = account
    messagebox.showinfo("Success", f"Account {acct_name} created successfully.")

def open_create_account_window():
    create_account_window = tk.Toplevel() 

    tk.Label(create_account_window, text="Account Name:").pack() 

    acct_name_entry = tk.Entry(create_account_window)
    acct_name_entry.pack()

    tk.Label(create_account_window, text="Initial Amount/Credit Limit:").pack()
    amount_entry = tk.Entry(create_account_window)
    amount_entry.pack()

    account_type_var = tk.StringVar()
    account_types = {"Chequing", "Savings", "Credit"}
    account_type_var.set("Chequing")  # Default value
    tk.OptionMenu(create_account_window, account_type_var, *account_types).pack()

    tk.Button(create_account_window, text="Create Account", command=lambda: create_account(account_type_var.get(), acct_name_entry.get(), float(amount_entry.get()))).pack()

def main_window():
    window = tk.Tk()
    window.title("Banking System")

    tk.Button(window, text="Create Account", command=open_create_account_window).pack()
    tk.Button(window, text="Account Operations", command=open_account_operations_window).pack()

    window.mainloop()

def deposit(account, amount):
    account.deposit(amount)
    messagebox.showinfo("Success", f"Deposited ${amount} to {account.name}")

def withdraw(account, amount):
    try:
        account.withdraw(amount)
        messagebox.showinfo("Success", f"Withdrew ${amount} from {account.name}")
    except BalanceException as e:
        messagebox.showerror("Error", str(e))

def check_balance(account):
    # Check if the account exists
    if account:
        balance = account.getBalance()
        messagebox.showinfo("Balance", f"Account {account.name} balance: ${balance}")
    else:
        messagebox.showerror("Error", "Account not found.")

def transfer(source_account, amount, recipient_account):
    # Check if both accounts exist
    if source_account and recipient_account:
        try:
            source_account.transfer(amount, recipient_account)
            messagebox.showinfo("Success", f"Transferred ${amount} from {source_account.name} to {recipient_account.name}")
        except BalanceException as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "One or more accounts not found.")

def purchase (account, amount, store):
    # Check if the account exists
    if account:
        try:
            account.purchase(amount, store)
            messagebox.showinfo("Success", f"Purchased ${amount} from {store} with {account.name}")
        except BalanceException as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Account not found.")

def open_account_operations_window():
    account_operations_window = tk.Toplevel()

    tk.Label(account_operations_window, text="Select Source Account:").pack()
    source_account_var = tk.StringVar()
    source_account_list = tk.OptionMenu(account_operations_window, source_account_var, *accounts.keys())
    source_account_list.pack()

    amount_entry = tk.Entry(account_operations_window)
    amount_entry.pack()

    # Function to create and show destination account selection
    def show_destination_account():
        tk.Label(account_operations_window, text="Select Destination Account:").pack()#
        destination_account_var = tk.StringVar()
        destination_account_list = tk.OptionMenu(account_operations_window, destination_account_var, *accounts.keys())
        destination_account_list.pack()

        # Update transfer button command with destination account
        transfer_button.config(command=lambda: transfer(accounts.get(source_account_var.get()), float(amount_entry.get()), accounts.get(destination_account_var.get())))

    # Transfer button initially without destination account selection
    transfer_button = tk.Button(account_operations_window, text="Transfer", command=show_destination_account)
    transfer_button.pack()

    #Function to create and show store selection
    def show_store():
        tk.Label(account_operations_window, text="Select Store:").pack()#
        store_var = tk.StringVar()
        store_list = tk.OptionMenu(account_operations_window, store_var, "Food Basics", "Walmart", "BestBuy", "No Frills", "Other")
        store_list.pack()

        # Update purchase button command with store
        purchase_button.config(command=lambda: purchase(accounts.get(source_account_var.get()), float(amount_entry.get()), store_var.get()))

    # Purchase button initially without store selection
    purchase_button = tk.Button(account_operations_window, text="Purchase", command=show_store)
    purchase_button.pack()

    tk.Button(account_operations_window, text="Deposit", command=lambda: deposit(accounts.get(source_account_var.get()), float(amount_entry.get()))).pack()
    tk.Button(account_operations_window, text="Withdraw", command=lambda: withdraw(accounts.get(source_account_var.get()), float(amount_entry.get()))).pack()
    tk.Button(account_operations_window, text="Check Balance", command=lambda: check_balance(accounts.get(source_account_var.get()))).pack()

if __name__ == "__main__":
    main_window()
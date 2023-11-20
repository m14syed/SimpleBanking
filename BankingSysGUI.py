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
    balance = account.getBalance()
    messagebox.showinfo("Balance", f"Account {account.name} balance: ${balance}")

def transfer(account, amount, recipient):
    try:
        account.transfer(amount, recipient)
        messagebox.showinfo("Success", f"Transferred ${amount} from {account.name} to {recipient.name}")
    except BalanceException as e:
        messagebox.showerror("Error", str(e))


def open_account_operations_window():
    account_operations_window = tk.Toplevel()

    tk.Label(account_operations_window, text="Select Account:").pack()
    selected_account_var = tk.StringVar()
    account_list = tk.OptionMenu(account_operations_window, selected_account_var, *accounts.keys())
    account_list.pack()

    amount_entry = tk.Entry(account_operations_window)
    amount_entry.pack()

    tk.Button(account_operations_window, text="Transfer", command=lambda: transfer(accounts[selected_account_var.get()], float(amount_entry.get()), accounts["Chequing"])).pack()
    tk.Button(account_operations_window, text="Deposit", command=lambda: deposit(accounts[selected_account_var.get()], float(amount_entry.get()))).pack()
    tk.Button(account_operations_window, text="Withdraw", command=lambda: withdraw(accounts[selected_account_var.get()], float(amount_entry.get()))).pack()
    tk.Button(account_operations_window, text="Check Balance", command=lambda: check_balance(accounts[selected_account_var.get()])).pack()

if __name__ == "__main__":
    main_window()
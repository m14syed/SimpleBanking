# Banking Application

This banking application is a Python-based simulation of basic banking operations. It supports different types of bank accounts, including Chequing, Savings, and Credit accounts, each with its own unique features and operations.

## Features

- **Chequing Account**: Standard banking account with functionalities for deposit, withdrawal, balance checking, and fund transfer.
- **Savings Account**: Inherits features from the Chequing account and adds a withdrawal fee for each transaction.
- **Credit Account**: Also based on the Chequing account but with a set credit limit and functions added/overriden to simulate a credit account. Includes a feature for a 2% rebate on purchases from select stores.
- **Custom Exception Handling**: Implements a `BalanceException` for handling insufficient funds scenarios.
- **Interactive Console Interface**: Allows users to create accounts, perform transactions, and access account information through a user-friendly console interface.

from Account import Account
from Customer import Customer
from DataSource import DataSource

"""from Transactions import Transactions as trans"""


class Bank:

    def __init__(self):
        self.allCustomers = []
        self.data_store = DataSource()
        self._load()

    def _load(self):
        self.allCustomers = self.data_store.getDataFromTextFile()

    def getCustomers(self):
        for customer in self.allCustomers:
            print(customer)

    def addCustomer(self, name, last_name, ssn):
        last_id = int(self.data_store.getLastId())
        last_id += 1
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                return "Customer already exists"
        new_customer = Customer(last_id, name, last_name, ssn, [])
        self.allCustomers.append(new_customer)
        self.data_store.addDataToFile(self.allCustomers)
        return "Customer creation successful!"

    def getCustomer(self, ssn):
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                print(customer)
                for account in customer.get_account():
                    print(account)

    def changeCustomerName(self, name, last_name, ssn):
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                customer.set_name(name, last_name)
        self.data_store.addDataToFile(self.allCustomers)

    def removeCustomer(self, ssn):
        for customer in self.allCustomers:
            if customer.get_ssn() == ssn:
                index = self.allCustomers.index(customer)
                self.allCustomers.pop(index)
        self.data_store.addDataToFile(self.allCustomers)

    def addAccount(self, ssn):
        last_account_number = int(self.data_store.getLastAccountNumber())
        last_account_number += 1
        for customer in self.allCustomers:
            if customer.get_ssn() == ssn:
                new_account = Account(last_account_number, "debit", 0.0)
                customer.get_account().append(new_account)
        self.data_store.addDataToFile(self.allCustomers)

    def getAccount(self, ssn, account_number):
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                for account in customer.get_account():
                    if account_number == account.get_account_number():
                        print(account)

    def removeAccount(self, ssn, account_number):
        for customer in self.allCustomers:
            if customer.get_ssn() == ssn:
                for account in customer.get_account():
                    index = customer.get_account().index(account)
                    if account_number == account.get_account_number():
                        customer.get_account().pop(index)

        self.data_store.addDataToFile(self.allCustomers)

    def deposit(self, ssn, account_number, amount: str):
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                for account in customer.get_account():
                    if account_number == account.get_account_number():
                        balance = account.get_account_balance()
                        balance += float(amount)
                        account.set_balance(balance)
        self.data_store.addDataToFile(self.allCustomers)

    def withdraw(self, ssn, account_number, amount: str):
        for customer in self.allCustomers:
            if ssn == customer.get_ssn():
                for account in customer.get_account():
                    if account_number == account.get_account_number():
                        if account.get_account_balance() >= float(amount):
                            balance = account.get_account_balance()
                            balance -= float(amount)
                            account.set_balance(balance)
                        else:
                            return "You dont have that much money"
        self.data_store.addDataToFile(self.allCustomers)

    """def showTransactions(self, id):

    def transactionMade(self):
        for customer in self.allCustomers:

"""
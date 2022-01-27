

class Customer:

    def __init__(self, customer_id, name, last_name, ssn, accounts):
        """Initiate variables: name, lastname, ssn"""
        self._customer_id = customer_id
        self._name = name
        self._last_name = last_name
        self._ssn = ssn
        self._accounts = accounts
        self._transactions = []

    def __str__(self):
        return f"ID: {self._customer_id}\nName: {self._name}\nLastname: {self._last_name}\nSSN: {self._ssn}"

    def get_customer_id(self):
        return self._customer_id
    def get_name(self):
        return self._name
    def get_last_name(self):
        return self._last_name
    def get_ssn(self):
        return self._ssn
    def get_account(self):
        return self._accounts
    def get_transactions(self):
        return self._transactions
    def set_name(self, name, last_name):
        self._name = name
        self._last_name = last_name

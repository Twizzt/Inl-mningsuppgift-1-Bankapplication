

class Account:

    def __init__(self, account_number, account_type, account_balance):
        """"""
        self._balance = float(account_balance)
        self._account_type = account_type
        self._account_number = account_number

    def __str__(self):
        return f"Accountnumber: {self._account_number}\nAccounttype: {self._account_type}\nAccountbalance: {self._balance}"

    def get_account_number(self):
        return self._account_number
    def get_account_type(self):
        return self._account_type
    def get_account_balance(self):
        return self._balance
    def set_balance(self, new_balance):
        self._balance = new_balance


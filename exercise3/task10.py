class BankAccount:
    def __init__(self, owner_name: str, account_number: str, balance: float):
        self.__owner_name = owner_name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    def __service_charge(self):
        service_fee = self.__balance * 0.01
        self.__balance -= service_fee

    def balance(self):
        return self.__balance


account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance())
account.deposit(100)
print(account.balance())

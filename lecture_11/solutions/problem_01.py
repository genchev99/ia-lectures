"""
Create a new class `PersonIdentification` with the following attributes:

- `first_name` - the first name of the person
- `last_name` - the last name of the person
- `id_number` - the id number if the person [EGN]

> It takes all if them as arguments in the constructor

Create a new class `BankAccountWallet` with the following attributes:

- `owner: PersonIdentification` - the owner of the wallet - he is of type `PersonIdentification`
- `balance: float` - the money balance in the wallet
- `account_identificator` - a number that uniquely identifies the account - can be autoincremented
  using `Class attributes`
    - https://dzone.com/articles/python-class-attributes-vs-instance-attributes

It defines and implements the following methods too:

- `deposit()` - adds money to the balance
- `withdraw()` - removes money from the balance if enough
- `print_balance()` - prints the balance in this format `balance: {balance}`

1. Create a new instance of `BankAccountWallet`
1. Deposit money to it (1000 dollars)
1. Print the balance
1. Withdraw money from it (755.3)
1. Print the balance
"""


class PersonIdentification:
    def __init__(self, first_name: str, last_name: str, id_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number


class BankAccountWallet:
    def __init__(self, owner: PersonIdentification, account_identificator: int):
        self.owner = owner
        self.balance = 0.0
        self.account_identificator = account_identificator

    def deposit(self, amount: float):
        self.balance = self.balance + amount

    def withdraw(self, amount: float):
        if self.balance < amount:
            print("Not enough money")
        else:
            self.balance = self.balance - amount  # self.balance -= amount

    def print_balance(self):
        print("balance: " + str(self.balance))


if __name__ == '__main__':
    owner = PersonIdentification("Petar", "Atanasov", "044123132")
    wallet = BankAccountWallet(owner, 1)
    wallet.deposit(1000.0)
    wallet.print_balance()
    wallet.withdraw(755.3)
    wallet.print_balance()


class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withrdaw(self, ammount):
        self.balance -= ammount


    def deposit(self, ammount):
        self.balance += ammount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# initial state
account = Account('balance.txt')
print(account.balance)

# test withrdaw
account.withrdaw(20)
print(account.balance)

# test deposit
account.deposit(500)
print(account.balance)

account.commit()

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

class Checking(Account):
    """This class generates checking  account objects"""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, ammount):
        self.balance = self.balance - ammount - self.fee

jack = Checking("jack.txt", 5)
jack.transfer(10)
print(jack.balance)
jack.commit()
print(jack.type)

john = Checking("john.txt", 5)
john.transfer(10)
print(john.balance)
john.commit()
print(john.type)

print(john.__doc__)

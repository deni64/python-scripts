class human:
    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = 0
        self.home = 0
    def present(self):
        print(f'my name is {self.name} and i am {self.age} years old')

    def earn_money(self):
        self.money += 1000
    
    def get_home(self):
        if self.money == self.price:
            print('hoorah I have just bought anew house')
        else:
            print('I dont have enough money to buy a new house, I need to work more')
    class house:
        def __init__(self, )

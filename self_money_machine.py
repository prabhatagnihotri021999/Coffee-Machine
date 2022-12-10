from self_coffee_machine import Coffe_Machine

class Money_Machine(Coffe_Machine):

    def __init__(self):
        super().__init__()
        self.money_received = 0

    def insert_coin(self):
        print('Please insert coins')
        self.quater = input('How many quater?:')
        self.dtimes = input('How many dtimes')
        self.nickles = input('How many nickles')
        self.pennies = input('How many pennies')

        self.money_received = round((int(self.quater) * 0.25 + int(self.dtimes) * 0.10 + int(self.nickles) * 0.05 + int(self.pennies) * 0.01),2)

    def check_money(self, coffe_machine):

        if(self.resources['balance'] <= self.money_received):
            print(f"Here is ${self.money_received - self.resources['balance']} in change")
            print(f"Here is your { coffe_machine.user_drink} enjoy it")
            print(f"Water: {coffe_machine.resources['water']}ml")
            print(f"Milk: {coffe_machine.resources['milk']}ml")
            print(f"Coffee: {coffe_machine.resources['coffee']}g")
            print(f"Balance: {coffe_machine.resources['balance']}")
        else:
            print("Sorry that's not enough money. Money refunded")

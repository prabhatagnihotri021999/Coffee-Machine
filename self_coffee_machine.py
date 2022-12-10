
class Coffe_Machine:

    def __init__(self):
        self.resources = { "water": 400, "milk": 300, "coffee": 200, "balance":0 }

    def Coffe(self):

        self.user_drink = input("What would you like? (espresso/latte/cappuccino/):")

    def check_resources(self):
        self.cr = 0
        resources_values = list(self.resources.values())
        resources_keys = list(self.resources.keys())

        if (self.user_drink.lower() == 'espresso'):
            resources_espresso = [200,0,75]
            for i in range(len(resources_espresso)):
                if (resources_espresso[i] >= resources_values[i]):
                    print(f"sorry there is not enough {resources_keys[i]}")
                    self.cr = 1

        if (self.user_drink.lower() == 'latte'):
            resources_espresso = [100,50,25]
            for i in range(len(resources_espresso)):
                if (resources_espresso[i] >= resources_values[i]):
                    print(f"sorry there is not enough {resources_keys[i]}")
                    self.cr = 1

        if (self.user_drink.lower() == 'cappuccino'):
            resources_espresso = [25,50,25]
            for i in range(len(resources_espresso)):
                if (resources_espresso[i] >= resources_values[i]):
                    print(f"sorry there is not enough {resources_keys[i]}")
                    self.cr = 1

    def check_input(self):

        if(self.user_drink.lower() == 'espresso'):
            self.resources['water'] -= 100
            self.resources['milk']  -= 50
            self.resources['coffee'] -= 25
            self.resources['balance'] = 2.5

        elif (self.user_drink.lower() == 'latte'):
            self.resources['water'] -= 100
            self.resources['milk'] -= 0
            self.resources['coffee'] -= 75
            self.resources['balance'] = 3.75

        elif (self.user_drink.lower() == 'cappuccino'):
            self.resources['water'] -= 25
            self.resources['milk'] -= 50
            self.resources['coffee'] -= 25
            self.resources['balance'] = 4.25

        elif(self.user_drink.lower() == 'report'):
            print(f"Water: {self.resources['water']}ml")
            print(f"Milk: {self.resources['milk']}ml")
            print(f"Coffee: {self.resources['coffee']}g")
            print(f"Balance: {self.resources['balance']}")

        else:
            print('Wrong input')
            exit()
            



        
    
        



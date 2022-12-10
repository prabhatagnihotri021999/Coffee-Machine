from self_coffee_machine import Coffe_Machine
from self_money_machine import Money_Machine


coffe_machine = Coffe_Machine()
money_machine = Money_Machine()

is_on = True
while is_on:
    coffe_machine.Coffe()
    if (coffe_machine.user_drink.lower()=='off'):
        break
    coffe_machine.check_resources()
    if(coffe_machine.cr == 1):
        continue
    coffe_machine.check_input()
    if coffe_machine.user_drink.lower()  == 'report':
        continue
    money_machine.insert_coin()

    money_machine.check_money(coffe_machine)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_off = False
while not machine_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")

    if choice == "off":
        machine_off = True

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink_of_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_of_choice):
            if money_machine.make_payment(drink_of_choice.cost):
                coffee_maker.make_coffee(drink_of_choice)
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menus = Menu()
money = MoneyMachine()

machine_off = False
while not machine_off:
    CHOICE = input(f"What would you like? ({menus.get_items()}): ")

    # Make turn off command
    if CHOICE == "off":
        machine_off = True
        print("Machine turned off")

    # Make report command
    elif CHOICE == "report":
        machine.report()
        print(f"Profit: {money.CURRENCY}{money.profit}")

    # menus.find_drink(CHOICE) equals to:  menus.menu[0/1/2]
    elif menus.find_drink(CHOICE) is not None:
        # If sufficient, ask for coins
        if machine.is_resource_sufficient(menus.find_drink(CHOICE)):
            # Ask for coins, functions will return True if the coins inserted are enough
            if money.make_payment(menus.find_drink(CHOICE).cost):
                # Make coffee and deduct the machine resources
                machine.make_coffee(menus.find_drink(CHOICE))

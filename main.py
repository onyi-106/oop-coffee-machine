from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#
#
machine = CoffeeMaker()
menus = Menu()
money = MoneyMachine()
# menu_item = menus.menu


# latte = menus.menu[0]
# espresso = menus.menu[1]
# cappuccino = menus.menu[2]
#
# # # print(latte)
# #
# #
# machine_off = False
# while not machine_off:
#     CHOICE = input(f"What would you like? ({menus.get_items()}): ")
# #
#     # Turn off command
#     if CHOICE == "off":
#         machine_off = True
#     # Show report command
#     if CHOICE == "report":
#         machine.report()
#
#     # TODO If the resources are sufficient, ask for coins
#     # TODO If the CHOICE is in the menu, proceed
#     # machine.is_resource_sufficient(CHOICE)
#     # if menus.find_drink(CHOICE) in menus.menu:
#     #     print("wooww ada ternyata")
#     menu_item = MenuItem("espresso", "water", "milk", "coffee", "cost")
#     # print(menus.menu[0])?
#     # menus.find_drink("latte")
#     # print(menus.menu)


print(len(menus.menu))

menu_quantity = len(menus.menu)
CHOICE = input(f"What would you like? ({menus.get_items()}): ")

# This equals to menus.menu[0/1/2]
item_chosen = menus.find_drink(CHOICE)
print(type(item_chosen))

# If sufficient, ask for coins
if item_chosen is not None:
    print("omaagaa")
    if machine.is_resource_sufficient(item_chosen):

else:
    print("Bruh")



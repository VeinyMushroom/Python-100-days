from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_processing = MoneyMachine()

shutdown = False
while not shutdown:
    user_selection = input(f"What would you like to order? {menu.get_items()}: ")

    if user_selection == "off":
        shutdown = True
    elif user_selection == "report":
        coffee_maker.report()
        money_processing.report()
    else:
        user_selection = menu.find_drink(user_selection)
        if user_selection:

            if coffee_maker.is_resource_sufficient(user_selection):
                if money_processing.make_payment(user_selection.cost):
                    coffee_maker.make_coffee(user_selection)
        else:
            print("Invalid command")

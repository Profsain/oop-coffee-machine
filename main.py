from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Create object from Class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option})> ").lower()
    if choice == "off":
        print("Turn off.......")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_resource_sufficient and is_payment_successful:
            coffee_maker.make_coffee(drink)
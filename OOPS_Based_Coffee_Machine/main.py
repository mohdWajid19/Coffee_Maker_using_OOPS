from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear


menu = Menu() #object for Menu class
coffee_maker = CoffeeMaker() #object for CoffeeMaker class
money_machine = MoneyMachine() #object for MoneyMachine class
is_true = True

while is_true:
    clear()
    user_need = input(f"WHAT Would you like to have,\n{menu.get_items()} enter the name of coffee : ")
    if user_need == 'espresso' or user_need == "latte" or user_need == 'cappuccino':
        for item in  menu.menu: #get cost from menu list in Menu class
            if item.name == user_need:
                cost = item.cost #storing cost of item
        user_wants = menu.find_drink(user_need) #store the object of drink user needs
        if coffee_maker.is_resource_sufficient(user_wants): #check if sufficient resources are available
            if money_machine.make_payment(cost): #check if payment is done or not
                coffee_maker.make_coffee(user_wants) #make coffee

    elif user_need == 'off':
        is_true = False #turn coffee machine off
    elif user_need == 'report': #see the statistics of coffee machine
        coffee_maker.report()
        money_machine.report()
    else: #if user makes a typo in input
        print("We Dont Understand what you need check menu again and input from menu ")
    if is_true and input("One more ☕?? (y/n) : ").lower() != 'y' :
        break
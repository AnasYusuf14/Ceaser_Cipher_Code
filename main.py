import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def print_report(resources):
    """This function takes a dictionary and print a report about resources"""
    for key in resources:
        print(f"{key} : {resources[key]}")
    print(f"money : {profit} $")


def check_resources(order_ingredients):
    """This function makes check for resources that needed to make coffee"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters ? :")) * 0.25
    total += int(input("how many dimes ? :")) * 0.1
    total += int(input("how many nickles ? :")) * 0.05
    total += int(input("how many pennies ? :")) * 0.01
    return  total

def check_payment(payment , drink_cost):
    """Return True if money is enough or False if money is not enough """
    if payment >= drink_cost:
        global profit
        profit += drink_cost
        rest = round(payment - drink_cost,2)
        print(f"Here is ${rest} in change.")
        return True
    else :
        print("Sorry that is not enough money , money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"Here is your {drink_name} ☕ ")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) /  (to make report enter 'report') / ( To turn off the mashine enter 'off') :")
    if choice == "off":
        is_on = False
    elif choice == "report" :
        print_report(resources)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_payment(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
    else:
        print("please enter an available drink!")

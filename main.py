MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 80
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0.0

def is_resources_sufficient(order_ingredients):
    """Returns True when ingredients are sufficient, False when ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated coins inserted"""
    print("Insert coins")
    total = int(input("How many Quarters: ")) * 0.25
    total += int(input("How many Dimes: ")) * 0.1
    total += int(input("How many Nickles: ")) * 0.05
    total += int(input("How many Pennies: ")) * 0.01
    return total

def is_transaction_succesfull(money_received, cost_drink):
    """Return true when the payment is accepted, False when payment is rejected."""
    if money_received >= cost_drink:
        change = round(money_received - cost_drink, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += cost_drink
        return True
    else:
        print("Sorry that's not enough money, money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

is_on = True
while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

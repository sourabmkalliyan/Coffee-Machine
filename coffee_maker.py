class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources"""
        print(f"Water: {self.resources['water']} mL")
        print(f"Milk: {self.resources['milk']} mL")
        print(f"Coffee Powder: {self.resources['coffee']} g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make = False
        can_make = True


    def make_coffee(self, order):
        """Deducts the required ingredients from the resources"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}.Enjoy")
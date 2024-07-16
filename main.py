## Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                return False
        return True

    def process_coins(self):
        try:
            quarters = int(input("Enter number of quarters: ")) * 0.25
            dimes = int(input("Enter number of dimes: ")) * 0.10
            nickels = int(input("Enter number of nickels: ")) * 0.05
            pennies = int(input("Enter number of pennies: ")) * 0.01

            total = quarters + dimes + nickels + pennies
            return total
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return 0

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            print(f"Here is your change of ${change:.2f}. Enjoy your sandwich!")
            return True
        else:
            print("Sorry, that's not enough money. Please insert more coins.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        recipe = recipes.get(sandwich_size)
        if recipe:
            ingredients_needed = recipe['ingredients']

            if self.check_resources(ingredients_needed):
                for ingredient, amount in ingredients_needed.items():
                    self.machine_resources[ingredient] -= amount
                print(f"Here is your {sandwich_size} sandwich. Enjoy!")
            else:
                print("Sorry, there are not enough ingredients to make your sandwich.")
        else:
            print("Sorry, we don't have that size of sandwich available.")


# Instantiate SandwichMachine with initial resources
machine = SandwichMachine(resources)

# Example usage:
print("Welcome to the Sandwich Machine!")
size = input("What size sandwich would you like (small/medium/large)? ").lower()

if size in recipes:
    order_ingredients = recipes[size]['ingredients']
    if machine.check_resources(order_ingredients):
        print(f"The {size} sandwich costs ${recipes[size]['cost']:.2f}.")
        coins_inserted = machine.process_coins()
        if coins_inserted > 0:
            if machine.transaction_result(coins_inserted, recipes[size]['cost']):
                machine.make_sandwich(size, order_ingredients)
    else:
        print("Sorry, we don't have enough ingredients to make that sandwich.")
else:
    print("Sorry, that size is not available.")

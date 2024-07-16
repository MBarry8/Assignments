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
            large_dollars = int(input("how many large dollars?: ")) * 1.00
            half_dollars = int(input("how many half dollars?: ")) * 0.50
            quarters = int(input("how many quarters?: ")) * 0.25
            nickels = int(input("how many nickels?: ")) * 0.05

            total = large_dollars + half_dollars + quarters + nickels
            return total
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return 0

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        recipe = recipes.get(sandwich_size)
        if recipe:
            ingredients_needed = recipe['ingredients']

            if self.check_resources(ingredients_needed):
                for ingredient, amount in ingredients_needed.items():
                    self.machine_resources[ingredient] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appetit!")
            else:
                print("Sorry, there is not enough ingredients to make your sandwich.")
        else:
            print("Sorry, we don't have that size of sandwich available.")

    def display_resources(self):
        print("Current Resources:")
        for ingredient, amount in self.machine_resources.items():
            print(f"{ingredient.capitalize()}: {amount} {'slice(s)' if 'bread' in ingredient else 'slice(s)' if 'ham' in ingredient else 'pound(s)'}")


recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}


machine = SandwichMachine(resources)

while True:
    action = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

    if action == "off":
        break
    elif action == "report":
        machine.display_resources()
    elif action in ["small", "medium", "large"]:
        size = action
        order_ingredients = recipes[size]['ingredients']

        print(f"Please insert coins for {size} sandwich.")
        coins_inserted = machine.process_coins()

        if coins_inserted > 0:
            cost = recipes[size]['cost']
            if machine.transaction_result(coins_inserted, cost):
                machine.make_sandwich(size, order_ingredients)
        else:
            print("No coins inserted. Order cancelled.")
    else:
        print("Invalid option. Please choose from (small/ medium/ large/ off/ report).")

print("Thank you for using the Sandwich Machine!")

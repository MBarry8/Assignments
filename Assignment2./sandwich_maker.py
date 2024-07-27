# sandwich_maker.py

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        return f"{sandwich_size} sandwich is ready. Bon appetit!"

    def display_resources(self):
        print("Current Resources:")
        for ingredient, amount in self.machine_resources.items():
            print(f"{ingredient.capitalize()}: {amount} {'slice(s)' if 'bread' in ingredient else 'slice(s)' if 'ham' in ingredient else 'ounce(s)'}")

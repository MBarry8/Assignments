# main.py

import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Create instances of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        action = input("What would you like? (small/medium/large/off/report): ").strip().lower()

        if action == "off":
            break
        elif action == "report":
            sandwich_maker_instance.display_resources()
        elif action in ["small", "medium", "large"]:
            size = action
            order_ingredients = recipes[size]['ingredients']

            print(f"Please insert coins for {size} sandwich.")
            coins_inserted = cashier_instance.process_coins()

            if coins_inserted > 0:
                cost = recipes[size]['cost']
                if cashier_instance.transaction_result(coins_inserted, cost):
                    print(sandwich_maker_instance.make_sandwich(size, order_ingredients))
            else:
                print("No coins inserted. Order cancelled.")
        else:
            print("Invalid option. Please choose from (small/medium/large/off/report).")

    print("Thank you for using the Sandwich Machine!")

if __name__ == "__main__":
    main()

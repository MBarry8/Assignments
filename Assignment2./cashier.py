# cashier.py

class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        try:
            large_dollars = int(input("How many large dollars?: ")) * 1.00
            half_dollars = int(input("How many half dollars?: ")) * 0.50
            quarters = int(input("How many quarters?: ")) * 0.25
            nickels = int(input("How many nickels?: ")) * 0.05
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
            print("Sorry, that's not enough money. Money refunded.")
            return False

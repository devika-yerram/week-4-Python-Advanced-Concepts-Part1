import threading
import time
import json

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} of {item_name}. New quantity: {self.items[item_name]}")

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            print(f"Removed {quantity} of {item_name}. New quantity: {self.items[item_name]}")
            if self.items[item_name] == 0:
                print(f"Item {item_name} is out of stock!")
        else:
            print(f"Cannot remove {quantity} of {item_name}. Insufficient stock or item does not exist.")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def save_to_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                json.dump(self.items, file)
            print(f"Inventory saved to {file_name}")
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.items = json.load(file)
            print(f"Inventory loaded from {file_name}")
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")

    def periodic_stock_check(self, threshold, interval):
        def check():
            while True:
                for item, quantity in self.items.items():
                    if quantity <= threshold:
                        print(f"Alert: {item} is low in stock! Current quantity: {quantity}")
                time.sleep(interval)

        threading.Thread(target=check, daemon=True).start()


if __name__ == "__main__":
    inventory = Inventory()

    # Add items to inventory
    inventory.add_item("Apple", 50)
    inventory.add_item("Banana", 30)
    inventory.add_item("Orange", 10)

    inventory.remove_item("Apple", 20)
    inventory.remove_item("Orange", 5)

    inventory.save_to_file("inventory_data.json")

    inventory.load_from_file("inventory_data.json")

    print("Current inventory state:")
    for item, quantity in inventory.items.items():
        print(f"{item}: {quantity}")

    inventory.periodic_stock_check(threshold=10, interval=5)

    while True:
        time.sleep(1)

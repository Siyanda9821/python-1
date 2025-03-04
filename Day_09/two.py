inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
]


def display_inventory(inventory):
    """Display the current inventory in a formatted way."""
    print("\n🗃️ Current Inventory:")
    for item in inventory:
        print(f"{item['name']} - Qty: {item['quantity']}, Price: ${item['price']:.2f}")
    print()


def task1_add_product(inventory):
    """Task 1: Add a new product to the inventory."""
    print("🆕 Add New Product")
    name = input("What is the product name? ")
    quantity = int(input("What is the quantity? "))
    price = float(input("What is the price? "))

    new_product = {"name": name, "quantity": quantity, "price": price}

    inventory.append(new_product)
    print(f"\n{new_product}")
    display_inventory(inventory)
    return inventory


def task2_update_product(inventory):
    """Task 2: Update an existing product in the inventory."""
    print("🔄 Update Existing Product")
    name = input("Enter product name to update: ")

    for item in inventory:
        if item["name"] == name:
            additional_quantity = int(input("Enter additional quantity: "))
            new_price = float(input("Enter new price: "))

            item["quantity"] += additional_quantity
            item["price"] = new_price

            print(f"Updated {name} successfully! 🎉")
            display_inventory(inventory)
            return inventory

    print(f"Product {name} not found in inventory. 😕")
    return inventory


def task3_add_or_update_product(inventory):
    """Task 3: Add or update product using for-else construct."""
    print("➕ Add or Update Product")
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    for item in inventory:
        if item["name"] == name:
            item["quantity"] = quantity
            item["price"] = price
            print(f"Updated existing product {name}! 🔄")
            break
    else:
        new_product = {"name": name, "quantity": quantity, "price": price}
        inventory.append(new_product)
        print(f"Added new product {name}! 🎉")

    display_inventory(inventory)
    return inventory


def main():
    # Initial inventory
    inventory = [
        {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
        {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
    ]

    display_inventory(inventory)

    while True:
        print("Inventory Management Menu:")
        print("1. Add New Product")
        print("2. Update Existing Product")
        print("3. Add or Update Product")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            inventory = task1_add_product(inventory)
        elif choice == "2":
            inventory = task2_update_product(inventory)
        elif choice == "3":
            inventory = task3_add_or_update_product(inventory)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again. 🤔")


if __name__ == "__main__":
    main()

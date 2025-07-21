import random
import json

shopping_list = []
FILENAME = "shopping_list.json"



# Define function to display menu options
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Mark item as purchased")
    print("4. Remove item")
    print("5. Save and exit")
    print("6. Load shopping list from file")
    print("7. Exit without saving")


# Define function to add items to the list (name, quantity, category, price, and if purchased)

def add_item():
    item_name = input("Enter item name: ").strip()
    if not item_name:
        print("Item name cannot be empty.")
        return
    
    quantity = input("Enter item quantity ").strip()
    if not quantity.isdigit():
        print("Quantity must be a number.")
        return
    quantity = int(quantity)


    category = input("Enter item category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return
    
    price = input("Enter item price: ").strip()
    try:
        price = float(price)
    except ValueError:
        print("Price must be a number.")
        return
    
    purchased = input("Is the item purchased (y/n)? ").strip().lower()
    if purchased not in ('y', 'n'):
        print("Invalid input for purchased status. Please enter 'y' or 'n'.")
        return
    purchased = purchased == 'y'

    item = {
        "name": item_name,
        "quantity": quantity,
        "category": category,
        "price": price,
        "purchased": purchased
    }

    shopping_list.append(item)
    print(f"Item: {item_name} added to the shopping list.")
    print(shopping_list)
    
    


    
# Define function to view the current shopping list

def view_list():
    if not shopping_list:
        print("Shopping list is empty.")
        return
    
    print("\nCurrent Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        status = "Purchased" if item["purchased"] else "Not Purchased"
        print(f"{index}. Name: {item['name']}, Quantity: {item['quantity']}, Category: {item['category']}, price: ${item['price']}, status: {status}")


# Define function to Mark items as purchased

def mark_item_purchased():
    if not shopping_list:
        print("Item not in shopping list.")
        return
    view_list()
    try:
        item_index = int(input("Enter the inex of the item to mark as purchased: ")) -1
        if item_index < 0 or item_index >= len(shopping_list):
            print("Invalid item index.")
            return
        shopping_list[item_index]["purchased"] = True
        print(f"Item: {shopping_list[item_index]['name']} marked as purchased.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")


# Define function to remove items from the list
def remove_item():
    if not shopping_list:
        print("Shopping list is empty.")
        return
    
    view_list()
    try:
        item_index = int(input("Enter the index of the item to remove: ") -1)
        if item_index < 0 or item_index > len(shopping_list):
            print("Invalid item index.")
            return
            removed_item = shopping_list.pop(item_index)
            print(f"Item: {removed_item['name']} has sucessfully been removed from shopping list.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    view_list()
    pass
    # try:
    #     item_index = int(input("Enter the index of the item to remove: ") -1)
    #     if item_index < 0 or item_index > len(shopping_list):
    #         print("Invalid item index.")
    #         return
    #         removed_item = shopping_list.pop(item_index)
    #         print(f"Item: {removed_item['name']} has sucessfully been removed from shopping list.")
    # except ValueError:
    #     print("Invalid input. Please enter a number.")


# Define function to save list as a JSON file
def save_list():
    pass

# Define a function to load the shopping list from a JSON file
def load_list():
    pass


# Define main function to run program loop

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            add_item()
        elif choice == "2":
            view_list()
        elif choice == "3":
            mark_item_purchased()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            save_list()
            print("Shopping list saved, exiting program.")
        elif choice == "6":
            load_list()
        elif choice == "7":
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice. Please try again.")
            break


if __name__ == "__main__":
    main()
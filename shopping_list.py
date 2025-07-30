import random
import json

#* Constant variables
FILENAME = "shopping_list.json"
#* Constants for discount feature (commented out for now)
# DISCOUNT_CHANCE = 0.3 # 30% chance of a random discount
# DISCOUNT_PERCENT = 15 # 15% discount

#* Initialize shopping list as an empty list
shopping_list = []


#* Define function to display menu options
def display_menu():
   
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Mark item as purchased")
    print("4. Remove item")
    print("5. Generate category summary")
    print("6. Save and exit")
    print("7. Load shopping list from file")
    print("8. Exit without saving")



#* Define function to add items to the list (name, quantity, category, price, and if purchased)

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
    
    price = float(price)
    
    
#* use random module to apply a random discount 
# if random.random() < DISCOUNT_CHANCE:
#     original_price = price
#     price = round(price * (1 - DISCOUNT_PERCENT / 100), 2)
#     print(f"Discount applied! Original price: ${original_price}, New price: ${price}")
    
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

    
#* Define function to view the current shopping list

def view_list():
    if not shopping_list:
        print("Shopping list is empty.")
        return
    
    print("\nCurrent Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        status = "Purchased" if item["purchased"] else "Not Purchased"
        print(f"{index}. Name: {item['name']}, Quantity: {item['quantity']}, Category: {item['category']}, price: ${item['price']}, status: {status}")


#* Define function to Mark items as purchased

def mark_item_purchased():
    if not shopping_list:
        print("Item not in shopping list.")
        return
    view_list()
    
    item_index = int(input("Enter the inex of the item to mark as purchased: ")) -1
    if item_index < 0 or item_index >= len(shopping_list):
        print("Invalid item index.")
        return
    shopping_list[item_index]["purchased"] = True
    print(f"Item: {shopping_list[item_index]['name']} marked as purchased.")
    
    


#* Define function to remove items from the list
def remove_item():
    if not shopping_list:
        print("Shopping list is empty.")
        return
    print("Items in the shopping list: ")

    
    view_list()
    
    item_index = int(input("Enter the index of the item to remove: "))
    if 1 <= item_index <= len(shopping_list):
        removed_item = shopping_list.pop(item_index - 1)
        print(f"Item '{removed_item['name']}' removed from the shopping list.")
    

#* Define function to generate a summary of items by category
def generate_category_summary():
    if not shopping_list:
        print("\nShopping list is empty.")
        return
    
    category_dict = {}
    for item in shopping_list:
        cat = item["category"]
        if cat not in category_dict:
            category_dict[cat] = {
                "count": 0,
                "total_cost": 0,
                "purchased": 0
            }
        
        category_dict[cat]["count"] += 1
        category_dict[cat]["total_cost"] += item["price"] * item["quantity"]
        if item["purchased"]:
            category_dict[cat]["purchased"] += 1

#* Display summary
    print("\nCategory Summary:")
    print("-" * 50)
    for category, data in category_dict.items():
        print(f"Category: {category}")
        print(f"  Count: {data['count']}")
        print(f"  Total Cost: ${data['total_cost']:.2f}")
        print(f"  Purchased: {data['purchased']}")
        print("-" * 50)



#* Define function to save list as a JSON file
def save_list():
        
        with open(FILENAME, 'w') as file:
            json.dump("/Users/erekofke/Desktop/shopping_list.txt", file)
            print(f"\nShopping list saved to {FILENAME}.")
        
    

#* Define a function to load the shopping list from a JSON file
def load_list():
    with open("/Users/erekofke/Desktop/shopping_list.txt", 'r') as file:
        global shopping_list
        shopping_list = json.load(file)
        print(F"Shopping list loaded from {FILENAME}")


#* Define main function to run program loop
#* Print decorative header
def main():
    print("\n" + "=" * 50)
    print("Welcome to the Shopping List Manager!")
    print("=" * 50)

    #* Load existing shopping list if available
    load_list()

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
            generate_category_summary()
        elif choice == "6":
            save_list()
            print("\nExiting program. Goodbye!")
            break
        elif choice == "7":
            load_list()
        elif choice == "8":
            print("\nExiting without saving. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-8")


if __name__ == "__main__":
    main()
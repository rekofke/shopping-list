import random
import json

shopping_list = []
FILENAME = "shopping_list.json"



# Define function to display menu options
def display_menu():
    pass

# Define function to add items to the list (name, quantity, category, price, and if purchased)

def add_item():
    pass
    
    


    
# Define function to view the current shopping list

def view_list():
    pass
        


# Define function to Mark items as purchased

def mark_item_purchased():
    pass


# Define function to remove items from the list
def remove_item():
    pass
    
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
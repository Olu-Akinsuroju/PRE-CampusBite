# --a menu system for a command line food ordering app
# Menu system
print("Menu system")

# Initial Menu
Menu = {
    "Burger": {"categories": "Fast Food", "price": 5},
    "Pizza": {"categories": "Italian", "price": 8},
    "Salad": {"categories": "Healthy", "price": 6}
}


# Function to add an item to the menu
def Add_item(menu):
    item = input("What is the name of the item? ")
    category = input("What category does the item belong to? ")
    price = input("What is the price of the item? ")

    # Add the new item to the menu
    menu[item] = {"categories": category, "price": price}
    print(f"Item '{item}' added to the menu.")

# funtion to update item
def update_item(menu):
    item_name = input("whta is the name of the item")
    if item_name not in menu:
        print("item not found in menu")
    else:
        print("\nChoose one of the followint to update about item:")
        print("1.price")
        print("2.category")
        print("3.name")

        option_chosen = input("Enter your choice: ")  

    if option_chosen == "1":
        new_price= input("what is price")
        try:
            new_price = int(new_price)
        except ValueError:
            print("Invalid price. It should be a number.")
            return
        menu[item_name]['price']==new_price
        print("price of '{item_name}hs been changed to '{new_price}")
    elif option_chosen =="2":
        new_category = input("what is the new category")
        menu[item_name]['category']  = new_category
        print(f"category of '{item_name}' has been changed to '{new_category}'")
    else:
          new_name = input ("what is the new name of the item")    
          menu[new_name] = menu.pop(item_name)
          print(f"Item '{item_name}' has been renamed to '{new_name}'.")

# funtion to remove item
def remove_item(menu):
    item_name = input("whta is the name of the item to remove")
    if item_name not in menu:
        print("item not found in menu")
    else:
      del menu[item_name]
      print(f"item '{item_name}has been removed from the menu")

    
#function to stimulate order
def stimulate_order(menu):
    print("Items available in the menu are displayed below:")
    Display_items(menu)
    
    total_cost = 0
    items_chosen = []

    while True:
        chosen_item = input("Type the name of the item you want to order (or type 'done' to finish): ")
        if chosen_item.lower() == 'done':
            break
        if chosen_item in menu:
            total_cost += menu[chosen_item]['price']
            items_chosen.append(chosen_item)
            print(f"Added '{chosen_item}' to your order. Current total: {total_cost}.")
        else:
            print(f"Item '{chosen_item}' not found in the menu. Please choose again.")

    print(f"Your order: {', '.join(items_chosen)}. Total cost: ${total_cost:.2f}")



# Function to display the menu
def Display_items(menu):
    print("Current Menu:")
    for item, details in menu.items():
        print(f"Item: {item}, Category: {details['categories']}, Price: {details['price']}")

# Main loop for menu options
while True:
    print("\nChoose one of the following options:")
    print("1. Add item")
    print("2. Update item")
    print("3. Remove item")
    print("4. Display items")
    print("5. Simulate order")
    print("6. Exit")

    option_chosen = input("Enter your choice: ")
    
    if option_chosen == "1":
        Add_item(Menu)
    elif option_chosen == "2":
        update_item(Menu)
    elif option_chosen == "3":
        remove_item(Menu)
    elif option_chosen == "4":
        Display_items(Menu)
    elif option_chosen == "5":
        stimulate_order(Menu)
    elif option_chosen == "6":
        print("Exiting the menu system. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option.")

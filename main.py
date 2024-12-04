import sys
from inventory import InventoryItem
from file_operations import load_from_csv, save_to_csv
from validation import validate_input
from data_analysis import get_inventory_stats
from report_generator import generate_report

def display_menu():
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Generate Report")
    print("6. Exit")

def update_item(inventory_items, item_id):
    # Find the item in the list by item_id
    item = next((item for item in inventory_items if item.item_id == item_id), None)
    
    if item:
        print(f"Current details of {item_id}:")
        print(f"Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Supplier: {item.supplier}")
        
        # Update item attributes
        new_name = input(f"Enter new name (current: {item.name}): ") or item.name
        new_quantity = validate_input(input(f"Enter new quantity (current: {item.quantity}): ") or item.quantity, "int")
        new_price = validate_input(input(f"Enter new price (current: {item.price}): ") or item.price, "float")
        new_supplier = input(f"Enter new supplier (current: {item.supplier}): ") or item.supplier
        
        # Update item in the inventory
        item.name = new_name
        item.quantity = new_quantity
        item.price = new_price
        item.supplier = new_supplier

        save_to_csv(inventory_items)  # Save the updated list to CSV
        print(f"Item {item_id} updated successfully.")
    else:
        print(f"Item with ID {item_id} not found.")

def delete_item(inventory_items, item_id):
    # Find the item in the list by item_id
    item = next((item for item in inventory_items if item.item_id == item_id), None)
    
    if item:
        inventory_items.remove(item)
        save_to_csv(inventory_items)  # Save the updated list to CSV
        print(f"Item {item_id} deleted successfully.")
    else:
        print(f"Item with ID {item_id} not found.")

def main():
    inventory_items = load_from_csv()  # Load inventory from CSV file
    
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            get_inventory_stats(inventory_items)

        elif choice == '2':
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            quantity = validate_input(input("Enter quantity: "), "int")
            price = validate_input(input("Enter price: "), "float")
            supplier = input("Enter supplier name: ")
            new_item = InventoryItem(item_id, name, quantity, price, supplier)
            inventory_items.append(new_item)
            save_to_csv(inventory_items)
            print("Item added successfully.")

        elif choice == '3':
            item_id = input("Enter item ID to update: ")
            update_item(inventory_items, item_id)  # Call update item logic

        elif choice == '4':
            item_id = input("Enter item ID to delete: ")
            delete_item(inventory_items, item_id)  # Call delete item logic

        elif choice == '5':
            generate_report(inventory_items)

        elif choice == '6':
            print("Exiting system.")
            sys.exit()

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

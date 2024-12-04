# file_operations.py
import csv
import pickle
from inventory import InventoryItem

def save_to_csv(inventory_items, filename="inventory.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Name', 'Quantity', 'Price', 'Supplier'])
        for item in inventory_items:
            writer.writerow([item.item_id, item.name, item.quantity, item.price, item.supplier])

def load_from_csv(filename="inventory.csv"):
    inventory_items = []
    
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Use next() with a default value to avoid StopIteration error

            if header is None:
                print(f"The file '{filename}' is empty or does not have a header.")
                return inventory_items  # Return an empty list if the file is empty

            # Process the rest of the rows
            for row in reader:
                if row:  # Ensure that the row is not empty
                    try:
                        item_id, name, quantity, price, supplier = row
                        
                        # Convert quantity to an integer and price to a float
                        inventory_items.append(InventoryItem(item_id, name, int(quantity), float(price), supplier))
                    except ValueError as e:
                        # This block will catch errors if conversion fails (e.g., non-numeric value for quantity/price)
                        print(f"Skipping row due to value error: {row} - {e}")
            
            if not inventory_items:
                print(f"No valid inventory items found in the file '{filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading the CSV file: {e}")

    return inventory_items

def save_to_pickle(inventory_items, filename="inventory.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(inventory_items, file)

def load_from_pickle(filename="inventory.pkl"):
    with open(filename, 'rb') as file:
        return pickle.load(file)

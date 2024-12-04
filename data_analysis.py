# data_analysis.py
import pandas as pd

def get_inventory_stats(inventory_items):
    data = {
        'Item ID': [item.item_id for item in inventory_items],
        'Name': [item.name for item in inventory_items],
        'Quantity': [item.quantity for item in inventory_items],
        'Price': [item.price for item in inventory_items],
        'Total Value': [item.total_value() for item in inventory_items],
    }
    df = pd.DataFrame(data)
    total_value = df['Total Value'].sum()
    avg_price = df['Price'].mean()
    print(f"Total Inventory Value: ${total_value:.2f}")
    print(f"Average Item Price: ${avg_price:.2f}")
    return df

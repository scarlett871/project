# report_generator.py
from data_analysis import get_inventory_stats

def generate_report(inventory_items, filename="inventory_report.csv"):
    df = get_inventory_stats(inventory_items)
    df.to_csv(filename, index=False)
    print(f"Report generated: {filename}")

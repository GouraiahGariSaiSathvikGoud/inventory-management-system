from database import initialize_db
import inventory
import reports

def print_menu():
    print("\n===== Inventory Management System =====")
    print("1. Add Item")
    print("2. View All Items")
    print("3. Update Item Quantity")
    print("4. Delete Item")
    print("5. Generate Reports")
    print("6. Exit")

def print_reports_menu():
    print("\n--- Reports ---")
    print("1. Total Inventory Value")
    print("2. Low Stock Report")
    print("3. Category Summary")

def main():
    initialize_db()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            category = input("Category: ").strip()
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))
                inventory.add_item(name, category, quantity, price)
                print("Item added successfully.")
            except ValueError:
                print("Invalid quantity or price. Must be numeric.")

        elif choice == "2":
            items = inventory.get_all_items()
            if not items:
                print("No items found.")
            for item in items:
                print(f"ID: {item['item_id']} | {item['name']} | {item['category']} | Qty: {item['quantity']} | ${item['price']}")

        elif choice == "3":
            try:
                item_id = int(input("Item ID: "))
                new_qty = int(input("New quantity: "))
                inventory.update_item_quantity(item_id, new_qty)
                print("Quantity updated.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            try:
                item_id = int(input("Item ID to delete: "))
                inventory.delete_item(item_id)
                print("Item deleted.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            print_reports_menu()
            rchoice = input("Choose report: ").strip()
            if rchoice == "1":
                print(f"Total Inventory Value: ${reports.total_inventory_value():.2f}")
            elif rchoice == "2":
                low_stock = reports.low_stock_report()
                if not low_stock:
                    print("No low-stock items.")
                for item in low_stock:
                    print(f"LOW STOCK - {item['name']}: {item['quantity']} left")
            elif rchoice == "3":
                summary = reports.category_summary()
                for row in summary:
                    print(f"{row['category']}: {row['item_count']} items, Qty {row['total_qty']}, Value ${row['value']:.2f}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
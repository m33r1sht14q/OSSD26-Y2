stock = 100
total_sold = 0

print("===== Inventory Management System =====")
print(f"Initial Stock: {stock} units")
print("Enter quantity sold for each sale (Enter -1 to exit)\n")

while True:
    quantity = int(input(f"Enter quantity sold (Current Stock: {stock}): "))

    if quantity == -1:
        print("\nSales session ended by user.")
        break

    if quantity <= 0:
        print("Error: Quantity sold must be greater than 0!\n")
        continue

    if quantity > stock:
        print(f"Error: Transaction rejected! Only {stock} units available.\n")
        continue

    stock -= quantity
    total_sold += quantity
    print(f"Sale successful! {quantity} units sold.\n")

    if stock == 0:
        print("Stock depleted! No more sales can be processed.")
        break

print("\n" + "=" * 35)
print(f"Total Units Sold : {total_sold}")
print(f"Remaining Stock  : {stock}")
print("=" * 35)
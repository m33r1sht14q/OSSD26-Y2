print("===== Electricity Bill Calculator =====")
print("Enter unit consumption for each customer (Enter -1 to exit)\n")

total_revenue = 0
customer_count = 0

while True:
    units = float(input("Enter units consumed: "))

    if units == -1:
        print("\nStopping bill processing...")
        break

    if units < 0:
        print("Error: Unit consumption cannot be negative! Please try again.\n")
        continue

    bill_amount = 0

    if units <= 100:
        bill_amount = units * 10
    elif units <= 200:
        bill_amount = (100 * 10) + ((units - 100) * 15)
    elif units <= 300:
        bill_amount = (100 * 10) + (100 * 15) + ((units - 200) * 20)
    else:
        bill_amount = (100 * 10) + (100 * 15) + (100 * 20) + ((units - 300) * 25)

    customer_count += 1
    total_revenue += bill_amount

    print(f"Customer #{customer_count} Total Bill: Rs. {bill_amount:.2f}\n")

print("\n" + "=" * 35)
print(f"Total Customers Processed: {customer_count}")
print(f"Total Revenue Collected  : Rs. {total_revenue:.2f}")
print("=" * 35)
print("===== Menu-Driven Number Analysis System =====")
print("Enter positive integers to analyze (Enter 0 to stop):\n")

even_count = 0
odd_count = 0
total_sum = 0
total_count = 0
largest_number = None

while True:
    number = int(input("Enter an integer: "))

    # Exit condition
    if number == 0:
        print("\nStopping data input...")
        break

    # Requirement: Ignore negative numbers using continue
    if number < 0:
        print("Negative number ignored.")
        continue

    # Process valid positive numbers
    total_count += 1
    total_sum += number

    # Determine even or odd
    if number % 2 == 0:
        print(f"{number} is Even.")
        even_count += 1
    else:
        print(f"{number} is Odd.")
        odd_count += 1

    # Track largest positive number
    if largest_number is None or number > largest_number:
        largest_number = number

# Final Summary Results
print("\n" + "=" * 40)
if total_count == 0:
    print("No valid positive numbers were entered.")
else:
    average = total_sum / total_count
    print(f"Total positive numbers entered : {total_count}")
    print(f"Count of Even numbers         : {even_count}")
    print(f"Count of Odd numbers          : {odd_count}")
    print(f"Largest positive number       : {largest_number}")
    print(f"Sum of positive numbers       : {total_sum}")
    print(f"Average of positive numbers   : {average:.2f}")
print("=" * 40)
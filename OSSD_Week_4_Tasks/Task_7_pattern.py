n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Error: Please enter a positive integer greater than 0.")
else:
    print("\n--- Standard Pattern ---")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    print("\n--- Inverted Pattern ---")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    print("\n--- Multiplication Table (1 to " + str(n) + ") ---")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()
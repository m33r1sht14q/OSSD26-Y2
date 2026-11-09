print("===== Fibonacci Sequence Analyzer =====")

while True:
    terms = int(input("Enter the number of terms to generate: "))

    if terms < 1:
        print("Error: Term count must be at least 1! Please try again.\n")
        continue
    break

a, b = 0, 1
fib_sum = 0
even_count = 0
odd_count = 0

print("\nFibonacci Sequence:")

for _ in range(terms):
    print(a, end=" ")

    fib_sum += a

    if a % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    a, b = b, a + b

print("\n" + "-" * 30)
print(f"Sum: {fib_sum}")
print(f"Even terms: {even_count}")
print(f"Odd terms: {odd_count}")
print("-" * 30)
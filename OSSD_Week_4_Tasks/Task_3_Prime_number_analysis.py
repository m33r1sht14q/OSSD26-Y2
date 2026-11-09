print("=== Prime Number Range Analyzer ===")


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

prime_count = 0
prime_sum = 0

print(f"\nPrime numbers between {start} and {end}:")


for num in range(start, end + 1):


    if num < 2:
        continue


    is_prime = True


    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break


    if is_prime:
        print(num, end=" ")
        prime_count = prime_count + 1
        prime_sum = prime_sum + num


print("\n-----------------------------------")
print(f"Total prime numbers found: {prime_count}")
print(f"Sum of prime numbers: {prime_sum}")
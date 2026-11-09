import random

secret_number = random.randint(1, 100)
attempts = 0

print("----- Number Guessing Game (1 to 100) -----")

while True:
    guess = int(input("Enter your guess: "))

    # Reject numbers outside 1-100 without losing an attempt
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100!\n")
        continue

    # Count valid attempts
    attempts += 1

    # Check the guess
    if guess == secret_number:
        if attempts == 1:
            print("PERFECT SCORE! You guessed it on the 1st try!")
        else:
            print(f"Correct! You won in {attempts} attempts!")
        break

    elif guess < secret_number:
        print("Too LOW!\n")

    else:
        print("Too HIGH!\n")

    # Game over after 7 attempts
    if attempts == 7:
        print(f"Game Over! The secret number was {secret_number}.")
        break
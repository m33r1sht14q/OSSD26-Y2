print("-----ATM Withdrawal System------")

print("Press 1 to check balance")
print("Press 2 to deposit money")
print("Press 3 to withdraw money")
print("Press 4 to Exit")

account_balance = 50000

while True:
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${account_balance}")

    elif choice == "2":
        deposit = int(input("Enter amount to deposit: "))

        # Validate that deposit is positive
        if deposit <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            account_balance += deposit
            print(f"Successfully deposited ${deposit}.")

    elif choice == "3":
        withdraw = int(input("Enter money for withdraw: "))

        if withdraw<=0:
            print("Withdraw amount must be greater than 0")

        else:
            account_balance-=withdraw
            print(f"You successfully withdraw ${withdraw} ")

    elif choice == "4":
        print("You are exiting ATM system")
        break

    else:
        print("Please Enter number between 1 and 4")
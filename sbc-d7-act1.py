import random

def print_menu():
    print("1. Check Balance")
    print("2. Open an Account")
    print("3. Close an Account")
    print("4. Withdraw Money")
    print("5. Deposit Money")
    print("6. Quit")
    print()

accounts = {}
balances = {}
menu_choice = 0
print_menu()

while True:
    try:
        menu_choice = int(input("Type in a number (1-6): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    print()
    
    if menu_choice == 1:
        account_number = input("Enter your account number: ")
        account_number = int(account_number)
        if account_number in accounts:
            print(f"Account number: {account_number}, Balance: ₱{balances[account_number]}")
        else:
            print("Account number not found.")
        print()
        
    elif menu_choice == 2:
        print("Opening a new account.")
        account_number = random.randint(10000, 99999)
        while account_number in accounts:
            account_number = random.randint(10000, 99999)
        accounts[account_number] = True
        balances[account_number] = 0
        print(f"Account number {account_number} opened with balance ₱0.")
        
    elif menu_choice == 3:
        print("Closing an account.")
        account_number = input("Account number: ")
        account_number = int(account_number)
        if account_number in accounts:
            del accounts[account_number]
            del balances[account_number]
            print(f"Account number {account_number} is closed.")
        else:
            print("Account number not found.")
            
    elif menu_choice == 4:
        print("Withdraw money from an account.")
        account_number = input("Account number: ")
        account_number = int(account_number)
        if account_number in accounts:
            withdraw_amount = float(input("How much money would you like to withdraw? > "))
            if withdraw_amount <= balances[account_number]:
                balances[account_number] -= withdraw_amount
                print(f"Your new balance is ₱{balances[account_number]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account number not found.")
            
    elif menu_choice == 5:
        print("Deposit money into an account.")
        account_number = input("Account number: ")
        account_number = int(account_number)
        if account_number in accounts:
            deposit_amount = float(input("How much money would you like to deposit? > "))
            balances[account_number] += deposit_amount
            print(f"Your new balance is ₱{balances[account_number]}")
        else:
            print("Account number not found.")
            
    elif menu_choice == 6:
        print("Quit.")
        break
        
    else:
        print("Please enter a number between 1 and 6.")
        
    print()
    print_menu()

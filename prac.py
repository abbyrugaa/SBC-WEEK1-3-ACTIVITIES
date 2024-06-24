def add_number(num_list):
    number = int(input("Enter a number to add: "))
    num_list.append(number)
    print(f"Number {number} added. Updated list:", num_list)

def remove_first(num_list):
    if num_list:
        num_list.pop(0)
        print("Result sa NAA boss:", num_list)
    else:
        print("List is empty, cannot pop from an empty list.")

def remove_last(num_list):
    if num_list:
        num_list.pop()
        print("Result sa WALA boss:", num_list)
    else:
        print("List is empty, cannot pop from an empty list.")

# Initial input
num = []
num.extend([int(input(f"Enter number {i+1}: ")) for i in range(3)])

print("Display User Numbers:", num)

while True:
    action = input("Enter 'naa' if naa, Enter 'wala' kung wala, Enter 'add' to add a number: ").strip().lower()

    if action == "naa":
        remove_first(num)
    elif action == "wala":
        remove_last(num)
    elif action == "add":
        add_number(num)
    else:
        print("Not Valid Input. Please enter 'naa', 'wala', or 'add'.")

    # Ask user if they want to continue
    choice = input("Do you want to continue? Enter 'yes' or 'no': ").strip().lower()
    if choice != 'yes':
        break

print("Program ended.")

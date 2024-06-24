# Initial input
num = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
print("Display User Numbers:", num)

def add(num_list):
    number = int(input("Enter a number to add: "))
    num_list.append(number)
    print(f"Number {number} added. Updated list:", num_list)

def stack(num_list):
    if num_list:
        num_list.pop(0)
        print("Result sa NAA boss:", num_list)
    else:
        print("List is empty, cannot pop from an empty list.")

def queue(num_list):
    if num_list:
        num_list.pop()
        print("Result sa WALA boss:", num_list)
    else:
        print("List is empty, cannot pop from an empty list.")

while True:
    action = input("Enter 'naa' if naa, 'wala' if wala, 'add' to add a number: ").strip().lower()

    if action == "naa":
        stack(num)
    elif action == "wala":
        queue(num)
    elif action == "add":
        add(num)
    else:
        print("Not Valid Input. Please enter 'naa', 'wala', or 'add'.")

    if input("Do you want to continue? Enter 'yes' or 'no': ").strip().lower() != 'yes':
        break

print("Program ended.")

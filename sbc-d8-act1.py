import os

def load_users():
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            return dict(line.strip().split(',') for line in file)
    return {}

def save_users(users):
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")

def register(users):
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
    else:
        password = input("Enter password: ")
        users[username] = password
        save_users(users)
        print("Successfully registered.")

def login(users):
    username = input("Enter username: ")
    if username in users:
        password = input("Enter password: ")
        if users[username] == password:
            print("Login successful.")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

def change_password(users):
    username = input("Enter username: ")
    if username in users:
        old_password = input("Enter old password: ")
        if users[username] == old_password:
            new_password = input("Enter new password: ")
            users[username] = new_password
            save_users(users)
            print("Password successfully changed.")
        else:
            print("Incorrect old password.")
    else:
        print("Username not found.")

def main():
    users = load_users()
    actions = {
        '1': register,
        '2': login,
        '3': change_password,
        '4': exit
    }

    while True:
        print("1. Register\n2. Log in\n3. Change password\n4. Exit")
        choice = input("Enter a number: ")
        if choice in actions:
            if choice == '4':
                break
            actions[choice](users)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

user = int(input("Enter the number of rows: "))

for i in range(user, 0, -1):
    print('*' * i)

for i in range(1, user + 1):
    if i == 2:
        print('*' + ' ' * (i-2) + '*')
    else:
        print('*' * i)

print("BINI")
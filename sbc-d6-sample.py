#FOR LOOP
#string = "Hello World"

#or char in string:
    #print(char)

#list_ = ["Zilong", "Miya", "Layla", "Nana"]
#for obj in list_:
    #print(obj)

#row = int(input("Row:"))
#for x in range(1,6):
    #print("*" * .lll.................x)

#WHILE LOOP
#log = True
#while log:
    #username = input("Username:")
    #password = input("Password:")
    #if username == "batman" and password == "akosiden":
       #print("Successfully Login")
        #log = False
    #else:
        #print("Login Failed, Try Again!")


word = input("Input a word to check:")

word = word.lower()

length_word = int(len(word))


for checker in range (len(word)):
    if word[-length_word] == word[-1]:
        print(word, "is a palindrome.")  
else:
        print(word, "is not a palindrome.")


n = int(input("Enter the number of rows: "))

# First part of the pattern
for i in range(n, 0, -1):
    print('*' * i)

# Second part of the pattern
for i in range(1, n + 1):
    if i == 2:
        print('*' + ' ' * (i-2) + '*')
    else:
        print('*' * i)

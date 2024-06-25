word = input("Enter a word: ")

length_word = int(len(word))

for checker in range(len(word)):
    if word[-length_word] == word[-1]:
        print(word, "is a palindrome.")     
    else:
        print(word, "is not a palindrome.")
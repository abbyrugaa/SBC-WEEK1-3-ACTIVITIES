word = "summer bootcamp"
u = word[0:7].title() + word[7:14].lower() + word[14].upper()
s = word[12].upper() + word[5].upper()
a = word[11:14] + word[4].upper()
b = word.replace("b", "L")
c = word.replace(" ","")

print(word.title())
print(u)
print(b[7:11])
print(a)
print(s)
print(c.isalpha())
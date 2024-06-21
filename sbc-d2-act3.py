from random import randint

oc = ["1", "2", "3", "5"]

b = input("Enter your bet (1 2 3): ")

res = "".join([oc[randint(0, 3)] for _ in range(3)])

if res == "123":
    out = "You Win!"
elif res[0] == "2" and res[1] == "1" and res[2] == "3":
    out = "You Partially Win!"
elif res == "555":
    out = "You lose!"
else:
    out = "Better Luck Next Time."

print(f"Result = {res}")
print(out)

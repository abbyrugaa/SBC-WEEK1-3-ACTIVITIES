from random import randint

ch = ["KULOB", "HAYANG"]

def get_winner(p1, p2, p3):
    if p1 == p2:
        res_p1_p2 = "Draw"
    elif p1 == "KULOB" and p2 == "HAYANG":
        res_p1_p2 = "HAYANG"
    elif p1 == "HAYANG" and p2 == "KULOB":
        res_p1_p2 = "HAYANG"
    else:
        res_p1_p2 = "KULOB"
    
    if p1 == p3:
        res_p1_p3 = "Draw"
    elif p1 == "KULOB" and p3 == "HAYANG":
        res_p1_p3 = "HAYANG"
    elif p1 == "HAYANG" and p3 == "KULOB":
        res_p1_p3 = "HAYANG"
    else:
        res_p1_p3 = "KULOB"
    
    if res_p1_p2 == "HAYANG" or res_p1_p3 == "HAYANG":
        return "P2 WINS!"
    elif res_p1_p2 == "Draw" and res_p1_p3 == "Draw":
        return "It's a draw!"
    else:
        return "P1 WINS!"

p1 = input("Enter your choice (KULOB/HAYANG): ").upper()

if p1 != "KULOB" and p1 != "HAYANG":
    print("Not Valid C. Please choose either KULOB or HAYANG.")
else:
    p2 = ch[randint(0, 1)]
    p3 = ch[randint(0, 1)]
    
    print(f"P1 (You) chose: {p1}")
    print(f"P2 chose: {p2}")
    print(f"P3 chose: {p3}")
    
    res = get_winner(p1, p2, p3)
    print(res)

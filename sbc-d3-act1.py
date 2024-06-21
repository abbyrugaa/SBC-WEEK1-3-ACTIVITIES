#nag import ug modules
from random import randint 

#nagset-up sa mga choices
choices = ["KULOB", "HAYANG"]

#nagkuha ug unsay iinput sa user
p1 = input("Enter your choice (KULOB/HAYANG): ").upper()

#nagvalidate sa giinput
if p1 not in choices:
    print("Please type only KULOB/HAYANG.")
else:
    p2 = choices[randint(0, 1)] #nag generate para ma randomize ang choices
    p3 = choices[randint(0, 1)]
    print(f"P1 chose: {p1}") #girpint ang mga choices
    print(f"P2 chose: {p2}")
    print(f"P3 chose: {p3}")
    
    #gi determine kinsay winner thru this conditonal statements
    if p1 == p2 == p3:
        print("It's a draw!")
    elif p1 != p2 and p1 != p3:
        print("P1 WINS!")
    elif p2 != p1 and p2 != p3:
        print("P2 WINS!")
    else:
        print("P3 WINS!")

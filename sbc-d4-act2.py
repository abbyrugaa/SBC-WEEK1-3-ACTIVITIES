from random import randint

outcome_choices = ["1", "2", "3", "5"] # Nag define ug mga possible outcomes

user_bet = input("Enter your bet (1 2 3): ") # Gkuha ang giinput sa user 

result = "".join([outcome_choices[randint(0, 3)] for _ in range(3)]) # ga generate ug random result


if result == "123": # Gi determine and outcome based sa result
    outcome_message = "You Win!"
elif result == "213":
    outcome_message = "You Partially Win!"
elif result == "555":
    outcome_message = "You lose!"
else:
    outcome_message = "Better Luck Next Time."

print(f"Result = {result}") # Gi display ag result ug ang outcome message
print(outcome_message)

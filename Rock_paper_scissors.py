import random

def game(n):
    select = ["rock", "paper", "scissors"]
    a = random.choice(select)
    print("Computer chose:",a)
    if n == a:
        print("It's a tie")
    elif (n == "rock" and a == "scissors") or \
         (n == "scissors" and a == "paper") or \
         (n == "paper" and a == "rock"):
        print("You Win!")
    else:
        print("You Lose!")

while True:
    n = input("Enter your choice (Rock/Paper/Scissors): ").lower()
    if n not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please choose Rock, Paper, or Scissors")
        continue
    game(n)
    choice = input("Would you like to continue? (y/n): ").lower()
    if choice == "n":
        print("Thanks for playing!")
        break



# import random
# select=["Rock","Paper","Scissors"]
# while True:
#     n=input("Enter your choice (Rock/Paper/Scissors):")
#     a=random.choice(select) 
#     if n==a:
#         print("Its a tie")
#     elif (n == "rock" and a == "scissors") or \
#         (n == "scissors" and a == "paper") or \
#          (n == "paper" and a == "rock"):
#         print("You Loose")
#     else :
#         print("You Win")
        
#         print("Would You like to Continue")
#         choice=input()
#         if choice=="n":
#             break
#         else:
#             pass

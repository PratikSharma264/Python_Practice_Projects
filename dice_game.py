#Loop
    #Ask user if roll or not
    #if user says yes
        #Ask user the n umber of dice to roll
        #generate 'n' number of random numbers
        #print result
    #if user says no
        #print thankyou ans exit
        #terminate loop
    #else
        #print invalid choice


# import random as ran
# die=[]
# while True:
#     ch=input("Do you want to roll the dice (y/n): ").lower()
#     if ch=="y":
#         n=int(input("Enter the number of die: "))
#         for i in range(n):
#             die.append(ran.randint(1,6))
#             print(die)
#     elif ch=='n':
#         print("Thank You!")
#         break
#     else:
#         print("Invalid Choice!")

import random as ran

while True:
    ch = input("Do you want to roll the dice (y/n): ").lower()
    if ch == "y":
        n = int(input("Enter the number of dice: "))      
        die = []        
        for i in range(n):
            die.append(ran.randint(1, 6))
        print(f"You rolled: {die}")
    elif ch == 'n':
        print("Thank You! Exiting...")
        break  
    else:
        print("Invalid Choice! Please enter 'y' to roll or 'n' to exit.")



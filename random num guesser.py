import random

print("Enter your guess between 1 and 100")

number_to_guess = random.randint(1, 100)

while True:
    x = int(input("Your guess: "))

    if x < number_to_guess:
        print("Too low! Try again.")
    elif x > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the right number: {number_to_guess}")
        break 
    print("The number was: ",number_to_guess) 

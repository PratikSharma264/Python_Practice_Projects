print("Welcome to a simple calculator")
while True:
    print("Enter the values to calculate")
    a=int(input())
    b=int(input())
    print("\nEnter the operation to perform'+,-,*,/")
    operation=input()
    if operation == '+':
        result = a+b
    elif operation == '-':
        result = a-b
    elif operation == '*':
        result =a*b
    elif operation == '/':
        if b!=0:
            result = a/b
        else:
            print("Invalid number.")
    else:
        print("Invalid Operation choosen.")
    print("The result is: ",result)
    print("Do you want to continue 'y/n")
    again=input().lower()
    if again != 'y':
        break
print("Thank you!")
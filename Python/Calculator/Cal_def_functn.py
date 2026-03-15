# creating calculator by functions
from unittest import result


def calculator():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number :"))
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        return num1 + num2 
    elif choice == 2:
        return num1 - num2 
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else: 
            return "Invalid input for division by zero"
    else:
        return "Invalid choice"
    
result = calculator()
print("Result : ", result)
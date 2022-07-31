# This program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
# Author: Chris Bagalwa
# 25/04/2022

# Import the math library
import math

# Prompt the user to choose the calculation they want to do
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment      - to calculate the amount of interest you'll earn on interest")
print("bond            - to calculate the amount you'll have to pay on a home loan")
choice = input("\nYour choice: ")
print()

# If the user chooses investment
if choice.lower() == "investment":
    # Prompt the user to input the amount of money that they are depositing
    P = float(input("Enter the deposit amount: "))
    # Prompt the user to input the interest rate (as a percentage)
    r = float(input("Enter the interest rate: "))
    r /= 100
    # Prompt the user to input the number of years they plan on investing for
    t = int(input("Enter the number of years: "))
    # Prompt the user to input whether they want simple or compound interest
    interest = input("Enter the type of interest to be applied (simple/compound): ")
    # variable to store the computed interest amount
    A = 0
    # if the user chooses simple interest
    if interest.lower() == "simple":
        # compute the simple interest using the given formula
        A = P * (1 + r * t)
    # else if the user chooses compound interest
    elif interest.lower() == "compound":
        # compute the compound interest using the given formula
        A = P * math.pow((1 + r), t)
    print()
    # Display the computed interest amount
    print(f"The {interest} interest is: {A:.2f}")

# Else if the user chooses bond
elif choice.lower() == "bond":
    # Prompt the user to input the present value of the house
    P = float(input("Enter the house value: "))
    # Prompt the user to input the interest rate
    r = float(input("Enter the annual interest rate: "))
    # Prompt the user to input the number of months they plan to take to repay the loan
    n = int(input("Enter the number of months: "))
    # Compute the monthly interest rate
    i = (r / 12) / 100
    # Compute the monthly payment using the given formula
    x = (i * P) / (1 - math.pow((1 + i),(-n)))
    print()
    # Display the computed monthly payment
    print(f"The monthly payment is: {x:.2f}")

# Else if the user selects an invalid choice
else:
    print("Invalid choice!")
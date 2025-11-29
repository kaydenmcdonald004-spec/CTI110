# Kayden McDonald
# Date
# P3LAB - Money Calculator
# This program allows the user to enter a money amount and calculates
# the most efficient number of dollars, quarters, dimes, nickels, and pennies.

# Ask user for money amount
amount = float(input("Enter amount of money: "))

# Convert dollars to cents
cents = int(amount * 100)

# Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Pennies
pennies = cents

# Output
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
# Kayden McDonald
# Date: 12/12/2025
# P5LAB – Self Checkout Simulation
# This program simulates a self-checkout machine. It generates a random total,
# asks the user for cash input, calculates change, and breaks it into coins.

import random

# ------------------------------------------------------
# FUNCTION: disperse_change
# Takes a float (change owed) and prints dollars and coins
# ------------------------------------------------------
def disperse_change(change):
    # Convert to cents to avoid floating-point issues
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("\nChange breakdown:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")


# ------------------------------------------------------
# FUNCTION: main
# Main logic of the program
# ------------------------------------------------------
def main():
    # Generate random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${amount_owed}")

    # Get user payment
    payment = float(input("Enter the amount of cash you will put into the machine: $"))

    # Calculate change
    if payment < amount_owed:
        print("Error: Payment is less than amount owed.")
        return

    change = round(payment - amount_owed, 2)
    print(f"Change owed: ${change}")

    # Call dispense function
    disperse_change(change)


# Call main function
main()

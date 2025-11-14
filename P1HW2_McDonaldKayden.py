# Kayden McDonald
# 11/13/2025
# P1HW2
# This program calculates remaining travel budget after expenses on gas, accommodation, and food.

"""
Pseudocode / Program Logic:

1. Ask user to input their total budget (number)
2. Ask user to input travel destination (text)
3. Ask user to input estimated expenses:
   a. Gas
   b. Accommodation
   c. Food
4. Add up all expenses
5. Subtract total expenses from budget to get remaining money
6. Display the travel destination, total expenses, and remaining budget
7. Ensure program works for any valid numeric input
"""

# --- Input Section ---
budget = float(input("Enter your total budget: $"))
destination = input("Enter your travel destination: ")
gas = float(input("Enter amount for gas: $"))
accommodation = float(input("Enter amount for accommodation: $"))
food = float(input("Enter amount for food: $"))

# --- Processing Section ---
total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

# --- Output Section ---
print()
print("Travel Destination:", destination)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)

# -----------------------------------------------------------
# Name: Kayden McDonald
# Assignment: P4HW1 – Score List, Average, and Letter Grade
# Description:
#   Program asks the user how many scores they want to enter.
#   Uses a loop to collect each score and validates that every
#   score is between 0 and 100. Invalid scores must be re-entered.
#   After collecting all scores, the program displays the lowest
#   score, removes it, shows the modified list, calculates the
#   average, and displays the letter grade for that average.
# -----------------------------------------------------------

# Pseudocode:
# 1. Ask user how many scores they want to enter.
# 2. Create an empty list to store scores.
# 3. Loop for the number of scores:
#       a. Ask for a score.
#       b. While score is invalid (not 0–100), make user re-enter.
#       c. Add valid score to list.
# 4. After all scores:
#       a. Find lowest score.
#       b. Remove it from the list.
#       c. Calculate average.
# 5. Determine letter grade from average.
# 6. Display lowest score, modified list, average, and letter grade.

# -----------------------------------------------------------

num_scores = int(input("How many scores do you want to enter? "))

scores = []   # list to hold the user's scores

for i in range(num_scores):
    score = float(input(f"Enter score #{i+1}: "))

    # validate score
    while score < 0 or score > 100:
        print("INVALID score entered!!!")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score #{i+1} again: "))

    scores.append(score)

print("\n------------ Results ------------")

# Get lowest score
lowest = min(scores)
print(f"Lowest Score: {lowest}")

# Remove lowest and show modified list
scores.remove(lowest)
print(f"Modified List: {scores}")

# Calculate average
average = sum(scores) / len(scores)
print(f"Scores Average: {average:.2f}")

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Letter Grade: {grade}")

print("---------------------------------")

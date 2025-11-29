# -----------------------------------------------------------
# Name: Kayden McDonald
# Assignment: P4HW2 – Employee Pay Calculator
# Description:
#   Program asks the user for employee names, hours worked,
#   and pay rate. Calculates regular pay, overtime pay, and
#   gross pay for each employee. Uses a sentinel loop that
#   ends only when the user enters "Done". At the end, the
#   program displays totals for overtime paid, regular paid,
#   gross pay, and number of employees entered.
# -----------------------------------------------------------

# Pseudocode:
# 1. Ask the user for an employee name.
# 2. While name is not "Done":
#       a. Ask for hours worked and pay rate.
#       b. If hours > 40:
#              overtime_hours = hours - 40
#              overtime_pay = overtime_hours * (pay_rate * 1.5)
#              regular_pay = 40 * pay_rate
#          else:
#              overtime_pay = 0
#              regular_pay = hours * pay_rate
#       c. gross_pay = regular_pay + overtime_pay
#       d. Display pay breakdown for employee.
#       e. Add regular_pay, overtime_pay, and gross_pay to running totals.
#       f. Count the employee.
#       g. Ask for next employee name.
# 3. When "Done" is entered:
#       Display totals for overtime, regular pay, gross pay,
#       and number of employees processed.
# -----------------------------------------------------------

# Totals
total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

name = input("Enter employee's name or 'Done' to finish: ")

while name != "Done":
    hours = float(input(f"Enter hours worked by {name}: "))
    pay_rate = float(input(f"Enter pay rate for {name}: "))

    # Calculate pay
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Display results for this employee
    print("-----------------------------------------")
    print(f"Employee Name: {name}")
    print(f"Hours Worked : {hours}")
    print(f"Pay Rate     : ${pay_rate:.2f}")
    print(f"Overtime Pay : ${overtime_pay:.2f}")
    print(f"Regular Pay  : ${regular_pay:.2f}")
    print(f"Gross Pay    : ${gross_pay:.2f}")
    print("-----------------------------------------\n")

    # Accumulate totals
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    employee_count += 1

    # Ask for next employee
    name = input("Enter employee's name or 'Done' to finish: ")

# Final totals summary
print("\n========== Payroll Summary ==========")
print(f"Total number of employees: {employee_count}")
print(f"Total Overtime Pay:        ${total_overtime:.2f}")
print(f"Total Regular Pay:         ${total_regular:.2f}")
print(f"Total Gross Pay:           ${total_gross:.2f}")
print("=====================================")
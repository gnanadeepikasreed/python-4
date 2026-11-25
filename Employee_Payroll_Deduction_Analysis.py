
# Employee Payroll and Deduction Analysis

# Number of employees
n = int(input("Enter number of employees: "))

# Lists to store employee details
employee_names = []
gross_salaries = []
net_salaries = []

for i in range(n):

    print("\nEnter details of Employee", i + 1)

    name = input("Enter employee name: ")

    basic_pay = float(input("Enter basic salary: "))
    allowances = float(input("Enter allowances: "))
    overtime_hours = float(input("Enter overtime hours: "))
    overtime_rate = float(input("Enter overtime rate per hour: "))
    incentives = float(input("Enter incentives: "))

    # Validate salary details
    if (basic_pay < 0 or allowances < 0 or
        overtime_hours < 0 or overtime_rate < 0 or
        incentives < 0):

        print("Invalid salary details!")
        continue

    # Calculate overtime amount
    overtime = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = basic_pay + allowances + overtime + incentives

    # Calculate progressive deductions
    if gross_salary <= 20000:
        deduction = gross_salary * 5 / 100

    elif gross_salary <= 40000:
        deduction = (20000 * 5 / 100) + (
            (gross_salary - 20000) * 10 / 100
        )

    else:
        deduction = (20000 * 5 / 100) + (
            20000 * 10 / 100
        ) + ((gross_salary - 40000) * 15 / 100)

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Store employee details
    employee_names.append(name)
    gross_salaries.append(gross_salary)
    net_salaries.append(net_salary)

    # Display salary statement
    print("\n========== SALARY STATEMENT ==========")

    print("Employee Name:", name)
    print("Basic Salary: Rs.", basic_pay)
    print("Allowances: Rs.", allowances)
    print("Overtime Amount: Rs.", overtime)
    print("Incentives: Rs.", incentives)

    print("--------------------------------------")

    print("Gross Salary: Rs.", round(gross_salary, 2))
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net_salary, 2))

    print("======================================")


# Display all employee salary details
print("\n========== EMPLOYEE PAYROLL SUMMARY ==========")

for i in range(len(employee_names)):

    print("\nEmployee:", employee_names[i])
    print("Gross Salary: Rs.", round(gross_salaries[i], 2))
    print("Net Salary: Rs.", round(net_salaries[i], 2))

print("\nPayroll Calculation Completed!")

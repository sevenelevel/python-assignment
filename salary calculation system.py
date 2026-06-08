basic = float(input("Enter Basic Salary: "))

# Calculate allowances (Extra pay added to salary)
db = basic * 0.30   # 20% Diwali Bonus
gross_salary = basic + db

# Calculate deductions (Money taken away)
tax = gross_salary * 0.10  # 10% Income Tax
net_salary = gross_salary - tax

print("Gross Salary:", gross_salary)
print("Tax Deducted:", tax)
print("Net Salary:", net_salary)
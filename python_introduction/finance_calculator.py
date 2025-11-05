monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)

interest_rate = 0.05  # Annual interest rate of 5%

projected_annual_savings = monthly_savings * 12 + (monthly_savings * interest_rate * 12)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year with interest: {projected_annual_savings}")
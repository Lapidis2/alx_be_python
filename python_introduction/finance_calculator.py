monthly_income = int(input("Enter your monthly income: "))
monthly_expenses  = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses 
Projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05
print("Your annual savings are:", Projected_savings)
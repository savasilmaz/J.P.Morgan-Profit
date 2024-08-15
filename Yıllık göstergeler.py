# Get annual income and expenses from the user
income = float(input("Enter the total annual income ($): "))
expenses = float(input("Enter the total annual expenses ($): "))

# Calculate Net Profit
net_profit = income - expenses

# Profit Margin (%)
profit_margin = (net_profit / income) * 100 if income != 0 else 0

# Expense to Income Ratio (%)
expense_income_ratio = (expenses / income) * 100 if income != 0 else 0

# Reporting
print("----------------------------")
print("Annual Financial Performance Report")
print("----------------------------")
print(f"Total Income: ${income:.2f}")
print(f"Total Expenses: ${expenses:.2f}")
print(f"Net Profit: ${net_profit:.2f}")
print(f"Profit Margin: %{profit_margin:.2f}")
print(f"Expense to Income Ratio: %{expense_income_ratio:.2f}")
print("----------------------------")

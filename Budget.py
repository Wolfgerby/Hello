budget = {
    "income": [],
    "expenses": []
}

# function to add income
def add_income(budget):
    amount = float(input("Enter income amount plz: "))
    budget["income"].append(amount)
    print(f"Added income: {amount}")

# function to add expense
def add_expense(budget):
    amount = float(input("Enter expense/spending amount plz: "))
    budget["expenses"].append(amount)
    print(f"Added expenses: {amount}")

# function to calculate total balance
def calculate_balance(budget):
    total_income = sum(budget["income"])
    total_expenses = sum(budget["expenses"])
    balance = total_income - total_expenses
    return total_income, total_expenses, balance

# loop
while True:
    action = input("Do you want to add income, add expenses, or view balance? (type 'exit' to quit): ").lower()
    if action == 'add income':
        add_income(budget)
    elif action == 'add expense':
        add_expense(budget)
    elif action == 'view balance':
        total_income, total_expenses, balance = calculate_balance(budget)
        print(f"Total Income: {total_income}, Total Expenses: {total_expenses}, Balance: {balance}")
    elif action == 'exit':
        break
    else:
        print("Invalid option, try again plz.")
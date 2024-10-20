budget = {
    "income": [],
    "expenses": []
}

# Function to add income
def add_income(budget):
    amount = float(input("Enter income amount: "))
    budget["income"].append(amount)
    print(f"Added income: {amount}")

# Function to add expenses
def add_expense(budget):
    amount = float(input("Enter expense amount: "))
    budget["expenses"].append(amount)
    print(f"Added expense: {amount}")

# Function to calculate balance
def calculate_balance(budget):
    total_income = sum(budget["income"])
    total_expenses = sum(budget["expenses"])
    balance = total_income - total_expenses
    return total_income, total_expenses, balance

# Function to calculate average monthly income and expenses
def calculate_monthly_average(budget, months):
    total_income = sum(budget["income"])
    total_expenses = sum(budget["expenses"])
    average_income = total_income / months if months > 0 else 0
    average_expenses = total_expenses / months if months > 0 else 0
    return average_income, average_expenses

# Function to save budget to a file
def save_budget_to_file(budget, filename='budget.json'):
    with open(filename, 'w') as file:
        json.dump(budget, file)
    print("Budget saved to file.")

# Function to load budget from a file
def load_budget_from_file(filename='budget.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved budget found. Starting fresh.")
        return {"income": [], "expenses": []}

# Main loop
budget = load_budget_from_file()
while True:
    action = input("Do you want to add income, add expense, view balance, save, load, or exit? ").lower()
    if action == 'add income':
        add_income(budget)
    elif action == 'add expense':
        add_expense(budget)
    elif action == 'view balance':
        total_income, total_expenses, balance = calculate_balance(budget)
        print(f"Total Income: {total_income}, Total Expenses: {total_expenses}, Balance: {balance}")
    elif action == 'save':
        save_budget_to_file(budget)
    elif action == 'load':
        budget = load_budget_from_file()
    elif action == 'calculate averages':
        months = int(input("Enter the number of months for average calculation: "))
        average_income, average_expenses = calculate_monthly_average(budget, months)
        print(f"Average Monthly Income: {average_income}, Average Monthly Expenses: {average_expenses}")
    elif action == 'exit':
        break
    else:
        print("Invalid option. Please try again.")
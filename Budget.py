#budget tools
budget={"income":[],
	"expenses":[]
	}
#function
#add
def add_income(budget):
	amount=float(input("Enter income amount plz:"))
	budget["income"].append(amount)	
	Print(f"Added income:{amount}")
def add_expense(budget):
	amount=float(input("Enter expense/spending amount plz"))
	budget["expenses"].append(amount)
	print(f"added expenses:{amount}")
#total
def calculate_balance(budget):
	total_income=sum(budget["income"])
	total_expenses=sum(budget["expenses"])
	balance=total_income-total_expenses
	return total_income,total_expenses,balance
#loop
while True:action=input("Do you want to add income, add expenses, or view balance?(type 'exit' to quit):").lower()
if action == 'add income':add_income(budget)
elif action == 'add expense':add_expense(budget)
elif action == 'view balance':toltal_income,total_expense,balance=calculate_balance(budget)
print(f"Total Income:{total_income}), Total expenses:{total_expenses},Balance:{balance}")
elif action == 'exit':
	break
else:
	print("invalid try again plz")

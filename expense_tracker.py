from expense import Expense
import calendar
import datetime 
def main():
    print("🎯Running expense tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000
    # get user input for expense
    expense = Get_User_Expense()
    #write it to the file
    Save_User_Expense_to_file(expense,expense_file_path)
    # read the file and summarize all the expenses
    Summarize_Expenses(expense_file_path,budget)
    

def Get_User_Expense():
    print(f"Getting user Expenses...💵")
    Expense_name = input("Enter your expense name: ").strip().lower().capitalize()
    Expense_amount = float(input("Enter your expense amount: "))
    expense_categories = [
        "🍌 Food",
        "🏠 Home",
        "🏢 Work",
        "🎉 Fun",
        "❓ Others"
    ]
    while True:
        print("Select a category: ")
        for i,category_name in enumerate(expense_categories,start=1):
            print(f" {i}. {category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        try:
            choice = int(input(f"Enter Categgory number{value_range}: "))

            if 1 <= choice <= len(expense_categories):
                Selected_category  = expense_categories[choice-1]
                new_expense = Expense(name=Expense_name,category=Selected_category,amount=Expense_amount)
                return new_expense
            else:
                print("Invalid Category Number! Please Try Again. \n")
        except ValueError:
            print("❌ Invalid input! Please enter a NUMBER only.\n")
def Save_User_Expense_to_file(expense: Expense,expense_file_path):
    print(f"Saving user Expenses💵: {expense} to {expense_file_path}")
    with open(expense_file_path,"a",encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def Summarize_Expenses(expense_file_path,budget):
    print(f"Sumarizing user Expenses...💵")
    expenses:list[Expense] = []
    with open(expense_file_path,"r",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category = line.strip().split(",")
            expense_amount = float(expense_amount)
            line_expenses = Expense(
                name=expense_name,amount=expense_amount,category=expense_category
            )
            expenses.append(line_expenses)
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses By Category💹: ")
    for key,amount in amount_by_category.items():
        print(f"  {key}:  ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent:.2f} this month")
    remaining_budget = budget - total_spent
    print(f"💴Budget remaining: ${remaining_budget:.2f} this month")

    now = datetime.datetime.now()
    day_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = day_in_month - now.day
    
    daily_budget = remaining_budget/remaining_days
    print(green_text(f"🔴Budget per day: ${daily_budget:.2f}"))

def green_text(text):
    print(f"\033[92m{text}\033[0m")
if __name__ == "__main__":
    main()
def add_expense(expense_file, category, amount):
    with open(expense_file, 'a') as file:
        file.write(category + ',' + str(amount) + '\n')
    print("Expense added successfully!")

def view_expenses(expense_file):
    try:
        with open(expense_file, 'r') as file:
            total_expenses = 0
            print("Category\tAmount")
            print("---------------------")
            for line in file:
                category, amount = line.strip().split(',')
                total_expenses += float(amount)
                print(category + '\t\t' + amount)
            print("---------------------")
            print("Total Expenses:\t" + str(total_expenses))
    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    expense_file = "expenses.txt"
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(expense_file, category, amount)
        elif choice == '2':
            view_expenses(expense_file)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
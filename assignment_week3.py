import json
import os
from datetime import datetime

#file path for storing expense data
DATA_FILE = "expenses.json"

#load existing data from file or create a new one if it doesn't exist
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

#save data back to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

#function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter the expense amount: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., food, transport, etc.): ")
        date = input("Press Enter for today or Enter the date (YYYY-MM-DD)")

        # Use current date if no input is provided
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": date
        }

        data = load_data()
        data.append(expense)
        save_data(data)

        print("Expense added successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

#function to display summary
def display_summary():
    data = load_data()
    if not data:
        print("No expenses found!")
        return

    monthly_total = 0
    category_expense = {}

    #calculate monthly total and category-wise expense
    current_month = datetime.today().strftime('%Y-%m')
    for expense in data:
        if expense['date'].startswith(current_month):
            monthly_total += expense['amount']
            category = expense['category']
            if category in category_expense:
                category_expense[category] += expense['amount']
            else:
                category_expense[category] = expense['amount']

    print(f"\n---Expense Summary for {current_month} ---")
    print(f"Total Expenses: {monthly_total:.2f}")

    print("\nCategory-wise Breakdown:")
    for category, total in category_expense.items():
        print(f"{category}: {total:.2f}")

#main function
def main_menu():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add a New Expense")
        print("2. View Monthly Summary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            display_summary()
        elif choice == '3':
            print("Exiting Expense Tracker.\n Bye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main_menu()

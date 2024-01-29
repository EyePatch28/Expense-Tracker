import json
import os
from datetime import datetime

# Load existing expense data from the JSON file
def load_expense_data():
    if os.path.exists("expense_data.json"):
        with open("expense_data.json", "r") as file:
            return [json.loads(line) for line in file]
    else:
        return []

# Function to get user input for daily expenses
def get_expense_input():
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the expense category (e.g., food, transportation, entertainment): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return {"amount": amount, "description": description, "category": category, "date": date}

# Function to save expense data to a JSON file
def save_expense_data(expense_data):
    with open("expense_data.json", "a") as file:
        json.dump(expense_data, file)
        file.write('\n')

# Function to categorize expenses
def categorize_expenses(expense_data, category):
    category_expenses = [expense for expense in expense_data if expense["category"] == category]
    return category_expenses

# Function to calculate monthly expense summary
def monthly_expense_summary(expense_data):
    # Implement logic to calculate and display monthly summary
    pass

# Load existing expense data at the beginning
expense_data = load_expense_data()

# User Interface Loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Log Daily Expense")
    print("2. View Category-wise Expenses")
    print("3. View Monthly Expense Summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        expense_input = get_expense_input()
        expense_data.append(expense_input)  # Add the new expense to the existing data
        save_expense_data(expense_input)
        print("Expense logged successfully!")

    elif choice == "2":
        category = input("Enter the category to view expenses: ")
        # Display category-wise expenses
        category_expenses = categorize_expenses(expense_data, category)
        print(category_expenses)

    elif choice == "3":
        # Display monthly expense summary
        monthly_expense_summary(expense_data)

    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

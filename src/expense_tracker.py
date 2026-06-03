"""
Expense Tracker CLI Application

A simple command-line application to manage personal expenses with persistent JSON storage.
Allows users to add, view, delete expenses and calculate total spending.

Author: Sai Charan Reddy
"""

import json
import os

# Get the data directory path relative to this script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
FILE_PATH = os.path.join(DATA_DIR, "expenses.json")


def load_expenses():
    """
    Load expenses from JSON file.
    
    Returns:
        list: List of expense dictionaries, or empty list if file doesn't exist or is invalid.
    """
    try:
        if not os.path.exists(FILE_PATH):
            return []

        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: Corrupted expenses file. Starting with empty expenses.")
        return []
    except IOError as e:
        print(f"Error reading expenses file: {e}")
        return []


def save_expenses(expenses):
    """
    Save expenses to JSON file with proper error handling.
    
    Args:
        expenses (list): List of expense dictionaries to save.
    """
    try:
        # Ensure data directory exists
        os.makedirs(DATA_DIR, exist_ok=True)
        
        with open(FILE_PATH, "w") as file:
            json.dump(expenses, file, indent=4)
    except IOError as e:
        print(f"Error saving expenses: {e}")


def add_expense():
    """
    Add a new expense to the tracker with input validation.
    
    Prompts user for expense name and amount, validates input, and saves to file.
    """
    try:
        name = input("Enter expense name: ").strip()
        
        # Validate expense name
        if not name:
            print("Error: Expense name cannot be empty.")
            return
        
        amount_str = input("Enter amount: ₹")
        amount = float(amount_str)
        
        # Validate amount
        if amount <= 0:
            print("Error: Amount must be a positive number.")
            return

        expenses = load_expenses()

        expenses.append({
            "name": name,
            "amount": amount
        })

        save_expenses(expenses)
        print(f"✓ Expense '{name}' (₹{amount}) added successfully!")
        
    except ValueError:
        print("Error: Invalid amount. Please enter a valid number.")


def view_expenses():
    """
    Display all recorded expenses in a formatted table.
    
    Shows expense index, name, and amount. Displays a message if no expenses exist.
    """
    expenses = load_expenses()

    if not expenses:
        print("\n✗ No expenses found.")
        return

    print("\n" + "=" * 35)
    print("             EXPENSES")
    print("=" * 35)

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']:<20} ₹{expense['amount']:>8.2f}")
    
    print("=" * 35)


def delete_expense():
    """
    Delete an expense from the tracker.
    
    Displays all expenses, prompts user for selection, validates input, and removes the selected expense.
    """
    expenses = load_expenses()

    if not expenses:
        print("\n✗ No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"✓ '{removed['name']}' (₹{removed['amount']}) deleted successfully!")
        else:
            print(f"Error: Invalid expense number. Please enter a number between 1 and {len(expenses)}.")

    except ValueError:
        print("Error: Please enter a valid number.")


def total_spending():
    """
    Calculate and display the total spending.
    
    Sums all expense amounts and displays the total in a formatted manner.
    """
    expenses = load_expenses()

    if not expenses:
        print("\n✗ No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print("\n" + "=" * 35)
    print(f"Total Spending: ₹{total:>23.2f}")
    print("=" * 35)


def menu():
    """
    Display the main menu and handle user input.
    
    Shows menu options and routes user to appropriate functions.
    Runs in a loop until user chooses to exit.
    """
    while True:
        print("\n" + "=" * 35)
        print("     EXPENSE TRACKER MENU")
        print("=" * 35)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Spending")
        print("5. Exit")
        print("=" * 35)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            total_spending()

        elif choice == "5":
            print("\n✓ Thank you for using Expense Tracker! Goodbye!")
            break

        else:
            print("✗ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    menu()
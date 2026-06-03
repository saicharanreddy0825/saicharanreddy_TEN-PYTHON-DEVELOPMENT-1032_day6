# Expense Tracker CLI

A robust command-line expense management application built with Python. Track your daily expenses effortlessly with persistent JSON-based data storage.

## 🎯 Features

- ✅ **Add Expense** - Record new expenses with name and amount
- ✅ **View Expenses** - Display all recorded expenses in a formatted table
- ✅ **Delete Expense** - Remove expenses from your tracker
- ✅ **Calculate Total Spending** - Get a summary of total expenses
- ✅ **Persistent Storage** - All data automatically saved to JSON file
- ✅ **Input Validation** - Robust error handling for invalid inputs
- ✅ **Professional UI** - Clean, user-friendly menu interface

## 📋 Project Structure

```
expense-tracker/
│
├── src/
│   └── expense_tracker.py       # Main application file
│
├── data/
│   └── expenses.json            # JSON data file (auto-created)
│
├── screenshots/                 # Application screenshots
│
├── README.md                    # This file
│
└── .gitignore                   # Git ignore rules
```

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher installed

### Steps

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. **Navigate to the src directory**
   ```bash
   cd src
   ```

3. **Run the application**
   ```bash
   python expense_tracker.py
   ```

## 💡 Usage Examples

### Adding an Expense
```
Enter your choice (1-5): 1
Enter expense name: Groceries
Enter amount: ₹500
✓ Expense 'Groceries' (₹500) added successfully!
```

### Viewing Expenses
```
Enter your choice (1-5): 2
===================================
             EXPENSES
===================================
1. Groceries             ₹500.00
2. Electricity Bill      ₹1200.00
===================================
```

### Checking Total Spending
```
Enter your choice (1-5): 4
===================================
Total Spending: ₹1700.00
===================================
```

### Deleting an Expense
```
Enter your choice (1-5): 3
[Shows list of expenses]
Enter expense number to delete: 1
✓ 'Groceries' (₹500.0) deleted successfully!
```

## 🔒 Data Storage

- All expenses are automatically saved to `data/expenses.json`
- Data persists even after closing the application
- File is created automatically if it doesn't exist
- JSON format ensures easy data backup and portability

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **JSON** - Data storage format
- **OS Module** - File path handling
- **Git & GitHub** - Version control and repository hosting

## ✨ Code Quality Features

- **PEP 8 Compliant** - Follows Python style guidelines
- **Comprehensive Docstrings** - Well-documented functions
- **Input Validation** - Validates all user inputs
- **Error Handling** - Graceful handling of errors
- **Clean Architecture** - Modular and readable code

## 🐛 Error Handling

The application handles various edge cases:
- Empty expense names
- Negative or zero amounts
- Invalid menu choices
- Corrupted JSON files
- Missing data directory (auto-created)

## 📝 Sample Data Structure

```json
[
    {
        "name": "Groceries",
        "amount": 500.00
    },
    {
        "name": "Electricity Bill",
        "amount": 1200.00
    }
]
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Sai Charan Reddy**

Feel free to reach out for questions or feedback!

## 🔗 Repository

[GitHub Repository Link](https://github.com/your-username/expense-tracker)

---

**Version**: 1.0.0  
**Last Updated**: June 2026
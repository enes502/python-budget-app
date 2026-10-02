# 💰 Python Budget App (OOP)

A command-line budget tracker application built with **Python**, utilizing **Object-Oriented Programming (OOP)** principles. This project is developed as part of the FreeCodeCamp curriculum to manage financial categories, track transactions, and generate spending charts.

---

## 🚀 Features

*   **Category Management:** Create individual categories (e.g., *Food, Clothing, Auto*) and track individual ledgers.
*   **Deposits & Withdrawals:** Add funds or record expenses with custom descriptions.
*   **Balance Checking:** Real-time balance calculations and fund sufficiency validations before withdrawals.
*   **Inter-category Transfers:** Seamlessly transfer funds between different categories with automatic logging.
*   **Visual Spending Chart:** Generates a text-based percentage bar chart representing spending distribution across categories.
*   **String Formatting:** Custom `__str__` implementation to cleanly print category ledgers and final totals.

---

## 📂 Project Structure

```text
├── budget.py         # Contains Category class and create_spend_chart function
└── README.md         # Project documentation

from budget import Category, create_spend_chart

# Create categories
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(60, 'groceries')

clothing = Category('Clothing')
clothing.deposit(500, 'initial deposit')
clothing.withdraw(20, 'clothes')

auto = Category('Auto')
auto.deposit(500, 'initial deposit')
auto.withdraw(10, 'gas')

# Print formatted ledger
print(food)

# Generate and print the spending chart
print(create_spend_chart([food, clothing, auto]))

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|          
 40|          
 30|          
 20|  o       
 10|  o       
  0|  o   o  o
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g

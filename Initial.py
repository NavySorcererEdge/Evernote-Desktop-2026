from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Transaction:
    description: str
    category: str
    amount: float
    transaction_type: str


class BudgetTracker:
    def __init__(self, budget: float):
        self.budget = budget
        self.transactions = []

    def add(self, description, category, amount, transaction_type):
        self.transactions.append(
            Transaction(description, category, amount, transaction_type)
        )

    def income(self):
        return sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.transaction_type == "income"
        )

    def expenses(self):
        return sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.transaction_type == "expense"
        )

    def category_totals(self):
        totals = defaultdict(float)

        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                totals[transaction.category] += transaction.amount

        return totals

    def report(self):
        income = self.income()
        expenses = self.expenses()
        balance = income - expenses
        remaining = self.budget - expenses

        print("Budget Tracker")
        print("==============")
        print(f"Budget:    ${self.budget:.2f}")
        print(f"Income:    ${income:.2f}")
        print(f"Expenses:  ${expenses:.2f}")
        print(f"Balance:   ${balance:.2f}")
        print(f"Remaining: ${remaining:.2f}")

        print("\nExpenses by Category")
        print("--------------------")

        for category, amount in sorted(
            self.category_totals().items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"{category}: ${amount:.2f}")


tracker = BudgetTracker(5000)

tracker.add("Monthly salary", "Salary", 4200, "income")
tracker.add("Freelance project", "Work", 850, "income")

tracker.add("Apartment", "Housing", 1400, "expense")
tracker.add("Groceries", "Food", 420, "expense")
tracker.add("Internet", "Services", 60, "expense")
tracker.add("Gym", "Health", 45, "expense")
tracker.add("New keyboard", "Technology", 120, "expense")
tracker.add("Restaurant", "Food", 85, "expense")

tracker.report()
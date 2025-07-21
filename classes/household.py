from roommate import Roommate
from expense import Expense

class Household:
    def __init__(self, name):
        self.name = name
        self.roommates = {}
        self.expenses = []

    def add_roommate(self, name):
        if name not in self.roommates:
            self.roommates[name] = Roommate(name)

    def add_expense(self, description, amount, paid_by):
        if paid_by not in self.roommates:
            raise ValueError(f"{paid_by} is not a roommate in this household.")

        expense = Expense(description, amount, paid_by)
        self.expenses.append(expense)
        self.split_expense(expense)

    def split_expense(self, expense):
        split_amount = expense.amount / len(self.roommates)
        for name, roommate in self.roommates.items():
            if name == expense.paid_by:
                roommate.balance += expense.amount - split_amount
            else:
                roommate.balance -= split_amount

    def show_balances(self):
        print(f"\nBalances for household: {self.name}")
        for roommate in self.roommates.values():
            print(roommate)
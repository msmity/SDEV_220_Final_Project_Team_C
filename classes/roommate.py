class Roommate:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def __str__(self):
        return f"{self.name}: {'owed' if self.balance < 0 else 'gets'} ${abs(self.balance):.2f}"
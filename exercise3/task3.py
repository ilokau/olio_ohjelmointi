
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
        
    def __str__(self):
        return f"The balance is {self.balance:.2f} euros"
    
    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95
        else:
            return None
    
    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90
        else:
            return None
        
    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError("ValueError: You cannot deposit an amount of money less than zero")
        else:
            self.balance += amount
        
    
card = LunchCard(50)
print(card)

card.eat_ordinary()
print(card)

card.eat_luxury()
card.eat_ordinary()
print(card)

card = LunchCard(10)
print(card)
card.deposit_money(15)
print(card)
card.deposit_money(10)
print(card)
card.deposit_money(200)
print(card)
card.deposit_money(-10)
print(card)
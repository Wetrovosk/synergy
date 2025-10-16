class CashBox:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, amount):
        self.money += amount

    def count_1000(self):
        return self.money // 1000

    def take_away(self, amount):
        if amount > self.money:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= amount

cash = CashBox(2500)
print(f"1. Начальный баланс: {cash.money} руб.")
print(f"   Целых тысяч: {cash.count_1000()}")

cash.top_up(800)
print(f"2. После пополнения на 800: {cash.money} руб.")
print(f"   Целых тысяч: {cash.count_1000()}")

cash.take_away(1300)
print(f"3. После снятия 1300: {cash.money} руб.")
print(f"   Целых тысяч: {cash.count_1000()}")

print("4. Попытка снять 5000 при балансе", cash.money, "руб.:")
try:
    cash.take_away(5000)
except ValueError as e:
    print(f"   Ошибка: {e}")

cash.top_up(3000)
print(f"5. После пополнения на 3000: {cash.money} руб.")
print(f"   Целых тысяч: {cash.count_1000()}")
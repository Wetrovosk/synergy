class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s  

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves_x = (dx + self.s - 1) // self.s  
        moves_y = (dy + self.s - 1) // self.s  

        return moves_x + moves_y
    
t = Turtle(x=0, y=0, s=2)

print(f"Начало: ({t.x}, {t.y}), шаг = {t.s}")
t.go_right()
t.go_up()
print(f"После right и up: ({t.x}, {t.y})")  

t.evolve()
print(f"После evolve: шаг = {t.s}") 

print("Ходов до (10, 10):", t.count_moves(10, 10))  

t.degrade()
print(f"После degrade: шаг = {t.s}")  

t2 = Turtle(s=1)
try:
    t2.degrade()
except ValueError as e:
    print("Ошибка:", e)
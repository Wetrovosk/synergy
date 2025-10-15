import random

# Ввод и проверка количества строк
try:
    rows = int(input("Введите количество строк: "))
    if rows < 1:
        print("Ошибка: количество строк должно быть >= 1")
        exit()
except ValueError:
    print("Ошибка: введите целое число для строк")
    exit()

# Ввод и проверка количества столбцов
try:
    cols = int(input("Введите количество столбцов: "))
    if cols < 1:
        print("Ошибка: количество столбцов должно быть >= 1")
        exit()
except ValueError:
    print("Ошибка: введите целое число для столбцов")
    exit()

# Создание первой матрицы
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-200, 200))
    matrix1.append(row)

# Создание второй матрицы
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(-200, 200))
    matrix2.append(row)

# Сложение матриц
result = []
for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(matrix1[i][j] + matrix2[i][j])
    result.append(new_row)

# Вывод первой матрицы
print("\nМатрица 1:")
for row in matrix1:
    print(row)

# Вывод второй матрицы
print("\nМатрица 2:")
for row in matrix2:
    print(row)

# Вывод суммы матриц
print("\nСумма матриц:")
for row in result:
    print(row)
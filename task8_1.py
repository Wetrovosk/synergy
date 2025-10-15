n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

# Переворачиваем список
numbers.reverse()

# Выводим каждый элемент на отдельной строке
for j in range(n):
    print(numbers[j])
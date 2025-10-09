# Задание: Ввод пятизначного числа
numer = int(input("Введите пятизначное целое число: "))
units = numer % 10
tens = (numer // 10) % 10
hundreds = (numer // 100) % 10
thousands = (numer // 1000) % 10
ten_thousands = numer // 10000
result = (tens ** units * hundreds) / (ten_thousands - thousands)
print(result)
x = int(input())

if x >= 2000000000:
    print("Ошибка вычисления: число должно быть меньше 2 миллиардов")
else:
    count = 0
    i = 1
    while i <= x:
        if x % i == 0:
            count += 1
        i += 1
    print(count)
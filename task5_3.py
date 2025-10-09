min_investment = int(input("Введите минимальную сумму инвестиций: "))
michael_money = int(input("Сколько долларов у Майкла: "))
ivan_money = int(input("Сколько долларов у Ивана: "))

if michael_money >= min_investment and ivan_money >= min_investment:
    print(2)
elif michael_money >= min_investment:
    print("Mike")
elif ivan_money >= min_investment:
    print("Ivan")
elif michael_money + ivan_money >= min_investment:
    print(1)
else:
    print(0)
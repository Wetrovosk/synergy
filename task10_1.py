# Создаём пустой словарь
pets = {}

# Запрашиваем данные у пользователя
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Добавляем информацию в словарь
pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

# Определяем правильное склонение для возраста
age = pet_age
if 10 < age % 100 < 20:
    years = 'лет'
else:
    last_digit = age % 10
    if last_digit == 1:
        years = 'год'
    elif 2 <= last_digit <= 4:
        years = 'года'
    else:
        years = 'лет'

# Получаем внутренний словарь
inner_dict = pets[pet_name]

# Извлекаем значения в нужном порядке
info_values = list(inner_dict.values())
pet_type_out = info_values[0]
pet_age_out = info_values[1]
owner_name_out = info_values[2]

# Выводим результат
print(f"Это {pet_type_out} по кличке \"{pet_name}\". Возраст питомца: {pet_age_out} {years}. Имя владельца: {owner_name_out}")
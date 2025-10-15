pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_pet(ID):
    if ID in pets:
        return pets[ID]
    else:
        return False

def get_suffix(age):
    if 10 < age % 100 < 20:
        return 'лет'
    last_digit = age % 10
    if last_digit == 1:
        return 'год'
    elif 2 <= last_digit <= 4:
        return 'года'
    else:
        return 'лет'

def pets_list():
    if not pets:
        print("Нет питомцев в базе.")
        return
    for ID in pets:
        pet_info = pets[ID]
        pet_name = list(pet_info.keys())[0]
        data = pet_info[pet_name]
        age = data["Возраст питомца"]
        suffix = get_suffix(age)
        print(f'ID: {ID} - Это {data["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {age} {suffix}. Имя владельца: {data["Имя владельца"]}.')

def create():
    if pets:
        last_id = max(pets.keys())
        new_id = last_id + 1
    else:
        new_id = 1

    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }

def read():
    ID = int(input("Введите ID питомца: "))
    pet_info = get_pet(ID)
    if pet_info == False:
        print("Питомец с таким ID не найден.")
        return

    pet_name = list(pet_info.keys())[0]
    data = pet_info[pet_name]
    age = data["Возраст питомца"]
    suffix = get_suffix(age)
    print(f'Это {data["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {age} {suffix}. Имя владельца: {data["Имя владельца"]}.')

def update():
    ID = int(input("Введите ID питомца: "))
    pet_info = get_pet(ID)
    if pet_info == False:
        print("Питомец с таким ID не найден.")
        return

    pet_name = list(pet_info.keys())[0]
    pet_info[pet_name]["Вид питомца"] = input("Введите новый вид питомца: ")
    pet_info[pet_name]["Возраст питомца"] = int(input("Введите новый возраст питомца: "))
    pet_info[pet_name]["Имя владельца"] = input("Введите новое имя владельца: ")

def delete():
    ID = int(input("Введите ID питомца: "))
    if ID in pets:
        del pets[ID]
    else:
        print("Питомец с таким ID не найден.")

command = ""
while command != "stop":
    command = input("Введите команду (create/read/update/delete/list/stop): ").strip().lower()
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    else:
        print("Неизвестная команда. Попробуйте снова.")
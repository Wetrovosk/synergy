my_dict = {}

for key in range(10, -6, -1):  # от 10 до -5 включительно
    my_dict[key] = key ** key

for key in range(10, -6, -1):
    print(f"{key}: {my_dict[key]}")
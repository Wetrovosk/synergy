my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def prnt(lst, i=0):
    if i >= len(lst):
        print("Конец списка")
        return
    print(lst[i])
    prnt(lst, i + 1)

prnt(my_list)
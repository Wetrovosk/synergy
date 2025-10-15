n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

n2 = int(input())
list2 = []
for i in range(n2):
    list2.append(int(input()))

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print(len(common))
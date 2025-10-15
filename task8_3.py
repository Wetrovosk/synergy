m = int(input())
n = int(input())

weights = []
for i in range(n):
    weight = int(input())
    weights.append(weight)

weights.sort()

left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1  
    right -= 1
    boats += 1

print(boats)
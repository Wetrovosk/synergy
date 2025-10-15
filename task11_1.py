def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input())

fact_n = factorial(n)

result_list = []
for num in range(fact_n, 0, -1):
    result_list.append(factorial(num))

print(result_list)
n = int(input())
numbers = list(map(int, input().split()))

result = [numbers[-1]] + numbers[:-1]

print(' '.join(map(str, result)))
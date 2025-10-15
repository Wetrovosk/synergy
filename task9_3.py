s = input().split()
seen = set()

for token in s:
    num = int(token)
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
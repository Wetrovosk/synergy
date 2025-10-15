s = input()

result = ""
for c in s:
    if c != ' ':
        result += c
    elif result and result[-1] != ' ':
        result += c

print(result)
word = input("Введите слово из маленьких латинских букв: ")

count_a = word.count("a")
count_e = word.count("e")
count_i = word.count("i")
count_o = word.count("o")
count_u = word.count("u")
count_vowels = count_a + count_e + count_i + count_o + count_u
count_consonants = len(word) - count_vowels

print("Сколько гласных: ", count_vowels)
print("Сколько согласных: ", count_consonants)
if count_a > 0:
    print("Сколько a:", count_a)
else:
    print("Сколько a:", False)

if count_e > 0:
    print("Сколько e:", count_e)
else:
    print("Сколько e:", False)

if count_i > 0:
    print("Сколько i:", count_i)
else:
    print("Сколько i:", False)

if count_o > 0:
    print("Сколько o:", count_o)
else:
    print("Сколько o:", False)

if count_u > 0:
    print("Сколько u:", count_u)
else:
    print("Сколько u:", False)
print("Числа, кратные 11 от 0 до 10000: ")
n = 1
m = 1
while n != 10000:
    if n % 11 == 0:
        print(n, end=" ")
    if m % 330 == 0:
        print()
    n += 1
    m += 1


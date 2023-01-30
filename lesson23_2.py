def digit(n):
    m = 0
    while n != 0:
        n //= 10
        m += 1
    return m


n = int(input("Введите число: "))
print("Количество разрядов числа: ", digit(n))
n = int(input("Сколько Вам лет?\n"))
if 0 < n < 100:
    if n%10 == 1 and n != 11:
        print("Вам", n, "год")
    elif n%10 == 2 or n%10 == 3 or n%10 == 4:
        print("Вам", n, "года")
    else:
        print("Вам", n, "лет")
else:
    print("Ошибка!")




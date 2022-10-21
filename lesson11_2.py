try:
    print("Введите сегодняшнюю дату")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))

    print("Введите дату Вашего рождения")
    day2 = int(input("День: "))
    month2 = int(input("Месяц: "))
    year2 = int(input("Год: "))
except ValueError:
    print("Некорректная дата!")

if (month - month2) > 0:
    age = year - year2
else:
    if (month - month2) == 0:
        if (day - day2) >= 0:
            age = year - year2
        else:
            age = year - year2 - 1
    else:
        age = year - year2 - 1

if 0 < age < 100:
    if age%10 == 1 and age != 11:
        print("Вам", age, "год")
    elif age%10 == 2 or age%10 == 3 or age%10 == 4:
        print("Вам", age, "года")
    else:
        print("Вам", age, "лет")
else:
    print("Ошибка!")

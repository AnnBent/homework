try:
    print("Введите дату рождения 1 человека: ")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))

    print("Введите дату рождения 2 человека: ")
    day2 = int(input("День: "))
    month2 = int(input("Месяц: "))
    year2 = int(input("Год: "))
except ValueError:
    print("Некорректная дата!")

if year > year2:
    print("2 человек старше")
elif year == year2:
    if month > month2:
        print("2 человек старше")
    elif month == month2:
        if day > day2:
            print("2 человек старше")
        elif day == day2:
            print("Эти два человека ровесники")
        else:
            print("1 человек старше")
    else:
        print("1 человек старше")
else:
    print("1 человек старше")
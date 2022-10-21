try:
    name = input("Введите Ваше Имя и Фамилию: ")
    age = int(input("Введите Ваш возраст: "))
    print(name + age)
except ValueError:
    print("Некорректное значение!")
except TypeError:
    print("Что-то пошло не так!")




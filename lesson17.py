import itertools
str1 = input("Введите строку: ")

def unique(obj: iter):
    args = []
    for a in obj:
        if a not in args:
            args.append(a)
            yield a

str2 = tuple(unique(str1))
print(str2)
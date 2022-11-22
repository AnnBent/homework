str1 = list(input("Введите строку: "))
str2 = list()
for i in str1:
    if i not in str2:
       str2.append(i)
str2 = tuple(str2)
print(str2)
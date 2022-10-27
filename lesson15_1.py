import random
n = []
summa = 0
for i in range(0, 10):
    n.append(random.randint(0, 10))
    i += 1
print(n)
n.sort()
print("Два наименьших элемента массива:", n[0],",", n[1])
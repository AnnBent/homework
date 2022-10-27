import random
n = []
summa = 0
for i in range(0, 10):
    n.append(random.randint(-20, 20))
    i += 1
print(n)
for i in n:
    if i > 0 and i%2 == 0:
        summa += i
print(summa)




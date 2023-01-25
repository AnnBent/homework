import re
counter = {}
str1 = "Мы любим, но делаем вид, что нам безразлично. Мы равнодушны, а делаем вид, что любим."
list1 = re.split("\. | |, |\.|\n", str1)
print(str1)
for i in list1:
    counter[i] = counter.get(i, 0) + 1
    print(i, "-", counter[i] - 1)

import re
str1 = "Мы любим, но делаем вид, что нам безразлично. Мы равнодушны, а делаем вид, что любим."
list1 = re.split("\. | |, |\.|\n", str1)
print(str1)
set1 = list1
for i in set1:
    print(i, "-", list1.count(i))


counter = {}
for i in range(int(input("Введите количество строк, а затем сами строки: "))):
    text = input().split()
    for word in text:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))



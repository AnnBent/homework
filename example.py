with open("class.txt") as file:
    marks_sum = marks_count = 0
    print("Учащиеся, с оценкой ниже 3 баллов: ")
    for line in file:
        line = line.rstrip("\n")
        marks_count += 1
        mark = int(line[-1])
        marks_sum += mark
        if mark < 3:
            print(line[:-1])
print("Средний бал по группе:", marks_sum / marks_count)
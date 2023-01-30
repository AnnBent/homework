with open("text.txt", 'r') as f:
    word = symbol = line_count = 0
    for line in f:
        print(line.rstrip())
        line_count += 1
        symbol = len(line.rstrip())
        line = line.split()
        word = len(line)
        print("Количество символов в строке: ", symbol,"Слов:" , word)
    print("Количество строк в тексте: ", line_count) 
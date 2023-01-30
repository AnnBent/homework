with open("text.txt", 'w') as f:
    while True:
        st = input()
        f.write(st)
        f.write("\n")
        if st == "":
            break


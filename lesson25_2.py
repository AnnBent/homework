from conventer import conventer

while True:
    n = int(input("Конвентер валют\n\nUSD -> BYN клавиша 1\nBYN -> USD клавиша 2\n"))
    if n == 1:
        usd = int(input("Введите сумму "))
        print(usd, "USD =", conventer.usd_byn(usd), "BYN")
    elif n == 2:
        byn = int(input("Введите сумму "))
        print(byn, "BYN =", conventer.byn_usd(byn), "USD")
    else:
        print("Конец программы")
        break
def bank():
    x = int(input("Сумма: "))
    y = int(input("Количество лет: "))
    n = 1.1
    sum = x * n ** y
    print("Накопленная сумма: ", round(sum, 2))


bank()

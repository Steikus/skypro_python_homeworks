def is_year_leap():
    y = int(input("Год високосный?: "))
    if (y % 4 == 0):
        print(True)
    else:
        print(False)


is_year_leap()

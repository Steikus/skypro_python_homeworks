season = ["Зима", "Весна", "Лето", "Осень"]


def month_to_season():
    month = int(input("Номер месяца: "))
    if month == 12 or month == 1 or month == 2:
        print("Сезон: " + season[0])
    elif month == 3 or month == 4 or month == 5:
        print("Сезон: " + season[1])
    elif month == 6 or month == 7 or month == 8:
        print("Сезон: " + season[2])
    elif month == 9 or month == 10 or month == 11:
        print("Сезон: " + season[3])
    else:
        print("Какой какой?")


month_to_season()

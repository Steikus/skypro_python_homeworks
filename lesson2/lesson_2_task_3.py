import math


def square(side):
    side = math.ceil(side)
    area = side * side
    return area


side = float(input("Сторона квадрата: "))
area = square(side)
print("Площадь квадрата:", area)
# Дойдя до последнего урока я нашёл решение ниже, в этом разберусь потом

# def square():
#     side = float(input("Сторона квадрата:"))
#     area = side * side
#     print("Площадь: ", round(area))


# square()

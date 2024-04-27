from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S24", "79123457869"),
    Smartphone("OnePlus", "10T", "79081234567"),
    Smartphone("Google", "Pixel 10", "79114203221"),
    Smartphone("Apple", "Iphone 15", "79183456842"),
    Smartphone("Xiaomi", "Mi 12", "79204809704")
    ]

for smartphone in catalog:
    print(smartphone.brand, "-",
          smartphone.model + ".", "+" + smartphone.number)

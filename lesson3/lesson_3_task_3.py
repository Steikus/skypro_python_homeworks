from address import Address
from mailing import Mailing

to_address = Address("123456", "Krasnodar", "Krasnaya", "12", "123")
from_address = Address("987654", "Suzdal", "Lenina", "5", "12")

delivery = Mailing(to_address, from_address, 15999, "RU213156")
print("Отправление", delivery.track, "из", delivery.from_address.index,
      delivery.from_address.city, delivery.from_address.street,
      delivery.from_address.house, "-", delivery.from_address. appartment,
      "в", delivery.to_address.index, delivery.to_address.city,
      delivery.to_address.street, delivery.to_address.house, "-",
      delivery.to_address.appartment + ".", "Стоимость ",
      delivery.cost, "рублей")

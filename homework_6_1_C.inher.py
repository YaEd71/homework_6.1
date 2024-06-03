class Car:
  price = 1000000
  def horse_powers(self):
      return 150
  
class Nissan(Car):
  price = 1200000
  def horse_powers(self):
      return 200

class Kia(Car):
  price = 900000
  def horse_powers(self):
      return 130

car1 = Car()
print(f"Car Price: {car1.price}")
print(f"Car Horse Powers: {car1.horse_powers()}")

nissan1 = Nissan()
print(f"Nissan Price: {nissan1.price}")
print(f"Nissan Horse Powers: {nissan1.horse_powers()}")

kia1 = Kia()
print(f"Kia Price: {kia1.price}")
print(f"Kia Horse Powers: {kia1.horse_powers()}")
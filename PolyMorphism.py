class Computer:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def device_type(self):
        print("this is a general computer")

class Laptop(Computer):
    def __init__(self, brand, year,battery_life):
        super().__init__(brand, year)
        self.battery_life=battery_life


    def device_type(self):
        print(f"this is a laptop with battery life of {self.battery_life}.")


class Desktop(Computer):
    def __init__(self, brand, year,has_power_supply):
        super().__init__(brand, year)
        self.has_power_supply=has_power_supply


    def device_type(self):
        print(f"this computer is a desktop with power supply: {self.has_power_supply}")


laptop1 = Laptop("Lenovo",2024,"88%")
desktop1 = Desktop("HP",2020, True)


laptop1.device_type()
desktop1.device_type()



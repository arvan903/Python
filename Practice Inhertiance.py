class Computer:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    

class Laptop(Computer):
    def __init__(self, brand, year,battery_life):
        super().__init__(brand, year)
        self.battery_life= battery_life

    def show_battery(self):
        print(f"the laptop {self.brand} {self.year} battery life is {self.battery_life}")




device1 = Laptop("Lenovo",2024,"86%")


device1.show_battery()


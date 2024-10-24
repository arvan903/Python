# Parent class (Base class)
class device:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        
    def device_info(self):
        print(f"brand: {self.brand}, year: {self.year}")
        
# Child class (Derived class)
class Phone(device):
    def __init__(self, brand, model,year):
        super().__init__(brand, year)
        self.model = model

    def turn_on(self):
        print(f"the phone {self.brand} {self.model} is turning on... ")



phone1 = Phone("Apple","iPhone 16",2024)

phone1.device_info()
phone1.turn_on()
class Phone:
    def __init__(self,Brand,Model,Year):
        self.brand = Brand
        self.model = Model
        self.year = Year


    def Turn_On(self):
        print(f"The Phone {self.brand} {self.model} is Turning On... ")


phone1 = Phone("Apple","iPhone 16",2024)
phone2 = Phone("Samsung","S24 Ultra",2023)

phone1.Turn_On()
phone2.Turn_On()
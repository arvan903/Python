class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.year = year
        self.model = model
    
    def vehicle_type(self):
        print("this is a general vehicle")


class MotorCycle(Vehicle):
    def __init__(self, brand, model, year,type):
        super().__init__(brand, model, year)
        self.type=type

    
    def vehicle_type(self):
        print(f"this is a {self.brand} {self.model} {self.type} made in {self.year} vehicle")

        
class Car(Vehicle):
    def __init__(self, brand, model, year,type):
        super().__init__(brand, model, year)
        self.type=type


    def vehicle_type(self):
        print(f"This is a {self.brand} {self.model} {self.type} made in {self.year} Vehicle")


car=Car("BMW","M3",2024,"Car")
bike=MotorCycle("Ducati","M52",2014,"Bike")


car.vehicle_type()
bike.vehicle_type()
class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The Engine Of {self.make} {self.model} Is Starting ... ")


car1=Car("Toyota","Corola",2020)
car2=Car("Honda","Civic",2009)

car1.start_engine()
car2.start_engine()

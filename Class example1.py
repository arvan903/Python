class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1=Person("Rashid",34)

person1.display_info()
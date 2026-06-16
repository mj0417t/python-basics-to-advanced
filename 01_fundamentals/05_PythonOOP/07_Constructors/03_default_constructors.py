class Car:
    def __init__(self):
        #initialising car with default attributes
        self.make='Toyota'
        self.model='Corola'
        self.year=2020

#creating instnace using default constructor
car=Car()
print(car.make)
print(car.model)
print(car.year)
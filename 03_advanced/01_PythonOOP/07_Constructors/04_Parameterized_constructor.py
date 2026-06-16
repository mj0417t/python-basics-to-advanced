class Car:
    def __init__(self,make,model, year):
        #initialising car with default attributes
        self.make=make
        self.model=model
        self.year=year

#creating instnace using default constructor
car=Car("honda","civic",2022)
print(car.make)
print(car.model)
print(car.year)
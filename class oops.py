class car:
    def __init__(self,brand,fuel_type):
        self.brand=brand
        self.fuel_type=fuel_type
    def car_details(self,milage:float):
        print(f"this is {self.brand} car and is {self.fuel_type} car and has a milage of {milage} kmph")
car1=car(brand="Benz",fuel_type="Disel")
car2=car(brand="Porche", fuel_type="petrol")

car1.car_details(16)
car2.car_details(8)


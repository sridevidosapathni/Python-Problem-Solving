class engine:
    def engine_type(self):
        print("this vehiclr has a disel engine")

class wheels:
    def number_of_wheels(self):
        print("this vehicle has 4 wheels")

class truck(engine,wheels):
    pass

truck=truck()
truck.engine_type()
truck.number_of_wheels()

            

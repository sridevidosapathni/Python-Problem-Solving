class shape:
    def area(self):
        print("calculating area")
class circle(shape):
    def area(self):
        print("area of circle:")
class rectangle(shape):
    def area(self):
        print("area of rectangle:lenght*breadth")

circle=circle()
rectangle=rectangle()
circle.area()
rectangle.area()

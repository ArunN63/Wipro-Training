from Oops_concepts.formulamethods import FM


class Rectangle(FM):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return  2 * (self.length + self.breadth)
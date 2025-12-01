from tkinter.font import names


class Cars:

    def __init__(self, name, year, expensive):
        self.name = name
        self.year = year
        self.expensive = expensive

    def base_method(self):
        return f"base action {self.name}"


    Kia5 = Cars(Kia5, 2008, 10)
    Opel = Cars(Opel, 2013, 14)


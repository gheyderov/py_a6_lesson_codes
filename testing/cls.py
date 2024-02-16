
class Calc:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def sumx(self):
        return self.a + self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b


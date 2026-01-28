from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    """

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    """
    Square is a special case of Rectangle
    (parent/child relationship).
    """
    def __init__(self, side: float):
        super().__init__(side, side)


if __name__ == "__main__":
    rect = Rectangle(4, 6)
    square = Square(5)

    print("Rectangle area:", rect.area())
    print("Rectangle perimeter:", rect.perimeter())

    print("Square area:", square.area())
    print("Square perimeter:", square.perimeter())

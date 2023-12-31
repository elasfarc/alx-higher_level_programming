#!/usr/bin/python3
"""definie a class Rectangle representing a rectangle
"""


class Rectangle:
    """an empty class Triangle that defines a triangle:
    """
    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two Rectangle objects and return the larger or equal one.

        This static method takes two Rectangle objects,
        compares their areas, and returns the larger or equal one.
        If either of the objects is not an instance of Rectangle,
        it raises a TypeError.

        Args:
            rect_1 (Rectangle): The first Rectangle object to compare.
            rect_2 (Rectangle): The second Rectangle object to compare.

        Returns:
            Rectangle: The Rectangle object that has an area greater
            than or equal to the other Rectangle.

        Raises:
            TypeError: If either `rect_1` or `rect_2`
            is not an instance of Rectangle.

        Example:
            rect1 = Rectangle(3, 4)
            rect2 = Rectangle(5, 2)
            larger_rect = Rectangle.bigger_or_equal(rect1, rect2)
        """
        are_rectangles = [isinstance(
            rec, Rectangle) for rec in [rect_1, rect_2]]
        if not all(are_rectangles):
            raise TypeError("rect_{} must be an instance of Rectangle".format(
                "1" if not are_rectangles[0] else "2")
            )

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __init__(self, width=0, height=0):
        """int the new rectangle instace

        Args:
            @width: width of the rectangle
            @height: height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @width.setter
    def width(self, width):
        """setter for the width field

        Args:
            @width: the new width
        """
        if not type(width) is int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """setter for the height field

        Args:
            @height: the new height
        """
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """return the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if any([e == 0 for e in [self.width, self.height]]):
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Return a string representation of a Rectangle object.

        If either the width or height of the rectangle is 0,
        an empty string is returned. Otherwise, a string is constructed
        by creating rows of string representation of print_symbol , with
        each row separated by a newline character
        """
        s = ""
        if self.width == 0 or self.height == 0:
            return s
        for row in range(0, self.height):
            for _ in range(self.width):
                s += str(self.print_symbol)
            s += '\n' if not row == self.height - 1 else ""
        return s

    def __repr__(self):
        """Return a string representation that can be used to
        recreate a Rectangle object."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor method for a Rectangle object."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

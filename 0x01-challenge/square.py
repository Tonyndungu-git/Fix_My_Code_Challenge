#!/usr/bin/python3
""" class square """


class square:
    def __init__(self, side_length):
        """
        Initialize the Square object.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.side_length ** 2

    def PerimiterOfMySquare(self):
        """
        Calculate the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.side_length

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"Square: side_length={self.side_length}"


if __name__ == "__main__":
    s = square(side_length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimiterOfMySquare())

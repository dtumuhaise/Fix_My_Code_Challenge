#!/usr/bin/python3
""" module for the square class """


class Square():
    """ defining the class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ instatiation of the class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ peremeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ create square object """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())

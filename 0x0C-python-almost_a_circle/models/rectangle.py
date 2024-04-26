#!/usr/bin/python3
"""

Module contains class Rectangle

Inherits from Base;
Inits superclass id
Contains private width, height, x, y
Contains public method area
Displays rectangle using "#" s
Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>
Updates attributes: arg1=id, arg2=width, arg3=height, arg4=x, arg5=y
Returnd=s dictionary representation of attributes
"""

from models.base import Base

Class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    Inherited Attributes:
    id
    Class Attributes:
    __width     __height
    __x         __y
    methods
    __init__(self, width, height, x=0, y=0, id=None):
    update(self, *args, ""kwags)
    width(self)     width(self, value)
    height(self)    height(self, value)
    x(self)         x(self,  value)
    y(self)         y(self, value)
    area(self)      display(self)
    __str__         to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        super().init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

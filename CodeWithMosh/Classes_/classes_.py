# Class: blueprint for creating new objects
# Object: instance of a class
# Class: Human
# Objects: John, Mary, Jack

class Point:
    """instance vs class attributes"""
    default_color = "red"


    """constructor"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """decorators"""
    @classmethod
    def zero(cls):
        return cls(0, 0)

    """Magic methods"""
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def  draw(self):
        print(f"Point ({self.x}, {self.y})")
"""Factory methods"""
point = Point.zero()
point.draw()    
Point.default_color = "yellow"    
point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined)
print(point == other)
print(point > other)
print(point < other)

print(str(point))
print(point.default_color)
print(Point.default_color)
point.draw()
"""class level attributes are shared across all instance level or object of the type"""
another = Point(3, 4)
another.draw()
print(another.default_color)
print(type(point))



class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
print(cloud.__dict__)
print(cloud._TagCloud__tags)
cloud.add("python")
cloud.add("python")

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(50)
product.price = 1
print(product.price)


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")
# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
print(m.weight)
print(isinstance(m, object))
issubclass(Mammal, Animal)

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass
from abc import ABC,abstractmethod
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")

stream = MemoryStream()
stream.open()

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

class TextBox:
    def draw(self):
        print("Textbox")

class DropDownList:
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

class Text(str):
    def duplicate(self):
        return self + self
    
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")
print(list)
text = Text("Python")
print(text.duplicate())

from collections import namedtuple
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p1 = Point(x=10, y=2)
print(p1.x)
# print(id(p1))
# print(id(p2))
print(p1 == p2)

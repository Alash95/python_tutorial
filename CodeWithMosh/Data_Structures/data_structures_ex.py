"""Lists"""

from array import array
from collections import deque
letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(len(chars))


letters[0] = "A"
print(letters[-1])
print(letters)
print(letters[0:3])
print(letters[::2])
print(numbers[::2])
print(numbers[::-1])

"""list unpacking"""
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers
print(first, last)
print(other)
first = numbers[0]
second = numbers[1]
third = numbers[2]

"""Looping over lists """
letters = ["a", "b", "c", "d"]

for index, letter in enumerate(letters):
    print(index, letter)

# Add
letters.append("e")
letters.insert(0, "-")
print(letters)

# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)

"""Finding items"""
letters = ["a", "b", "c", "d"]
print(letters.count("e"))
if "e" in letters:
    print(letters.index("e"))

"""Sorting lists"""
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(sorted(numbers, reverse=True))

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

"""Lambda functions"""
items.sort(key=lambda item: item[1])
print(items)


prices = []
for item in items:
    prices.append(item[1])

print(prices)

prices = list(map(lambda item: item[1], items))
print(prices)
for item in prices:
    print(item)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

"""list comprehension"""
prices = [item[1] for item in items]
print(prices)
filtered = [item for item in items if item[1] >= 10]
print(filtered)

"""zip function"""
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

"""Stacks LIFO"""
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")


"""Queue FIFO"""
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")

"""Tuples"""
point = (1, 2) + (3, 4)
point1 = (1, 2) * 2
point = tuple("Hello World")
print(point)
point = (1, 2, 3)
print(point[0:2])
print(type(point))

x, y, z = point
if 10 in point:
    print("exists")
# point[0] = 10

x = 10
y = 11

z = x
x = y
y = z
x, y = y, x
a, b = 1, 2
print("x", x)
print("y", y)

"""Arrays"""

numbers = array("i", [1, 2, 3])
numbers[0] = 10
numbers.append(4)
numbers.insert(5, -1)
numbers.remove(4)

"""Sets"""
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
first = set(numbers)
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("Yes")

"""Dictionaries"""
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key in point:
    print(key, point[key])
for key, value in point.items():
    print(key, value)

"""Generator expressions/Dictrionary comprehensions"""
values = []
for x in range(5):
    values.append(x *2)
    print(values)
from sys import getsizeof
values = {x: x * 2 for x in range(5)}
print(values)
values = [x * 2 for x in range(100000)]
print("gen:", getsizeof(values))


values = (x * 2 for x in range(100000))
# for x in values:
#     print(x)
print("gen:", getsizeof(values))

"""Unpacking operator"""
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)


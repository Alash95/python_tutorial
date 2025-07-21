"""Variables Basics"""

students_count = 1000
rating = 4.99
is_published = False
# \"
# \'
# \\
# \n
course = "   Python Programming   "

print(students_count)


"""Strings & Slicing"""
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

"""escape sequences"""
# \"
# \'
# \\
# \n

"""Formatted strings"""
first = "Mosh"
last = "Hamedani"
full = first +" " + last
full_1 = f"{first} {last}"
print(full)
print(full_1)


"""string methods"""
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

"""numbers"""
x = 1
x = 1.1
x = 1 + 2j #a + bi
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3

"""type conversion"""
x = input("x: ")
y = int(x) + 1
print(f"x:  {x}, y:  {y}")
# int(x)
# float(x)
# bool(x)
# str(x)

"""Falsy and trusy values"""
bool(0)
bool(1)
bool(-1)
bool(5)
bool("")
bool("False")
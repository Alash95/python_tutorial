# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown")
# print("Execution continues")

# try:
#     with open("exceptions_.py") as file, open("another.txt") as target:
#         print("File opened")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
#     file.close()
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
    """

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
    """

print("firstcode=", timeit(code1, number=10000))
print("firstcode=", timeit(code2, number=10000))

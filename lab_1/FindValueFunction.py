import math


def find_value_of_func(x, y):

    if y < 10:
        z = x * y + y
    else:
        z = x + math.exp(y)

    return z


value_x = float(input("Enter a value for x: "))
value_y = float(input("Enter a value for y: "))

print("Result: " + str(find_value_of_func(value_x, value_y)))

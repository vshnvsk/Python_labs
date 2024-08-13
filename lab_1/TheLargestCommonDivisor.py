def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


value_x = int(input("Enter a value for x: "))
value_y = int(input("Enter a value for y: "))


if value_x <= 0 or value_y <= 0:
    print("The numbers must be positive")
else:
    print("Result: " + str(gcd(value_x, value_y)))

import math


def find_first_value(x, epsilon):
    def a_n(n):
        return (x ** (2 * n) * math.sin(x ** n)) / math.factorial(n ** 2)

    previous_value = a_n(1)

    for n in range(2, 101):
        current_value = a_n(n)
        if abs(current_value - previous_value) < epsilon:
            return current_value, n
        previous_value = current_value

    return None, None


value_x = float(input("Input a value of x: "))
value_epsilon = float(input("Input a value of epsilon: "))

value, index = find_first_value(value_x, value_epsilon)

if value is not None:
    print(f"The first value that satisfies the condition: a - {index} = {value}")
else:
    print("The condition is not met for the first 100 members of the sequence.")

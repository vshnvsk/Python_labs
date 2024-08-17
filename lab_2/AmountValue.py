import math


def amount_value(x, a, epsilon):

    if (x and a) == 0:
        return "Error"

    def term(k):
        return math.cos(a ** k + x ** k) / math.factorial(k ** 2)

    N = 1

    while True:
        S_N = sum(term(k) for k in range(N))
        S_2N = sum(term(k) for k in range(2 * N))

        if abs(S_2N - S_N) < epsilon:
            break

        N *= 2

    return S_2N, N


value_x = float(input("Input a value of x: "))
value_a = float(input("Input a value of a: "))
value_epsilon = float(input("Input a value of epsilon: "))

result, terms_count = amount_value(value_x, value_a, value_epsilon)
print(f"Amount value: {round(result, 2)}, The number of terms taken into account: {terms_count}")


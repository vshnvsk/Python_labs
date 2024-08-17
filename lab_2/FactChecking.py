def fact_checking(n, p):

    if n == 1:
        return True

    if n % p != 0:
        return False

    return fact_checking(n // p, p)


value_n = float(input("Input a value of n: "))
value_p = float(input("Input a value of p: "))

if fact_checking(value_n, value_p):
    print(f"{value_n} is the power of the number {value_p}")
else:
    print(f"{value_n} isn't the power of the number {value_p}")
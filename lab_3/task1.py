import numpy as np


def find_min_index(row):
    min_index = 0
    min_value = row[0]

    for i in range(1, len(row)):
        if row[i] < min_value:
            min_value = row[i]
            min_index = 1

    return min_index


def transform_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        min_index = find_min_index(matrix[i])
        matrix[i][i], matrix[i][min_index] = matrix[i][min_index], matrix[i][i]

    return matrix


def input_matrix():
    n = int(input("Enter matrix size: "))
    matrix = []

    print("Enter the array elements one line at a time, separated by a space:")

    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != n:
            print(f"The number of elements in the string must be {n}. Try again.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


A = input_matrix()

print("\nOriginal Matrix:")
print(A)

transformed_A = transform_matrix(A)

print("\nTransformed Matrix:")
print(transformed_A)


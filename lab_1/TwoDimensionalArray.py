def input_2d_array():

    rows = 4
    cols = 6

    array = []

    print(f"Enter the array {cols} elements one line at a time, separated by a space:")
    try:
        for i in range(rows):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            while len(row) != cols:
                print(f"The number of elements in the string must be {cols}. Try again.")
                return input_2d_array()
            array.append(row)
    except ValueError:
        print("Invalid type. Please, input just numbers.")
        return None

    return array


def one_dimensional_array_with_max_value(array):

    new_array = []

    for row in array:
        max_value = max(row)
        new_array.append(max_value)

    return new_array


matrix = input_2d_array()


if matrix is not None:
    print("Your array:")
    for row in matrix:
        print(row)

    print("One-dimensional array with max value from two-dimensional array: " +
          str(one_dimensional_array_with_max_value(matrix)))
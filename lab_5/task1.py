import math
import matplotlib.pyplot as plt


def func():
    x_values = list(range(-3, 4))
    y_values = []

    for x in x_values:
        y = 15 * math.sin(10 * x) * math.cos(3 * x)
        y_values.append(y)
        print(f"x: {x}, y: {y}")

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of the function 15*sin(10*x)*cos(3*x)')
    plt.grid(True)

    plt.savefig('function_plot_task1.png', format='png')

    plt.show()


func()
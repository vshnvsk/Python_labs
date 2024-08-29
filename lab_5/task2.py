import matplotlib.pyplot as plt


def func():
    user_str = str(input("Enter your string: \n"))
    data = []
    vocabulary = {}

    for i in user_str.split():
        data.append(i)

    for word in data:
        count = 1
        for symbol in word:
            vocabulary[symbol] = count
            if symbol in vocabulary.keys():
                count += 1

    print(vocabulary)

    labels = list(vocabulary.keys())
    values = list(vocabulary.values())

    plt.bar(labels, values)
    plt.savefig('histogram_task2.png', format='png')
    plt.show()


func()
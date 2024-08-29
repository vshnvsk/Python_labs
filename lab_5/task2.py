import matplotlib.pyplot as plt


def func():
    user_str = str(input("Enter your string: \n"))
    data = []
    vocabulary = {}
    count = 1

    for i in user_str.split():
        data.append(i)

    for word in data:
        for symbol in word:
            if symbol not in vocabulary.keys():
                count = 1
                vocabulary[symbol] = count
            else:
                count += 1
                vocabulary[symbol] = count

    print(vocabulary)

    labels = list(vocabulary.keys())
    values = list(vocabulary.values())

    plt.bar(labels, values)
    plt.savefig('histogram_task2.png', format='png')
    plt.show()


func()
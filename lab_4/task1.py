def find_odd_numbers():
    with open('task1.txt', 'r+') as file:
        content = file.read()
        data = []

        for i in content:
            if i.isdigit() and int(i) % 2 != 0:
                data.append(i)
        print(data)

        new_content = '\n'.join(data) + content

        file.seek(0)

        file.write(new_content)

        file.truncate()

        file.close()


find_odd_numbers()
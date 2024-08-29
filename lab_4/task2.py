def change_symbol():
    with open("task2_1.txt", 'r') as file_1:
        content = file_1.read()
        data = []

        for i in content:
            if i.isdigit():
                data.append(i)
        print(data)

        with open("task2_2.txt", 'w') as file_2:
            data_2 = []

            for i in data:
                if int(i) == 0:
                    temp = '1'
                    data_2.append(temp)
                elif int(i) == 1:
                    temp = '0'
                    data_2.append(temp)

            print(data_2)

            new_content = '\n'.join(data_2)

            file_2.write(new_content)
            file_2.close()

        file_1.close()


change_symbol()
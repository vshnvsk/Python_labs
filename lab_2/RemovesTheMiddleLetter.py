def removes_the_middle_letter(s):

    new_s = s.split()
    vocabulary = []

    for word in new_s:
        if len(word) % 2 == 0:
            vocabulary.append(word)
        else:
            index_to_remove = len(word) // 2
            modified_word = word[:index_to_remove] + word[index_to_remove + 1:]
            vocabulary.append(modified_word)

    return vocabulary


user_str = str(input("Enter your sentences separated by a space: \n"))

print("Your sentences without the middle letter in odd words:")
print(removes_the_middle_letter(user_str))
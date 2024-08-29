import matplotlib.pyplot as plt
import re


def analyze_sentence_types(text):
    regular_sentences = re.findall(r'[^.!?…]+[.]', text)    # Звичайні речення
    question_sentences = re.findall(r'[^.!?…]+\?', text)    # Питальні речення
    exclamatory_sentences = re.findall(r'[^.!?…]+!', text)  # Окличні речення
    ellipsis_sentences = re.findall(r'[^.!?…]+…', text)     # Речення з трикрапкою

    sentence_counts = {
        'Regular': len(regular_sentences),
        'Questions': len(question_sentences),
        'Exclamations': len(exclamatory_sentences),
        'Ellipsis': len(ellipsis_sentences)
    }

    print(sentence_counts)

    labels = list(sentence_counts.keys())
    values = list(sentence_counts.values())

    plt.bar(labels, values)

    plt.xlabel('Sentence Type')
    plt.ylabel('Frequency')
    plt.title('Frequency of Sentence Types in Text')

    plt.savefig('sentence_type_histogram_task3.png', format='png')

    plt.show()


user_text = """
Це звичайне речення. А це питальне речення? Це окличне речення! І ось ще одне речення з трикрапкою…
Ще одне звичайне речення. Що ти робиш? Як чудово! Це теж окличне речення! А що з трикрапкою…
"""

analyze_sentence_types(user_text)
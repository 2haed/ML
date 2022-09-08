import regex as re
import numpy as np
import random
from collections import Counter


def reading(filename) -> list:
    with open(filename, 'r') as reading_file:
        text = [re.split("[^a-zа-яё]+", re.sub("[[:punct:]]", '', x.lower().strip())) for x in reading_file.readlines()]
        sum = []
        for i in text:
            sum += i
        ctr = Counter(sum)
        list = []
        for key, val in ctr.items():
            items = (key, val / len(ctr))
            list.append(items)
        return list


# def tokenization(text) -> dict:
#     bigram_counts = {}
#     for i in range(len(text)- 1):
#         bigram = (text[i], text[i+1])
#         if bigram in bigram_counts.keys():
#             bigram_counts[bigram] += 1
#         else:
#             bigram_counts[bigram] = 1
#     print(bigram_counts)
#     return bigram_counts


def generator(list, length) -> str:
    word_list = [x[0] for x in list]
    variaty_list = [x[1] for x in list]
    generated_str = ''
    generated_words = random.choices(word_list, weights=variaty_list, k=length)
    for word in generated_words:
        generated_str += word
        generated_str += ' '
    return generated_str


def write(filename, str):
    with open(filename, 'w') as writing_file:
        writing_file.write(str)


formatted_text = reading('text_for_training_eng.txt')

# word_list = [x[0] for x in formatted_text]

# tokenization(word_list)
print(generator(formatted_text, int(input('Введите длину предложения: '))))

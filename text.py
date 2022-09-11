import time

import regex as re
import numpy as np
import random
from collections import Counter

filename = 'Palahniuk Chuck. Fight Club - royallib.ru.txt'


def str_reading(filename: str):
    try:
        with open(filename, 'r', encoding='windows-1251') as reading_file:
            text = reading_file.read()
            text = re.sub(r"[!?]+$", '', text.lower())
            text = re.split("[^a-яё]+", text)
            return text
    except FileNotFoundError as e:
        return False, e

def dict(text, n) -> dict:
    dict = {}
    for i in range(len(text) - (n-1)):
        next_words = []
        for j in range(n-1):
            next_words.append(text[i+j+1])
        if text[i] not in dict:
            dict[text[i]] = [' '.join(next_words)]
        else:
            dict[text[i]].append([' '.join(next_words)])
    print(dict)
    # for key, val in dict.items():
    #     for k, v in Counter(val).items():
    #         val = (k,v)
    #         if val in dict[key]:
    #             dict[key] = [val]
    #         else:
    #             dict[key].append(val)
    # for key, val in dict.items():
    #     filtered_val = [x for x in val if type(x) != str]
    #     val.clear()
    #     for x in filtered_val:
    #         val.append(x)
    # return dict


def generate(dictionary, length) -> str:
    keys = list(dictionary.keys())
    variaty_list = []
    word_list = []
    generated_str = ''
    k = random.choice(keys)
    for i in range(length):
        for j in range(len(dictionary[k])):
            variaty_list.append(dictionary[k][j][1])
            word_list.append(dictionary[k][j][0])
        generated_phrase = random.choices(word_list, weights=variaty_list, k=1)
        variaty_list.clear()
        word_list.clear()
        generated_str += k + " " if i > 0 and k != generated_str.split()[-1] else " "
        generated_str += generated_phrase[0]
        generated_str += ' '
        k = generated_phrase[0].split()[1] if generated_phrase[0].split()[1] in dictionary else random.choice(keys)
    splitted_str = generated_str.split()
    splitted_str = splitted_str[:(len(splitted_str)-length)]
    generated_str = ' '.join(splitted_str)
    print(generated_str)


# dictionary = {
#     'ads': [('ahjdfd asd', 3), ('gsas dddf', 2),],
#     'asdds': [('saa sdd', 1), ('gs df', 1), ('asas dd', 2)],
#     'asdfs': [('sag dfgd', 2), ('asd gsdf', 1),],
#     'gdfs': [('sa sdd', 5), ('ag sdf', 1),]
# }
# key = list(dictionary.keys())
# values = list(dictionary.values())
# k = random.choice(key)
# variaty_list = []
# word_list = []
# # for val, key in dict.items():
# #     print(val, key[0][0].split()[random.randint(0,1)])
# for j in range(len(dictionary[k])):
#     variaty_list.append(dictionary[k][j][1])
#     word_list.append(dictionary[k][j][0])
# print(word_list)
# print(variaty_list)
x1 = time.time()
dictionary = dict(str_reading(filename), 5)
# print(dictionary)
# generate(dictionary, int(input('Введите длину строки: ')))
x2 = time.time()
print(f' Программма сработала за: {x2-x1}')
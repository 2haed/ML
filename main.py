import regex as re
import numpy as np
import random
from collections import Counter
import time

FILENAME = 'text_for_training_eng.txt'


def str_reading(filename) -> list:
    with open(filename, 'r') as reading_file:
        text = reading_file.read()
    text = re.sub("[[:punct:]]", '', text.lower())
    text = re.split("[^a-яё]+", text)
    return text


def dict(text) -> dict:
    dict = {}
    for i in range(len(text) - 1):
        if text[i] not in dict:
            dict[text[i]] = [text[i + 1]]
        else:
            dict[text[i]].append(text[i + 1])
    for key, val in dict.items():
        for k, v in Counter(val).items():
            val = (k, v)
            if val in dict[key]:
                dict[key] = [val]
            else:
                dict[key].append(val)
    for key, val in dict.items():
        filtered_val = [x for x in val if type(x) != str]
        val.clear()
        for x in filtered_val:
            val.append(x)
    return dict


def generator(filename, length) -> str:
    dictionary = dict(str_reading(filename))
    keys = list(dictionary.keys())
    variaty_list = []
    word_list = []
    generated_str = ''
    k = random.choice(keys)
    for i in range(length):
        for j in range(len(dictionary[k])):
            variaty_list.append(dictionary[k][j][1])
            word_list.append(dictionary[k][j][0])
        generated_word = random.choices(word_list, weights=variaty_list, k=1)
        variaty_list.clear()
        word_list.clear()
        generated_str += generated_word[0]
        generated_str += ' '
        k = generated_word[0]
    return generated_str


x1 = time.time()
print(*generator('text_for_training_eng.txt', int(input())).split())
x2 = time.time()
print(f'\nВремя потраченное на генерацию: {x2 - x1}')

import time

import regex as re
import numpy as np
import random
from collections import Counter

filename = 'test.txt'


def str_reading(filename: str):
    try:
        with open(filename, 'r', encoding='UTF-8') as reading_file:
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
            dict[text[i]].append(' '.join(next_words))
    for key, val in dict.items():
        for k, v in Counter(val).items():
            val = (k,v)
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

def generate(filename, length, n, prefix=None) -> str:
    dictionary = dict(str_reading(filename), n)
    keys = list(dictionary.keys())
    variaty_list = []
    word_list = []
    if prefix and prefix in dictionary:
        generated_str = prefix
        k = prefix
    else:
        k = random.choice(keys)
        generated_str = k
    for i in range(length):
        for j in range(len(dictionary[k])):
            variaty_list.append(dictionary[k][j][1])
            word_list.append(dictionary[k][j][0])
        generated_phrase = random.choices(word_list, weights=variaty_list, k=1)
        variaty_list.clear()
        word_list.clear()
        generated_str += k + " " if i > 0 and k != generated_str.split()[-1] else " "
        generated_str += generated_phrase[0]
        k = generated_phrase[0].split()[n-2] if generated_phrase[0].split()[n-2] in dictionary else random.choice(keys)
    generated_str = ' '.join(generated_str.split()[:length]).replace("  ", " ")
    print(generated_str)


x1 = time.time()
generate(filename, 10, 5, 'для')
x2 = time.time()
print(f' Программма сработала за: {x2-x1}')
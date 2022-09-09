import regex as re
import numpy as np
import random
from collections import Counter

filename = 'text_for_training_eng.txt'

def list_reading(filename) -> list:
    with open(filename, 'r') as reading_file:
        text = [re.split("[^a-zа-яё]+", re.sub("[[:punct:]]", '', x.lower().strip())) for x in reading_file.readlines()]
        sum = []
        for i in text:
            sum += i
        return sum

def dict(list) -> dict:
    dict = {}
    for i in range(len(list) - 1):
        if list[i] not in dict:
            dict[list[i]] = [list[i+1]]
        else:
            dict[list[i]].append(list[i+1])
    # print(dict)
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



def generator(filename, length) -> list:
    generated_str = ''
    dictionary = dict(list_reading(filename))
    key_list = dictionary.keys()
    print(key_list)
    for i in range(length):
        k = random.choice(key_list)
        generated_words = random.choices(k, weights=dict[k])


dict(list_reading('test.txt'))
# print(generator('test.txt', 5))
dict = {
    'ads': [('ahjdfd', 3), ('gsasdddf', 2),],
    'asdds': [('saasdd', 1), ('gsdf', 1), ('asasdd', 2)],
    'asdfs': [('sagdfgd', 2), ('asdgsdf', 1),],
    'gdfs': [('sasdd', 5), ('agsdf', 1),]
}
values = list(dict.values())
keys = list(dict.keys())
k = random.choice(keys)
a = random.randint(0,len(dict[k])-1)
print(a)
print(dict[k])
print(values)
for i in range(len(values)):
    for j in i:
        print(values[i][j])
# for i in range(5):
#     k = random.choice(keys)
#     a = random.randint(0,len(dict[k])-1)
#     generated_words = random.choices(dict[k], weights=dict[k])
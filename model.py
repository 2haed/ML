import random
import pickle
from typing import Union

import regex as re
from collections import Counter
from dataclasses import dataclass, field


@dataclass
class BigramModel:
    model_filename: str = field(default="model.pkl")
    model_weights: dict = field(default_factory=dict)

    def fit(self, filename: str) -> tuple[bool, Union[Exception, None]]:
        try:
            with open(filename, 'r') as reading_file:
                text = reading_file.read()
        except FileNotFoundError as e:
            return False, e

        try:
            text = re.sub("[[:punct:]]", '', text.lower())
            text = re.split("[^a-яё]+", text)
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
            self.model_weights |= dict
            return True, None
        except Exception as e:
            return False, e

    def generate(self, length, prefix=None) -> tuple[bool, Union[Exception, None]]:
        try:
            with open(self.model_filename, 'rb') as f:
                self.model_weights = pickle.load(f)
        except FileNotFoundError as e:
            return False, e
        try:
            keys = list(self.model_weights.keys())
            variaty_list = []
            word_list = []
            generated_str = prefix + " " if prefix is not None else ''
            k = random.choice(keys)
            for _ in range(length - int(prefix is not None)):
                for j in range(len(self.model_weights[k])):
                    variaty_list.append(self.model_weights[k][j][1])
                    word_list.append(self.model_weights[k][j][0])
                generated_word = random.choices(word_list, weights=variaty_list, k=1)
                variaty_list.clear()
                word_list.clear()
                generated_str += generated_word[0]
                generated_str += ' '
                k = generated_word[0]
            yield generated_str
            with open('generated.txt', 'w') as f:
                f.write(generated_str)
            return True, str
        except Exception as e:
            return False, e

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(file=self.model_filename, mode='wb') as file:
            pickle.dump(self.model_weights, file)

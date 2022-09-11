import random
import pickle
import string
from typing import Union
from collections import Counter
from dataclasses import dataclass, field


@dataclass
class NgrammModel:
    model_filename: str = field(default="model.pkl")
    model_weights: dict = field(default_factory=dict)

    def fit(self, filename: str, n: int) -> tuple[bool, Union[Exception, None]]:
        try:
            with open(filename, 'r', encoding='UTF-8') as reading_file:
                text = reading_file.read()
        except FileNotFoundError as e:
            return False, e
        try:
            text = text.lower().translate(str.maketrans("", "", string.punctuation + "«»—…")).replace('\n\n', '\n').split(" ")
            dict = {}
            for i in range(len(text) - (n - 1)):
                next_words = []
                for j in range(n - 1):
                    next_words.append(text[i + j + 1])
                if text[i] not in dict:
                    dict[text[i]] = [' '.join(next_words)]
                else:
                    dict[text[i]].append(' '.join(next_words))
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
            if len(self.model_weights) != 0:
                random.seed(random.randint(0, len(self.model_weights)))
                print("yes")
                keys = list(self.model_weights.keys())
                variaty_list = []
                word_list = []
                generated_str = ''
                if prefix:
                    prefix = ' '.join(prefix)
                else:
                    prefix = random.choice(list(self.model_weights.keys()))
                generated_str += ' '.join(prefix.split()[:-1])
                if prefix.split()[-1] not in self.model_weights.keys():
                    k = random.choice(keys)
                else:
                    k = prefix.split()[-1]
                    generated_str += " "
                    generated_str += k
                for i in range(length):
                    for j in range(len(self.model_weights[k])):
                        variaty_list.append(self.model_weights[k][j][1])
                        word_list.append(self.model_weights[k][j][0])
                    generated_phrase = random.choices(word_list, weights=variaty_list, k=1)
                    variaty_list.clear()
                    word_list.clear()
                    generated_str += k + " " if i > 0 and k != generated_str.split()[-1] else " "
                    generated_str += generated_phrase[0]
                    k = generated_phrase[0].split()[-1] if generated_phrase[0].split()[-1] in self.model_weights else random.choice(keys)
                generated_str = ' '.join(generated_str.split()[:length]).replace("  ", " ")
                generated_str += ' '
            else:
                generated_str = 'Текст слишком короткий для генерации по данной модели'
            yield generated_str
            with open('generated.txt', 'a+') as f:
                f.write(generated_str)
            return True, str
        except Exception as e:
            return False, e

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(file=self.model_filename, mode='wb') as file:
            pickle.dump(self.model_weights, file)
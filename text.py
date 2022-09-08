from nltk.corpus import brown
from nltk.tokenize import word_tokenize
import regex as re


def set_reading(filename) -> set:
    with open(filename, 'r') as reading_file:
        text = [re.split("[^a-zа-яё]+", re.sub("[[:punct:]]", '', x.lower().strip())) for x in reading_file.readlines()]
        sum = []
        for i in text:
            sum += i
        return set(sum)


def list_reading(filename) -> list:
    with open(filename, 'r') as reading_file:
        text = [re.split("[^a-zа-яё]+", re.sub("[[:punct:]]", '', x.lower().strip())) for x in reading_file.readlines()]
        sum = []
        for i in text:
            sum += i
        return sum


lower_case_corpus = list_reading('text_for_training_eng.txt')
vocab = set_reading('text_for_training_eng.txt')

print('lower_case_corpus lenght: ', len(lower_case_corpus), '\n')
print('vocab lenght: ', len(vocab))

bigram_counts = {}
trigram_counts = {}


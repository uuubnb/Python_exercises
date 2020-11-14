import string
import random

TARGET_STRING = ''
TARGET_STRING_LEN = 0
SYMBOLS = string.ascii_uppercase + ' ' + string.punctuation
# SYMBOLS = string.ascii_uppercase + ' '
GENERATIONS = 100
GENERATION_POPULATION = 100
all_generations = []
best_string = {
    'string': '',
    'score': 0,
    'generation_base': ''
}

def create_random_string(target_len):
    return ''.join(random.choice(SYMBOLS) for _ in range(target_len))

def create_initial_strings():
    all_generations.append([create_random_string(TARGET_STRING_LEN) for _ in range(GENERATION_POPULATION)])

def get_string_score(string):
    score = 0
    for i in range(TARGET_STRING_LEN):
        if string[i] == TARGET_STRING[i]:
            score += 1
    return score 

def update_best_string(string, score):
    best_string['string'] = string
    best_string['score'] = score

def check_match():
    generation = all_generations[-1] # a list with a last generated generation with 100 children
    for string in generation:
        score = get_string_score(string)
        if score > best_string['score']:
            update_best_string(string, score)

def print_best_string():
    print('Generation number ' + str(len(all_generations)))
    print(best_string['string'])

def monkeys(target_string):
    global TARGET_STRING
    TARGET_STRING = target_string
    global TARGET_STRING_LEN
    TARGET_STRING_LEN = len(target_string)
    create_initial_strings()
    check_match()
    print_best_string()


if __name__ == '__main__':
    # monkeys(input('Enter your target string: ').upper())
    monkeys('ME THINKS IT IS LIKE A WEASEL')


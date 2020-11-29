import string
import random
from time import sleep

TARGET_STRING = ''
TARGET_STRING_LEN = 0
SYMBOLS = string.ascii_uppercase + ' ' + string.punctuation
GENERATION_POPULATION = 100
all_generations = []
best_string = {
    'string': '',
    'score': 0,
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

def find_best_string():
    generation = all_generations[-1] # get the last generation
    for string in generation:
        score = get_string_score(string)
        if score > best_string['score']:
            best_string['string'] = string
            best_string['score'] = score

def create_strings_from_base(base):
    for i in range(len(base)):
        if base[i] != TARGET_STRING[i]:
            base = base[:i] + random.choice(SYMBOLS) + base[i+1:]

    return base

def create_next_generation():
    all_generations.append([create_strings_from_base(best_string['string']) for _ in range(GENERATION_POPULATION)])

def print_best_string():
    print(f'Generation number: {len(all_generations)}')
    print(best_string['string'])
    score = best_string['score']
    print(f'The score is: {score}\n')

def monkeys(target_string):
    global TARGET_STRING
    TARGET_STRING = target_string
    global TARGET_STRING_LEN
    TARGET_STRING_LEN = len(target_string)
    create_initial_strings()
    find_best_string()
    print_best_string()

    while not best_string['string'] == TARGET_STRING:
        create_next_generation()
        find_best_string()
        print_best_string()
        sleep(1)
    print('SCRIPT FINISHED')
    return None


if __name__ == '__main__':
    # monkeys(input('Enter your target string: ').upper())
    monkeys('ME THINKS IT IS LIKE A WEASEL')

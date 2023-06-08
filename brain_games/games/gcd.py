from random import randint
from math import gcd
RULE = 'Find the greatest common divisor of given numbers.'
NUMBER_MIN = 1
NUMBER_MAX = 100


def generate_data():
    first_number = randint(NUMBER_MIN, NUMBER_MAX)
    second_number = randint(NUMBER_MIN, NUMBER_MAX)
    question = f'{first_number} {second_number}'
    right_answer = gcd(first_number, second_number)
    return question, str(right_answer)

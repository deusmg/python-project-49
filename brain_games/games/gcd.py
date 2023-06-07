from random import randint
from math import gcd
RULE = 'Find the greatest common divisor of given numbers.'
FIRST_NUMBER = 1
SECOND_NUMBER = 1


def generate_data():
    FIRST_NUMBER = randint(1, 101)
    SECOND_NUMBER = randint(1, 101)
    question = f'{FIRST_NUMBER} {SECOND_NUMBER}'
    right_answer = gcd(FIRST_NUMBER, SECOND_NUMBER)
    return question, str(right_answer)

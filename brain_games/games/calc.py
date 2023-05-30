import random
from random import randint
RULE = "What is the result of the expression?"


def data_generate():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    signs = ['+', '-', '*']
    operator = random.choice(signs)
    question = f'{first_number} {operator} {second_number}'
    if operator == '+':
        right_answer = first_number + second_number
    elif operator == '-':
        right_answer = first_number - second_number
    elif operator == '*':
        right_answer = first_number * second_number
    return question, str(right_answer)

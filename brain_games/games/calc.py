import random
from random import randint
RULE = 'What is the result of the expression?'
NUMBER_MIN = 1
NUMBER_MAX = 100


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def generate_data():
    first_number = randint(NUMBER_MIN, NUMBER_MAX)
    second_number = randint(NUMBER_MIN, NUMBER_MAX)
    operation = ['+', '-', '*']
    operator = random.choice(operation)
    question = f'{first_number} {operator} {second_number}'
    right_answer = calculate(first_number, second_number, operator)
    return question, str(right_answer)

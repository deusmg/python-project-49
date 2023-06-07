import random
from random import randint
RULE = 'What is the result of the expression?'
FIRST_NUMBER = 1
SECOND_NUMBER = 1


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def generate_data():
    FIRST_NUMBER = randint(1, 100)
    SECOND_NUMBER = randint(1, 100)
    operation = ['+', '-', '*']
    operator = random.choice(operation)
    question = f'{FIRST_NUMBER} {operator} {SECOND_NUMBER}'
    right_answer = calculate(FIRST_NUMBER, SECOND_NUMBER, operator)
    return question, str(right_answer)

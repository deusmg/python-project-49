from random import randint
RULE = 'What number is missing in the progression?'
START = 1
STEP = 1
STOP = 1
POINT = 1


def generate_data():
    START = randint(0, 100)
    STEP = randint(1, 11)
    STOP = START + STEP * 10
    POINT = randint(0, 8)
    nums = list(range(START, STOP, STEP))
    right_answer = f'{nums[POINT]}'
    nums[POINT] = '..'
    question = ' '.join(map(str, nums))
    return question, right_answer

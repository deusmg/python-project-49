from random import randint
RULE = 'What number is missing in the progression?'
NUMBER_MIN = 1
NUMBER_MAX = 100
LIST_LEN = 10
STEP_MAX = 11
POINT_MIN = 0
POINT_MAX = 8


def progression_gen(start, step, stop, point):
    nums = list(range(start, stop, step))
    nums[point] = '..'
    return nums


def generate_data():
    start = randint(NUMBER_MIN, NUMBER_MAX)
    step = randint(NUMBER_MIN, STEP_MAX)
    stop = start + step * LIST_LEN
    point = randint(POINT_MIN, POINT_MAX)
    right_answer = str(start + step * point)
    question = ' '.join(map(str, progression_gen(start, step, stop, point)))
    return question, right_answer

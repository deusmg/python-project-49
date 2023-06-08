import prompt
ATTEMPTS_COUNT = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(ATTEMPTS_COUNT):
        question, right_answer = game.generate_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(
                f'"{answer}" is the wrong answer ;(. '
                f'The correct answer was "{right_answer}".'
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

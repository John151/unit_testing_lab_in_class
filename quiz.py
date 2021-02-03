# can you see the bug in this program?

def is_correct_answer(user_answer, correct_answer):
    """ Check if user's answer is the same as the correct
    answer, ignoring case """
    string_correct_answer = str(correct_answer).lower().strip()
    string_user_answer = str(user_answer).lower().strip()
    return string_user_answer == string_correct_answer


def main():
    question = 'How many senators in the US senate?'
    answer = 100

    print(question)
    user_answer = input('What is your answer? ')

    if is_correct_answer(user_answer, answer):
        print('Correct!')
    else:
        print(f'Sorry, the answer is {answer}')


if __name__ == '__main__':
    main()
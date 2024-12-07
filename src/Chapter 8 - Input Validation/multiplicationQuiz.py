import sys
import time
from time import sleep


def quiz():
    print('========= Welcome to my Multiplication Quiz =========')
    correct = False
    count = 0
    start = time.time()
    while not correct:
        try:
            answer = int(input('What is 0 x 0? (%i tries)\n' % count))
            if answer.is_integer():
                if answer == 0:
                    print('Correct!')
                    correct = True
                    sleep(1)
                else:
                    print('you are incorrect')
                    count += 1

            if count == 3 and correct == False:
                print('You have made %i attempts, we will move on to the next question.\n' % count)
                break

            end = time.time()
            length = end-start
            if length > 8:
                print('You took too long! Incorrect! Moving on...')
                break
        except ValueError:
            print('invalid input, try again')

    correct = False
    count = 0
    start = time.time()
    while not correct:
        try:
            answer = int(input('What is 1 x 1? (%i tries)\n' % count))
            if answer.is_integer():
                if answer == 1:
                    print('Correct!')
                    correct = True
                    sleep(1)
                else:
                    print('you are incorrect')
                    count += 1

            if count == 3 and correct == False:
                print('You have made %i attempts, we will move on to the next question.\n' % count)
                break

            end = time.time()
            length = end - start
            if length > 8:
                print('You took too long! Incorrect! Moving on...')
                break
        except ValueError:
            print('invalid input, try again')

    correct = False
    count = 0
    start = time.time()
    while not correct:
        try:
            answer = int(input('What is 2 x 2? (%i tries)\n' % count))
            if answer.is_integer():
                if answer == 4:
                    print('Correct!')
                    correct = True
                    sleep(1)
                else:
                    print('you are incorrect')
                    count += 1

            if count == 3 and correct == False:
                print('You have made %i attempts, we will move on to the next question.\n' % count)
                break

            end = time.time()
            length = end - start
            if length > 8:
                print('You took too long! Incorrect! Moving on...')
                break
        except ValueError:
            print('invalid input, try again')

    correct = False
    count = 0
    start = time.time()
    while not correct:
        try:
            answer = int(input('What is 3 x 3? (%i tries)\n' % count))
            if answer.is_integer():
                if answer == 9:
                    print('Correct!')
                    correct = True
                    sleep(1)
                else:
                    print('you are incorrect')
                    count += 1

            if count == 3 and correct == False:
                print('You have made %i attempts, we will move on to the next question.\n' % count)
                break

            end = time.time()
            length = end - start
            if length > 8:
                print('You took too long! Incorrect! Moving on...')
                break
        except ValueError:
            print('invalid input, try again')

    correct = False
    count = 0
    start = time.time()
    while not correct:
        try:
            answer = int(input('What is 4 x 4? (%i tries)\n' % count))
            if answer.is_integer():
                if answer == 16:
                    print('Correct!')
                    correct = True
                    sleep(1)
                else:
                    print('you are incorrect')
                    count += 1

            if count == 3 and correct == False:
                print('You have made %i attempts, we will move on to the next question.\n' % count)
                break

            end = time.time()
            length = end - start
            if length > 8:
                print('You took too long! Incorrect! Moving on...')
                break
        except ValueError:
            print('invalid input, try again')

    correct = False
    count = 0
    start = time.time()
    while not correct:
        try:
            answer = int(input('What is 5 x 5? (%i tries)\n' % count))
            if answer.is_integer():
                if answer == 25:
                    print('Correct!')
                    correct = True
                    sleep(1)
                else:
                    print('you are incorrect')
                    count += 1

            if count == 3 and correct == False:
                print('You have made %i attempts, we will move on to the next question.\n' % count)
                break

            end = time.time()
            length = end - start
            if length > 8:
                print('You took too long! Incorrect! Moving on...')
                break
        except ValueError:
            print('invalid input, try again')

try:
    quiz()
except KeyboardInterrupt:
    sys.exit(0)

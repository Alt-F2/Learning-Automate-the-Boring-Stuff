import random

toss = random.randint(0,1) # 0 is tails, 1 is heads
flips = ['tails', 'heads']

guess = input('Guess the coin toss! Enter heads or tails: \n')
if flips[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if flips[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


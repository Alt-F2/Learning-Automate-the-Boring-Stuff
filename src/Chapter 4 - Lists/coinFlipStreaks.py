import random

numberOfStreaks = 0
coin = ('H', 'T')

for experimentNumber in range(10000):
    flips = []
    onStreak = 0

    for i in range(100):
        # creates list of 100 'heads' or 'tails' values.
        flips.append(coin[random.randint(0, 1)])

    for j in range(len(flips) - 1):
        if flips[j] == flips[j+1]:
            onStreak += 1
        else:
            onStreak = 0

        if onStreak == 6:
            numberOfStreaks += 1
            onStreak = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
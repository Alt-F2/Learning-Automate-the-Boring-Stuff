import sys

import pyinputplus as pyip

def breadPreference():
    response = pyip.inputMenu(choices=['wheat', 'white', 'sourdough'], prompt= 'What type of bread would you like?\n')
    return response

def proteinPreference():
    response = pyip.inputMenu(choices=['chicken', 'turkey', 'ham', 'tofu'], prompt= 'What type of protein would you like?\n')
    return response

def cheesePreference():
    response = pyip.inputYesNo(prompt='Would you like cheese?\n')
    if response == 'yes':
        response = pyip.inputMenu(choices=['cheddar', 'Swiss', 'mozzarella'], prompt= 'What type of cheese would you like?\n')
    else:
        response += ' cheese'

    return response

def toppingPreference():
    response = pyip.inputYesNo(prompt='Would you like toppings?\n')
    return response

def sandwichCount():
    response = pyip.inputInt(prompt='How many sandwiches would you like?\n', greaterThan=1)
    return response

try:
    choices = [breadPreference(), proteinPreference(), cheesePreference(), toppingPreference(), sandwichCount()]
    print('* Bread: %s' % choices[0]
          + '\n* Protein: %s' % choices[1]
          + '\n* Cheese: %s' % choices[2]
          + '\n* Toppings? %s' % choices[3]
          + '\n* Sandwich no. %i' % choices[4])

except KeyboardInterrupt:
    sys.exit(0)
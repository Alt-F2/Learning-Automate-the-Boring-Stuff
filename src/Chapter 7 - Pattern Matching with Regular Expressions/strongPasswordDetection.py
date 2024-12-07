import re
import sys


def passwordStrength(password):
    validatedpw = pwValidation.search(password)
    print(validatedpw.group())

pwValidation = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

try:
    passwordStrength('dafdsfsfasdf')
except AttributeError:
    print('Invalid Password')
    sys.exit(0)
import re
import sys


def detectDate(text):
    date = dateRegex.search(text)

    day, month, year = date.groups()

    if month == '02' and int(year) % 4 == 0:
        if day > '28':
            raise AttributeError
    elif month == '02':
        if day > '29':
            raise AttributeError
    elif month == '04' or '06' or '09' or '11':
        if day > '30':
            raise AttributeError

    print(date.group() + ' is a valid date.')


dateRegex = re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[0-9][0-9][0-9]|2[0-9][0-9][0-9])')

try:
    detectDate('Hello, today is: 28/02/1000')
except AttributeError:
    print('Incorrect date entered.')
    sys.exit(0)
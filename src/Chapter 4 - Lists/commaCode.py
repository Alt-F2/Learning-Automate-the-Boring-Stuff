spam = ['apples', 'bananas', 'tofu', 'cats']

def to_comma_separated(list):
    if not list:
        return

    return ', '.join(list)

print(to_comma_separated(spam))

def collatz(number):
      if number % 2 == 0:
          print(number // 2)
          return number // 2
      else:
          print(3 * number + 1)
          return 3 * number + 1

while True:
    try:
        numberEntry = int(input('Enter an Integer:\n'))
        break
    except ValueError:
        print("The input was not a valid integer.")

while numberEntry != 1:
    numberEntry = collatz(numberEntry)
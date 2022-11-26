import random
import time


def bet(numm, amount):
    print('Please wait')
    time.sleep(2)
    choice = random.randint(1, 31)
    if choice == numm:
        print(choice)
        print('You won!')
        return amount * 2
    else:
        print(choice)
        print(f'-{amount}$')
        print('Try again!')
        return 0

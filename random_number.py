import random

try:
    min = int(input('Low number = '))
    max = int(input('High number = '))

    rand_num = random.randint(min, max)

    print('A random number between {0} and {1} is: {2}'.format(min, max, rand_num))
except:
    print('Sorry, something went wrong')

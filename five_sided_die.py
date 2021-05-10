import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()

    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result


print('Rolling 5-sided die...')
print(rand5())
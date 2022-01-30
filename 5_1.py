'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
'''


def odd_nums(nums):
    '''
    odd number generator from 1 to "nums"
    :param nums: the limit of the list of numbers
    :return: integer
    '''
    for i in range(1, nums + 1, 2):
        yield i


nums = int(input("Введите число: "))

for n in odd_nums(nums):
    print(n, end=', ')
'''
2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.
'''

# num = int(input("Введите число: "))
# odd_nums = (_ for _ in range(1, num + 1, 2))
#
# for n in odd_nums:
#     print(n, end=', ')

print(*[_ for _ in range(1, int(input("Введите число: ")) + 1, 2)])

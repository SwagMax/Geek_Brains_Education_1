'''
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a)Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
b)К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
'''

# a)

#Создаем пустой список
cube_list = []
#добавляем новое значение (нечетное, в кубе) циклом
for i in range(1001):
    if i % 2:
        cube_list.append(i**3)
    i += 1
# Разбить число на цифры, сложить цифры, проверить на кратность 7
sum = 0
med_sum = 0
maj_sum = 0
for n in cube_list:
    med_sum = n
    while n > 0:
        m = n % 10
        n //= 10
        sum += m
    if sum % 7 == 0:
        maj_sum += med_sum
    sum = 0
print(maj_sum)

# b)
#Создаем пустой список
cube_list = []
#добавляем новое значение (нечетное, в кубе, +17) циклом
for i in range(1001):
    if i % 2:
        cube_list.append(i**3+17)
    i += 1
# Разбить число на цифры, сложить цифры, проверить на кратность 7
sum = 0
med_sum = 0
maj_sum = 0
for n in cube_list:
    med_sum = n
    while n > 0:
        m = n % 10
        n //= 10
        sum += m
    if sum % 7 == 0:
        maj_sum += med_sum
    sum = 0
print(maj_sum)
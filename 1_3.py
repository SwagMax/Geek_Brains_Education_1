'''
3.Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой
для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

for i in range(1,101):
    if i % 10 == 1:
        if i % 100 == 11:
            print(f'{i} Процентов')
            continue
        print (f'{i} Процент')
    elif i % 10 in [2,3,4]:
        if i % 100 in [12,13,14]:
            print(f'{i} Процентов')
            continue
        print(f'{i} Процента')
    elif i % 10 in [5,6,7,8,9,0]:
        print(f'{i} Процентов')
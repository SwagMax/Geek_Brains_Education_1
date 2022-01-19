'''Дан список:
    ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и
дополнить нулём до двух целочисленных разрядов:
    ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
    в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!

*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача
намного серьёзнее, чем может сначала показаться.'''

data_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in data_list:
    #print(i)
    if i.isnumeric():
        j = i
#        print(f' {j} \n {type(j)}')
        if not int(j) // 10:            #проверка на разрядность
            j = '0' + j                 #добавление "0" перед числом
        j = '"' + j + '"'               #добавить кавычку до и после
#        print(f' {j} \n {type(j)}')
        idx = data_list.index(i)        #получение индекса в списке
#        print("index raven", idx)
        data_list.insert(idx, j)        #вставка элемента по индексу
        data_list.pop(idx+1)            #удаление значения старого индекса
#        print(data_list)

    elif i.find('+') != -1:             #если найдешь + то:
        _num = ''
        for k in i:                     #повторять для символа k в строке i:
            if k.isnumeric():           #если символ k число, то:
                _num += k               #приписать к строке _num
        if _num != '':                  #если строка уже заполнилась (например 5 15)
            if not int(_num) // 10:     #проверка на разрядность
                _num = '0' + _num       #добавление "0" перед числом
            idx = data_list.index(i)    #получение индекса в списке
#            print("index raven", idx)
            num = (f'"+{_num}"')         #добавить знак, кавычку до и после
            data_list.insert(idx, num)  #вставка элемента по индексу
            data_list.pop(idx + 1)      #удаление элемента по старого индекса
#        print(data_list)

    elif i.find('-') != -1:
        _num = ''
        for k in i:                     #повторять для символа k в строке i:
            if k.isnumeric():           #если символ k число, то:
                _num += k               #приписать к строке _num
        if _num != '':                  #если строка уже заполнилась (например 5 15)
            if not int(_num) // 10:     #проверка на разрядность
                _num = '0' + _num       #добавление "0" перед числом
            idx = data_list.index(i)    #получение индекса в списке
#            print("index raven", idx)
            num = (f'"-{_num}"')         #добавить знак, кавычку до и после
            data_list.insert(idx, num)  #вставка элемента по индексу
            data_list.pop(idx + 1)      #удаление элемента по старого индекса
#        print(data_list)
print(' '.join(data_list))
'''3. Создать собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop».

При этом
скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и
строки. Во время ввода пользователем очередного элемента необходимо реализовать
проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение
должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.'''


class Validation:
    def __init__(self):
        self.my_list = []

    def val_input(self):
        while True:
            try:
                val = int(input('Введите число: '))
                self.my_list.append(val)
                #print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Не верный тип значения!!!")
                stop = input(f'Для выхода - введите "stop": ')
                if stop.lower() != 'stop':
                    print(validation.val_input())
                else:
                    print(f'{self.my_list}')
                    return f'Game over'


validation = Validation()
print(validation.val_input())














#a = Validation()
#print()
#try_except = Validation()
#print(try_except.my_input())


#fluggegecheimen

# while True:
        #     s = 's'
        #     val = input()
        #     if val.isdigit(): #True
        #         self.my_list.append(val)
        #         print('ok')
        #         try_except.my_input()
        #     elif val.lower() == s:
        #         print(self.my_list)
        #
        #     else:
        #         print('Only numerical')
        #         try_except.my_input()
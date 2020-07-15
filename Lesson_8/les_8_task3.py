# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class MyError(ValueError):
    def __init__(self):
        self.my_list = []

    def my_input(self):

        str_input = ""
        while not str_input == "stop":
            str_input = input("Введите значение списка (stop для выхода): ")
            try:
                if str_input.isdigit():
                    number = int(str_input)
                    self.my_list.append(number)
                else:
                    raise MyError()
            except MyError as err:
                print(f"Недопустимое значение!")
                yes_or_no = input(f"Попробовать еще раз? Да/Нет ")

                if yes_or_no.lower() == 'да':
                    print(try_except.my_input())
                else:
                    str_input = "stop"

        return f"Сформированный список: {self.my_list}"


try_except = MyError()
print(try_except.my_input())

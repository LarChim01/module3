# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
#
#     Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
#     Функция должна выводить эти параметры.
#     Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
#     Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#1
print_params()
print_params(8, 4)
print_params(b=25)
print_params(c=[1, 2, 3])
# 2
#     Создайте список values_list с тремя элементами разных типов.
#     Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
#     Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
#
values_list = [3, "Urban", [1, 2, 3]]
print_params(*values_list)
values_dict = {'a': 45, 'b': True, 'c': [1, 2, 3]}
print_params(**values_dict)
values_dict = {'c': [1, 2, 3]}
list_=[1,2]
print_params(*list_, **values_dict)
# 3.Распаковка + отдельные параметры:
#
#     Создайте список values_list_2 с двумя элементами разных типов
#     Проверьте, работает ли print_params(*values_list_2, 42)
#
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
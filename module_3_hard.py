
# Подсчёт суммы всех чисел и длин всех строк"

# Что должно быть подсчитано:
#
#     Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#     Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
#
def calculate_structure_sum(*arg):
    global sum
    for i in arg:
        if isinstance(i, list):  # для каждого элемента списка снова вызываем функцию
            for j in i:
                calculate_structure_sum(j)
        elif isinstance(i, (int ,float)): #если  число прибавляем его к сумме
            sum += i
            return
        elif isinstance(i, str): #если строка прибавляем её длину
            sum += len(i)
            return
        elif isinstance(i, tuple):
            for j in i:
                calculate_structure_sum(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                calculate_structure_sum(key)
                calculate_structure_sum(value)
        elif isinstance(i, set): # если тип set

            calculate_structure_sum(list(i))

    return sum

sum=0
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)

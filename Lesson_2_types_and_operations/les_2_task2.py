# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

array = []
for i in range(1, 10):
    array.append(int(input(f"Введите - {i}-ое значение списка: ")))
print(f"Текущий список - {array}")

if len(array) % 2 == 0:
    len_array = len(array)  # четное
else:
    len_array = len(array) - 1  # нечетное

for i in range(0, len_array, 2):
    x = array[i]
    array[i] = array[i + 1]
    array[i + 1] = x

print(f"Итоговый список - {array}")

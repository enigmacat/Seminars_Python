# ====================================================================
# Задача №1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# =====================================================================

list = [3, 7, 4, 9, 1, 5, 3]
sum = 0
for i in range(1, len(list), 2):
    sum += list[i]
print(f"{list} -> сумма элементов на нечётных позициях: {sum}")
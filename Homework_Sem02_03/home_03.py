# ================================================================
# Задача №3. Задайте список из (2*N+1) элементов,заполненных
# числами из промежутка [-N, N]. Найдите произведение
# элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся
# в списке, который вы сами заполняете.
# ==============================================================

import random

input_number = int(input("Введите число N: "))
index_length = 5

input_index = [
    random.randint(0, 2*input_number) for i in range(index_length)
]

input_numbers  = [item for item in range(-input_number,input_number+1)]

def list_items_multiply(numbers: list, index:list)->int:
    multiply = 1
    for item in index:
        multiply*=numbers[item]
    return multiply

res = list_items_multiply(input_numbers, input_index)

print ("Индексы", input_index)
print ("Ряд чисел", input_numbers)
print ("Произведение элементов с заданными индексами =", res)

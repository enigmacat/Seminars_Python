# ===========================================================
# Задача №1. Вычислить число Pi c заданной точностью d,
#  не используя ф. round()
# ===========================================================

import math


def my_pi(number: float, numbers_of_digits: int) -> float:
    last_digit = int(PI*10**(numbers_of_digits+1) % 10)

    ratio = 10**numbers_of_digits

    if last_digit < 5:
        return number*ratio // 1 / ratio

    return (number*ratio+1) // 1 / ratio


PI = math.pi
input_number = int(input("Количество знаков после запятой:"))
print(my_pi(PI, input_number))

# ======================================================================
# Задача №4. Напишите программу, которая принимает на вход координаты
#  двух точек и находит расстояние между ними в 2D пространстве.
# =======================================================================

from math import *
a = int(input("Координаты X первой точки:"))
b = int(input("Координаты Y первой точки:"))
a1 = int(input("Координаты X второй точки:"))
b1 = int(input("Координаты Y второй точки:"))
z = sqrt((a1-a)**2+(b1-b)**2)
print(round(z, 3))

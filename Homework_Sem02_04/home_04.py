# ===================================================
# Задача №4. Требуется посчитать сумму чётных чисел,
# расположенных между числами 1 и N включительно.
# =======================================================


n = int(input("Введите число N: "))
res = 0
for i in range(1, n+1):
    if i % 2 == 0:
        res += i
print(f"Сумма чётных чисел равна {res}")
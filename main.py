# ДЗ 1: решение квадратного уравнения.
import math

def count(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return [x1, x2]
    if D == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []

print("Введите коэффициенты:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

res = count(a, b, c)
if len(res) == 0:
    print("Уравнение не имеет корней")
elif len(res) == 1:
    print(f"Уравнение имеет единственный корень: х = {res[0]}")
else:
    print(f"Уравнение имеет два корня: х1 = {res[0]}, х2  {res[1]}")

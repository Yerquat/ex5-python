# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def summ(a, b):
    # s = 1
    if b > 0:
        s = 1 + summ(a, b-1)  # здесь вместо "1" было "s"
        return s
    return a
a = int(input())
b = int(input())
print(summ(a, b))
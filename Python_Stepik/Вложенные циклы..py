#1. Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3 состоящую из данного числа (числа отделены одним пробелом)

n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()

#2. Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, где в i-ой строке указано число i (числа отделены одним пробелом)

n = int(input())
for i in range(n):
    for j in range(5):
        print(i+1, end=' ')
    print()

#3. Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n

n = int(input())
for i in range(n):
    for j in range(9):
        print(i + 1, "+", j + 1, "=", (i + 1) + (j + 1))
    print()

#4. Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n

n = int(input())
centr = n // 2 + 1
count = 0
for i in range(1, n + 1):
    if i > centr:
        count -= 1
    else:
        count += 1
    for j_ in range(count):
        print('*', end='')
    print()

#5. Дано натуральное число nn. Напишите программу, которая печатает численный треугольник

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1, end='')
    print()
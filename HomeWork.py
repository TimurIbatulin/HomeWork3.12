# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12


a = []
y = int(input('Введите значение длинны массива - '))
for k in range(y):
    k = input(f'Введите {k+1} значания списка- ')
    a.append(k)
print(f'{a} на нечетных позициях', end=' ')
sum = 0
i = 0
for z in a:
    if i != 0:
        if i%2 != 0:
            print(z, end=' ')
            if z.isdigit():
                sum += int(z)
    i += 1
print(f'ответ: {sum}')



# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = []
l = int(input('введите желаемую длинну списка - '))
for k in range(l):
    k = input(f'Введите {k+1} значение cписка (целое число) - ')
    list.append(k)
print(list, end='=>')
d = 1
w = int(-1)
h = int(l/2)
for u in range(h):
    d = int(list[u])*int(list[w])
    w -=1
    print(d, end=' ')
if l%2==1:    
    w = int(l/2)
    d = int(list[w])**2
    print(d)
    

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

list = []
y = int(input('Введите количество чисел в списке - '))
for x in range(y):
    x = input(f'Введите {x+1} вещественное число списка - ')
    list.append(x)
print(list, end='=>')
w = 0
r = 0
min = float(list[0])
max = 0
t = 0
for l in range(y):
    w = float(list[l])*10//10
    r = float(list[l])-w
    if r < min:
        min = r
    elif r > max:
        max = r
t = round(max - min, 2)
print(t)


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


y = int(input('Введите число переводимое в двоичный код - '))
z = 2
t = str()
list = []
while y > 1:
    z = y%2
    y = int(y/2)
    t = t + str(z)
if y == 1:
    t = t + str(y)
reversedstring=''.join(reversed(t))
print(reversedstring)


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

f = int(input('Введите число для расчета числа Фибоначи-'))
f_min = None
f_max = None
f_n2 = 1
f_n1 = 0
box = 0
fibonachi = []
if f < 0:
     f = f * -1
for x in range(f):
    box = f_n2 - f_n1
    fibonachi.append(box)
    f_n2 = f_n1
    f_n1 = box
fibonachi.reverse()
fibonachi.append(0)
f_n2 = 1
f_n1 = 0
for z in range(f-1):
    box = f_n2 +f_n1
    fibonachi.append(box)
    f_n1 = f_n2
    f_n2 = box
print(f'для к = {f} список будет выглядеть так:',fibonachi)



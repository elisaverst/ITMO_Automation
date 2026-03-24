def task_1():  # вывести наибольшее из чисел
    a = 7
    b = 5
    if a > b:
        print(a)
    else:
        print(b)

task_1()


def task_2(a, b):  # вывести “yes”, если числа отличаются друг от друга на 135, иначе - “no”
    if abs(a - b) == 135:
        print('yes')
    else:
        print('no')

task_2(200, 66)


def task_3(m):  # вывести название сезона года
    if m <= 2 or m == 12:
        print('зима')
    if 3 <= m <= 5:
        print('весна')
    if 6 <= m <= 8:
        print('лето')
    if 9 <= m <= 11:
        print('осень')

task_3(12)


def task_4(a, b, c):  # вывести “yes”, если все числа больше 10, иначе - “no”
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')

task_4(11, 31, 20)


def task_5(num_list: list) -> int:  # количество положительных чисел
    count = 0
    for num in num_list:
        if num > 0:
            count += 1
    print(count)

task_5([1, -5, 3, 0, 5])


def task_6(y, m):  # количество дней
    d = (y * 12 + m) * 29
    print(d)

task_6(2, 3)

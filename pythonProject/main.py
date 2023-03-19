import random


# Функция заполнения случайными числами
def auto_fill():
    return [random.randint(1, 100) for x in range(1, 10)]


# Функция ввода элементов с клавиатуры
def manual_fill():
    print("Введите элементы массива:")
    try:
        return list(map(int, input().split()))
    except:
        print("Ввод некоректен. Работа программы завершена(")
        exit()


# Выбор способа ввода пользователем
try:
    choise = int(input("Введите 1, чтобы заполнить список с клавиатуры, 2, чтобы заполнить случайными числами\n"))
except:
    print("Ввод некоректен. Работа программы завершена(")
    exit()

if choise == 1:
    a = manual_fill()
elif choise == 2:
    a = auto_fill()
else:
    print("Вы не выбрали ни один из препложенных вариантов. Работа программы завершена")
    exit()
# Вывод списка
print("Ваш массив:", " ".join(map(str, a)))

# Функция нахождения длинны массива
def get_len_list(list):
    count = 0
    for item in list:
        count += 1
    return count

# Функция нахождения суммы массива
def get_sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

# Функция обработки массива со встроенными функциями
def transformation1(list):
    b = [x for x in list if not x % 2]
    if len(b) == 0:
        print("В массиве нет четных элементов. Работа программы завершена")
        exit()
    medium = sum(b) / len(b)
    i = 0
    print("Среднее арифметическое четных чисел =", medium)
    while i < len(list):
        if list[i] < medium:
            list.pop(i)
            i = 0
            continue
        i += 1

    print("Преобразованный массив:", " ".join(map(str, list)))


# Функция обработки массива без встроенных функций
def transformation2(list):
    b = [x for x in list if not x % 2]
    if get_len_list(b) == 0:
        print("В массиве нет четных элементов. Работа программы завершена")
        exit()
    medium = get_sum_list(b)/ get_len_list(b)
    i = 0
    print("Среднее арифметическое четных чисел =", medium)
    c = filter(lambda x: x > medium, list)

    print("Преобразованный массив:", " ".join(map(str, c)))


# Выбор варианта обработки массива пользователем
try:
    choise = int(input("Введите 1, чтобы преобразовать массив с использованием стандартных функций,"
             "\n2, чтобы преобразовать массив без использования стандартных функций\n"))
except:
    print("Ввод некоректен. Работа программы завершена(")
    exit()

if choise == 1:
    transformation1(a)
elif choise == 2:
    transformation2(a)
else:
    print("Вы не выбрали ни один из препложенных вариантов. Работа программы завершена")
    exit()
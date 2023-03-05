from task1 import reformat_timestamp
from task2 import min_el
while True:
    if input("Введите номер задания: 1 или 2\n") == "1":
        sa = input("Введите время в секундах:\n")
        print(reformat_timestamp(int(sa)))
    else:
        choise = input("если вы хотите ввести отсортированный массив введите 1, иначе 2\n")
        a = input("введите элементы массива через пробел\n")
        if choise == "1":
            print("минамальный элемент = ", min_el(a, 1))
        if choise == "2":
            print("минамальный элемент = ", min_el(a, 2))
    if input("Введите 1 для выхода, 2 для продолжения\n") == "1":
        exit(0)

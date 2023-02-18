import csv
import os.path
from pathlib import Path
import datetime as dt
import pandas as pd


# Функция нахождения числа файлов в папке
def count_files():
    directory = Path(input("Введите путь к папке, в которой необходимо посчитать число файлов.\n"))
    # files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    try:
        tree = list(os.walk(directory))
        print("число файлов в выбранной папке =", len(tree))
    except:
        print("Проверьте корректность ввода пути")


# Функция вывода
def f_out(d):
    print("На вход полученны следующие данные:")
    columns = ['Date', 'Time', 'Bool', 'Gender']
    print(" ".join(map(str, columns)))
    st = ""
    for i in range(len(d)):
        for j in range(len(d[i])):
            # print(d[i].get(columns[j]), d[i])
            st += d[i].setdefault(columns[j]) + " "
        print(st)
        st = ""

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


# Функция считывания из файла в словарь
def f_read():
    FILENAME = "users.csv"
    d = list()
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # d.update({int(index): row})
            d.append(dict(row))
    return d


# Функция записи новых данных
def f_write():
    #     writer.writeheader()
    columns = ['Date', 'Time', 'Bool', 'Gender']
    FILENAME = "users.csv"
    data = input('Введите дату в формате год.месяц.день\n')
    r, t = map(int, input('Введите часы, минуты\n').split())
    with open(FILENAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = columns)
        writer.writerow({'Date': data,
                          'Time': dt.time(r, t),
                          'Bool': bool(input('Если сотрудник зашел введите 1, если вышел нажмите Enter\n')),
                          'Gender': input('Введиде "M" для мужского пола, "W" для женского\n')})
    f_out(f_read())


# Функция вывода вошедших
def ch2():
    columns = ['Date', 'Time', 'Bool', 'Gender']
    print(" ".join(map(str, columns)))
    st = ""
    for i in range(len(d)):
        # print(d[i].setdefault('Bool'))
        if d[i].setdefault('Bool') == 'True':
            for j in range(len(d[i])):
                    st += d[i].setdefault(columns[j]) + " "
            print(st)
            st = ""


try:
    choise = int(input("Введите 1, чтобы узнать число файлов в папке,"
                       " 2, чтобы считать данные из файла и начать работу с данными постелителей\n"))
except:
    print("Ввод некоректен. Работа программы завершена(")
    exit()
if choise == 1:
    count_files()
elif choise == 2:
    d = f_read()
    f_out(d)
    columns = ['Date', 'Time', 'Bool', 'Gender']
    while True:
        ch = int(input("Для ввода новых данных введите 1, для вывода только вошедших нажмите 2,\n"
                   " для сортировки по дате нажмите 3, для сортировки по полу нажмите 4,"
                   "\n для выхода нажмите 5 \n"))
        if ch == 5:
            break
        elif ch == 1:
            f_write()
        elif ch == 2:
            ch2()
        elif ch == 3:
            d = f_read()
            d = sorted(d, key=lambda f: f["Date"])
            f_out(d)
        elif ch == 4:
            d = f_read()
            d = sorted(d, key=lambda f: f["Gender"])
            f_out(d)
        else:
            print('Вы не выбрали ни один из предложенных вариантов, попробуйте еще раз...')




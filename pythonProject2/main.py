import numpy as np

# Функция заполнения элементами массива
def inpuuuuuut(a: list[list[float]]):
    try:
        choise = int(input("Введите 1, чтобы считать матрицу из файла, 2, чтобы заполнить случайными числами\n"))
    except:
        print("Ввод некоректен. Работа программы завершена(")
        exit()
    if choise == 1:
        a = np.loadtxt('lab_file_input.txt')    # Чтение данных их файла
    elif choise == 2:
        N, M = map(int, input('Введите число строк (N) и число столбцов (M)\n').split()) # Ввод размера масива
        a = np.random.randint(1, 100, size=(N, M)) # Заполнение случайными числами
        a = a.astype("float")
    np.savetxt('lab_file_output', a, fmt='%d')
    return a


# Функция обработки массива
def update_array(a: list[list[float]]):
    max_el = np.amax(a, axis=0)
    f = open('lab_file_output', 'a')
    N, M = a.shape
    for i in range(N):
       for j in range(M):
           a[i][j] /= max_el[j]
           a[i][j] = format(a[i][j], '.3f')
           f.write(str(a[i][j]) + " ") # Запись поделенных элементов в файл
       f.write("\n")
a = np.array([[]])
a = inpuuuuuut(a)
update_array(a)

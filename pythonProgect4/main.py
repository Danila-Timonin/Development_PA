from Person import *

example = Record_list()
print("Исходный список:\n" + str(example))
while True:
    ch = int(input("Для ввода новых данных введите 1, для вывода посетителей мужского пола нажмите 2,\n"
                   "для сортировки по дате нажмите 3, для сортировки по статусу(ВХОД/ВЫХОД) нажмите 4,"
                   "\nдля сортировки по индексу нажмите 6, для вывода с помощью итератора - 7,\n"
                   "с помощью генератора - 8, для обращения по индексу введите 9\n"
                   "для выхода нажмите 5 \n"))
    if ch == 5:
        break

    elif ch == 1:
        example.new_record()

    elif ch == 2:
        print(example.only_men())

    elif ch == 3:
        example.sort_by_date()
        print(example)

    elif ch == 4:
        example.sort_by_state()
        print(example)

    elif ch == 6:
        example.sort_by_Number()
        print(example)

    elif ch == 7:
        for it in example:
            print(it)

    elif ch == 8:
        for i in example.generator():
            print(i)

    elif ch == 9:
        index_ = int(input("Введите индекс объкта, который вы хотите вывести(индексация начинается с '0')\n"))
        print(example[index_])
    else:
        print('Вы не выбрали ни один из предложенных вариантов, попробуйте еще раз...')
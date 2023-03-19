import csv

# классы неявно наследуются от object

# класс, каждый объект которого будет использоваться для хранения одной записи
class Record:
    # возможные ключи
    Variants = ["_Number", "_Date", "_Time", "_State", "_Gender"]
    _Number: int
    _Date: str
    _Time: str
    _State: bool
    _Gender: str

    # заполняем все данные посетителя
    def __init__(self, Number, Date, Time, State, Gender):
        self.__setattr__("_Number", Number)
        self.__setattr__("_Date", Date)
        self.__setattr__("_Time", Time)
        self.__setattr__("_State", State)
        self.__setattr__("_Gender", Gender.rstrip())

    # с помощью __setattr__ создаем проверку на имя ключа при добавлении
    # элемента, если ключ не предусмотрен - ошибка
    def __setattr__(self, key, value):
        if key in self.Variants:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError("Данный атрибут отсутствует")

    #реализуем вывод объектов
    def __str__(self):
        return str(self._Number) + ", " + self._Date + ", " + self._Time + ", " + \
            self.__bool_to_string(self._State) + ", " + self._Gender

    # статический метод, преобразующий атрибут "State" в более читабельную форму
    @staticmethod
    def __bool_to_string(state):
        if state:
            return "Посетитель зашел"
        elif not state:
            return "Посетитель вышел"


# класс, который хранит все записи
class Record_list:
    iter_index = 0
    records = []

    # при создании экземпляра данные считываются из файла и создантся список
    def __init__(self):
        self.read_file()

    def read_file(self):
        with open("users.csv", "r", newline="") as file:
            text = file.readlines()
            for line in text:
                line.rstrip()
                self.records.append(Record(int(line.split(",")[0]), line.split(",")[1], line.split(",")[2],
                                    line.split(",")[3], line.split(",")[4]))

    # заносим новую запись в файл, еще раз вызываем функцию чтения файла
    def new_record(self):
        columns = ['Number', 'Date', 'Time', 'State', 'Gender']
        data = input('Введите дату в формате год.месяц.день\n')
        time = input('Введите часы.минуты\n')
        state = bool(input('Если сотрудник зашел введите 1, если вышел нажмите Enter\n'))
        gender = input('Введиде "M" для мужского пола, "W" для женского\n')
        with open("users.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow({'Number': str(len(self.records) + 1),
                             'Date': data,
                             'Time': time,
                             'State': state,
                             'Gender': gender})
        self.records.append(Record(str(len(self.records) + 1), data, time, state,
                                   gender))

    def __str__(self):
        str_ = ""
        for i in Record.Variants:
            str_ += i + " "
        str_ += "\n"
        for i in self.records:
            str_ += str(i) + "\n"
        return str_

    # сортировка по дате
    def sort_by_date(self):
        self.records.sort(key=lambda init: init._Date)

    # сортировка по переменной, определяющей выход и вход
    def sort_by_state(self):
        self.records.sort(key=lambda init: init._State)

    # сортировка ао индексу
    def sort_by_Number(self):
        self.records.sort(key=lambda init: init._Number)

    # возращает только мужчин
    def only_men(self):
        str_ = ""
        for i in self.records:
            if i._Gender == "M":
                str_ += str(i) + "\n"
        return str_

    # итератор
    def __iter__(self):
        return self

    # переопределение next для использования итератора
    def __next__(self):
        if self.iter_index >= len(self.records):
            self.iter_index = 0
            raise StopIteration
        else:
            self.iter_index += 1
            return self.records[self.iter_index - 1]

    # реализация обращения по индексу
    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")
        elif 0 <= item < len(self.records):
            return self.records[item]
        else:
            raise IndexError("Выход за границы списка.")

    # реализация генератора
    def generator(self):
        index = 0
        while index < len(self.records):
            yield self.records[index]
            index += 1
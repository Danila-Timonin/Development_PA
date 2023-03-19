from random import randrange

d_sate = ["good", "very_well", "no_good"]


class Transpost:
    def __init__(self, name, model_engin):
        self.__name = name
        self.__state = d_sate[randrange(3)]
        self.__engin = model_engin

    def _get_state(self):
        return self.__state

    def _get_inf(self):
        return "Марка: " + self.__name + "\nДвигатель: " + self.__engin

class Engine:
    def __init__(self, model_engine):
        self.__model_engine = model_engine


class Subaru_engine(Engine):
    def __init__(self, model_engine):
        Engine.__init__(self, model_engine)
        self.__engine_lound = {
            "good": "I like eat oil! I must do it!",
            "very_well": "I like eat oil, but I will not do it, because I am very good car",
            "no_good": "knock knock knock knock knock knock knock knock..."}

    def check_engine(self, state):
        return self.__engine_lound.get(state)


class Subaru_car(Transpost):
    def __init__(self, model_engine):
        Transpost.__init__(self, "Subaru", model_engine)
        self.__engine = Subaru_engine(model_engine)

    def lound(self):
        return self.__engine.check_engine(self._get_state())


class Toyota_engine():
    def __init__(self, model_engine):
        self.__model_engine = model_engine
        self.__engine_lound = {
            "good": "Jug-jug Jug-jug Jug-jug Jug-jug Jug-jug",
            "very_well": "Jug-jug Jug-jug Jug-jug Jug-jug Jug-jug",
            "no_good": "Jug-jug Jug-jug Jug-jug Jug-jug Jug-jug"}

    def check_engine(self, state):
        return self.__engine_lound.get(state)


class Toyota_car(Transpost):
    def __init__(self, model_engine):
        Transpost.__init__(self, "Toyota", model_engine)
        self.__engine = Toyota_engine(model_engine)

    def lound(self):
        return self.__engine.check_engine(self._get_state())


while True:
    choise = input("Выберите, машину какой марки вы хотите купить:"
                   "\nдля выбора Subaru введите 1, для выбора Toyota введите 2\n\t")
    if choise == '1':
        model_engine = input("Отлично, вы выбрали Subaru, давайте определимся с моделью ДВС:\n\t")
        car = Subaru_car(model_engine)
        print("Информация о вашей машине\n" +car._get_inf() + "\nСостояние вашей машины: "
              + car._get_state() + "\nДля проверки работы двигателя нажмите Enter\t")
        input()
        print(car.lound() + "\n")
    elif choise == '2':
        model_engine = input("Отлично, вы выбрали Toyota, давайте определимся с моделью ДВС:\n\t")
        car = Toyota_car(model_engine)
        print("Информация о вашей машине\n" + car._get_inf() + "\nСостояние вашей машины: "
              + car._get_state() + "\nПослушаем, какие звуки она издает: нажмите Enter\t")
        input()
        print(car.lound() + "\n")
    else:
        exit()
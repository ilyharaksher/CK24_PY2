# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Student:
    def __init__(self, name: str, group: str):
        """
        Создание и подготовка к работе объекта "Студент"

        :param  name: Имя студента
        :param  group: Группа студента

        Примеры:
        >>> student = Student("Иванов И.А.", "33328492/20001") # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(group, str):
            raise ValueError("Группа студента должна быть типа str")
        self.group = group

    def change_group(self, new_group: str) -> None:
        """
        Изменение группы студента
        :param new_group: Новая группа студента

        Примеры:
        >>> student = Student("Иванов И.А.", "33328492/20001")
        >>> student.change_group("4442305/30001")
        """
        if not isinstance(new_group, str):
            raise TypeError("Новая группа студента должна быть типа str")

    def change_name(self, new_name: str) -> None:
        """
        Изменение имени студента
        :param new_name: Новое имя студента

        Примеры:
        >>> student = Student("Иванов И.А.", "33328492/20001")
        >>> student.change_name("4442305/30001")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новая группа студента должна быть типа str")

    def say_name(self) -> str:
        """
        Функция, которая выводит имя студента

        :return: Имя студента
        Примеры:
        >>> student = Student("Иванов И.А.", "33328492/20001")
        >>> student.say_name()
        """

class Lamp:
    def __init__(self, is_on: bool, battery: float):
        """
        :param is_on: включена ли лампа
        :param battery: заряд батареи
        Пример:
        >>> lamp = Lamp(True, 54)
        """
        if not isinstance(is_on, bool):
            raise TypeError("Лампа работает или нет может быть только True или False")
        self.is_on = is_on

        if not isinstance(battery, (int, float)):
            raise TypeError("Информация о батарее должна быть числом")
        if battery < 0:
            raise ValueError("Заряд в батарее должен быть положительным числом")
        self.battery = battery

    def is_lamp_on(self) -> bool:
        """
        Функция, которая показывает, включена ли лампа

        :return: Включена ли лампа

        Пример:
        >>> lamp = Lamp(True, 45):
        >>> lamp.is_lamp_on()
        """
        ...

    def charge_lamp(self, charge: float) -> None:
        """
        :param charge: на сколько процентов нужно зарядить батарею

        :raise ValueError: если сумма прибаленного и текущего заряда превышает 100%
        Пример:
        >>> lamp = Lamp(True, 45)
        >>> lamp.charge_lamp(50)
        """
        if not isinstance(charge, (int,float)):
            raise TypeError("Добавляемый заряд должен быть числом")
        if charge < 0:
            raise ValueError("Заряд должен быть положительным числом")
        ...

    def press_the_switch(self) -> str:
        """
        Функция, которая выключает включенную лампу и включает выключенную
        :return: Описание текущего состояния лампы (вкл/выкл)

        Пример:
        >>> lamp = Lamp(True, 5)
        >>> lamp.press_the_switch()
        """

class Wall:
    def __init__(self, height: float, width: float):
        """
        :param height: высота стены
        :param width: ширина стены

        Пример:
        >>> wall = Wall(220, 600)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стены должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота стены должна быть положительным числом")
        self.height = height

        if not isinstance(height, (int, float)):
            raise TypeError("Ширина стены должна быть типа int или float")
        if height <= 0:
            raise ValueError("Ширина стены должна быть положительным числом")
        self.height = height

    def expand_width(self, new_width) -> None:
        """
        Функция, увеличивающая ширину стены
        :param new_width: новая ширина
        :raise ValueError: если новая ширина меньше старой
        """
        ...
    def glue_wallpaper(self, height_wallpaper:float, width_wallpaper:float) -> str:
        """
        Функция, показывающая влезут ли обои на стену
        :param height_wallpaper: высота обоев
        :param width_wallpaper: ширина обоев
        :return: строку, говоряющую о то, что обои наклеить можно
        """
        ...

if __name__ == "__main__":
# TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

class Animal:
    """ Базовый класс для животных. """

    def __init__(self, name: str, age: int):
        """
        Инициализирует животное с именем и возрастом.

        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self._name = name  # Непубличный атрибут
        self._age = age  # Непубличный атрибут

    @property
    def name(self) -> str:
        """ Возвращает имя животного. """
        return self._name

    @property
    def age(self) -> int:
        """ Возвращает возраст животного. """
        return self._age

    def speak(self) -> str:
        """ Возвращает звук, который издает животное. """
        return "Some sound"

    def __str__(self) -> str:
        """ Возвращает строковое представление животного. """
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        """ Возвращает формальное представление животного. """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"


class Dog(Animal):
    """ Класс для собак. """

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализирует собаку с именем, возрастом и породой.

        :param name: Имя собаки.
        :param age: Возраст собаки в годах.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self._breed = breed  # Непубличный атрибут

    @property
    def breed(self) -> str:
        """ Возвращает породу собаки. """
        return self._breed

    def speak(self) -> str:
        """ Переопределяет метод speak для собаки.
        Возвращает звук, который издает собака.

        Причина переопределения: чтобы предоставить специфичный звук для собаки.
        """
        return "Woof!"

    def __str__(self) -> str:
        """ Возвращает строковое представление собаки. """
        return f"{super().__str__()}, breed={self.breed}"


class Cat(Animal):
    """ Класс для кошек. """

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализирует кошку с именем, возрастом и цветом.

        :param name: Имя кошки.
        :param age: Возраст кошки в годах.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self._color = color  # Непубличный атрибут

    @property
    def color(self) -> str:
        """ Возвращает цвет кошки. """
        return self._color

    def speak(self) -> str:
        """ Переопределяет метод speak для кошки.
        Возвращает звук, который издает кошка.

        Причина переопределения: чтобы предоставить специфичный звук для кошки.
        """
        return "Meow!"

    def __str__(self) -> str:
        """ Возвращает строковое представление кошки. """
        return f"{super().__str__()}, color={self.color}"


if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 2, "Black")

    print(dog)
    print(repr(dog))
    print(dog.speak())

    print(cat)
    print(repr(cat))
    print(cat.speak())

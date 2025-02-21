from abc import ABC, abstractmethod
from typing import List, Tuple, Any

class PhysicalObject(ABC):
    """
    Абстрактный класс, описывающий физический объект.

    Атрибуты:
        mass (float): Масса объекта.
        volume (float): Объем объекта.
        material (str): Материал объекта.
    """

    def __init__(self, mass: float, volume: float, material: str):
        """
        Конструктор класса PhysicalObject.

        Args:
            mass (float): Масса объекта.
            volume (float): Объем объекта.
            material (str): Материал объекта.

        Raises:
            ValueError: Если масса или объем не положительные.
        """
        if mass <= 0:
            raise ValueError("Масса должна быть положительной.")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным.")

        self.mass = mass
        self.volume = volume
        self.material = material

    @abstractmethod
    def move(self, distance: float, direction: Tuple[float, float]) -> None:
        """
        Перемещает объект на заданное расстояние в заданном направлении.

        Args:
            distance (float): Расстояние, на которое нужно переместить объект.
            direction (Tuple[float, float]): Направление движения (x, y).

        Returns:
            None
        """
        ...

    @abstractmethod
    def rotate(self, angle: float) -> None:
        """
        Поворачивает объект на заданный угол.

        Args:
            angle (float): Угол поворота в градусах.

        Returns:
            None
        """
        ...


class DataStructure(ABC):
    """
    Абстрактный класс, описывающий структуру данных.

    Атрибуты:
        size (int): Размер структуры данных.
        data_type (str): Тип данных, которые могут храниться в структуре.
    """

    def __init__(self, size: int, data_type: str):
        """
        Конструктор класса DataStructure.

        Args:
            size (int): Размер структуры данных.
            data_type (str): Тип данных.

        Raises:
            ValueError: Если размер отрицательный.
        """
        if size < 0:
            raise ValueError("Размер должен быть неотрицательным.")
        self.size = size
        self.data_type = data_type

    @abstractmethod
    def insert(self, element: Any) -> None:
        """
        Вставляет элемент в структуру данных.

        Args:
            element (Any): Элемент для вставки.

        Returns:
            None
        """
        ...

    @abstractmethod
    def remove(self, element: Any) -> Any:
        """
        Удаляет элемент из структуры данных.

        Args:
            element (Any): Элемент для удаления.

        Returns:
            Any: Удаленный элемент.
        """
        ...


class SocialNetwork(ABC):
    """
    Абстрактный класс, описывающий социальную сеть.

    Атрибуты:
        num_users (int): Количество пользователей в сети.
        name (str): Название социальной сети.
    """

    def __init__(self, num_users: int, name: str):
        """
        Конструктор класса SocialNetwork.

        Args:
            num_users (int): Количество пользователей.
            name (str): Название сети.

        Raises:
            ValueError: Если количество пользователей отрицательное.
        """
        if num_users < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным.")
        self.num_users = num_users
        self.name = name

    @abstractmethod
    def post_message(self, message: str) -> None:
        """
        Публикует сообщение в социальной сети.

        Args:
            message (str): Текст сообщения.

        Returns:
            None
        """
        ...

    @abstractmethod
    def connect_users(self, user1_id: int, user2_id: int) -> None:
        """
        Устанавливает связь между двумя пользователями.

        Args:
            user1_id (int): ID первого пользователя.
            user2_id (int): ID второго пользователя.

        Returns:
            None
        """
        ...


class ConcretePhysicalObject(PhysicalObject):
    def move(self, distance: float, direction: Tuple[float, float]) -> None:
        """
        Перемещает объект.

        Args:
            distance (float): Расстояние.
            direction (Tuple[float, float]): Направление.

        Returns:
            None

        >>> obj = ConcretePhysicalObject(10, 1, "wood")
        >>> obj.move(5, (1,0))
        """
        pass

    def rotate(self, angle: float) -> None:
        """
        Поворачивает объект.

        Args:
            angle (float): Угол.

        Returns:
            None

        >>> obj = ConcretePhysicalObject(10, 1, "wood")
        >>> obj.rotate(90)
        """
        pass

class ConcreteDataStructure(DataStructure):
    def insert(self, element: Any) -> None:
        """
        Вставляет элемент.

        Args:
            element (Any): Элемент.

        Returns:
            None

        >>> data = ConcreteDataStructure(5, "int")
        >>> data.insert(5)
        """
        pass

    def remove(self, element: Any) -> Any:
        """
        Удаляет элемент.

        Args:
            element (Any): Элемент.

        Returns:
            Any: Удаленный элемент.

        >>> data = ConcreteDataStructure(5, "int")
        >>> data.insert(5)
        >>> data.remove(5)
        """
        pass


class ConcreteSocialNetwork(SocialNetwork):
    def post_message(self, message: str) -> None:
        """
        Публикует сообщение.

        Args:
            message (str): Сообщение.

        Returns:
            None

        >>> fb = ConcreteSocialNetwork(2_000_000_000,"Facebook")
        >>> fb.post_message('Hello world!')
        """
        pass

    def connect_users(self, user1_id: int, user2_id: int) -> None:
        """
        Устанавливает связь между пользователями.

        Args:
            user1_id (int): ID первого пользователя.
            user2_id (int): ID второго пользователя.

        Returns:
            None

        >>> fb = ConcreteSocialNetwork(2_000_000_000,"Facebook")
        >>> fb.connect_users(123, 456)
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

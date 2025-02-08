from abc import ABC, abstractmethod
from typing import List, Tuple

class PhysicalObject(ABC):


    def __init__(self, mass: float, volume: float, material: str):
        if mass <= 0:
            raise ValueError("Масса должна быть положительной.")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным.")

        self.mass = mass
        self.volume = volume
        self.material = material

    @abstractmethod
    def move(self, distance: float, direction: Tuple[float, float]) -> None:

        obj = ConcretePhysicalObject(10, 1, "wood")
        obj.move(5, (1,0))


    @abstractmethod
    def rotate(self, angle: float) -> None:

        obj = ConcretePhysicalObject(10, 1, "wood")
        obj.rotate(90)


class DataStructure(ABC):

    def __init__(self, size: int, data_type: str):
        if size < 0:
            raise ValueError("Размер должен быть неотрицательным.")
        self.size = size
        self.data_type = data_type



    @abstractmethod
    def insert(self, element: any) -> None:

        data = ConcreteDataStructure(5, "int")
        data.insert(5)


    @abstractmethod
    def remove(self, element: any) -> any:

        data = ConcreteDataStructure(5, "int")
        data.insert(5)
        data.remove(5)



class SocialNetwork(ABC):

    def __init__(self, num_users: int, name: str):
        if num_users < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным.")
        self.num_users = num_users
        self.name = name


    @abstractmethod
    def post_message(self, message: str) -> None:

        fb = ConcreteSocialNetwork(2_000_000_000,"Facebook")
        fb.post_message('Hello world!')


    @abstractmethod
    def connect_users(self, user1_id: int, user2_id: int) -> None:
        fb = ConcreteSocialNetwork(2_000_000_000,"Facebook")
        fb.connect_users(123, 456)

class ConcretePhysicalObject(PhysicalObject):
    def move(self, distance: float, direction: Tuple[float, float]) -> None:
        pass

    def rotate(self, angle: float) -> None:
        pass

class ConcreteDataStructure(DataStructure):
    def insert(self, element: any) -> None:
        pass

    def remove(self, element: any) -> any:
        pass


class ConcreteSocialNetwork(SocialNetwork):
    def post_message(self, message: str) -> None:
        pass

    def connect_users(self, user1_id: int, user2_id: int) -> None:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
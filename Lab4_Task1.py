from typing import List


class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str, users_count: int) -> None:
        """
        Инициализирует объект SocialNetwork.

        Args:
            name: Название социальной сети.
            users_count: Количество пользователей.
        """
        self.name = name
        self.users_count = users_count
        self._internal_data = "Some internal data"  # Пример инкапсулированного атрибута

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"Social Network: {self.name}, Users: {self.users_count}"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта, которое может быть использовано для его воссоздания."""
        return f"SocialNetwork(name='{self.name}', users_count={self.users_count})"

    def get_network_info(self) -> str:
        """Возвращает информацию о социальной сети."""
        return f"{self.name} has {self.users_count} users."

    def _internal_method(self) -> str:  # Инкапсулированный метод.
        """Внутренний метод для работы с данными."""
        return self._internal_data


class VK(SocialNetwork):
    """Дочерний класс для социальной сети VK, наследуемый от SocialNetwork."""

    def __init__(self, name: str, users_count: int, popular_groups: List[str]) -> None:
        """
        Инициализирует объект VK.

        Args:
            name: Название социальной сети.
            users_count: Количество пользователей.
            popular_groups: Список популярных групп.
        """
        super().__init__(name, users_count)
        self.popular_groups = popular_groups

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"VK: {self.name}, Users: {self.users_count}, Popular groups: {', '.join(self.popular_groups)}"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта, которое может быть использовано для его воссоздания."""
        return f"VK(name='{self.name}', users_count={self.users_count}, popular_groups={self.popular_groups})"

    def get_network_info(self) -> str:
        """
        Перегруженный метод. Возвращает информацию о социальной сети VK,
        включая список популярных групп.

        Перегрузка обоснована необходимостью добавления информации о популярных группах,
        специфичной для VK.
        """
        return f"{self.name} has {self.users_count} users and popular groups: {', '.join(self.popular_groups)}"

    def get_popular_groups(self) -> List[str]:
        """
        Возвращает список популярных групп.
        Этот метод унаследован от базового класса (хотя и не был явно определен там).
        В данном случае он наследует поведение метода  _internal_method.
        """
        return self.popular_groups




if __name__ == "__main__":
    network = SocialNetwork("Generic Social Network", 1000000)
    print(network)
    print(repr(network))
    print(network.get_network_info())

    vk = VK("VK", 50000000, ["MDK", "Борщ"])
    print(vk)
    print(repr(vk))
    print(vk.get_network_info())
    print(vk.get_popular_groups())

""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""
import dataclasses


@dataclasses.dataclass
class User:
    username: str
    user_id: int
    name: str

    def make_username_capitalized(self):
        return self.username.capitalize()

    def generate_short_user_description(self):
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'

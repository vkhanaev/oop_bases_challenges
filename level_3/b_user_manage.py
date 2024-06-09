"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self) -> None:
        self.usernames = []

    def add_user(self, username) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username) -> None:
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print("Такого пользователя не существует.")


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    um = UserManager()
    um.add_user("Tom")
    print(um.get_users())

    am = AdminManager()
    am.add_user("Tom")
    am.ban_username("Sam")
    print(am.get_users())

    sam = SuperAdminManager()
    sam.add_user("Tom")
    sam.ban_username("Tom")
    sam.ban_all_users()
    print(sam.get_users())

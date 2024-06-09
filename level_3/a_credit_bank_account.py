"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> int:
        return self.balance > 1000


if __name__ == '__main__':
    ba = BankAccount("Ivanov Ivan Ivanovich", 123.45)
    ba.increase_balance(45.12)
    ba.decrease_balance(45.12)

    ca = CreditAccount("Ivanov Ivan Ivanovich", 123.45)
    ca.increase_balance(45.12)
    ca.decrease_balance(45.12)
    print(ca.is_eligible_for_credit())

from .animal import Animal
from random import randint


class Hen(Animal):

    def __init__(
            self,
            name: str,
            age: int,
            say_word='Ко-ко-ко-ко'
    ):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'зерно', 'пшоно'}
        )
        self.animal_type = 'Курка'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за куркою певну кількість годин, ми отримуємо 10 яєць. Якщо догляд триває менше години, отримуємо від 1 до 5 яєць.
        :param hours: кількість годин догляду,
        :return: отримуємо від 1 до 10 яєць.
        """
        while hours <= 0:
            hours += 1

        if hours > 2:
            print(f'Ви доглядаєте за {self} {hours} годин і отримуєте десяток курячих яєць.')
            return 'курячі яйця: 10 шт.'
        print(f'Ви доглядаєте за {self} {hours} годин і отримуєте декілька курячих яєць.')
        return f'курячі яйця: {randint(1, 5)} шт.'


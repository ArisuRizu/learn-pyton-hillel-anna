from .animal import Animal


class Cow(Animal):
    def __init__(self, name: str, age: int, say_word='Мууу!'):
        """
        Клас відповідає за симуляцію життєдіяльності корови.
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'трава', 'сіно'}
        )
        self.animal_type = 'Корова'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за коровою протягом певного часу, ми отримуємо молоко.
        :param hours: час догляду за твариною,
        :return: отримуємо молоко або нічого.
        """
        if hours > 1:
            print(f'Ви доглядаєте за {self} {hours} годин та отримуєте відро молока')
            return 'відро молока'
        print(f'Ви доглядаєте за {self} {hours} годин.')
        return ''

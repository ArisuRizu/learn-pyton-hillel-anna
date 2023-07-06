from .animal import Animal


class Dog(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Гав-гав!'
    ):
        """
        Клас відповідає за симуляцію життєдіяльності собаки.
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'каша', 'м\'ясо', 'кістки', "тортик"}
        )
        self.animal_type = 'Пес'

    def treat(self, hours: int) -> str:
        """
        Доглядаючи за собакою певний час, ми отримуємо гарний настрій.
        :param hours: кількість годин догляду,
        :return: отримуємо нічого або гарний настрій.
        """
        if hours > 2:
            print(f'Ви граєтесь з {self} {hours} годин і у Вас покращується настрій.')
            return 'чудовий настрій'
        print(f'Ви гуляєте з {self} {hours} годин.')
        return ''

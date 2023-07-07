from .animal import Animal

class Cat(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Мяу-Мяуу-МЯУУУ!',
    ):
        """
        Клас відповідає за симуляцію тварини - кота.
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'сухий корм', 'вологий корм', 'недоїдки', 'павук'}
        )

        self.animal_type = 'Кіт'

    def treat(self, hours: int) -> str:
        """
        Догляд за собою здійснює сам кіт, що покращує йому настрій.
        :param hours: час догляду за собою,
        :return: отримуємо знищений диван або нічого.
        """
        while hours <= 0:
            hours += 1

        if hours > 2:
            print(f'{self} дряпає диван {hours} годин і Ви отримуєте зіпсований диван.')
            return 'зіпсований диван'

        print(f'{self} з\'їв павука та дрімає {hours} годин.')
        return ''



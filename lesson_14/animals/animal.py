class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set):
        """
        Клас відповідає за симуляцію життєдіяльності тварин на фермі.
        :param name: ім'я тварини,
        :param age: вік тварини,
        :param say_word: яким "висловом" тварина розмовляє,
        :param preferred_food: раціон харчування
        """
        self.animal_type = '???'
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self.hungry = True
        self.visited_veterinarian = False  # Поле перевірки відвідування ветеринара

    def __str__(self):
        return f'{self.animal_type} {self.name}'

    def say(self):
        """
        Тварина вимовляє "фрази" для привернення уваги.
        """
        print(f'{self} каже: {self.say_word}')

    def eat(self, food: str):
        """
        Метод відповідає за симуляцію харчування тварини на фермі.
        Якщо передана їжа присутня у списку preferred_food, то тварина наїдається і self.hungry = False.
        В іншому випадку тварина не їсть.
        :param food: що їмо.
        """
        if not self.hungry:
            return
        if food in self.preferred_food:
            print(f'{self} їсть {food}')
            self.hungry = False
        else:
            print(f'{self} таке не їсть: {food}')
            self.say()

    def treat(self, hours: int):
        """
        Метод догляду за твариною.
        :param hours: скільки годин ми проводимо з твариною,,
        :return: що отримуємо натомісць
        """
        pass
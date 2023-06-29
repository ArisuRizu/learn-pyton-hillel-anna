from random import randint, choice


class Cat:
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        """
        Клас кіт
        :param name: ім'я
        :param age: вік
        :param breed: порода
        :param preferred_food: їжа яку полюбляє
        """
        print('До Вас приєднався котик')
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food

        self.hungry = True
        self.hours_outdoors = 0
        self.daily_food = []

    def __str__(self):
        """
        Функція в якій зазначаємо підсумкову інформацію про дії кота за день, тобто його основні дані, кличка, порода, вік та скільки він гуляв, та що їв
        """
        starting_str = f"За день котик '{self.name}' породи {self.breed.capitalize()}, якому {self.age}"
        if self.age == 1:
            starting_str += " рік"
        elif 2 <= self.age <= 4:
            starting_str += " роки"
        else:
            starting_str += " років"

        if self.hungry:
            starting_str += ", голодний"
        else:
            starting_str += f", гуляв: {self.hours_outdoors} години, їв: {', '.join(self.daily_food)}"

        return starting_str

    def perform_action(self):
        """
        Функція з виконання випадкової дії: мявчати, їсти або гулти
        """
        actions = ['meow', 'eat', 'walk']
        action = choice(actions)

        if action == 'meow':
            self.meow()
        elif action == 'eat':
            self.eat()
        elif action == 'walk':
            self.walk()

    def meow(self):
        """
        Функція з мявчання
        """
        meowing_str = '-'.join(["мяу"] * randint(1, 3)).capitalize()
        print(f"'{self.name}' м'явкає -> {meowing_str}!")

    def eat(self):
        """
        Кіт їсть випадкову їжу зі списку potential_food
        """
        potential_food = ['сухий корм', 'вологий корм', 'суші', 'лосось', 'сметана', 'риба', 'молоко', 'недоїдки',
                          'Фікус']

        if self.hungry:
            if potential_food:
                food = choice(potential_food)
                if food in self.preferred_food:
                    print(f"'{self.name}' їв те, що любить: {food}")
                elif food == 'Фікус':
                    print(f"'{self.name}' нудить від Фікуса")
                else:
                    print(f"'{self.name}' їв з їжі: {food}")
                self.daily_food.append(food)
                self.hungry = False

        else:
            print(f"'{self.name}' не голодний")

    def walk(self):
        """
        Кіт гуляє випадкову кількість годин
        """
        hours = randint(1, 3)
        print(f"'{self.name}' гуляє {hours} години")
        self.hours_outdoors += hours

    """
          Функція сну
      """
    def sleep(self):
        print(f"Зараз '{self.name}' дрімає")


if __name__ == '__main__':
    """
        Головна частина де зазначаємо інформацію про котів, та, що полюбляють з їжі
    """
    cats = [
        Cat('Желе', 2, 'мейн-кун', {'сухий корм', 'риба'}),
        Cat('Ківі', 3, 'перс', {'вологий корм', 'молоко'}),
        Cat('Торнадо', 4, 'сіам', {'сухий корм'}),
        Cat('Салямі', 1, 'британський', {'сухий корм', 'недоїдки'}),
        Cat('Вінні', 2, 'болотна рись', {'вологий корм', 'сметана'}),
        Cat('Суфле', 5, 'сфінкс', {'суші', 'лосось'})
    ]

    """
         Зазначаємо рандомну кількість разів прогулянки та їжі
    """
    for cat in cats:
        eat_count = randint(1, 4)
        walk_count = randint(1, 4)

        for _ in range(eat_count):
            cat.perform_action()

        for _ in range(walk_count):
            cat.walk()

        if randint(1, 10) <= 3:
            cat.perform_action()

        cat.sleep()

        if not cat.daily_food:
            print(f"'{cat.name}' голодний")

        print(cat)

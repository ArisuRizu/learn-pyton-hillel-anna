from animals import Dog, Hen, Cow, Cat
from random import choices, randint

if __name__ == '__main__':
    animals = [
        Dog("'Бобик'", 3),
        Hen("'Коко'", 2),
        Cow("'Пельмень'", 5),
        Cat("'Бабай'", 1)
    ]

    animals_in_need_of_veterinarian = []  # Список тварин, які потребують догляду у ветеринара.

    available_food = ['сухий корм', 'вологий корм', 'недоїдки', 'павук', 'сіно', 'траву', "зерно", "пшоно", "кашу", "м'ясо", "кістки", "тортик"]

    what_we_got = []
    what_we_lost = []
    for animal in animals:
        animal.say()

        # Перевірка, чи потрібно тварині до ветеринара
        if not animal.visited_veterinarian:
            animals_in_need_of_veterinarian.append(animal)
            animal.visited_veterinarian = choices([True, False], weights=[0.5, 0.5])[0]

        eaten_food = choices(available_food, k=3)
        for food in eaten_food:
            what_we_lost.append(food)
            animal.eat(food)

        if animal.hungry:
            print(f'{animal} голодний! Швиденько нагодуйте його.')

        what_we_got.append(animal.treat(randint(0, 5)))
        print('=' * 30)

    what_we_lost_unique = list(set(what_we_lost))
    print(f'Сьогодні на фермі витрачено: {", ".join(what_we_lost_unique)}.')

    what_we_got_filtered = [item for item in what_we_got if item]
    if what_we_got_filtered:
        print(f'Отримали: {", ".join(what_we_got_filtered)}.')
    else:
        print(f'Від тварин сьогодні не отримали нічого.')

    print('=' * 30)
    # Виведення тварин, які потребують догляду
    if len(animals_in_need_of_veterinarian) > 0:
        print("Необхідність відвідування ветеринара:")
        for animal in animals_in_need_of_veterinarian:
            if animal.visited_veterinarian:
                print(f"{animal} був у ветеринара")
            else:
                print(f"{animal} потребує огляду ветеринара")
    else:
        print("Всі тварини були у ветеринара")

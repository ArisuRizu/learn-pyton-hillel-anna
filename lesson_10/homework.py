# Програма для створення та сортування нотаток.
notes = []

# Функція зі створення нотатки, в ній ми здійснюємо додавання нотатки, перевірку чи нотатка вже існує.
def add_note():
    while True:
        note = input('Введіть нотатку: ')
        if note in notes:
            print('Ця нотатка вже існує.')
        else:
            notes.append(note)
            print('Нотатка успішно додана!')

        # Запитуємо у користувача чи бажає він ще додати нотатку, а також інформуємо на випадок введення ним некоректної команди.
        choice = input('Бажаєте додати ще нотатку? (так або ні): ').lower()
        while choice not in ['так', 'ні']:
            print('Невідома команда. Спробуйте ще раз.')
            choice = input('Бажаєте додати ще нотатку? (так або ні): ').lower()

        if choice != 'так':
            break

# Функція з сортування нотаток, сортуємо за заданними пораметрами, також перевіряємо чи є взагалі, що сортувати.
def sort_notes(order, num_notes):
    if not notes:
        print('Неможливо сортувати, оскільки Ви не додали жодної нотатки.')
        return

    if order == 'earliest':
        sorted_notes = sorted(notes)
        print('Від найранішої до найпізнішої:')
        print_notes = sorted_notes[:num_notes]
        for note in print_notes:
            print(note)
    elif order == 'latest':
        sorted_notes = sorted(notes, reverse=True)
        print('Від найпізнішої до найранішої:')
        print_notes = sorted_notes[:num_notes]
        for note in print_notes:
            print(note)
    elif order == 'longest':
        sorted_notes = sorted(notes, key=len, reverse=True)
        print('Від найдовшої до найкоротшої:')
        print_notes = sorted_notes[:num_notes]
        for note in print_notes:
            print(note)
    elif order == 'shortest':
        sorted_notes = sorted(notes, key=len)
        print('Від найкоротшої до найдовшої:')
        print_notes = sorted_notes[:num_notes]
        for note in print_notes:
            print(note)

# Функція з вводу даних користувачем.
def user_input():
    while True:
        command = input('\nДоступні команди: \n> add (створити нотатку)\n> sort (сортувати нотатки) \n> exit (вийти з програми) \nЩо бажаєте виконати?\n').lower()

        if command == 'add':
            add_note()

        elif command == 'sort':
            if not notes:
                print('Неможливо сортувати, оскільки Ви не додали жодної нотатки.')
            else:
                print('\nДоступні команди сортування: \n> earliest (від найранішої до найпізнішої) \n> latest (від найпізнішої до найранішої) \n> longest (від найдовшої до найкоротшої) \n> shortest (від найкоротшої до найдовшої)')
                order = input('\nЗа яким критерієм сортувати нотатки? ').lower()
                if order in ['earliest', 'latest', 'longest', 'shortest']:
                    num_notes = int(input('Скільки нотаток ви бажаєте побачити? '))
                    sort_notes(order, num_notes)
                else:
                    print('Невірний критерій сортування. Спробуйте ще раз.')

        elif command == 'exit':
            print('Дякуємо, що скористалися нашою програмою. До нових зустрічей!')
            break

        else:
            print('Невідома команда. Спробуйте ще раз.')


if __name__ == '__main__':
    print('Вас вітає програма для створення та сортування нотаток.')
    user_input()

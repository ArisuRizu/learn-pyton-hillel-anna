# Програма для створення та сортування нотаток.
notes = []
# Задаємо ім'я файлу, в якому будуть зберігатись нотатки.
file_name = 'notes.txt'

# Завантажуємо нотатки зі збереженого файлу, якщо файл існує.
def load_notes(file_name):
    try:
        with open(file_name, 'r') as file:
            notes = [line.strip() for line in file.readlines()]
    except Exception:
        notes = []
    return notes

# Функція для створення нотаток, у випадку коли нотатка створена, запитуэмо чи бажаэ користувач створити ще одну. Якщо выдповыдь ны то повертаэмось до головного меню.
def add_note():
    while True:
        note = input('Введіть нотатку: ')
        if note in notes:
            print('Ця нотатка вже існує.')
        else:
            notes.append(note)
            print('Нотатка успішно додана!')

        choice = input('Бажаєте додати ще нотатку? (так або ні): ').lower()
        while choice not in ['так', 'ні']:
            print('Невідома команда. Спробуйте ще раз.')
            choice = input('Бажаєте додати ще нотатку? (так або ні): ').lower()

        if choice != 'так':
            break

# Функція для сортування нотаток з урахуванням помилки у разы якщо нотаток немає.
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

# Функція що зберігає введені користувачем нотатки.
def save_notes():
    with open(file_name, 'w') as file:
        for note in notes:
            file.write(note + '\n')
    print('Нотатки успішно збережено.')

# Функція діалогу з користувачем.
def user_input():
    while True:
        command = input('\nДоступні команди: \n> add (створити нотатку)\n> sort (сортувати нотатки) \n> save & exit (зберегти та вийти з програми) \nЩо бажаєте виконати?\n').lower()

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

        elif command == 'save & exit':
            save_notes()
            print('Дякуємо, що скористалися нашою програмою. До нових зустрічей!')
            break

        else:
            print('Невідома команда. Спробуйте ще раз.')


if __name__ == '__main__':
    print('Вас вітає програма для створення та сортування нотаток.')
    # Здійснюємо завантаження нотаток зі збереженного файлу.
    notes = load_notes(file_name)
    user_input()
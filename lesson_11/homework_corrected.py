# Функція для завантаження нотаток зі збереженого файлу.
def load_notes(file_name):
    try:
        with open(file_name, 'r') as file:
            notes = [line.strip() for line in file.readlines()]
    except Exception:
        notes = []
    return notes

# Функція для додавання нотатки.
def add_note():
    note = input('Введіть нотатку: ')
    if note in notes:
        print('Ця нотатка вже існує.')
    else:
        notes.append(note)
        print('Нотатка успішно додана!')

# Функція для сортування нотаток за найпізнішою датою.
def sort_latest(num_notes):
    sorted_notes = sorted(notes, reverse=True)
    print('Від найпізнішої до найранішої:')
    print_notes(sorted_notes, num_notes)

# Функція для сортування нотаток за найдовшою довжиною.
def sort_longest(num_notes):
    sorted_notes = sorted(notes, key=len, reverse=True)
    print('Від найдовшої до найкоротшої:')
    print_notes(sorted_notes, num_notes)

# Функція для сортування нотаток за найкоротшою довжиною.
def sort_shortest(num_notes):
    sorted_notes = sorted(notes, key=len)
    print('Від найкоротшої до найдовшої:')
    print_notes(sorted_notes, num_notes)

# Функція для виведення відсортованих нотаток.
def print_notes(notes_list, num_notes):
    print_notes = notes_list[:num_notes]
    for note in print_notes:
        print(note)

# Функція для збереження нотаток у файл.
def save_notes(file_name):
    with open(file_name, 'w') as file:
        for note in notes:
            file.write(note + '\n')
    print('Нотатки успішно збережено.')

# Функція для діалогу з користувачем.
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
                if order == 'earliest':
                    sort_notes(order)
                elif order == 'latest':
                    num_notes = int(input('Скільки нотаток Ви бажаєте побачити? '))
                    sort_latest(num_notes)
                elif order == 'longest':
                    num_notes = int(input('Скільки нотаток Ви бажаєте побачити? '))
                    sort_longest(num_notes)
                elif order == 'shortest':
                    num_notes = int(input('Скільки нотаток Ви бажаєте побачити? '))
                    sort_shortest(num_notes)
                else:
                    print('Невірний критерій сортування. Спробуйте ще раз.')

        elif command == 'save & exit':
            save_notes(file_name)
            print('Дякуємо, що скористалися нашою програмою. До нових зустрічей!')
            break

        else:
            print('Невідома команда. Спробуйте ще раз.')


if __name__ == '__main__':
    print('Вас вітає програма для створення та сортування нотаток.')
    # Задаємо ім'я файлу, в якому будуть зберігатись нотатки.
    file_name = 'notes.txt'
    # Здійснюємо завантаження нотаток зі збереженого файлу.
    notes = load_notes(file_name)
    user_input()

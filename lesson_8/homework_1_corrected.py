# Функція, яка здійснює розрахунок часу на основі введених секунд.
def converter(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    # Словник, який використовується для належного виводу результату конвертування.
    converter_dict = {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

    return converter_dict

# Функція для отримання вводу користувача та конвертування секунд.
def user_input_converter():
    while True:
        user_input = input('Введіть кількість секунд для опрацювання: ')
        try:
            seconds = int(user_input)
            if seconds <= 0:
                print('Нажаль, я не можу конвертувати те, чого не має. Потрібно вводити секунди від 1. Спробуйте ще!')
            else:
                result = converter(seconds)
                print(result)
                print(f'Дякую, що завітали, до нових зустрічей {user_name}!')
                break
        except Exception:
            print('Нажаль, це не число, тому я не можу його сконвертувати. Спробуйте ще!')

if __name__ == '__main__':
    print('Вітаю користувач! Я допоможу Вам конвертувати секунди у дні, години та хвилини.')
    user_name = input("Як Вас звати? ")
    print(f'Супер, {user_name}, починаємо!')
    user_input_converter()



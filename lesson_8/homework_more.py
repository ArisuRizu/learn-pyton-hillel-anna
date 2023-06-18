# Функція, що перевіряє, чи є число простим.
# Так як ми не використовуємо сет з чисел, то через функцію зазначаємо певний алгоритм:
def is_prime(number):
    # Перевіряємо, чи введене число більше 2, якщо менше то введене число не є простим.
    if number < 2:
        return False
    # Перевіряємо, чи введене число має дільник на який ділиться без залишку. Якщо має, то число складене, якщо не має то число є простим.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Функція для отримання вводу користувача та перевірки числа.
def user_input():
    while True:
        try:
            user_input = int(input('Будь ласка, введіть число, яке бажаєте перевірити: '))
            if is_prime(user_input):
                print(f'Число {user_input} є простим.')
            else:
                print(f'Число {user_input} не є простим.')
            break
        except Exception:
            print('Нажаль, ви ввели не число. Спробуйте ще раз.')

# Виклик функції для отримання вводу користувача та перевірки числа.
if __name__ == '__main__':
    print('Вітаю! Це програма, яка перевіряє, чи є введене число простим.')
    user_input()
    print('Дякую за використання нашої програми. Бажаємо успіхів!')

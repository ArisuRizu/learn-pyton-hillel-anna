# Програма для видалення дужок та тексту, що міститься в них зі строки.
# user_input - введені дані від користувача.

print('Вітаю, це програма, що не полюбляє дужки та інформацію в них.')
user_input = input('Для перевірки моєї серйозності можеш написати текст: ')

# Цикл перевіряє чи є у введеному користувачем рядку відкриваюча дужка.
while '(' in user_input:
    start_index = user_input.index('(')
    end_index = user_input.find(')')
# Перевіряємо чи є закриваюча дужчка, якщо вона присутня то виконуємо умову.
    if end_index != -1:
        user_input = user_input[:start_index] + user_input[end_index + 1:]
# Припиняємо цикл у разі якщо не має закриваючої дужки.
    else:
        break

# У разі якщо користувач вводить багато різних дужок то ми їх видаляємо.
user_input = user_input.replace('(', '').replace(')', '')

print(user_input)
print('Так краще!')
# Програма для видалення дужок та тексту, що міститься в них зі строки.
# user_input - введені дані від користувача.

print('Вітаю, це програма, що не полюбляє дужки та інформацію в них.')
user_input = input('Для перевірки моєї серйозності можеш написати текст: ')

# Якщо строка має дужку то ми видаляємо її разом з текстом всередині, цикл повторюється.
while '(' in user_input:
    user_input = user_input[:user_input.index('(')] + user_input[user_input.index(')') + 1:]
    else:
        break

user_input = user_input.replace('(', '').replace(')', '')

print(user_input)
print('Так краще!')
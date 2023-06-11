# Програма, яка перевіряє чи є введена строка паліндромом:
# user_input - введені дані від користувача.

print('Вітаю, це програма, що перевіряє чи є введена строка паліндромом.')
user_input = input('Для перевірки введіть строку та натисніть Enter: ')

# Переводимо в нижній регістр, позбавляємо пробілів, табуляцій, переносів на нову строку та розділових знаків.
user_input = user_input.lower().replace(' ', '').replace('\t', '').replace('\n', '').replace(',', '').replace('.', '').replace('?', '').replace('-', '').replace('!', '')

if user_input == user_input[::-1]:
    print('Вказана строка є паліндромом!')
    print('Дякую за користування, приходьте ще!')
else:
    print('Вказана строка не є паліндромом!')
    print('Дякую за користування, приходьте ще!')
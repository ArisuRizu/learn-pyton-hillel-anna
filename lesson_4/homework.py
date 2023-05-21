#user_name - ім'я користувача програми

user_name = input('Приємно бачити нові обличчя серед користувачів! Як тебе звати? ')
print('Для запуску БОТа привітайтесь будь-ласка,', user_name)

#user_answer - відповідь, що надає користувач

while True:
    user_answer = input()
    if 'хай' in user_answer.lower() or 'привіт' in user_answer.lower() or 'доброго дня' in user_answer.lower():
        print('Доброго вечора, я бот з України!')
    elif 'як справи' in user_answer.lower() or 'що робиш' in user_answer.lower() or 'чим займаєшся' in user_answer.lower():
        print('Вчусь програмувати на Python! А ти чим займаєшся?')
    elif 'фільм' in user_answer.lower() or 'кінотеатр' in user_answer.lower() or 'серіал' in user_answer.lower():
        print("Вибачаюсь, що втручаюсь, я не знаю про що йдеться мова, але раджу до перегляду фільм Джон Уік 4, він просто бомба!")
    elif 'бувай' in user_answer.lower() or 'надобраніч' in user_answer.lower() or 'гудбай' in user_answer.lower() or 'до зустрічі' in user_answer.lower():
        print('I\'ll be back, так, що до зустрічі в мережі', user_name, '!')
        break
    else:
        print('Що?Що? Не розумію :(')
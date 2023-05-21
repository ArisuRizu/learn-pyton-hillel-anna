#user_name - ім'я користувача програми

user_name = input('Приємно бачити нові обличчя серед користувачів! Як тебе звати? ')
print('Для запуску БОТа привітайтесь будь-ласка,', user_name)

#user_answer - відповідь, що надає користувач

while True:
    user_answer = input().lower()
    if 'хай' in user_answer or 'привіт' in user_answer or 'доброго дня' in user_answer:
        print('Доброго вечора, я бот з України!')
    elif 'як справи' in user_answer or 'що робиш' in user_answer or 'чим займаєшся' in user_answer:
        print('Вчусь програмувати на Python! А ти чим займаєшся?')
    elif 'фільм' in user_answer or 'кінотеатр' in user_answer or 'серіал' in user_answer:
        print("Вибачаюсь, що втручаюсь, я не знаю про що йдеться мова, але раджу до перегляду фільм Джон Уік 4, він просто бомба!")
    elif 'бувай' in user_answer or 'надобраніч' in user_answer or 'гудбай' in user_answer or 'до зустрічі' in user_answer:
        print('I\'ll be back, так, що до зустрічі в мережі', user_name, '!')
        break
    else:
        print("Що?Що? Не розумію :(")
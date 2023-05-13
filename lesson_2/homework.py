import math
# Програма, яка конвертує градуси у радіани.
# degrees - градуси
# radian - радіан

input('Вас вітає програма яка конвертує градуси у радіани, для продовження натисніть Enter')
degrees = float(input('Введіть градуси для конвертації у радіани: '))

print("Радіан становить: ")
radian = round((degrees * math.pi / 180), 5)
print(radian)



# Програма, що рахує абонплату за комунальним лічильника електроенергії.
# current_indicator - поточні показники лічильника
# previous_indicator - попередні показники лічильника
# rate - тариф
# subscription - абонплата

input('Вас вітає програма для розрахунку абонплати за комунальним лічильником електроенергії, для продовження натисніть Enter')
current_indicator = float(input('Введіть поточні показники комунального лічильника: '))
previous_indicator = float(input('Введіть попередні показники комунального лічильника: '))
rate = float(input('Введіть тариф: '))

print("Ваша абонплата становить: ")
subscription = round(((current_indicator - previous_indicator) * rate), 2)
print(subscription)



# Програма, що рахує податок від надхождення прибутку на рахунок підприємця.
# size_income - розмір надходження
# tax_percent - відсоток податка
# tax - налог
# income - прибуток

input('Вас вітає програма для розрахунку податку від надхождення прибутку на рахунок підприємця, для продовження натисніть Enter')
size_income = float(input('Введіть розмір надходження: '))
tax_percent = float(input('Введіть відсоток податка: '))

print("Потрібно сплатити податку: ")
tax = round((size_income / 100 * tax_percent), 2)
print(tax)
print("Чистий прибуток становить: ")
income = round((size_income - (size_income / 100 * tax_percent)), 2)
print(income)



# Програма, що рахує витрати на паливо.
# fuel_consumption - витрачання палива за 100км
# price - ціна за 1 літр палива
# distance - відстань в км
# consumption - витрачання палива за 1 км
# money_distance - вартість пального на визначену кількість км

input('Вас вітає програма для розрахунку витрат пального на визначену відстань в км, для продовження натисніть Enter')
fuel_consumption = float(input('Введіть дані щодо витрат пального автомобілем на 100 км: '))
price = float(input('Введіть нинішню вартість за 1 л пального: '))
distance = float(input('Введіть відстань в км яку необхідно проїхати: '))

print("Вартість пального на вказану відстань становить: ")
consumption = round(fuel_consumption / 100 * distance)
money_distance = round((consumption * price), 2)
print(money_distance)


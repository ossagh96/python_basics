# 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

a = 'Номер урока:'
b = 1
print(a,b)

b = input('Введите номер урока:')
print(a,b)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input('Введите время в секундах:'))
minutes = seconds / 60
hours = int(minutes / 60)
minutes = int(minutes % 60)
seconds = int(seconds % 60)
print(hours,':',minutes,':',seconds)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

a = input('Введите число:')
b = int(a+a)
c = int(a+a+a)
a = int(a)
print(a+b+c)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

a = abs(int(input('Введите целое, положительное число:')))
number = 0
numbers_list = []
while a >= 1:
    number = a % 10
    a = a // 10
    numbers_list.append(number)

print(max(numbers_list))

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
revenue = int(input('Выручка за период:'))
cost = int(input('Выручка за период:'))

gross_margin = revenue - cost

if revenue >= cost:
    print(f'Фирма прибыльна: прибыль = {gross_margin}')
else:
    print(f'Фирма убыточна: убыток = {gross_margin}')

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
gross_margin_percent = gross_margin / revenue

if revenue >= cost:
    print(f'Рентабельность = {gross_margin_percent}')
else:
    print('Фирма не рентабельна')

# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Результат в первый день:'))
b = int(input('Желаемый результат:'))

days = 1
while a <= b:
    a = a * 1.1
    days += 1

print(f'Желаемый результат будет достигнут на день {days}')
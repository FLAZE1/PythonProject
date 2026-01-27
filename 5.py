# ? составные выражения / (and,or)

# * И (and)
# age=25
# balance=1000
# if age>=18 and balance>500:
#     print('Покупка разрешена')
# else:
#     print('Недостаточно средств или мал возвраст')
#
# # * или (or)
# day == 'Sunday'
# if day=='Sunday' or day=='Saturday':
#     print('Выходной')
# else:
#     print('Работа')
#
# # * не (not)
# is_banned=False
# if not is_bannes:
#     print('Доступ разрешен')
# else:
#     print('Доступ разрешен')

# ! Порядок выполнения действий
# * ()
# * not
# * and
# * or

# ? вложенные конструкции
'''
username ='admin'
password='1234'
if username == 'admin':
    print('Логин найден')
    if password == '1234':
        print('Верно')
    else:
        print('Не верно')
else:
    print('Логин не верный')
'''
#1
'''
a=int(input())
if 9<=a<=21:
    print('Магазин открыт')
else:
    print('Магазин закрыт')
'''
#2
'''
a=(input('Есть ли дисконтная карта'))
b=int(input('Введите сумму'))
if a=='да' or 'Да' or 'ДА' and b>5000:
    print('Для вас скидка')
else:
    print('Скидки нет')
'''
#3
a=123
b=int(input('Введите пин-код'))
if b==a:
    c=int(input('Сколько хотите снять'))
    if c>10000:
        print('В банкомате столько нету')
    else:
        print('успешно')
else:
    print('Пин-код неверный')



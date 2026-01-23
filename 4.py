# # ? boolean / bool / логический тип данных
# my_bool_1=True
# my_bool_2=False
# print(my_bool_1,my_bool_2)
#
# # ? логические операторы
# print(5>3)
# print(5>=3)
# print(5<3)
# print(5<=3)
# print(5==3)
# print(5!=3)
#
# # ? условные операторы /if-elif-else
# # * 1. if (если)
# num=10
# if num >10:
#     print('Число положительное')
#
# # * 2. if-else
# age=12
# if age>=12:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')
#
# # * 2. if-elif-else
# color='yellow'
# if color=='green':
#     print('едем')
# elif color=='yellow':
#     print('ждем')
# elif color=='red':
#     print('стой')
# else:
#     print('не работает')
#
# #1
# a=int(input())
# if a>0:
#     print('+')
# else:
#     print('-')
#
# #2
# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# else:
#     print(b)
#
# #3
# a=int(input())
# if a%2==0:
#     print('Четное')
# else:
#     print('Нечетное')
#
# #4
# a=int(input())
# if a%10==0:
#     print('Оканчивается на 0')
# else:
#     print('другое')
#
# #5
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b+c and b<c+a and c<a+b:
#     print('Можно')
# else:
#     print('Нет')

# #6
# score=90
# if score>=90:
#     print('Отлично')
# elif 70<=score<=89:
#     print('Хорошо')
# elif 50<=score<=69:
#     print('удовлетворительно')
# else:
#     print('не сдал')

#7
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a<=n<=a+b or a+b+c<=n<=a+c+d+b:
    print('да')
else:
    print('нет')
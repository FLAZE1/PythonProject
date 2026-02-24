# ? break, continue and else в циклах (for else/while else)

# * 1. break - полностью прерывает цикл
# while True:
#     num = int(input('Введите число (0 - выход)'))
#     if num == 0:
#         print('Выход из цикла')
#         break
#     print(f'Вы ввели {num}')

# for i in range(3):
#     code = int(input())
#     if code == 1234:
#         print('Код верный')
#         break
#     print('Код неверный')

# * continue - пропускает текущую итерацию
# for i in range(7):
#     if i % 2 != 0:
#         continue
#     print(i ** i)
#     print(f'Число {i}')

# * конструкция while else - выполнится, если не было break

# i=0
# while i<5:
#     print(i)
#     i += 1
# else:
#     print('Цикл завершился')

# * for else - выполнится, если не было break
# for i in range(5):
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print('Цикл завершился')
# num=6
# for i in range(10):
#     if i==5:
#         continue
#     elif i>40:
#         break
#     print(i * num)
#     print(f'Число {i}')

#2

a=int(input())
for i in range(2,a):
    if a%i==0:
        break
else:
    print(a,'Число простое')













#1
'''
a=0
while a != 10:
    a+=1
    print(a)
'''

# ? while
# цикл работает пока условие истинно
# while True:
#     print('hello')

# * счетчик
'''
i=0
while i<5:
    print(i)
    i+=1

i=5
while i<10:
    print(i)
    i+=2
'''
# * пример
'''
num=int(input('Введите стоимость товара,0 завершить'))
total=0
while num!=0:
    total += num
    print('Итого',total)
    num=int(input('Введите стоимость товара,0 завершить'))
'''

#2
'''
a=1

while a<=19:
    print(a)
    a+=2
'''

#3
'''
a=0
total=0

while a<=50:
    total+=a
    a+=1
print(total)
'''

#4
'''
total=0
while True:
    a=int(input())
    if a =='стоп':
        break
    total+=a
print(total)
'''

#5


from math import*
# * модуль
# x=-42.42
# abs_x=abs(x)
# print(f'Было {x} стало {abs_x}')

# * Импорт модулей
# ? import math
# print(math.pi)
# print(math.ceil(4.2))
# print(math.floor(4.9))

# from math import pi, ceil, floor
# print(pi)
# print(ceil(4.2))
# print(floor(4.9))

# from math import*
# print(pi)
# print(ceil(4.2))
# print(floor(4.9))

# import math as m
# print(m.pi)
# print(m.ceil(4.2))
# print(m.floor(4.9))

#from math import ceil as c ,floor as f
# print(c(4.2))
# print(f(4.9))

# from math import *
# print(ceil(4.2)) #округление вверх
# print(floor(4.9)) #округление вниз

# print(2**5)

# print(log2(32))
# print(log(x:32, base:2)) #логарифм с универсальным основанием

from random import *
r = randint(1,6)

#Хартли
# N=50
# i=ceil(log2(50))
# print(i)

# N=129
# i=ceil(log2(129))
# print(i)

#2 обьем сообщения
# i=5
# L=517
# I=L * i /8
# print(ceil(I))

#найти I в байтах
# N=80
# L=100
# i=ceil(log(N))
# I=ceil(i*L / 8)
# print(I)

# L=317
# N=4090+10
# i=ceil(log2(N))
# I=ceil(L * i /8)
# n=262144
# V=(I*n)/(2**20)
# print(I)
# print(V)

L=5
N=7084+10
i=ceil(log2(N))
I=ceil(L * i /8)
n=22528
V=(I*n)/(2**10)
print(I)
print(V)
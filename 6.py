# ? цикл for
# * 1 перебор чисел range
# for i in range(5): #0 1 2 3 4
#     print(f'Итерация:{i}')
#
# # * 2 от и до
# for i in range(5,10): # 5 6 7 8 9
#     print(f"Интопритация: {i}")
#
# # * 3 через
# for i in range(5, 10,2): # i = 5 7 9
#     print(f"Итерация: {i}")

# #1
# for i in range(10,0,-1):
#     print(i)

# #2
# a=int(input())
# for i in range(1,11):
#     print(a*i)

# #3
# n=int(input())
# for i in range(0,n+1,2):
#     print(i)

# #4
# total=0
# n=int(input())
# for i in range(1,n):
#     total+=i
# print(total)

#1
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b%6==0 and b%10==4:
        s=b+s
print(s)
'''
from pkgutil import resolve_name

#2

'''
a=int(input())
maxi=0
for i in range(a):
    b=int(input())
    if b%5==0 and b>maxi:
        maxi=b
print(maxi)
'''

#16
'''
a=int(input())
s=0
d=0
for i in range(a):
    b=int(input())
    if b>10:
        d+=b
        s+=1
print(d/s)
print(s)
'''
#17
'''
a=int(input())
s=0
d=0
for i in range(a):
    b=int(input())
    if 13<=b<=20:
        d+=b
        s+=1
print(d/s)
print(s)
'''
#18
'''
a=int(input())
s=0
d=0
for i in range(a):
    b=int(input())
    if 10<=b<=15:
        d+=b
        s+=1
print(d/s)
print(s)
'''

#19
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b<30 and b%2==0:
        s+=b
print(s)
'''
#20
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b<=25 and b%10!=3:
        s+=b
print(s)
'''
#21
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b%221 < 7:
        s+=1
print(s)
'''

#22
'''
a=int(input())
min=30001
for i in range(a):
    b=int(input())
    if b%112 < 9 and b<min:
        min=b
print(min)
'''

#23
'''
a=int(input())
max=0
for i in range(a):
    b=int(input())
    if b%112 == 4 and b>max:
        max=b
print(max)
'''

#24
'''
a=int(input())
min=30001
for i in range(a):
    b=int(input())
    if b>150 and b<min:
        min=b
print(min)
'''

#25
'''
a=int(input())
max=0
for i in range(a):
    b=int(input())
    if b<150 and b>max:
        max=b
print(max)
'''
#16
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if 99>=b>9 and b<29:
        s+=b
print(s)
'''
#16
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if 99>=b>9 and b%10!=b//10:
        s+=1
print(s)
'''

#16
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if 99>=b>9 and b%10==b//10:
        s+=1
print(s)
'''

#16
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if 99>=b>9 and b%10<b//10:
        s+=1
print(s)
'''

#1
'''
a=int(input())
maxi=0
for i in range(a):
    b=int(input())
    if b%5==0 and b>maxi:
        maxi=b
print(maxi)
'''

#2
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b%6==0:
        s+=b
print(s)
'''

#3
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b%4==0:
        s+=1
print(s)
'''

#4
'''
a=int(input())
mini=30001
for i in range(a):
    b=int(input())
    if b%3==0 and b<mini:
        mini=b
print(mini)
'''

#5
# a=int(input())
# s=0
# for i in range(a):
#     b=int(input())
#     if b%10==4:
#         s+=b
# print

# a=int(input())
# s=0
# for i in range(a):
#     b=int(input())
#     if b%2==0 and b<30:
#         s+=b
# print(s)

# m = [
#     [8,10],
#     [11,8],
#     [17,1],
#     [2,32],
#     [-5,25],
#     [13,-13],
#     [15,11],
#     [3.-15],
#     [4,24]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         x=k[0]
#         y=k[1]
#         if x > 12 or y >=A:
#             i+=1
#
#        if i==6:
#            print(A)

# m = [
#     [-8,11],
#     [1,-20],
#     [1,-25],
#     [4,-37],
#     [7,46],
#     [30,-14],
#     [30,-4],
#     [30,15],
#     [80,-30],
#     [80,-3]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         s=k[0]
#         t=k[1]
#         if s>=A and t<1:
#             i+=1
#     if i==5:
#         print(A)


# m=[
#     [6,8],
#     [3,5],
#     [-7,2],
#     [7,7],
#     [9,8],
#     [-1,3],
#     [-4,5],
#     [6,9],
#     [2,-1]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         x=k[0]
#         y=k[1]
#         if x>=7 and y>A:
#             i+=1
#     if i==2:
#         print(A)

# m=[
#     [6,8],
#     [3,5],
#     [-7,2],
#     [7,7],
#     [9,8],
#     [-1,3],
#     [-4,5],
#     [6,9],
#     [2,-1]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         x=k[0]
#         y=k[1]
#         if x > y and y > 0 and x>A:
#             i+=1
#     if i==0:
#         print(A)


# m=[
#     [5,4,6],
#     [2,1,0],
#     [3,-2,4],
#     [0,6,3],
#     [9,6,6],
#     [11,9,2],
#     [3,1,3],
#     [6,6,6],
#     [20,19,19],
#     [3,6,0]
# ]
#
# for k in m:
#     a=k[0]
#     b=k[1]
#     c=k[2]
#     if (a>b and b>5) or (c>4):
#         print('Да')
#     else:
#         print('НЕТ')

# m=[
#     [1,2],
#     [11,2],
#     [1,12],
#     [11,12],
#     [-11,-12],
#     [-11,12],
#     [-12,11],
#     [10,10],
#     [10,5]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         s=k[0]
#         t=k[1]
#         if s>10 or t>A:
#             i+=1
#     if i==7:
#         print(A)

# m=[
#     [1,2],
#     [11,2],
#     [1,12],
#     [11,12],
#     [-11,-12],
#     [-11,12],
#     [-12,11],
#     [10,10],
#     [10,5]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         s=k[0]
#         t=k[1]
#         if s>10 or t>A:
#             i+=1
#     if i==3:
#         print(A)


# m=[
#     [1,2],
#     [11,2],
#     [1,12],
#     [11,12],
#     [-11,-12],
#     [-11,12],
#     [-12,11],
#     [10,10],
#     [10,5]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         s=k[0]
#         t=k[1]
#         if s>10 or t>A:
#             i+=1
#     if i==3:
#         print(A)


# m=[
#     [-9,11],
#     [2,7],
#     [5,12],
#     [2,-2],
#     [7,-9],
#     [12,6],
#     [9,-1],
#     [7,11],
#     [11,-5]
# ]
#
# for A in range(0,100):
#     i=0
#     for k in m:
#         s=k[0]
#         t=k[1]
#         if s>A or t>11:
#             i+=1
#     if i==3:
#         print(A)

# s=int(input())
# t=int(input())
#
# if s % 7 == t:
#     print('YES')
# else:
#     print('NO')

m=[
    [1,2],
    [11,2],
    [1,12],
    [11,12],
    [-11,-12],
    [-11,12],
    [-12,11],
    [10,10],
    [10,5]
]

for A in range(0,100):
    i=0
    for k in m:
        s=k[0]
        t=k[1]
        if s>10 or t>A:
            i+=1
    if i==6:
        print(A)
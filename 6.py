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

a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b%2==0 and b<30:
        s+=b
print(s)
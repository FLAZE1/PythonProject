# Напишите программу подсчёта суммы цифр в записи натурального числа.
# На вход программе подаётся натуральное число. Программа должна напечатать только одно число - сумму цифр
#1
'''
n = int(input())
s = 0
while n > 0:
    k = n % 10
    if k % 3 ==0:
        s+=1
    n=n//10
print(s)
'''
#2
'''
n=int(input())
s = 0
while n>0:
    k = n % 10
    if k % 4 == 0:
        s += 1
    n = n // 10
print(s)
'''

#3
'''
s=0
n = int(input())
while n==0:
    if n % 6 == 0 and n % 10 == 4:
        s += n
print(s)
'''

#4
'''
s=0
n = int(input())
while n!=0:
    if n % 4 == 0 or n % 9 == 0:
        s += n
    n = int(input())
print(s)
'''

#5
'''
n=int(input())
s = 0
while n > 0:
    k = n % 10
    if k % 4 != 0:
        s += k
    n = n // 10
print(s)
'''

#6
'''
n=int(input())
s=0
while n > 0:
    k = n % 10
    if k % 3 != 0:
        s += k
    n= n // 10
print(s)
'''

#7
'''
n=int(input())
s=0
while n > 0:
    k = n % 10
    if k > 7:
        s += k
    n= n // 10
print(s)
'''

#8
'''
s=0
n = int(input())
while n!=0:
    if 100<=n<=999 and n % 4 == 0:
        s += n
    n = int(input())
print(s)
'''

#9
'''
n=int(input())
s=0
while n > 0:
    k = n % 10
    if k <= 6:
        s += k
    n = n // 10
print(s)
'''

#10
'''
n=int(input())
mini=9
while n > 0:
    k = n % 10
    if k<mini:
        mini = k
    n = n // 10
print(mini)
'''

#11
'''
n = int(input())
maxi = 0
while n > 0:
    k = n % 10
    if k > maxi:
        maxi = k
    n = n // 10
print(maxi)
'''

# s=0
# a=0
# n=int(input())
# for i in range(n):
#     b=int(input())
#     s+=b
#     if b > 0:
#         a +=1
# print(s/n)
#
# if a >= 5:
#     print('YES')
# else:
#     print('NO')

# s=0
# n = int(input())
# while n!=0:
#     if n%4==0 and n % 10 == 6:
#         s += n
#     n = int(input())
# print(s)

s=0
a=30000
while True:
    n=int(input())
    if n == 0:
        break

    if n>s:
        s=n
        s+=n
    elif n<a:
        a=n
        a+=n
print(s)
print(a)
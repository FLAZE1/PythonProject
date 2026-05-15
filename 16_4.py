'''
Напишите программу подсчёта суммы элементов последовательности натуральных чисел, запись
которых в 11-ричной системе счисления оканчивается на цифру 4. В ответе запишите только сумму.
На вход программе сначала подаётся количество элементов последовательности N (1 <= N <= 1000)
затем каждый элемент последовательности в отдельной строке. Программа должна напечатать только
одно число записанную в десятичной системе счисления. искомую сумму элементов,
5 15 13 26 41 19 -> 41
'''

'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if num % 11 == 4:
        num_sum += num
print(num_sum)
'''

'''
Напишите программу подсчёта суммы элементов последовательности натуральных чисел, запись которых в 5-ричной системе счисления оканчивается на 11. 
В ответе запишите только сумму. На вход программе сначала подаётся количество элементов последовательности N (1 <= N <= 1000) затем каждый элемент 
последовательности в отдельной строке. Программа должна напечатать только одно число записанную в десятичной системе счисления. искомую сумму элементов,
4 131 31 27 162 -> 162
'''

'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if num % 25 == 6:
        num_sum += num
print(num_sum)
'''
#9
'''
a=int(input())
s=0
for i in range(a):
    b=int(input())
    if b % 6 == 0 and b % 10 == 4:
        s+=b
print(s)
'''
#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if num % 27 == 16:
        num_sum += num
print(num_sum)
'''
#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if num % 9 == 5:
        num_sum += num
print(num_sum)
'''
#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if num % 12 == 7:
        num_sum += num
print(num_sum)
'''

#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if (num // 8)%8  == 3:
        num_sum += num
print(num_sum)
'''

#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if (num // 7)%7  ==2:
        num_sum += num
print(num_sum)
'''
#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if (num // 4)%4  == 3:
        num_sum += num
print(num_sum)
'''
#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if (num // 3)%3  == 1:
        num_sum += num
print(num_sum)
'''

#42
'''
count = int(input())
num_sum = 0
s=0
for i in range(count):
    num = int(input())
    if num % 7 == 5:
        num_sum += 1
        s+=num
if num_sum>0:
    print(s//num_sum)
else:
    print('NO')
'''

#16
'''
count = int(input())
num_sum = 0
for i in range(count):
    num = int(input())
    if num % 49 == 15:
        num_sum += num
print(num_sum)
'''

#16
# count = int(input())
# num_sum = 0
# for i in range(count):
#     num = int(input())
#     if num % 64 == 26:
#         num_sum += num
# print(num_sum)


# n=int(input())
#
# s=0
#
# for i in range(n):
#     b=int(input())
#     if b%10==3:
#         s+=1
# print(s)

# n=int(input())
#
# s=0
#
# for i in range(n):
#     b=int(input())
#     if b%10==4 and b%6==0:
#         s+=1
# print(s)


# n=int(input())
#
# maxi=0
# mini=30000
# for i in range(n):
#     b=int(input())
#     if b>maxi:
#         maxi=b
#     if b<mini:
#         mini=b
# if mini<30:
#     print(maxi)
#     print('YES')
# else:
#     print(maxi)
#     print('NO')

#1
# n=int(input())
#
# s=0
# b=0
#
# for i in range(n):
#     a=int(input())
#     if a>=8:
#         s+=1
#         b+=a
# print(s)
# print(b/s)

#2

# a=1
# s=0
# f=0
#
# while a!=0:
#     a=int(input())
#     if a % 10 ==1:
#         s+=a
#         f+=1
# if f>0:
#     print(s/f)
# else:
#     print('NO')

#3


# s=0
#
# while True:
#     a=int(input())
#     if a==0:
#         break
#     if a % 4 == 0 and a % 10 == 0:
#         s+=1
# print(s)

#4
#
# a=int(input())
# b=int(input())
# s=0
#
# for i in range(a,b+1):
#     if i % 2 == 0:
#         s+=1
# print(s)


# a=int(input())
#
# maxi=0
#
# for i in range(a):
#     b=int(input())
#     if b%10==3 and b>maxi:
#         maxi=b
# print(maxi)

# a=int(input())
#
# mini=30000
#
# for i in range(a):
#     b=int(input())
#     if b%3==0 and b<mini:
#         mini=b
# print(mini)
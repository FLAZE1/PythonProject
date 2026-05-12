# a = [23,56,45]
# a.append(34)
# a.sort()
# print(a)

# l=[]
# num = int (input())
# total_min=0
# total_max=0
# while num != 0:
#     l.append(num)
#     num = int(input())
# l.sort()
# total_min = l[0] + l[1]
# total_max = l[-1] + l[-2]
#
# print(total_max)
# print(total_min)

# s=0
# n = int(input())
# while n!=0:
#     if n%7==0 or n % 10 == 7 and 9<n<100:
#         s += 1
#     n = int(input())
# print(s)

# n = int(input())
# s=0
# b=0
# for i in range(n):
#     a=int(input())
#     s += a
#     if a > 80:
#         b += 1
# if b >= 3:
#     print(s/n)
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# s=0
# f=0
# for i in range(n):
#     b=int(input())
#     if b % 13 == 0 or b % 20 == 0:
#         s+=b
#         f += 1
# print(f)
# print(s)


# num = int(input())
# l = []
# w=0
# for i in range(4):
#     s=int(input())
#     if s<=30:
#         l.append(s)
#
# l.sort()
# print(l[0])
# print(l[-1])

# n = int(input())
#
# s=0
#
# l=18*60+30
#
# for i in range(n):
#     m=int(input()).split()
#     r=m*60+m
#     if r <= l:
#         s+=1
# print(s)
s=input().split()
print(int(s[0]),int(s[1]))
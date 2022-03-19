# code _up 파이썬 기초 문제 100선 

# #basic output
#6001
print('Hello')
#6002
print('Hello World')
#6003
print('Hello')
print('World')
#6004
print("'Hello'")
#6005
print('''"Hello World"''')
#6006
print('"!@#$%^&*()\'')
#6007
print('''"C:\\Download\\\'hello'.py"''')
#6008
print('''print("Hello\\nWorld")''')

# #basic input
#6009
print(input())
#6010 #print(input())
print(int(input()))

#6011 #print(input())
print(float(input()))
#6012
a = int(input())
b = int(input())
print(a)
print(b)

# #6013
# a = input()
# b = input()
# print('{b}\n{a}'.format(b=b, a=a))
# #6014
# a = float(input())
# for i in range(3):
#     print(a)

# #6015
# a, b = input().split()
# print('{}\n{}'.format(int(a), int(b)))
# #6016
# a, b = input().split()
# print('{} {}'.format(b, a))

# #6017
# s = input()
# print(s,s,s)
# #6018
# print(time[0]+':'+time[1])

# #6019
# date = input().split('.')
# date.reverse()
# print('-'.join(date))
# #6020
# print(''.join(input().split('-')))

# #6021
# s = input()
# for i in s:
#     print(i)
# #6022
# date = input()
# print(date[:2] + ' ' + date[2:4] + ' ' + date[4:])

# #6023
# date = input().split(':')
# print(date[1])
# #6024
# a, b = input().split()
# s = a + b
# print(s)

# #6025
# a, b = input().split()
# print('{}'.format(int(a)+int(b)))
# #6026
# a = float(input())
# b = float(input())
# print('{}'.format(a + b))

#6027
print('%x'%int(input()))
#6028
print('%x'.upper()%int(input()))

#6029
print('%o'%int(input(), 16))
#6030
print(ord(input()))

#6031
print(chr(int(input())))

#########################################
# 정수 입력받기
n = int(input())
# 실수 입력받기
n = float(input())
##########################################

#6032
print(-int(input()))
#6033
print(chr(ord(input())+1))
#6034
a, b = input().split()
print(int(a) - int(b))

#6035
a, b = input().split()
print(float(a) * float(b))
#6036
s = input().split()
for i in range(int(s[1])):
    print(s[0], end='')
# s = input().split()
# print(s[0] * int(s[1]))

#6037
count = int(input())
s = input()
print(s * count)
#6038
a, b = input().split()
print(int(a) ** int(b))


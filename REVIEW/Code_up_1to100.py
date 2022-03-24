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

#6039
a, b = input().split()
print(float(a) ** float(b))
#6040
a, b = input().split()
print(int(a) // int(b))

#6041
a, b = input().split()
print(int(a) % int(b))
#6042
print(round(float(input()), 2))

#6043
a, b = map(float, input().split())
print('%.3f' %round((a / b), 3))
#6044
a, b = input().split()
a = int(a)
b = int(b)
if(a >= 0 and b != 0):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(round((a / b), 2))

#6045
# print(a + b + c, round((a + b + c / 3), 2))
# 위 코드와 같이 작성할 경우 a + b + c / 3 부분에서 2.0값이 아닌 3.0값이 나오게 된다.
# 이 이유는 a + b + c / 3은 연산자 우선순위에 의해 a + b + (c / 3) = 1 + 2 + (3/3) = 3.0이라는 결과가 나오게 된다.
# 따라서 괄호를 적절히 사용하여 연산 우선순위를 맞춰 계산한 (a + b + c) / 3 = (1 + 2 + 3) / 3 = 2.0으로 예상한 값이 나오게 된다.
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c, round(((a + b + c) / 3), 2))

#6046
print(int(input())<<1)
#6047
a, b = map(int, input().split())
print(a * (2 ** b))

#6048
a, b = map(int, input().split())
print(a < b)
#6049
a, b = map(int, input().split())
print(a == b)

#6050
a, b = map(int, input().split())
print(a <= b)

#6051
a, b = map(int, input().split())
print(a != b)

#6052
print(bool(int(input())))

#6053
print(not bool(int(input())))

#6054
a, b = map(int, input().split())
print(bool(a) and bool(b))
#6055
a, b = map(int, input().split())
print(bool(a) or bool(b))

#6056
a, b = map(int, input().split())
if (bool(a) != bool(b)):
    print(True)
else:
    print(False)

#6057
a, b = map(int, input().split())
if (bool(a) == bool(b)):
    print(True)
else:
    print(False)

#6058
a, b = map(int, input().split())
print(bool(a) is False and bool(b) is False)
#6059
print(~int(input()))

#6060
a, b = map(int, input().split())
print(a & b)
#6061
a, b = map(int, input().split())
print(a | b)

#6062
a, b = map(int, input().split())
print(a ^ b)
#6063
a, b = map(int, input().split())
print(a if a > b else b)

#6064
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)

#6065
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print(int(i))

#6066
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print('even')
    else:
        print('odd')

#6067
data = int(input())
if(data % 2 == 0 and data < 0):
    print('A')
elif(data % 2 != 0 and data < 0):
    print('B')
elif(data % 2 == 0 and data > 0):
    print('C')
elif(data % 2 != 0 and data > 0):
    print('D')

#6068
score = int(input())
if(score >= 90):
    print('A')
elif(score >= 70):
    print('B')
elif(score >= 40):
    print('C')
elif(score >= 0):
    print('D')

#6069
grade = input()
if(grade == 'A'):
    print('best!!!')
elif(grade == 'B'):
    print('good!!')
elif(grade == 'C'):
    print('run!')
elif(grade == 'D'):
    print('slowly~')
else:
    print('what?')

#6070
month = int(input())
season = ''
if(month in [12, 1, 2]):
    season = 'winter'
elif(month in [3, 4, 5]):
    season = 'spring'
elif(month in [6, 7, 8]):
    season = 'summer'
else:
    season = 'fall'
print(season)

#6071
i = True
while(i):
    num = int(input())
    if(num == 0):
        i = False
    else:
        print(num)
#6072
num = int(input())
while(num > 0):
    print(num)
    num -= 1

#6073
num = int(input())
while(num > 0):
    num -= 1
    print(num)
#6074
a = input()
count = 0
while(count <= ord(a)-97):
    print(chr(97+count), end=' ')
    count += 1
#6075
n = int(input())
for i in range(n + 1):
    print(i)
#6076
n = int(input())
for i in range(n + 1):
    print(i)

#6077
n = int(input())
s = 0
for i in range(n + 1):
    if(i % 2 == 0):
        s += i
print(s)
#6078
c = ''
while(c != 'q'):
    c = input()
    print(c)


#6079
n = int(input())
i = 0
s = 0
while(s < n):
	i += 1
	s += i
print(i)
#6080
n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print('{} {}'.format(i, j))

#6081
n = input()
for i in range(1, 15 + 1):
	print('%x*%x=%x'.upper() %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))
#6082
n = int(input())
for i in range(1, n + 1):
    if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print('X', end = ' ')
    else:
        print(i, end = ' ')

#6083
a, b, c = map(int, input().split())
count = 0
for i in range(a):
	for j in range(b):
		for k in range(c):
			print('{} {} {}'.format(i, j, k))
			count += 1
print(count)
#6084
h, b, c, s = map(int, input().split())
mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
print('{} MB'.format(mb))
#6085
w, h, b = map(int, input().split())
mb = round(((w*h*b) / 8 / 1024 / 1024), 2)
print('{:.2f} MB'.format(mb))


#6086
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
    if(total >= n):
        break
print(total)
#6087
n = int(input())
for i in range(1, n + 1):
    if(i % 3 == 0):
        pass
    else:
        print(i)
#6088
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total += b
print(total)

#6089
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total *= b
print(total)
#6090
a, m, d, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total = total * m + d
print(total)

#6091
a, b, c = map(int, input().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)
#6092
from random import randint
n = int(input())
temp = [0] * 23
nums = input().split()
for i in nums:
    temp[int(i)-1] += 1
for i in temp:
    print(i, end=' ')

#6093
n = int(input())
nums = input().split()
nums.reverse()
for i in nums:
    print(int(i), end=' ')
#6094
n = int(input())
nums = map(int, input().split())
print(min(nums))

#6095
li = [[0 for i in range(19)] for j in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if(li[x-1][y-1] != 1):
        li[x-1][y-1] = 1
for i in li:
	print(' '.join(map(str, i)))
#6096
li = []
for i in range(19):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(19):
        li[a-1][j] = 1 if li[a-1][j] != 1 else 0
        li[j][b-1] = 1 if li[j][b-1] != 1 else 0
for i in li:
    print(' '.join(map(str, i)))

#6097
li = []
h, w = map(int, input().split())
for i in range(h):
	li.append([])
	for j in range(w):
		li[i].append(0)
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            li[x-1][y-1] = 1
            y += 1
        else:
            li[x-1][y-1] = 1
            x += 1
for i in li:
    print(' '.join(map(str, i)))

#6098
li = []
for i in range(10):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
x, y = 1, 1
flag = True

while flag:
    if li[x][y] == 2:
        li[x][y] = 9
        flag = False
    elif (li[x][y+1]) == 1:
        if li[x+1][y] == 1:
            li[x][y] = 9
            flag = False
        else:
            li[x][y] = 9
            x += 1
    else:
        li[x][y] = 9
        y += 1
for i in li:
    print(' '.join(map(str, i)))
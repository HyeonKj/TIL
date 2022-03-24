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


    ##########################################

""" 1. list comprehension: 리스트 컴프리헨션

파이썬은 다른 언어와 달리 특이한 문법을 가지고 있는데 바로 리스트 컴프리헨션이다. 리스트 컴프리헨션이란 파이썬의 자료형 중 하나인 리스트의 값을 할당할 때 편리하게 리스트를 정의하는 방법이다.

예를 들어 리스트 컴프리헨션이 없이 리스트에 1부터 10까지의 숫자 리스트를 할당하는 예시 코드를 보자.

# 리스트의 값을 각각 타이핑해 정의하는 방법
>>> li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 빈 리스트를 만들고 for반복문을 이용해 리스트의append()함수를 이용해 정의하는 방법
>>> li = []
>>> for i in range(1, 10+1):
	li.append(i)

	
>>> li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
첫 번째 방법인 타이핑하는 방법은 특정한 값을 넣어야 하는 경우를 제외하고 위처럼 순차적이거나 일정 패턴이 존재하는 경우 입력해야 할 데이터가 많아질수록 프로그래밍이 아닌 단순 노동에 가깝게 된다.

두 번째 방법은 첫 번째 방법보다는 단순 타이핑 작업이 줄어들어 간편해졌다. 이 방법은 빈 리스트를 만들고, for 반복문을 작성하고, 리스트의 메서드를 호출해서 값을 추가시키는 작업을 해야 한다.

그러나 리스트 컴프리헨션을 이용해서 위 코드와 동일한 작업을 한 줄만 작성하여 수행할 수 있다.

  """

# 1.1. 리스트 컴프리헨션 기본 사용법

# 리스트 컴프리헨션은 기본적으로 [할당할 값 for 순차적으로 받을 변수 in 이터레이터]와 같이 사용한다.

# # 리스트 컴프리헨션을 이용해 정의하는 방법
# >>> li = [i for i in range(1, 10+1)]
# >>> li
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 리스트 컴프리헨션의 다양한 사용 예1
# >>> li = [i*2 for i in range(1, 10+1)]
# >>> li
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # 리스트 컴프리헨션의 다양한 사용 예2
# >>> num = [10, '20', 30, '40', 50]
# >>> li = [x for x in num]
# >>> li
# [10, '20', 30, '40', 50]

# # 리스트 컴프리헨션의 다양한 사용 예2
# >>> li = [x*2 for x in num]
# >>> li
# [20, '2020', 60, '4040', 100]
# 위 예제들을 보면서 '이렇게 하나 저렇게 하나 거기서 거기 아니야?'라고 생각할 수도 있다. 하지만 프로그래밍을 하다 보면 엄청난 양의 코드를 작성하게 될 텐데 그 수많은 코드 중에 같은 기능을 하는 코드를 보다 간결하고 이해하기 쉽도록 작성하면 보기도 좋고 차후에 유지보수도 하기 좋은 코드를 만들 수 있을 것이다.

 

# 1.2. 리스트 컴프리헨션 조건 추가

# 리스트 컴프리헨션은 또한 조건문을 추가시켜 값을 필터링할 수 있다. 사용 방법은 [할당할 값 for 순차적으로 받을 변수 in 이터레이터 if 조건]으로 조건에 참인 경우 값만 할당된다.

# # 리스트 컴프리헨션에 조건을 추가해 필터링하는 방법
# >>> li = [i*2 for i in range(1, 10+1) if i % 2 == 0]
# >>> li
# [4, 8, 12, 16, 20]
 

# 1.3. 중첩된 리스트 컴프리헨션 

# 리스트 컴프리헨션은 중첩된 for문과 동일한 작업을 할 수 있도록 작성할 수도 있다.

# # 리스트 컴프리헨션 없이 중첩된 for문으로 리스트에 값 할당하는 방법
# >>> li = []
# >>> for i in range(5):
# 	for j in range(5):
# 		li.append(i*j)

		
# >>> li
# [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16]

# # 리스트 컴프리헨션을 이용해 중첩된 for문과 동일하게 값 할당하는 방법
# >>> li = [i*j for i in range(5) for j in range(5)]
# >>> li
# [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16]

# # 리스트 컴프리헨션에서 중첩for문과 조건문 사용 예
# >>> li = [i*j for i in range(5) for j in range(5) if i*j % 2 != 0]
# >>> li
# [1, 3, 3, 9]


'''
코드	설명
%s	    문자열(string)
%c	    문자 1개(character)
%d	    정수(integer)
%f	    부동소수(floating-point)
%o	    8진수
%x	    16진수
%%      Literal % (문자로서 % 자체를 표현)'''



''' 
format() 메서드 
# format() 메서드는 문자열 안에 변수를 대입하기 편하게 해주는 메서드이다.
# 
# a = 10
b = 20

# 자동 인덱싱, {}안에 인덱스를 입력하지 않을 경우 앞자리부터 0, 1, 2 순서로 자동 인덱싱된다.
print('{} + {} = {}'.format(a, b, a+b))

# 지정 인덱싱, {}안에 인덱스를 입력해 각 위치에 넣을 값 순서를 정해줄 수 있다.
print('{0} + {1} = {2}'.format(a, b, a+b))
print('{1} + {0} = {2}'.format(a, b, a+b))



# format() 좌측 정렬
print("1{0:<10}2".format("python"))
print("1{:<10}2".format("python"))
# format() 우측 정렬
print("1{0:>10}2".format("python"))
print("1{:>10}2".format("python"))
# format() 가운데 정렬
print("1{0:^10}2".format("python"))
print("1{:^10}2".format("python"))

'''
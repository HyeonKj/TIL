# 1. @@@@@@@@@@@@@@@@@@@@@@@
# a = int(input())
# print(a)

# 2. @@@@@@@@@@@@@@@@@@@
# b = float(input())
# print(b)

# 3. ################
# a = input() 
# b = input()
# print(a)
# print(b)

""" # 4. ##################
a = input()
b = input()
print(b)
print(a)

# 5. ###################
f = float(input())
print(f)  #f에 저장되어있는 값을 출력하고 줄을 바꾼다.
print(f)
print(f) """

""" # 6. ###############
a, b = input().split()
print(a)
print(b) """

# # 7. ##############
# n, m = input().split(' ')
# print(m, n)

# 8. ################
# s = input()
# print(s, s, s)

#9. #################
# a, b = input().split(':')
# print(a, b, sep=':')

# 10. ###################
# y, m, d = input().split('.')
# print(d, m, y, sep='-')

# 11. ###############3
# birth, n = input().split('-')
# print(birth, n, sep='')

# 12. ###############
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

# #13. ##################
# s = input()
# print(s[0:2], s[2:4], s[4:6])

# 14. ###############
# s = input().split(':')
# print(s[1])

#15. ###############
# w1, w2 = input().split()
# s = w1 + w2
# print(s)

#16. ##################
# a, b = input().split()
# c = int(a) + int(b)
# print(c)

# 17. @@@@@@@@@@@@@
# n1 = float(input())
# n2 = float(input())
# print(n1 + n2)

#18. #####################3

""" a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  """ #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

# 19. ###############
""" num = input()
n = int(num)
print('%X'% n) """

# 20 . ###################
# n = ord(input())
# print(n)

""" # 21. 
c = int(input())
print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 

# 22. 
i = input()
print(chr(n+1))

# 23. 
a, b = input()
c = int(a) - int(b)
print(c)


# 24. $$$$
w, n = input().split()
print(w*int(n))

# 25. ####
n = input()
s = input()
print(int(n)*s)

# 26. ############
a=float(input())
print( format(a, ".2f") )

# 27. #
a = bool(int(input()))
print(not a)

# 28. ####
n = int(input())
print(bool(n))

# 29. 
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 30 ###########3\
#다음 코드는 홀 수만 더해 출력한다.
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==1 :
    s += i

print(s)

#31. ###########
n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n!=0 :
  n = int(input())
  if n!=0 :
    print(n)

# 32. #########
a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# 33. #########
a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
# print('%o' % n)  # n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력
"""
# 34.###########
n = int(input())
print(-n)

# 34, ###########
# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

# 예시
# ...
# print(chr(n+1))

# 참고
# 숫자는 수를 표현하는 문자로서 '0' 은 문자 그 자체를 의미하고, 0은 값을 의미한다.

# 힌트
# 아스키문자표에서 'A'는 10진수 65로 저장되고 'B'는 10진수 66으로 저장된다.
# 따라서, 문자도 값으로 덧셈을 할 수 있다. 어떤 문자의 값에 1을 더하면 그 다음 문자의 값이 된다.



# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# 예시
# ...
# c = int(a) - int(b)
# print(c)

# 참고
# 수 - 수는 차(subtraction)가 계산된다.



# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

# 예시
# ...
# m = float(f1) * float(f2)
# print(m)

# 참고
# 수 * 수는 곱(multiplication)이 계산된다.





# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 예시
# #다음 코드는 홀 수만 더해 출력한다.
# n = int(input())
# s = 0
# for i in range(1, n+1) :
#   if i%2==1 :
#     s += i

# print(s)

# 참고
# while 이나 for 반복실행구조를 이용할 수 있다.
# 다른 방법이나 while 반복실행구조를 이용해서도 성공시켜 보자.



# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# a = 10
# b = 20
# # f-string을 이용해 값 대입하기
# print(f'{a} + {b} + {a+b}')
# print(f'{b} + {a} + {a+b}')


""" s = 'python'
# f-string 좌측 정렬
print(f'1{s:<10}2')
# f-string 우측 정렬
print(f'1{s:>10}2')
# f-string 가운데 정렬
print(f'1{s:^10}2') """



# # f-string을 이용해 가운데 정렬하며 공백을 '-'로 채우기
# print(f'{s:-^10}')
# # f-string을 이용해 좌측 정렬하며 공백을 '!'로 채우기
# print(f'{s:!<10}')
# # f-string을 이용해 좌측 정렬하며 공백을 '0'로 채우기
# print(f'{s:0<10}')
# # f-string을 이용해 우측 정렬하며 공백을 '0'로 채우기
# print(f'{s:0>10}')



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




#6045
# print(a + b + c, round((a + b + c / 3), 2))
# 위 코드와 같이 작성할 경우 a + b + c / 3 부분에서 2.0값이 아닌 3.0값이 나오게 된다.
# 이 이유는 a + b + c / 3은 연산자 우선순위에 의해 a + b + (c / 3) = 1 + 2 + (3/3) = 3.0이라는 결과가 나오게 된다.
# 따라서 괄호를 적절히 사용하여 연산 우선순위를 맞춰 계산한 (a + b + c) / 3 = (1 + 2 + 3) / 3 = 2.0으로 예상한 값이 나오게 된다.

# >>> a = 1
# >>> b = 2
# >>> c = 3

# >>> print(a + b + c, round((a + b + c / 3), 2))
# 6 4.0

# >>> print(a + b + c, round(((a + b + c) / 3), 2))
# 6 2.0



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

# 6032
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




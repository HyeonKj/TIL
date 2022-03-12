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



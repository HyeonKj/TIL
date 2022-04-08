# 주목할 만한 python 문법

 

# 1. 값 입력받기

# 파이썬으로 알고리즘 문제를 해결하다 보면 사용자의 입력을 받아 원하는 값을 출력해야 하는 일이 많이 발생한다. 그래서 파이썬에서는 어떤 방법으로 값을 입력받고 입력된 값을 원하는 객체(정수형, 문자열형, 소수형)로 변환시키는지 알아보자.

 

# 1.1. 일반 문자열 입력받기

# 아래 예제 코드는 파이썬 표준 입력 input() 함수로 입력을 받는데 기본적으로 모든 값을 문자열로

# 문자열 입력받기
word = input()
# python is fun!
# word
# 'python is fun!'
#  type(word)
# <class 'str'>

# 숫자(number)를 입력받아도 문자열로 저장된다.
num = input()
1024
# num
# '1024'
# type(num)
# <class 'str'>

# 논리값(boolean)을 입력받아도 문자열로 저장된다.
bool = input()
True
# >>> bool
# 'True'
# >>> type(bool)
# <class 'str'>

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


""" 1. 값 입력받기

파이썬으로 알고리즘 문제를 해결하다 보면 사용자의 입력을 받아 원하는 값을 출력해야 하는 일이 많이 발생한다. 그래서 파이썬에서는 어떤 방법으로 값을 입력받고 입력된 값을 원하는 객체(정수형, 문자열형, 소수형)로 변환시키는지 알아보자.

 

1.1. 일반 문자열 입력받기

아래 예제 코드는 파이썬 표준 입력 input() 함수로 입력을 받는데 기본적으로 모든 값을 문자열로 반환하는 것을 보여준다.

# 문자열 입력받기
>>> word = input()
python is fun!
>>> word
'python is fun!'
>>> type(word)
<class 'str'>

# 숫자(number)를 입력받아도 문자열로 저장된다.
>>> num = input()
1024
>>> num
'1024'
>>> type(num)
<class 'str'>

# 논리값(boolean)을 입력받아도 문자열로 저장된다.
>>> bool = input()
True
>>> bool
'True'
>>> type(bool)
<class 'str'> """

""" 1.2. 값 입력받을 때 숫자로 입력받기 

1.1. 절의 예시처럼 파이썬 input()함수는 입력받을 수 있으나 모든 값을 문자열로 반환 처리하기 때문에 숫자를 입력받기 위해서는 추가적인 코드를 작성해줘야 한다. int() 함수를 이용해서 값을 int형으로 형 변환시킬 수 있다. 따라서 정수형 값을 입력받아 숫자 연산을 할 수 있는 것이다.

# 숫자 입력받기 1
>>> num = int(input())
1024
>>> num
1024
>>> type(num)
<class 'int'>

# 숫자 입력받기 2
>>> num = input()
1024
>>> num = int(num)
>>> type(num)
<class 'int'> """

""" 1.3. 값 입력받을 때 공백으로 나눠 여러 값 입력받기 

알고리즘 문제에서 값을 입력받을 때 공백으로 나눠 여러 값을 입력받아야 하는 경우가 있다. 그런 경우 map() 함수와 input().split()을 이용해서 값을 입력받는다.

>>> a, b, c, d, e = input().split()
1 2 3 4 5
>>> a
'1'
>>> b
'2'
>>> c
'3'
>>> d
'4'
>>> e
'5'
>>> a, b
('1', '2')
>>> a, b, c, d, e = map(int, input().split())
1 2 3 4 5
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> e
5
>>> a, b
(1, 2) """


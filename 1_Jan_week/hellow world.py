'''vscode, pycharm 을 많이 씀.C언어나 C++언어는 컴파일언어라 빠르다.
파이썬은 그렇게 빠르지 않다. 인간의 언어를 변환하는 것이기 때문에...
데이터 분석할 때 편리하게 사용함. 주피터 노트북은 시각화 하기도 편리함!
'''
"""
print("Hellow World")
import turtle
line=turtle.Turtle()
line = turtle.Turtle()
line.forward(50)
line.right(120)
line.forward(50)
line.right(120)
line.forward(50)
"""
'''
코드	설명
\n	문자열 안에서 줄을 바꿀 때 사용
\t	문자열 사이에 탭 간격을 줄 때 사용
\\	문자 \를 그대로 표현할 때 사용
\'	작은따옴표(')를 그대로 표현할 때 사용
\"	큰따옴표(")를 그대로 표현할 때 사용
'''
"""
a = "Life is too short, You need Python"

a[:2]
print(a)

a[3:]
"""

'''
for문과 while문을 써야할 때와 아닐때를 구분할 수 있어야 한다.
while문은 계속 반복하고 for문은 지정해준데까지만 반복함.

break하고 continue문이 있다. 컨티뉴문은 해당하면 출력하지 않고 위로 올라가게 된다.
출력하지 않게 된다. break도 똑같이 False면 반복문이 끝나게 되고 그 다음도 출력하지 않는다.
컨티뉴는 그 다음 변수도 계속 출력하게 하지만 브레이크와 다른 점이다. '''
"""
test = ['다크나이트', '라라랜드', '기생충']
for i in test:
    print(i)
    
"""

add=0
for i in range(1,11):
    add=add+i
    print(add)

for i in range(2,20):
    for x in range(1,10):
        print(i*x,end="")
    print('')
help(print)

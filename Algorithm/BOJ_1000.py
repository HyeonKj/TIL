""" print("hello")

a,b,c = map(int, input().split())
print(a+b+c) """
# 입력 1 2 3 결과 : 6

# input은 한줄, 문자열로 받는다.
# map은 int, [],반복가능한 함수로 들어온다. 
# split을 잘 사용해야한다. 

# 표준 입력 예제(input)
# 가로가 아니라 세로로 엔터로 띄어쓴다면? 어떻게 스플릿하는가?
#-> : 한줄입력이기 때문에 수만큼 input 입력하면 된다.

#프린트는 데이터를 출력하는 방법이다. 자동 줄바꿈 
# 옵션 sep = "\n" 프린트 3번쓸 것을 한줄로 써줌 end ="@"end는 프린트의 본질인 줄바꿈을 없애는 것임. 프린트 끝에 값을 설정하는것임.
""" a,b,c = map(int, input().split())
print(a,b,c, end="&") """
""" 
# input 기본
a = input()
b = int(input())
c = float(input())

print(a, b, c)
print(type(a), type(b), type(c))

# map 이용하기
a, b = map(int, input().split())
c, d = input().split()
e, f = map(int, input())

print(a, b)
print(c, d)
print(e, f)

# print
print(a, b, c, d, e)
print(a, b, c, d, e, sep="&")
print(a, b, c, d, e, end="!")
 """

""" #1. BOJ 1000번
a, b =map(int, input().split())
print(a+b) """

#2. BOJ 2558번
A=int(input())
B=int(input())
print(A+B)


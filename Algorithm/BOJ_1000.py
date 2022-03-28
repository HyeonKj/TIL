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

""" #2. no.2558 BOJ
A=int(input())
B=int(input())
print(A+B)
 """

""" #3. no.10950 BOJ
test = int(input()) 

for i in range(test): 
    a,b = map(int,input().split())
    print(a+b) """


""" #4. no.10953 BOJ
T = int(input())

for i in range(T):
    A, B=map(int, input().split(','))
    print(A+B) """


""" #5. no.11021 BOJ
T = int(input())
for i in range(T):
    A, B = map(int,input().split())
    print("Case #{}: {}".format(i+1, A+B)) 
    
    F-string은 가장 많이 쓰이고 가장 빠름. (권장)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(f"Case #{i + 1}: {a + b}")
    """

""" #6. no.11022 BOJ
T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A+B}") """

""" #7. no.2438 BOJ

num = int(input())
for i in range(num, num+1):
    i = i * '*'
    print(f"{i}")

x=int(input())
for i in range(1,x+1):
    print("*"*i) """

""" #8. no.2439 
x=int(input())
for i in range(1,x+1):
    print(' '*(x-i)+"*"*i) """

# 실습. no.10995 별찍기 -20 
N = int(input())

if N == 1:
    print('*')
    
else:
    for i in range(N):
        if i % 2 == 0:
            print('* ' * N)
        else:
            print(' *' * N)

# 나는 요리사다 
a = [sum(list(map(int,input().split()))) for i in range(5)]
print(a.index(max(a))+1,max(a))

# # 2947번

tree = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]

while True:
    for i in range(len(tree)-1):
        if tree[i] > tree[i+1]:
            tree[i], tree[i+1] = tree[i+1], tree[i]
            print(" ".join(map(str, tree)))

    if tree == answer:
        break

#평균은 넘겠지 
    a = int(input())
for _ in range(a):
    count = 0
    arr = list(map(int, input().split()))
    avg = (sum(arr)-arr[0])/arr[0] #sum(arr)-arr[0] == sum(arr[1:])
    for i in arr[1:]:
        if i > avg:
            count+=1
    r = count/arr[0]*100
    print(f"{r:.3f}%")
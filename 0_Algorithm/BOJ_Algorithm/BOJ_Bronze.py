""" list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[1][j] * list_b[i][j], end = " ")
    print() """

"""  # 비슷한 다른 문제1 
list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

# 1번
# list_c = [[0] * 3 for i in range(2)]
# for i in range(2):
#     for j in range(3):
#         list_c[i][j] = list_a[i][j] * list_b[i][j]

# 2번
# list_c = []
# for i in range(2):
#     temp = []
#     for j in range(3):
#         temp.append(list_a[i][j] * list_b[i][j])
#     list_c.append(temp)

# 2번을 더 간단하게 (list comprehension 이용)
list_c = [[list_a[i][j] * list_b[i][j] for j in range(3)] for i in range(2)]

# 출력
for i in range(2):
    for j in range(3):
        print(list_c[i][j], end=" ")
    print() """


""" # no.1100 하얀 칸 
ans=0
for i in range(8):
     ans+=input()[i%2::2].count('F')
print(ans)

# Pythonic

print(sum(input()[i % 2 :: 2].count("F") for i in range(8)))


#하얀 칸 길게 풀어 쓴 코드 
chess = 0
for i in range(8):
    table = str(input())
    for j in range(8):
        if i%2 == 0 and j%2 == 0:
            if table[j] == 'F':
                chess+=1
        elif i%2!=0 and j%2!=0:
            if table[j]=='F':
                chess+=1
print(chess) """
""" 
# 나는 요리사다 
score = []

for i in range(5):
    score.append(sum(map(int, input())))

print(score.index(max(score))+1, max(score))

scores = []
max = 0
maxidx = 0
for i in range(5):
    scores.append(sum(map(int, input().split())))

for idx, score in enumerate(scores):
    if score > max:
        maxidx = idx
        max = score

print('{} {}'.format(maxidx + 1, max))
 """
# 평균은 넘겠지 4344
for _ in range(int(input())):
    n, *scores = map(int, input().split())
    average = sum(scores) / n
    high_scores = [score for score in scores if score > average]

    result = (len(high_scores) / n) * 100
    print(f"{result:.3f}%")

# 듣보잡 
# n, m = map(int, input().split())

# a = set()

# for i in range(n):
#     a.add(input())

# b = set()

# for i in range(m):
#     b.add(input())

# result = sorted(list(a & b))

# print(len(result))

# for i in result:
#     print(i)

# 5622 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
test = 0
for j in range(len(word)):
    for i in dial:
        if word[j] in i:
            test += dial.index(i)+3
print(test)

#명령 프롬프트 1032
n = int(input())
first, others = input(), [input() for _ in range(n - 1)]
pattern = ""

for i, char in enumerate(first):
    for other in others:
        if char != other[i]:
            pattern += "?"
            break
    else:
        pattern += char

print(pattern)

# 더 간결한 풀이

n = int(input())
files = [input() for _ in range(n)]
pattern = ""

for columns in zip(*files):
    pattern += "?" if columns.count(columns[0]) < n else columns[0]

print(pattern)

# 세로 읽기 10798번 
words = [input() for _ in range(5)]
max_len = max(len(word) for word in words) # 가장 긴 문자열을 기준으로 설정

for i in range(max_len):
    for word in words:
        if i < len(word): # 길이가 짧은 문자열에 대해 에러 방지
            print(word[i], end="")

#색종이 
# 도화지를 모두 0이 담긴 이차원 리스트로 초기화
paper = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            # 색칠 (이미 칠해진 곳이라도 1이기 때문에 중복X)
            paper[i][j] = 1

# 도화지에 있는 모든 1의 합을 구하기 (색종이가 차지하는 면적)
print(sum(sum(line) for line in paper))

#직사각형 네 개의 합집합 면적 구하기 2669번
paper = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

print(sum(sum(line) for line in paper))

#스도쿠 채점 9291
def is_correct(sudoku):
    for line in sudoku:
        if len(set(line)) < 9: # 1~9에서 하나라도 중복되면 길이가 9보다 작음
            return False
    return True


for t in range(1, int(input()) + 1):
    if t > 1:
        input()

    sudoku1 = [list(map(int, input().split())) for _ in range(9)]

    sudoku3 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            line = [sudoku1[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            sudoku3.append(line)

    if is_correct(sudoku1) and is_correct(zip(*sudoku1)) and is_correct(sudoku3):
        print(f"Case {t}: CORRECT")
    else:
        print(f"Case {t}: INCORRECT")

# 나는 요리사다 2953번
a = [sum(list(map(int,input().split()))) for i in range(5)]
print(a.index(max(a))+1,max(a))

# 더 간결한 풀이

scores = [sum(map(int, input().split())) for i in range(5)]
winner_score = max(scores)
print(scores.index(winner_score) + 1, winner_score)


#23841 데칼코마니 
n,m=map(int,input().split())
graph=[]
for i in range(n):
    temp=list(input())
    for j in range(m//2):
        if temp[j]!='.':
            temp[m-j-1]=temp[j]
        elif temp[m-j-1]!='.':
            temp[j]=temp[m-j-1]
    graph.append(temp)
    
for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j],end="")
    print()


# 5086 배수와 약수

import sys
input = sys.stdin.readline

num = tuple(map(int, input().split()))

while num != (0, 0):
    a = num[0]

# 1712
a, b, c = map(int, input().rstrip().split())

if c - b <= 0:
    print(-1)
else:
    print(a//(c-b) + 1)

#10669
from datetime import data
today = data.today()
print(today.isoformat())

#10757
a, b = map(int, input().split())
# print(a+b)

#10718
print("강한친구 대한 육군")
print("강한친구 대한 육군")

# 10869
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# 10926

id = input("")
print(id +"??!")

#10998
a, b = map(int, input().split())
print(a*b)

# 11283
print(ord(input()) - 44031)

#11654
print(ord(input()))

#11942
print("고려대학교")

#14654
N, K = map(int, input().split())

for _ in range(N):
    A, B = map(int, input().split())
print("비와이")

#23827 수열
n=int(input())
num_list=list(map(int,input().split()))
sum_list=sum(num_list)
res=0
for i in num_list:
    sum_list-=i
    res=(res+i*sum_list)%1000000007
print(res)

# 1463

n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

#1003
t = int(input())

for i in range(t):
    n = int(input())

    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")

    else:
        d = [[0] * 2 for _ in range(n + 1)]
        d[0][0] = 1
        d[1][1] = 1
        d[2] = [1, 1]
        for j in range(3, n + 1):
            d[j][0] = d[j - 1][0] + d[j - 2][0]
            d[j][1] = d[j - 1][1] + d[j - 2][1]

        print("%d %d" % (d[n][0], d[n][1]))

#2156
n = int(input())

wine = []

for i in range(n):
    wine.append(int(input()))

d = [0]*n

d[0] = wine[0]
if n > 1:
    d[1] = wine[0]+wine[1]

if n > 2:
    d[2] = max(wine[2]+wine[1], wine[2]+wine[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])

print(d[n-1])

#2225
n, k = map(int, input().split())

d = [[0]*(k+1) for _ in range(n+1)]

for i in range(k+1):
    d[0][i] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        d[i][j] = d[i][j-1] + d[i-1][j]
        d[i][j] %= 1000000000

print(d[n][k])

#12865
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])

# 2098
n = int(input())

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))

#2133
n = int(input())

dp = [0]*(n+1)

if n % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2

    print(dp[n])

#1904
n = int(input())

dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])

#1149
n = int(input())

cost = []
minCost = -int(1e9)
dp = [[0]*3 for _ in range(n)]
for i in range(n):
    cost.append(list(map(int, input().split())))

dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
    dp[i][1] = min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
    dp[i][2] = min(dp[i-1][0] + cost[i][2], dp[i-1][1] + cost[i][2])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

#1932
n = int(input())

arr = []
dp = [[0]*n for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))

# 1001
A, B = input().split()
print(int(A)-int(B))

#1008
A,B = map(int,input().split())
print(A/B)

# 1009
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10 % 10 % 10)
        else:
            print((a**b) % 10 % 10 % 10)

# 1032
n = int(input())
a = list(input())
a_len = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))

# 1085
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

#2557
print("Hello World!")

#10718
print("강한친구 대한육군\n"*2)

# 고양이
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
# 오늘의 배운점 : 역슬래시를 출력할때는 두개를 연속해서 써야 한다.

# 개 10172
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')  # \'앞에 \을 붙여준다.
print('|"^"`    |')
print("||_/=\\\__|")  # \\ 앞에 \을 하나 더 붙여준다.

#10998
A,B = input().split()
print(int(A)*int(B))

A,B = map(int,input().split())
print(A*B)

#10926
print(input() + "??!")

# 18108
y = int(input())

print(y - 543)

#10430
A,B,C = map(int,input().split())

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
# sep='\n'로 줄바꿈

#1330
A,B = map(int,input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

#9498
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else:
    print('F')

# 윤년 2753
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)

#14681
x= int(input())
y= int(input())

if x > 0 and y > 0 :	# x,y: 양수
    print('1')
elif x < 0 and y > 0 :	# x:음수, y:양수
    print('2')
elif x < 0 and y < 0 :	# x,y: 음수
    print('3')
else:
    print('4')

# 2884
H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	

# 2525
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)

#2480

a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))


# 구구단
n = int(input())

for i in range(1,10):  # 1~9
    print(n, '*', i, '=', n*i)

# 8393 합
a = int(input())
sum = 0
for i in range(a+1):
    sum = sum + i
print(sum)

#15552
import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

# 2741
n = int(input())

for i in range(n):
    print(i+1)

# 1978
n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)

# 2581 소수 
start_num = int(input())
last_num = int(input())

sosu_list = []
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수리스트에 추가
            
if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)


# 11653 소인수분해
n = int(input())

if n == 1:
    print('')

# 2부터 하나씩 나눠보기
for i in range(2, n+1):
    if n % i == 0:
    	#해당 숫자로 나눌 수 없을 때까지 나누기
        while n % i == 0:
            print(i)
            n = n / i

# 1929 소수구하기
m, n = map(int, input().split())

def isprime(m, n):
  n += 1                            # for문 사용을 위한 n += 1
  prime = [True] * n                # n개의 [True]가 있는 리스트 생성
  for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
    if prime[i]:                    # prime[i]가 True일때
      for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)

isprime(m, n)

# 3009

x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)

#15596 번 함수

def solve(a):
    return sum(a)

def solve(a):
    total = 0
    for x in a:
        total += x
    return total

#3053
import math

r = int(input())
print(r*r*math.pi)  # 원의 넓이
print(2*r*r)  # 택시기하학 원의 넓이

import math
r = int(input())
print(f'{r*r*math.pi:.6f}')
print(f'{2*r*r:.6f}')

#4153
while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break  # 세 수가 0이면 break
    max_num = max(nums)
    nums.remove(max_num)  # 빗변의 길이는 직각삼각형 세변의 길이중 가장 길다.
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')


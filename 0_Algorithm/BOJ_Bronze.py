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

#10872
n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)

#10870
n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)
print(fibonacci[n])

# 블랙잭 
from itertools import permutations

n, m = map(int, input().split())

num = list(map(int, input().split()))
permutationArray = permutations(num, 3)
ans = 0
for i in permutationArray:
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans)

# 2231
n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)

# 2750 수 정렬 버블정렬
N = int(input())

numbers = []

for _ in range(N) : 
    numbers.append(int(input()))

# Bubble Sort
for i in range(len(numbers)) : 
    for j in range(len(numbers)) : 
        if numbers[i] < numbers[j] : 
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
for n in numbers : 
    print(n)

# 삽입 정렬
N = int(input())
nums = []

for _ in range(N) : 
    nums.append(int(input()))

# Insert Sort
for i in range(1, len(nums)) :
    while (i>0) & (nums[i] < nums[i-1]) :
        nums[i], nums[i-1] = nums[i-1], nums[i]
        
        i -= 1
        
for n in nums : 
    print(n)


# 5086 
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')

# 2740 분할정복 행렬곱셈. 
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))


#행렬 곱셈 
C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

#출력문
for i in C:
    for j in i:
        print(j, end = ' ')
    print()

# 11050 이상계수 1 분할론 
from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)

# 1008
a = float(input())
b = float(input())
print(a/b)

a,b = input().split()
a = float(a)
b = float(b)
#print(a/b)
print(round(a/b,9))

a, b = map(int , input().split()) 
print(a/b)

# 1009 분산처리
import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	aa=a%10

	if aa == 0: # 패턴 1
		print(10)
	elif aa in [1,5,6]: 
		print(aa)
	elif aa in [4,9]: #패턴 2
		bb=b%2
		if bb == 0:
			print(aa*aa%10)
		else:
			print(aa)
	else: #패턴 4
		bb=b%4  
		if bb ==0:
			print(aa**4%10)
		else:
			print(aa**bb%10)

# 1075
n = input()
f = int(input())
a = int(n[:-2] + '00')
while True:
    if a % f == 0:
        break
    a += 1
print(str(a)[-2:])

#1076
color = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
f = color.index(input())
s = color.index(input())
t = color.index(input())
r = int(str(f) + str(s)) * (10 ** t)
print(r)

#1110
input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정 
print(cnt)

# 1145 적어도 대부분의 배수 
a = list(map(int, input().split()))
n = min(a)
while True:
    cnt = 0
    for i in range(5):
        if n % a[i] == 0:
            cnt += 1
    if cnt > 2:
        print(n)
        break
    n += 1

# 1152
print(len(input().splie()))

word = input().split()
print(len(word))

# 1157
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])

# 1159
from collections import Counter
n = int(input())
player = []
fn = []
cnt = 0
for i in range(n):
    a = input()
    player.append(a[0])
player_count = Counter(player)
for i, j in player_count.items():
    if j >= 5:
        fn.append(i)
        cnt += 1
fn.sort()
if cnt == 0:
    print("PREDAJA")
else:
    for i in fn:
        print(i, end='')


# 1173
N, m, M, T, R = map(int, input().split())
cnt = t = 0
now = m
while cnt < N:
    if m+T > M:
        break
    if now + T <= M:
        now += T
        cnt += 1
    else:
        now = max(now-R, m)
    t += 1
print(t if cnt == N else -1)


#1193
input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  

gap = max_num - input_num 
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  #분자
    under = gap + 1  #분모
else :  # 사선 라인이 홀수번째 일 때
    top = gap + 1  #분자
    under = line - gap  #분모
print(f'{top}/{under}')

# 1212
# print(bin(int(input(), 8)[2:])

# 1225
num1, num2 = input().split()
num1, num2 = list(map(int, num1)), list(map(int, num2))

print(sum(num1) * sum(num2))

#1233 주사위 
s1, s2, s3 = map(int, input().split())
li = [0]*81
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            li[i+j+k] += 1
print(li.index(max(li)))

#1236 성 지키기
n, m = map(int,input().split())
board = []

for _ in range(n):
    board.append(input())

a, b = 0, 0

for i in range(n):
    if "X" not in board[i]:
        a += 1

for j in range(m):
    if "X" not in [board[i][j] for i in range(n)]:
        b += 1

print(max(a ,b))

# 1247 부호
from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(N)]
    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")

# 1252 이진수 덧셈
A, B = map(str, input().split())
A = int(A, 2)
B = int(B, 2)
C = A + B

print(bin(C)[2:])

#1259
while True:
    word = input()
    palindrom = word[::-1]
    if word=='0':
        break
    
    if word==palindrom:
        print('yes')
    else:
        print('no')

# 1264
while 1:
    s = input()
    if s == '#':
        break
    cnt = 0
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
    print(cnt)

#1267 핸드폰 요금 
n = int(input())
s = list(map(int, input().split()))
y = 0
m = 0
for i in s:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15
if y < m:
    print('Y %d' % y)
elif y > m:
    print('M %d' % m)
else:
    print('Y M %d' % y)

# 1271
n, m =input().split()
n = int(n)
m = int(m)
print(n//m)
print(n&m)

# 1284
while 1:
    N = input()
    if N == '0':
        break
    res = len(N)+1
    for n in N:
        if n == '0':
            res += 4 
        elif n == '1':
            res += 2
        else:
            res += 3
    print(res)

#1296
ms = input()
n = int(input())
li = sorted([input() for i in range(n)])
max_p = max_i = 0
for i in range(n):
    L = ms.count("L") + li[i].count("L")
    O = ms.count("O") + li[i].count("O")
    V = ms.count("V") + li[i].count("V")
    E = ms.count("E") + li[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_p < p:
        max_p = p
        max_i = i
print(li[max_i])

# 1297
d, h, w = map(int, input().split())
r = d / ((h ** 2 + w ** 2) ** 0.5)
print(int(h * r), int(w * r))

# 1333
if __name__ == '__main__':
    n, l, d = map(int, input().split())
    check = [False] * (n * l + 5 * (n - 1))

    for i in range(n):
        s = (l + 5) * i
        for j in range(s, s + l):
            check[j] = True

    answer = 0
    while answer < len(check):
        if not check[answer]:
            break
        answer += d
    print(answer)

# 1350
n = int(input())
s = list(map(int, input().split()))
a = int(input())
sum = 0
for i in s:
    if i % a == 0:
        sum += i // a
    else:
        sum += i // a + 1
print(sum * a)

# 1356
n = input()
n_len = len(n)
true = 0
for i in range(n_len - 1):
    left = 1
    right = 1
    for j in range(i + 1):
        left *= int(n[j])
    for k in range(i + 1, n_len):
        right *= int(n[k])
    if left == right:
        print("YES")
        true = 1
        break
if true == 0:
    print("NO")

# 1357
x, y = map(str, input().split())
s = str(int(x[::-1]) + int(y[::-1]))
print(int(s[::-1]))

# 1362
if __name__ == '__main__':
    cnt = 0
    while True:
        o, w = map(int, input().split())
        if o == 0 and w == 0:   # "0 0" 입력 시 모든 시나리오 끝남
            quit()

        die = False
        while True:
            action, n = input().split()
            if action == '#' and n == '0':
                break

            if not die:
                n = int(n)
                if action == 'E':
                    w -= int(n)
                elif action == 'F':
                    w += int(n)

            if w <= 0:  # 사망
                die = True

        cnt += 1
        if w <= 0:
            print("%d RIP" % cnt)
        elif o / 2 < w < o * 2:
            print("%d :-)" % cnt)
        else:
            print("%d :-(" % cnt)

# 1371
import sys

s = sys.stdin.read()
li = [0]*26
for c in s:
    if c.islower():
        li[ord(c)-97] += 1
for i in range(26):
    if li[i] == max(li):
        print(chr(97+i), end='')

#1373
import sys

x = sys.stdin.readline()
ten_number = 0
answer = ''
for i in range(len(x)):
    ten_number += int(x[-1])*(2**i)
    x = x[:-1]

while ten_number != 0: 
    answer += str(ten_number%8)
    ten_number = ten_number // 8
print(answer[::-1])

# 1373 -2 
print(oct(int(input(),2))[2:])

#1392
N, Q = map(int, input().split())
li = [int(input()) for _ in range(N)]
for _ in range(Q):
    t = int(input())
    for i in range(N):
        if t < sum(li[:i+1]):
            print(i+1)
            break

#1402
for _ in range(int(input())):
    A, B = map(int, input().split())
    print("yes")

#1408
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
if t < 0:
    t += 60*60*24
h = t//3600 
m = (t%3600)//60 
s = t%60
print("%02d:%02d:%02d" % (h,m,s))

# 1418
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

s = [0 for i in range(n+1)]
for i in range(2,n+1):
    if s[i] == 0:
        for t in range(i,n+1,i):
            if t%i == 0:
                s[t] = max(s[t],i)
ans = 0
for i in s:
    if i <= m:
        ans += 1
print(ans-1)

# 1434
N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))
i = j = t = in_box = 0
while i < N and j < M:
    if box[i] < t+book[j]:
        t = 0
        i += 1
    else:
        in_box += book[j]
        t += book[j]
        j += 1
print(sum(box)-in_box)    

# 1440
a=int(input())
b=int(input())
over=b-a
 
if over >=31:print("You are speeding and your fine is $500.")
elif over>20:print("You are speeding and your fine is $270.")
elif over>0:print("You are speeding and your fine is $100.")
else:print("Congratulations, you are within the speed limit!")

# 1453
N = int(input())
PC_Georgia = list(map(int, input().split()))        
PC_checkmate = [0] * 101 #PC방 자리
PC_refused = 0 #거절당한 사람

for i in PC_Georgia:
    if PC_checkmate[i] != 0:
        PC_refused += 1
    else:
        PC_checkmate[i] += 1

print(PC_refused)

# 1526
n = int(input())
while True:
    flag = True
    for i in str(n):
        if i!="4" and i!="7":
            flag = False
            n -= 1
    if flag :
        print(n)
        break

#1546
n = int(input())  # 과목 수
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list :
    new_list.append(score/max_score *100)  # 새로운 점수 생성
test_avg = sum(new_list)/n
print(test_avg)

# 1547
N = int(input())

cups = [1,2,3]
for _ in range(N):
    x, y = map(int, input().split())
    
    xi = cups.index(x)
    yi = cups.index(y)
    
    cups[xi], cups[yi] = cups[yi], cups[xi]
    
print(cups[0])

# 1550
print(int(input(), 16))

# 1551
N, K = map(int, input().split())
li = list(map(int, input().split(',')))
for _ in range(K):
    t = [li[i+1]-li[i] for i in range(len(li)-1)]
    li = t
print(*li, sep=',')

# 1592
N, M, L = map(int, input().split())
li = [0]*N
cnt = i = 0
while li[i] < M-1:
    li[i] += 1
    cnt += 1
    i = (i+L)%N if li[i]%2 == 1 else (i-L)%N
print(cnt)

# 1598
a, b = map(int, input().split())
x1 = (a-1)//4 + 1 
y1 = (a-1)%4
x2 = (b-1)//4 + 1 
y2 = (b-1)%4
print(abs(x2-x1) + abs(y2-y1))

# 1652
n = int(input())
s = []
cnt_w = 0
cnt_h = 0
position_w = 0
position_h = 0
for i in range(n):
    s.append(input())
for i in s:
    for j in i:
        if j == '.':
            cnt_w += 1
        else:
            if cnt_w > 1:
                position_w += 1
            cnt_w = 0
    if cnt_w > 1:
        position_w += 1
    cnt_w = 0
for i in range(n):
    for j in range(n):
        if s[j][i] == '.':
            cnt_h += 1
        else:
            if cnt_h > 1:
                position_h += 1
            cnt_h = 0
    if cnt_h > 1:
        position_h += 1
    cnt_h = 0
print(position_w, position_h)

# 1668
li = [int(input()) for _ in range(N)]
left_cnt = right_cnt = 0
left_max = right_max = 0
for n in li:
    if n > left_max:
        left_max = n
        left_cnt += 1
for n in li[::-1]:
    if n > right_max:
        right_max = n
        right_cnt += 1
print(left_cnt)
print(right_cnt)

# 1672
import sys
input = sys.stdin.readline

n = int(input())
dna = list(input().rstrip())
itp = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G", "GA":"C", "CA":"A", "TA":"G", "CG":"T", "TG":"A","TC":"G"}

a,b = "", dna.pop()
for _ in range(n-1):
    a = dna.pop()
    if a == b:
        continue
        
    b = itp[a+b]
print(b)

#1673
while 1:
    try:
        n, k = map(int, input().split())
        res = 0 
        res += n
        while n//k:
            res += n//k
            n = n//k + n%k
        print(res)
    except:
        break

# 1681
N,l = list(map(int,input().split(' ')))

num = 1 # 양의 정수이기 때문에 0이 아닌 1부터 시작합니다
cnt = 0	# 라벨을 붙인 개수
while True:
    if str(l) not in str(num): #해당 숫자를 사용할 수 있으면
        cnt+=1	#라벨을 붙입니다
        if cnt == N: #N개의 원소를 다 라벨링했다면
            print(num) #마지막 값을 출력하고
            break #반복문을 그만둡니다
        num+=1	#반복문이 끝나지 않았다면 다음 숫자로 넘어갑니다

    else:	#l이 포함되어 해당 숫자를 사용할 수 없다면
        num+=1	#다음 숫자로 넘어갑니다

#1703
while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    n = 1
    for i in range(li[0]):
        sf = li[2*i + 1]
        p = li[2*i + 2]
        n = n*sf - p
    print(n)

# 1712
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))

# 1718
text, key = input(), input()

answer = ''

for i in range(len(text)):
    if text[i] == ' ': answer += ' '
    else: answer += chr((ord(text[i]) - ord(key[i%len(key)]) - 1) % 26 + ord('a'))

print(answer)

#1731
li = []
for _ in range(int(input())):
    li.append(int(input()))
    
ans = li[-1]
if li[2]-li[1] == li[1]-li[0]:
    ans += (li[1]-li[0])
elif li[2]//li[1] == li[1]//li[0]:
    ans *= (li[1]//li[0])

print(ans)

# 1773 폭죽쇼
N, C = map(int, input().split())
check = [False]*(C+1)
ans = 0

for _ in range(N):
    n = int(input())
    for i in range(n, C+1, n):
        if not check[i]:
            check[i] = True
            ans += 1
print(ans)

# 1813
import sys
n=int(sys.stdin.readline())
hs=list(map(int,sys.stdin.readline().split()))
tmp=[0]*100001
cnt=0
checker=0
for i  in range(n):
    tmp[hs[i]]+=1
for i in range(len(tmp)):
    if tmp[i]==i: cnt=i; checker=1
if checker==0 : print(-1); exit()
else: print(cnt)


# 1834
n = int(input())
num = 0
for i in range(n + 1, n ** 2, n + 1):
    num += i
print(num)

#1837
P, K = map(int, input().split())
li = [1]*K
for i in range(2, int(K**0.5)+1):
    if li[i] == 1:
        for j in range(i+i, K, i):
            li[j] = 0
prime = [i for i in range(2, K) if li[i] == 1]

good, bad = 1, 0
for n in prime:
    if P%n == 0:
        good, bad = 0, n
        break
print("GOOD" if good else f"BAD {bad}")

# 1855
import sys

k = int(sys.stdin.readline().rstrip())
str = sys.stdin.readline().rstrip()

lst = []
str1 = ''

for i in range(int(len(str)/k)):
    if i % 2 == 1:
        str1 = str[i*k:i*k+k]
        lst.append(str1[::-1])
    else:
        lst.append(str[i*k:i*k+k])


for i in range(k):
    for j in range(int(len(str)/k)):
        print(lst[j][i], end="")

# 1864
d = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while 1:
    s = input()
    if s == '#':
        break
    res = 0
    for i in range(len(s)):
        res += d[s[i]] * 8**(len(s)-i-1)
    print(res)


# 1871
for _ in range(int(input())):
    L, D = input().split('-')
    n = int(D)
    s = 0
    for i in range(3):
        s += (ord(L[i])-65) * 26**(2-i)
    print("nice" if abs(s-n) <= 100 else "not nice")

# 1919
a = [0 for i in range(26)]
b = [0 for i in range(26)]
count = 0
a_gram = input()
b_gram = input()
a_gram = list(a_gram)
b_gram = list(b_gram)
for i in range(0, len(a_gram)):
    a[ord(a_gram[i]) - 97] += 1
for i in range(0, len(b_gram)):
    b[ord(b_gram[i]) - 97] += 1
for i in range(0, 26):
    if a[i] != b[i]:
        count += abs(a[i] - b[i])
print(count)

# 1924 2007년
Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())
 
for i in range(x-1):
    Day = Day + arrList[i]
Day = (Day + y) % 7
 
print(weekList[Day])
 
'''
# calendar module 사용
import calendar

arrList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int,input().split())

Day = calendar.weekday(2007, x, y)
print(arrList[Day])
'''

# 1942
import datetime
from datetime import timedelta

for i in range(3):
    start,end=input().split()

    st=int(start.replace(":",""))
    ed=int(end.replace(":",""))

    stH,stM,stS=map(int,start.split(":"))
    edH,edM,edS=map(int,end.split(":"))

    stime=datetime.datetime(2021,1,1,stH,stM,stS)

    tmp_time=stime.strftime('%H%M%S')

    # 1씩 더하기 때문
    sec=1

    cnt=0
    if int(tmp_time)%3==0:
            cnt+=1
    etime=datetime.datetime(2021,1,1,edH,edM,edS)
    etime=etime.strftime('%H%M%S')

    while True:
        if tmp_time==etime:
            break
        
        # sec만큼 증가 (여기서 sec은 1)
        stime=stime+timedelta(seconds=sec)
        tmp_time=stime.strftime('%H%M%S')
        if int(tmp_time)%3==0:
            cnt+=1


    print(cnt)

# 1952
m, n = map(int,input().split())
grid = [[0 for _ in range(n)] for _ in range(m)]
# 우하좌상
direct = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}

end = m*n-2
cnt = 0
head = 0
i,j = 0,0
grid[i][j] = "X"
while end>=0:
    condi = False
    if 0<=i+direct[head][0]<m and 0<=j+direct[head][1]<n:
        if grid[i+direct[head][0]][j+direct[head][1]] != "X":
            grid[i+direct[head][0]][j+direct[head][1]] = "X"
            i,j = i+direct[head][0],j+direct[head][1]
            condi = True
    if not condi:
        cnt += 1
        head = (head+1)%4
        i,j = i+direct[head][0],j+direct[head][1]
        grid[i][j] = "X"
    end -= 1
print(cnt)

# 1964
n = int(input())
dot = 5
inc = 7
for i in range(1, n):
    dot += inc
    inc += 3
print(dot % 45678)

#1975
import sys
input = sys.stdin.readline

def func(x, b):
    if x !=0 and x % b == 0: return 1+func(x//b,b)
    else: return 0

c = [0] * 1001
for x in range(2, 1001):
    c[x] = sum(func(x, b) for b in range(2, x+1))

for _ in range(int(input())):
    x = int(input())
    print(c[x])

# 1977
m = int(input())
n = int(input())
num = []
i = 1
while i ** 2 <= n:
    if m <= i ** 2 <= n:
        num.append(i ** 2)
    i += 1
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])

# 2010
import sys

n = int(input())
s = 0
for _ in range(n):
    s += int(sys.stdin.readline())
print(s-n+1)

# 2037
if __name__ == '__main__':
    keyboard = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
                ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
    p, w = map(int, input().split())
    text = input()

    total = 0
    past_j = ''
    for i in range(len(text)):
        if text[i] == ' ':
            total += p
            past_j = ''
        for j in range(len(keyboard)):
            for k in range(len(keyboard[j])):
                if text[i] == keyboard[j][k]:
                    if j == past_j:
                        total += w
                    total += (1+k) * p
                    past_j = j
    print(total)

# 2052
N = int(input())
s = "%.300f" % 2 ** -N
end = len(s)
for i in range(end-1, 1, -1):
    if s[i] != '0':
        end = i
        break
print(s[:end+1])

# 2061 
L, K = map(int, input().split())
li = [1]*K
for i in range(2, int(K**0.5)+1):
    if li[i] == 1:
        for j in range(i+i, K, i):
            li[j] = 0
prime_li = [i for i in range(2, K) if li[i] == 1]

good = 1
for n in prime_li:
    if L%n == 0:
        print(f"BAD {n}")
        good = 0
        break
if good == 1:
    print("GOOD")

# 2083
if __name__ == '__main__':
    while True:
        name, age, weight = input().split()
        age, weight = int(age), int(weight)
        if name == '#' and age == 0 and weight == 0:
            quit()

        if age > 17 or weight >= 80:
            print("%s Senior" % name)
        else:
            print("%s Junior" % name)

#2145 
while(True):
    n = int(input())
    if n == 0:
        break
    while(n>9):
        n = sum(map(int,list(str(n))))
        # n이 673일 때, 스트링 변환 후 리스트에 담으면 ["6","7","3"] 꼴이 된다.
        # map은 이같은 배열 안의 스트링을 int형으로 편하게 변환시켜 주는 기능을 한다.
    print(n)

#2153
pn = [0 for i in range(1050)]
for i in range(2, 32):
    for j in range(i * 2, 1050, i):
        pn[j] = 1
n = input()
word = 0
for i in n:
    if i.islower() == True:
        word += ord(i) - 96
    else:
        word += ord(i) - 38
if pn[word] == 0:
    print('It is a prime word.')
else:
    print('It is not a prime word.')

# 2154
s = ""
for i in range(1, 100001):
    s += str(i)

print(s.index(input())+1)

#2161
N = int(input())
card_list = [i for i in range(1, N+1)]
discarded_card = []

while len(card_list) != 1:
    discarded_card.append(card_list.pop(0)) #버리기
    card_list.append(card_list.pop(0)) #뒤로 옮기기

for i in discarded_card:
    print(i, end = ' ')
print(card_list[0])

# 2163
N, M = map(int,input().split())

print(N*M-1)

#2167
n, m = map(int, input().split())
a = []
dp = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = a[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

#2204 도비의 난독증 테스트
if __name__ == '__main__':
    while True:
        voca = []
        n = int(input())
        if n == 0:
            quit()
        for i in range(n):
            voca.append(input())
        voca.sort(key=str.lower)
        print(voca[0])

# 2231
N = int(input())
result = 0

for i in range(1, N+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == N):                 
        result = i                   
        break

print(result)

# 2292 벌집
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)

# 2309 일곱난쟁이
s = []
for i in range(9):
    s.append(int(input()))
sum_s = sum(s)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (s[i] + s[j]) == 100:
            one = s[i]
            two = s[j]
s.remove(one)
s.remove(two)
s.sort()
for i in s:
    print(i)

#2338 긴자리 계산
a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

# 2355 시그마
a, b = map(int, input().split())
n_max = max(a, b)
n_min = min(a, b)
n = n_max - n_min
s = (n * (n + 1)) // 2
print(s + (n_min * (n + 1)))

# 2386
while True :
  n = input()
  if n == '#' :
    break
  value = n[0]
  data = n[2::]
  result = data.count(value) + data.count(value.upper())
  print(value, result)

# 2420
N, M = map(int, input().split())
print(abs(N-M))

# 2438
inp = int(input())
for i in range(1,(inp+1)):
    print("*" * i)

# 2439 star1
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)

# 2440 star2
a=int(input())
for i in range(1,a+1):
    print("*"*(a-i+1))

# 2938
sugar = int(input())
bags = 0

while sugar >= 0:
    if sugar % 5 == 0:		# 남은 설탕이 5로 나누어 떨어진다면
        bags += sugar // 5	# 봉지 개수를 더하고 끝
        print(bags)
        break
    sugar -= 3			# 아니라면 3kg짜리 봉지를 하나씩 더해본다
    bags += 1
else:
    print(-1)			# 빼다가 총 설탕이 음수가 되면 -1

#  2935 소음 
a = int(input())
op = input()
b = int(input())
if op == '*':
    print(a * b)
else:
    print(a + b)

# 3003
cp = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-li[i], end=' ')
    
# 3053 택시 기하학
import math
r = int(input())
print(r*r*math.pi)
print(2*r*r) # 택시기하학 원의 넓이

# 3053- 2 
import math
r = int(input())
print(f'{r*r*math.pi:.6f}')
print(f'{2*r*r:.6f}')

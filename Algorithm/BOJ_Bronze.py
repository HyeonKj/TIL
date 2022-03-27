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


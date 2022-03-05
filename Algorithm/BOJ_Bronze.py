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
# 평균은 넘겠지 


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

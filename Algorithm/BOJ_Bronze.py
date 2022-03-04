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


# no.1100 하얀 칸 
ans=0
for i in range(8):
     ans+=input()[i%2::2].count('F')
print(ans)

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
print(chess)
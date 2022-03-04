""" list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[1][j] * list_b[i][j], end = " ")
    print() """

 # 비슷한 다른 문제1 
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
    print()


# no.1100 하얀 칸 

chess = [input() for i in range(8)]
num = 0

for j in range(8):
    for x in range(8):
        if y % 2 == x % 2 and chess[j][x] == 'F':
            num + =1
print(num)
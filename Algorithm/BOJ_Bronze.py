""" list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[1][j] * list_b[i][j], end = " ")
    print() """

# 비슷한 다른 문제1 
print("first array")
list_a = [list(map(int, input().split())) for i in range(2)]
print("second array")
list_b = [list(map(int, input().split())) for i in range(2)]

list_c = []
for i in range(2):
    for j in range(3):
        list_c.append(list_a[i][j] * list_b[i][j], end =" ")
        
    print(list_c[0])


a = []
a.insert[1, 2, 3, 4]
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()

#############################

N = int(input())
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0} # 주사위의 아랫면에 따른 윗면 로테이션 등록(리스트 인덱스 기준)

maxnum = 0 # 최대값을 저장해둘 상수 선언
for i in range(6): # 첫 번째 주사위를 기준으로 1~6까지 모두 순회
    result = [] #각 주사위마다 옆면의 최대값 1개를 저장해둘 리스트 선언
    temp = [1, 2, 3, 4, 5, 6] # 주사위 각 면에 써져있는 1~6
    temp.remove(dice[0][i]) # 주사위 아랫면의 숫자 제거
    next = dice[0][rotate[i]] # 첫 번째 주사위의 윗면 값 계산
    temp.remove(next) # 첫 번째 주사위의 윗면 값 삭제
    result.append(max(temp)) # 첫 번째 주사위의 옆면들 중 가장 큰 값 삽입
    for j in range(1, N): # 두 번째 주사위부터 마지막 주사위까지 반복
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(next) # 현재 주사위의 아랫면 숫자 제거
        next = dice[j][rotate[dice[j].index(next)]] # 현재 주사위의 윗면 계산
        temp.remove(next) # 현재 주사위의 윗면 삭제
        result.append(max(temp)) # 현재 주사위의 옆면들 중 가장 큰 값 삽입
    result = sum(result) # 각 주사위마다의 최대값을 모두 더한다.
    if maxnum < result: # 이전의 최대값과 현재의 최대값을 비교하여 더 큰 값을 저장한다.
        maxnum = result

print(maxnum)

######################
import sys
input = sys.stdin.readline

n = int(input())
board = sorted([tuple(map(int,input().split())) for _ in range(n)])

last_idx, last_h = board[0]
result = 0
while(True):
    max_idx,max_h = 0,0
    # 현재 위치부터 큰 것이 나올 때까지 탐색
    for j in range(board.index((last_idx,last_h))+1,n):
        cur_idx,cur_h = board[j]
        if cur_h > last_h:
            result += (cur_idx-last_idx)*last_h
            last_idx,last_h = cur_idx,cur_h
            break
        if cur_h > max_h:
            max_idx,max_h = cur_idx,cur_h
    # 현재 위치보다 큰 것이 없다면 가장 컸던 것까지만 곱해주고 인덱스를 그곳으로 옮김
    else:
        result += last_h + (max_idx-last_idx-1)*max_h
        last_idx,last_h = max_idx,max_h
        if last_idx == 0:
            break
print(result)

######################
list = [int(input()) for i in range(9)]

total = sum(list)

for i in range(9):
    for j in range(i+1,9):
        if 100 == total - (list[i] + list[j]): 
            num1,num2=list[i],list[j]

            list.remove(num1)
            list.remove(num2)
            list.sort() # 오름차순 정리

            for i in range(len(list)):
               print(list[i])
            break

    if len(list)<9:
        break

##################
melon = int(input()) # 참외 개수 K
values = [input().split() for _ in range(6)] # 나머지 2~7 line의 6 줄을 입력 받는다.
directions = [int(v[0]) for v in values] # 방향을 뽑아내서 저장한다.
lengths = [int(v[1]) for v in values] # 길이를 뽑아내서 저장한다.
max_lengths, box_lengths = [], [] # 큰 박스의 길이, 작은 박스의 길이를 담을 배열

for i in range(1, 5):
    if directions.count(i) == 1: # direction이 한번만 존재한다 == 큰 박스의 변
        max_lengths.append(lengths[directions.index(i)]) # 큰박스의 변 길이 저장
        temp = directions.index(i) + 3 # 큰 박스 + 3 == 작은 박스의 변
        if temp >= 6:
            temp -= 6 # cycle을 위해 6 이상일 경우 -6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)



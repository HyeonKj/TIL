""" #no.11720
n = int(input())
# numbers = list(map(int, input()))
# print(sum(numbers))
print(sum(map(int, input())))

#2. 
number = int(input())
print(sum(map(int, input()))) """

""" #1.    no. 2750 숫자 정렬하기 
number = int(input())
num = []

for i in range(number):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)
 """
""" #2.
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

# 정렬
sorted_numbers = sorted(numbers)

# 출력
for number in sorted_numbers:
    print(number) """

""" # 리스트 3 자가진단 1 리스트 내포
n = int(input())
print([i**2 for i in range(1, 1+n)]) """

""" # 리스트 3 형성평가 1
n = int(input())
print(["No."+str(i) for i in range(1, n+1)]) """

# 2562번 최댓값 
# numbers = [int(input()) for _ in range(9)]

# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)

# LIST Comprehension1 

""" n = int(input())
numbers = [i * i for i in range(1, n + 1)]
print(numbers)

# LIST Comprehension2 
n = int(input())
numbers = [f"No.{i}" for i in range(1, n + 1)]
print(numbers) """

""" # 가독성과 재사용성이 중요하다
# 최댓값 
# 1. 입력을 받아서 리스트를 만든다. 
num = [int(input()) for i in range(9)]
max_num = max(num)
# 2. 최댓값
print(max_num)

# 3. 몇 번째 수인가?
print(num.index(max_num)+1) """

#2차원 리스트
a =[list(map(int, input().split())) for i in range(3)]
# for i in range(3):
#     line = list(map(int, input().split()))

print(a)
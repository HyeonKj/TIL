""" #no.11720
number = int(input())

print(sum(map(int, input()))) """

#no. 2750
number = int(input())
num = []

for i in range(number):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)
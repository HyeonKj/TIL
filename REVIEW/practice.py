# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:38:32 2022

@author: user
"""

x = int(input("첫 번째 숫자를 입력하세요 : "))
y = int(input("두 번째 숫자를 입력하세요 : "))
result = 1
for i in range(y):
    result = result * x
print(result)


n = map(int, input().split())

print(min(n))

x=int(input())
y=int(input())
ans=1
for i in range(y):
    ans=ans*x
    
print(ans)


sum = 0
x = 1


for i in range(1,21):
    sum = sum + x
    x = x + i

print(sum)

print("today is running")
'''
print("7+4=",7+4)
print("7*4=",7*4)
print("7/4=",7/4)
print("2**3=",2**3)
print("5%3=",5%3)


import turtle as t

d=400

t.forward(d)
t.left(120)
t.forward(d)
t.left(120)
t.forward(d)
t.left(120)
들여쓰기를하면 반복이 안된다. 들여쓰기 중요성!!! 


for x in range(10):
    print("Hello!")
    
for x in range(3):
    print(100)
    print(200)
print(300)

    
import turtle as t

for x in range(3):
    t.forward(100)
    t.left(120)

for x in range(4):
    t.forward(100)
    t.left(90)

t.circle(100)


print("[0-4")
for x in range(5):
    print(x)

print("[1-10]")
for x in range(1, 11):
    print(x)


s=0
for x in range(1, 11):
    s=s+x
    print("x:",x,"sum:",s)

s=1
for x in range(1, 11):
    s=s*x
    print("x:",x,"sum",s)
    


import turtle as t
t.forward(100)
t.right(100)
t.forward(100)


import turtle as t
n=5
t.color("purple")
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()

import turtle as t 
n=50
t.bgcolor("black")
t.color("white")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

name = input("your name?")
print("Hello", name)


x=input("?")
a=int(x)

x=input("?")
b=int(x)

print(a*b)
'''
'''
a=3
if a==2:
    print("A")

if a==3:
    print("B")

if a==4:
    print("C")

else:
    print("D")


x= input("12+23=")
a=int(x)

if a==12+23:
    print("천재여!")
else:
    print("바보야!")


print("[1-10]")
x=1
while x<=10:
    print(x)
    x=x+1
    
s=0
x=1
while x <=10:
    s=s+x
    print("x:",x,"sum:",s)
    x=x+1

s=0
for x in range(1,11):
    s=s+x
    print("x:",x,"sum:",s)

    
def hello():
    print("just")

hello()
hello()
hello()

def hello2(name): 인자가 있는 함수 
    print("Hello",name)
    
hello2("Justin")
hello2("john")
hello2("mike")


def square(a): 결괏값이 있는 함수 
    c=a*a
    return c

def triangle(a, h):
    c=a*h/2
    return c

s1=4
s2=square(s1)
print(s1,s2)

print(triangle(3,4))


def sum_func(n):그래픽 함수응용(1~N)까지의 합
    s=0
    for x in range(1,n+1):
        s=s+x
    return s

print(sum_func(10)) 왜 이렇게 나오는 것인지 . 
print(sum_func(100)) 고민해봐야할 것 

def sum_func(n):
    s=1
    for x in range(1,n+2):
        s=s*x
    return s

print(sum_func(20))
print(sum_func(10))
'''


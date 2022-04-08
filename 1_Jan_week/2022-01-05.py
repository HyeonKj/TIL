"""
2022 - 01 - 05 ~ 1월 첫번째 주 파이썬 기초 

def add(a,b):
    return a+b
result = add(a=3, b=7)
print(result)

result = add(b=5, a=3)
print(result)

def add_many(*args):
    result=0
    for i in args:
        result=result +i
    return result

result=add_many(1,2,3)
print(result)

result=add_many(1,2,3,4,5,6,7)
print(result)

"""
'''
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args:
            result = result +i
    elif choice =="mul":
        result=1
        for i in args:
            result=result *i
    rerurn result

result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul',1,2,3,4,5)
print(result)

오류 일어남;'''
'''
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
{'a':1}
print_kwargs(name='foo',age=3)
{'age':3,'name':'foo'}

def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
result=(7,12)
result1,resutl2=add_and_mul(3,4)

def add_and_mul(a,b):
    return a+b
    return a*b
result=add_and_mul(2,3)
print(result)

def add_and_mul(a,b):
    return a+b
result=add_and_mul(3,5)
print(result)

def say_nick(nick):
    if nick=="바보":
        return
    print("나의 별명은 %s입니다is foolish"%nick)

say_nick('yahoo')
say_nick('foooool')


def say_myself(name, old, man=True이런 디폴트값은 항상 마지막에 두는 게 맞음 !) ):
    print("나의 이름은 %s입니다."%name)
    print("나의 나이는 %s살입니다."%old)
    if man:
        print("남자")
    else:
        print("여자")

say_myself("박응용",27)
say_myself("박응용",26, False)
'''
"""
a=1
def vartest(a):
    a=a+1
    print(a)
vartest(a)
print(a)

def vartest(hello):
    hello=hello+1

def vartest(a):
    a=a+1

vartest(3)
print(a)
"""
'''
a=1d
def vartest(a):
    a=a+1
    return a
a=vartest(a)
print(a)

a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)

'''
"""

add= lambda a, b: a+b
result=add(3,4)
print(result)
같은 내용이다. 아래와 같음. 램다함수 
def add(a,b):
    return a+b
result = add(3,4)
print(result)

"""
'''
add= lambda a,b: a*b
result=add(3,4)
print(result)

for i in range(10):
    print (i, end='')

    
f=open("C:/doit/새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i
    print(data)
    ''''''
f=open("C:/doit/새파일.txt",'r')
line = f.readline()
print(line)
f.close()
'''
'''
f=open("C:/doit/새파일.txt",'r')
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

while 1:
    data=input()
    if not data: break
    print(data)
'''
"""
f=open("C:/doit/새파일.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()

f=open("C:/doit/새파일.txt",'r')
data=f.read()
print(data)
f.close()
이게 젤 편한듯 

f=open("새파일.txt", 'w')
for i in range(1,11):
    data ="%d번째 줄입니다.\n"%i
    f,write(data)
f.close()


f=open("C:/doit/a.txt",'w')
f.close()

"""
'''
f=open("C:/doit/새파일.txt",'r')
while True:
    line=f.readline()
    if not line:break
    print(line)
f.close()


f=open("C:/doit/새파일.txt",'r')
data=f.read()
print(data)
f.close()

f=open("C:/doit/새파일.txt",'a')
for i in range(11,30):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

f=open("C:/doit/새파일.txt", 'w')
f.write("life is too short, you need love")
f.close()

with open("C:/doit/a.txt", "w")as f:
    f.write("Life is too short, you need python")
'''
"""
f= open("C:/doit/새파일2.txt",'w')
f.close()
"""




'''
#01-07 첫째주 금요일
'''

"""
def add_mul(choice, *args):
*"는 마지막에 들어가야 함. !!!! *args !!!

"""



def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs['a'])

print_kwargs(a=1,b=2,c=3)
''' 튜플형태, 리스트형태, 딕셔너리형태
kwrgs 주로 씀.실무에서 . '''

def add_and_mul(a,b):
    return a+b, a*b
print(add_and_mul(2,3))

'''쉘이라고 부르는 것은 cmd또한 그러하다. 프린트 안쓰고 그냥 나오는 것을 쉘이라고
합니다. 일반적으로 print꼭 써야 결과가 나옵니다.
ㅁㄴㅇㄻㄴㅇㄻㄴㅇㄻㄴㅇㄹ;
함수는 return을 맞이하는 순간 함수가 사라진다.
그 밑에 명령은 실행할 수 없다.
'''

def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
say_myself("정현경",24,0)

'''
매개변수로 안되는 것이 있음. 초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓는 것을
잊지 말자!

번역변수를 사용하는 것은 주의해야 한다. 최대한 쓰지 않도록 . 정말 필요할 때만. ㅇ
함수가 끝나는 순간 효력ㅇ ㅣ사라진다.

lambda함수는 간단하게 만들 수 있는 것이다.
def와 동일한 역할을 한다. 함수를 한줄로 간결하게 만들 때 사용
'''
"""



add1=lambda a,b:a+b
ded add2(a,b):
    return a+b
완전히 동일한 문장이다. 
    

f=open("nenenew.txt",'w')
print(type(f))

f.close()
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)
    
f=open(r"C:\Users\user\Desktop\빅데이터\python\새파일임.txt","r")
lines = f.readlines()
for line in lines:
    line = line.strip() 
    print(line)
f.close()

with문과 함께 사용하는 것이 파일 닫기를 깜빡해도 상관없기 때문에
실무에서 자주 씀. with문 쓰자. 

with open(r"C:\Users\user\Desktop\빅데이터\python\새파일임.txt","r") as f:
    lines = f.read()
    print(lines)

import sys
args=sys,argv[1:]
for i in args:
    print(1)

"""



class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

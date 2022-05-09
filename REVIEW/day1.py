'''a =2
b=3
a*b
print(a*b)

a=[]
b=[1,2,3]
c=[1,2,'life','is']
d=[1,2,'life',['is']]
print(d)
print(a,b,c)
print(d[1:])


print(len(a))

print(str(c[1])+"hi")
a= [1,2,3,4,5]
print(a.append(4))
print(a)
a.append([3,2,1])
print(a)

a= [1,2,3]
a.index(3)
# 2
# a.index(1)
# 0 
a.reverse()

a.pop()
#3
a=[1,2]

a.count(1)

a.extend([4,5])

t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a','b',('ab','ac'))

del t1[0]

t1=(1,2,'a','b')
t1[0]='c'
'''
# 함수를 선언한다.
def 함수이름():
    print("안녕하세요") #2 #6
    print("안녕하세요") #2 #7
    print("안녕하세요") #4 #8

# 함수를 호출한다.
함수이름() #1
함수이름() #5

# 매개변수 만들기
def 함수이름(매개변수1, 매개변수2, 매개변수3, 매개변수4):
    print("안녕하세요" + str(매개변수1))
    print("안녕하세요" + str(매개변수2))
    return 매개변수1 + 매개변수2 + 매개변수3 + 매개변수4
    print("안녕하세요" + str(매개변수3))
    print("안녕하세요" + str(매개변수4))
    return 매개변수1 + 매개변수2 + 매개변수3 + 매개변수4

함수이름(1,2,3,4)

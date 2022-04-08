'''for x in [8,(4,5,6),{4,5,6}]:
    print(x)
    
(a,b)=(1,2)
print(a,b)

for(a,b)in[(3,4),(4,5),(6,7)]:
    print(a+b)
a="apple"
b=["apple","banana"]
c=(4,5,6)
for x in a:
    print(x, end="")


a=[4,5,6,7]
for x in range(len(a)):
    if a[x]<4:
        continue
    print("%d값으로 pass"%(a[x]))
for x in range(1,10):
    print("2x%d=%d"%(x,2*x))
for x in range(1,10):
    print("3 X%d=%d"%(x,3*x))
    

a=(input("숫자를 입력하세요"))
for x in range(1, 10):
    print("%d X %d = %d"%(a, x,a*x))

a=int(input("숫자를 입력하세요"))
for x in range(1,10):
    print("%d x %d = %d"%(a, x,a*x))
    
for x in range(1, 10):
    for x1 in range(1, 10):
        print("%d X %d = %d"%(x, x1,x*x1))
print("\n")

tree=0
while tree <10:
    tree=tree+1
    print("나무를 %d번 찍었습니다."%tree)
    if tree ==10:
        print("나무가 넘어갑니다.")


prompt ="""
1.Add
2.Del
3.List
4.Quit
enter number:"""
number = 0
while number !=3:
    print(prompt)
    number=int(input())
    
        


coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee-1
    print("남은 커피의 양은 %d개 입니다."%coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


    
coffee =10
while True:
    money=int(input("돈을 넣어주세요"))
    if money ==300:
        print("커피를 줍니다.")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피를 줍니다."%(money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다."%coffee)
    if coffee ==0:
        print("커피가 다 떨어졌다. 판매중지한다.")
        break


a=0
while a<10:
    a=a+1
    if a%2==0: continue
    print(a)
while True:
    print("ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.")

    import random
    난수로 생성 실수를 난수로 생성 ??? 정수를 난수로 생성 랜덤이 정수
print(random.randint(1,100))
    

import random
실수를 난수로 생성
for x in range(5):
    print(random.random())
print("="*30)

특정범위의 실수를 난수로 생성
for x in range(5):
    print(random.uniform(1,100))
print("="*30)
정수를 난수로 생성
for x in range(6):
    print(random.randint(1,100))
print("="*30)
정수를 step을 더해서 난수로 생성 
for x in range(5):
    print(random.randrange(1,100,10))
    
'''

a="life is too short, you need python"
if"wife" in a : print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a : print("need")
else: print("none")

n=0
s=0
while n<1000:
    n+=1
    if(n%3)!=0:continue
    s=s+n
print(s)


num = 0
while num <4:
    num+=1
    print("*"*num)

sum = 0
for x in range(1,101):
    sum += x
print(sum)

A=[70,60,55,75,95,90,80,80,85,100]
sum=0
for x in A:
    sum+=x
print(sum/10)

numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)

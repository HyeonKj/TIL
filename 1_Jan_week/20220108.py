"""
미션 알고리즘 :Q1.

x=int(input("숫자를 입력하세요:"))
if x%2==0:
      print("짝수입니다.")
else:
    print("홀수입니다.")
            



a=int(input("숫자1을 입력하시오."))
b=int(input("숫자2을 입력하시오."))
c=int(input("숫자3을 입력하시오."))

x=(a,b,c)
print(min(x))
"""
"""

a=int(input("숫자1 입력:"))
b=int(input("숫자2 입력:"))
c=1
for i in range(int(b)):
   c*=int(a)
print(c)



x=int(input())
y=int(input())
ans=1
for i in range(y):
    ans=ans*x
    
print(ans)
"""
"""
a=0.0
b=0.0
for i in range(1,100,2):
    a=a-(i/(i+1))
for i in range(2,100,2):
    b=b+(i/(i+1))
print(a+b)

"""

a=0
sum=0
for i in range(1,21):
    sum+=i
print(sum)

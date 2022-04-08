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

#a=0
#sum=0
# for i in range(1,21):
#     sum=sum+i
# print(sum)

# print(12*1)

# print('풍선')
# print("나비")
# # print("하"*10)
#참/거짓
# print(5>10)
# print(5<10)
#애완동물을 소개해주세요~
# print("우리집 강아지의 이름은 연탄이에요")
# print('연탄이는 4살이며, 산택을 아주 좋아해요')
# print("연탄이는 어른일까요?")
# animal="강아지"
# name="연탄이"
# age=4
# hobby="산책"
# is_adult=age>=3
'''
print("우리집"+animal+"의 이름은"+name+"이고 예뻐요.")
hobby="공놀이"
print(name+"는"+str(age)+"살이며,"+hobby+"을 아주 좋아해요.")
print(name,"는",age,"살이며,",hobby,"을 아주 좋아해요")
print(name+"는 어른일까요?"+str(is_adult))
'''
# station="인천공항"
# print(station+"행 열차가 들어오고 있습니다.")
# print(5%4)
# print(2**3) #2의 3승
# print(5//2) # 몫을 구하는 것 
# print(2^3)

from dataclasses import replace


print("READ\bApple")
print("rad      apple")
url="http://naver.com"
my_str=url.replace("http://","")
print(my_str)
my_str=my_str[:my_str.index(".")]
print(my_str)
password=my_str[:3]+str(len(my_str))+str(my_str.com)
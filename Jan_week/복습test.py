s1=set([1,2,3])
s1
"이스케이프 코드 "

"""
01-07 초기 복습 내용. 반복함. 3번째라고 하심
알긴 알겠는데... 적용을 혼자 못하겠음
문자열 포매팅 ... 3가지
스트링은 데이터값 고정
포매팅은 데이터값을 변경시키고 싶을 때 외부데이터가 적용시킬 수 있게 하기 위해서
쓴다. %데이타 %d 숫자 대입 %s 문자대입
{}중괄호 ""객체라서 명령어 입력 가능. 
%0.4f '0'은 데이터 위치 최대 자릿수 .
0번째 1번째.
"{{234}}"이렇게 두번써서 문자로 나타낸다.
f문자열 포매팅 d.get 숫자값 가져올 수 있음ㅇ.
a.count 문자가 몇개가 있는지 세림 
a.find 몇번째 문자인가 없는 문자는 NONE, -1로 표기 
문자에 관련된 함수.

a. index 못찾으면 시스템 메시지를 날것으로 뿌려준다. 에러표시

upper/ lower
lstrip/ rstrip /strip

아스키코드 A하고 a하고 컴퓨터에서 다른 단어로 표기됨. 구분 O
컴파일 = 사람이 알아볼수잇는 단어를 컴퓨터로 바꿔주는 거시기
replace
split
list []
 리스트 예시 a= [2,3,['fide','is']]
 리스트명 = [요소1, 요소2 요소3...]
 리스트도 인덱싱 가능
 더하기 곱하기 가능
 sort
 reverse
 index
 insert
 remove
 a.remove()
 pop 끄집어내기 1,2,3 pop(3) => 1,2 만 남음
 count ㄸ
 extend 풀어서 들어감.
 튜플은 수정이 불가능함(). 리스트는 수정 가능 []
 소괄호가 튜플, []대괄호가  리스트 .
 삭제도 불가능함. 변경하지도 못함 튜플은.
 나머지 연산, 다 가능
 딕셔너리 자료형
 키벨류



KEY1:VALUE1, KEY2:VALUE2,
{'a':'pey',1:'a',1:'b'}XXX
딕셔너리 만들때 중복으로 쓰면 안됨. 키값이 유일해야함 
a. keys 키값만 뽑는다.
for k in a.keys():
print(k)
pey
a
b


집합 자료형
&|union.
1add1개 추가할때 .


불자료형
True False type(a) type(b)
1==1 2>1 3<5
데이터가 있으면 다 참이다. [] () {} 거짓. 0,"",거짓
변수라는 것은 데이터를 메모리에 공간이 생기는 것


ㅁ,ㅠ=ㅠ,ㅁ a,b=b,a 바꾸면 될 듯 .
input ("값을 입력하세여.:")
print=출력기기
이프문.
x in list []not in 맞으면 트루 아니면폴스 
x in () not in
x in () not in

pocket = ['종이','돈']
if '돈'in pocket:

elif card:
else
조건문 표현식 한줄로도 쓸 수 있음 조건이 가운데로 옴.



함수 *args) 튜플이 . .. choice 'mul' 매개변수를 중간에 넣을 수는 없다.
함수안에서 변수의 효력 범위
a=1
def vartest(a)
a=a+1
print(a)
=1ㅇ 된다.
return값을 설정하거나 글로벌을 사용하여 함수안에서 쓰는 메모리를 밖에서도
받아서 처리할 수 있도록 하는 방법 임.
global a(=나 외부에 있는 애야~ )내부에서 직접적으로 외부애를 찾아서
쓰기 때문에 .

lambda 함수 a,b: a+b
add = lambda a,b : a+b
result
f=open("새파일.txt", 'w')
f.close()
파일 객체 = open(파일 이름, 파일 열기 모드)

r = 파일을 읽기만 할 때 사용 
w= 쓰기모드 
a=추가 모드 


f.open("새파일.txt",'w')
역슬래시를 두개하거나 해야 에러가 안남.

for i in rage(11,20):
data="%d ~~~"%i

컬렉션이라고 부르는 애들 특징. 문자열, 리스트, 튜플, 딕셔너리, 집합,등
반복가능한 애들. 반복하는데 쓰인다. 

"""

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

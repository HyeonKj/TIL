""" # 문자열은 변경 불가능한 자료형이다.
word = "aplle"

word+= " banana"
print(word)

s='abcdefghijklmnopqrstuvwxyz'
print(s[::2])
# [Start:end:step뛰어넘는거]
# s[2:5:-1]에서 -1은 #반대방향

print(s[::-1]) #전체를 반대 방향으로 인출
# 만일 범위 밖의 s[220:300] ''에러나지 않고 빈문자열이나온다.

#10988 BOJ 팰린드롬인지 확인하기 
word = input()
print(1 if word==word[::-1] else 0)

w = input()
n = 0 """

""" #오타맨 고창영 no.2711
t=int(input())

for i in range(t):
    n, word = input().split()
    n=int(n)
    print(word[:n-1]+word[n:]) """

""" #태보태보 총난타 no.17248
l, r=input().split("(^0^)")
print(l.count('@'),r.count("@")) """

""" # no.2789 유학금지
data = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

value = input()
for i in range(len(value)) :
  if value[i] not in data :
    print(value[i], end='') """

""" #no.2789 replace 사용

word = input()

for i in ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']:
  word = word.replace(i, "")

print(word)

# 유학 금지
word = input()

for i in "CAMBRIDGE":
    word = word.replace(i, "")

print(word) """

#특수 문자 출력하기 
print("문자열")
print("따옴표출력안됨""")
print('따옴표출력\"\"')
print("\\")
print(r"\\")
print("한줄 \n 두번째 줄")
print("한\t줄 \n 두\t번\t째 줄\t")
print("\"안녕하세요\'")
print("\"C:\Download\\'hello'.py\"")
print('print("Hello\\nWorld")')
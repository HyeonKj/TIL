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

#태보태보 총난타 no.17248
l, r=input().split("(^0^)")
print(l.count('@'),r.count("@"))
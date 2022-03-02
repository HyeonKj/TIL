# 문자열은 변경 불가능한 자료형이다.
word = "aplle"

word+= " banana"
print(word)

s='abcdefghijklmnopqrstuvwxyz'
print(s[::2])
# [Start:end:step뛰어넘는거]
# s[2:5:-1]에서 -1은 #반대방향

print(s[::-1]) #전체를 반대 방향으로 인출

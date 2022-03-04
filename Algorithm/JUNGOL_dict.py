""" # 딕셔너리 기본 문제 
animations = {
    "Pockemon" : "Pickachu",
    "Digimon" : "Agumon",
    "Yugioh" : "Black Magicion"
}

word = input()
# if word in animations:
#     print(animations[word])
# else:
#     print("I don't know")

print(animations.get(word, "I don't know")) """

# 딕셔너리 기본 문제 2
# num = int(input())
# nat_cap = {}

# for i in range(num):
#     word = input().split()
#     nat_cap[word[0]]= word[1]

# word = input()
# print(nat_cap.get(word,'Unknown Country'))

#### 다른 방법 #####
# num = int(input())

# dict = {}

# for i in range(num):
#     country = input().split()
#     dict[country[0]] = country[1]

# country = input()
# print(dict.get(country, "Unknown Country"))

# dictionary 
foul = list(input().split())
dic = {}

for name in set(foul):
    dic[name] = foul.count(name)

min_foul = min(dic.values())

for name in dic:
    if dic[name] == min_foul:
        print(name)
print(min_foul)
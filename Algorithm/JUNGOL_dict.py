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
# n = int(input())
# countries = {}

# for i in range(n):
#     country, city = input().split()
#     countries[country] = city

# print(countries.get(input(), "Unknown Country"))

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

# dictionary 3번 파울 횟수 
# 딕셔너리 만들기
""" players = input().split()
fouls = {}

for player in players:
    # 1)이미 선수가 있어요?
    if player in fouls:
        fouls[player] +=1
    #2) 선수가 없어요?
    else:
        fouls[player] = 1

# 2. 최소 파울 갯수 찾기 
min_foul = min(fouls.values())

# 3. 가장 파울 적게 한 선수 출력
for player, foul in fouls.items():
    if fouls== min_foul:
        print(player)

# 4. 최소 파울 갯수 
print(min_foul) """
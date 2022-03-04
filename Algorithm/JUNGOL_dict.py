# 딕셔너리 기본 문제 
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

print(animations.get(word, "I don't know"))


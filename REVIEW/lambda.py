# map(함수, 리스트)
map(lambda x: x ** 2, range(5))             # 파이썬 2
[0, 1, 4, 9, 16]  
list(map(lambda x: x ** 2, range(5)))     # 파이썬 2 및 파이썬 3
[0, 1, 4, 9, 16]

# lambda 매개변수 : 표현식

# >>> def hap(x, y):
# ...   return x + y
# ...
# >>> hap(10, 20)
# 30

# 램다 함수식 표현
# >>> (lambda x,y: x + y)(10, 20)
# 30

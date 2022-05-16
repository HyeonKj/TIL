'''
데이터 프레임
열 삭제 
하는 방법

df.drop(['삭제할 열이름','삭제할 열 이름2'], axis = 1, inplace=True)

axis = 1 삭제를 가로로할 것인지 세로로할 것인지에 따라서 0과 1이 붙는다. 
열 기준으로 삭제할 때는 axis = 1 이라고 기입. 혹은 
axis = columns라고 쓸 수 있다. 
p.s 자꾸 까먹지 말라. 
'''
# df.drop(['a'], axis=1, inplace = True)

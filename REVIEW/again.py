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
# import folium
'''
라이브러리 
사용법
# branca 라이브러리 수정사항 반영 
pip install git+https://github.com/python-visualization/branca.git@master
 
# 행 열 전환
데이터프레임이름.transpose()
데이터프레임이름(columns=데이터프레임이름.iloc[0],inplace=True)와
데이터프레임이름=데이터프레임이름.drop(데이터프레임이름.index[0])를 해주면 행열 전환을 잘 마무리 할 수 있다.

# 예시
df = df.transpose()	#행 열 전환
df.rename(columns=df.iloc[0], inplace=True)	# 행열이 전환된 데이터프레임의 열 이름 제대로 수정
df = df.drop(df.index[0])
 '''
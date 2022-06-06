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



### 슬라이싱 
city = 'seoul'
print(city[-1])  # 결과 값: l
print(city[-2])  # 결과 값: u
print(city[-3])  # 결과 값: o
print(city[-4])  # 결과 값: e
print(city[-5])  # 결과 값: s

객체 = [start:end:step]
start : 객체에서 가져올 시작 인덱스(index)값입니다. start 인덱스(index)값부터 객체에 일부를 가져옵니다.
end : end는 말 그대로 마지막 객체까지의 값을 가져올 인덱스(index)값입니다. 여기서 주의해야 될 점은 start는 start 인덱스(index) 값부터 시작이지만 end는 end 인덱스(index)값 전까지 객체를 가져옵니다.
step: step은 step 인덱스(index) 만큼 건너뛰어서 객체 값을 가져옵니다. (생략할 경우 인덱스(index) 값은 1이 됩니다.

code_name_last:
nonetype = nothing_to_do
what. am i doing for , at the moment get your feels
every day is painful
but , i know that this situation will be come.
so whatever

딕셔너리.get()
dict.keys()
dict.values()


plotly 라이브러리 시각화가 예쁘게 잘 나온다, 
import plotly.graph_objsasgo
import plotly
data=[ go.Bar( x=['x1', 'x2', 'x3', 'x4'], y=[11, 13, 17, 19] )] layout = plotly.graph_objs.Layout( title='Bar-chart') figure = plotly.graph_objs.Figure( data=data, layout=layout) plotly.offline.plot(figure, filename='basic_bar_chart.html')


 '''
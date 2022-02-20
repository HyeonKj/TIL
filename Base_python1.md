1. 라이브러리 불러오기
import [라이브러리] as [사용할이름]

2. 파일 불러오기 
import pandas as pd
data = pd.read_csv('파일경로/파일이름.csv')

3. [DataFrame 변수명].shape
ex. 데이터 다운로드 ~
# 데이터 다운로드 링크로 데이터를 코랩에 불러옵니다.

!wget 'https://bit.ly/3gLj0Q6'

import zipfile
with zipfile.ZipFile('3gLj0Q6', 'r') as existing_zip:
    existing_zip.extractall('data')


import pandas as pd

#데이터 불러오기
train = pd.read_csv('data/train.csv') 
test = pd.read_csv('data/test.csv')

4. python 데이터 확인하기 
import pandas as pd

train = pd.read_csv('data/train.csv')

train.head() # train 데이터의 상단 5개 행 출력
ex. 
import pandas as pd

train = pd.read_csv('data/train.csv')

# 정답 코드
train.head(100) 

5. 결측치 확인하기 
import pandas as pd
import numpy as np

df = pd.DataFrame({
        'name': ['kwon', 'park', 'kim'],
        'age':[30, np.nan, 19],
        'class':[np.nan, np.nan, 1]

df.isnull().sum()
-------------------------

import pandas as pd

train = pd.read_csv('data/train.csv') 
test = pd.read_csv('data/test.csv')

print(train.isnull())
print('\n--------------------------------train.csv 각 열 별 결측치 수--------------------------------\n')
print(test.isnull().sum()) 

6. 전처리 파이썬 데이터 기본 정보 
df.info()
--------------------

info() 매서드를 사용하면 피쳐들의 기본 정보(결측치와 데이터 타입 등 )를 확인할 수 있습니다. 모델링에 앞서 결측치가 있다면, 결측치들을 어떻게 다뤄야할지 고민하고 처리하는 과정이 필요합니다.

7. 전처리 파이썬 결측치 삭제, 대체
dropna()를 사용하면 결측치를 갖는 행을 데이터프레임 객체에서 삭제합니다.
DataFrame.dropna()
DataFrame.fillna() -> fillna()를 사용시 모든 결측치를 인자값으로 대체할 수 있습니다. 

#결측치 데이터 제거
train.dropna(inplace =True)

#결측치 특정 상수 값으로 대체
train.fillna(0,inplace = True)

#결측치 해당 변수 평균 값으로 대체
train.fillna(train.mean(),inplace = True)
test.fillna(train.mean(),inplace = True)

#결측치 보간법으로 채우기
train.interpolate(inplace=True)

8. 연속형 변수 변환
#연속형 변수 시각화
for col in train.columns:
    plt.figure(figsize = (4,4))
    plt.title(col)
    sns.histplot(train[col])
    plt.show()
    
#데이터 분포가 불균형한 경우  Min-Max Normalization

#train['hour_bef_pm2.5'] = np.log1p(train['hour_bef_pm2.5'])
#train['hour_bef_pm10'] = np.log1p(train['hour_bef_pm10'])

test['hour_bef_pm2.5'] = np.log1p(test['hour_bef_pm2.5'])
test['hour_bef_pm10'] = np.log1p(test['hour_bef_pm10'])

sns.histplot(train['hour_bef_pm2.5'])


9. 모델링
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()

X_train = train.drop(['id','count'],axis =1)
y_train = train['count']
X_test = test.drop('id', axis = 1)

from sklearn.model_selection import GridSearchCV

RandomForestRegressor()

param = {'min_samples_split': [30, 50, 70],
        'max_depth': [5, 6, 7],
        'n_estimators': [50, 150, 250]}

gs = GridSearchCV(estimator=model, param_grid=param, scoring = 'neg_mean_squared_error', cv = 3)

gs.fit(X_train, y_train)



10. 제출파일 생성 

submission = pd.read_csv('data/submission.csv')
pred = gs.predict(X_test)
submission['count']  = pred
submission.to_csv('gridsearch.csv', index = False)
======================
## LSA 의 특징 0321 
# theory studying
=======================


======================
# 02- 03-25-2022

- 관찰된 X를 설명하는 z의 존재를 가정
- Z는 은닉 또는 잠재 변수

* 잠재변수는 관찰 불가능 하거나 또는 현재 데이터에 포함되지 않은 변수를 말한다. 
* 주로 이론적으로 가정되는 개념(사랑, 지능, 등)

- 텍스트에 대한 비지도 학습 
- 문서의 단어 빈도에 영향을 미치는 잠재변수를 가정 
    - 위의 잠재변수를 = 주제(topic)이라고 함. 
## 일상의 의미에서의 우리가 알고 있는 주제와는 다름 

- 행렬 분해에 의한 방법. 
- 확률 분포에 의한 방법. 
LSA의 Z값을 구해야 하는 데 쓰이는 방법 
1. 행렬 분해
m x n 크기의 행렬은 m x k크기의 
선형 모형 y = wx + b 도 행렬의 곱셈 형태로 나타낼 수 있음.



======================
- 계산이 비교적 단순하다
- 통계학에서 매우 많이 사용
- 주제의 해석이 어려움 
- 차원의 수를 정하기 어려움
- 제약을 걸더라도 해가 많음 . 

단어 문서를 행렬 X를 ZW의 형태로 표현 
차원 축소 : 단어보다 주제의 수가 적음

====================
단점이 이렇게 많은 데 왜 ? 쓰느냐, 장점도 있다. 문서의 유사도를 알아보고 싶을 때, 
==============

특이값 분해 (SVD): 행렬 분해 

- 하나의 행렬을 여러 개의 행렬의 곱 형태로 나타내는 것
    - LU 분해
    - QR 분해 
    - 촐레스키 분해
    - 고유값 분해
    - 특이값 분해 

===================
* TDM은 m개의 문서를 표현하기 위해 n가지 단어로 표현
* U*은 m개의 문서를 k가지 주제로 표현
* n >> k이므로 문서를 나타내는 **차원이 축소**되었다고 이해할 수 있음 

# **LSA = truncated LSA를 통해 차원축소한 것. 텍스트의 구조를 파악하는 방법이다** 
======================

### 차원 축소의 시각적 이해 
- 문서들이 단어가 아닌 의미상으로 재배치
- 동음이의어, 오탈자 등이 어느정도 처리됨
- 문서에 존재하는 noise가 줄어서 더 잘 분류됨. 

========
# LSA 실습 
========

''' 
pip install wget # wget 설치 

!wget -c https://github.com/euphoris/datasets/raw/master/neurips.zip

import wget
wget.download('https://github.com/euphoris/datasets/raw/master/neurips.zip')

import pandas as pd
df = pd.read_csv('neurips.zip')
df.head(10)

df.tail()

#전처리 

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
cv = TfidfVectorizer(stop_words = 'english', max_features = 2000)

#SVD
from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=100, random_state=1234)
x.shape

svd.fit(x)
svd.components_.shape
svd.components_

word_idx = words.index('topic')
word_idx

svd를 했다는 것은 문서가 차원과 어떤 관계가 있느냐, 
혹은 차원과 단어가 어떤 관계가 있느냐를 알 수 있다. 
이 차원으로 문서를 설명할 수 있고 단어를 설명할 수 있다.

1. 문서가 차원과 어떤 관계가 있느냐.
2. 차원과 단어가 어떤 관계가 있느냐.


========================
### 회전 
========================

### LSA는 해가 무수히 많음

### R은 kxk 형태의 행렬, R(-1)승은 그 역행렬

### kxk행렬은 k차원에서 회전을 나타냄 

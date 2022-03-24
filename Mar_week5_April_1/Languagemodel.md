# 언어 모형과 n-gram 
===================
## : 자연어 문장의 확률을 계산하는 모형 
### 예) a. 나는 밥을 먹었다. 
###     b. 나는 밥을 마셨다. 
##     a)가 b)보다 확률이 높음. 

# 언어 모형은 다양한 자연어 처리에 활용됨.

## 사전학습(pre-training) : 언어 모형은 텍스트만으로 학습이 가능 
##          - 사전 학습된 언어 모형으로 학습 효율을 높임


## 자연어 생성 :
##              자연어 문장을 생성할 때 확률이 높은 표현을 고를 수 있음. 

=======================
## n-gram =  n개의 토큰을 묶어서 세는 것 

## gram = 글이나 그림(그리스어)instagram, grammer

ex. " i have a dream"
1-gram : i, have, a , dream
2-gram : i have, have a, a dream
3-gram : i have a , have a dream
=================================

### n-gram 언어 모형
- 문장을 이루는 토큰의 확률을 n-gram으로 추정 
- 문장의 확률 = 토큰의 확률의 곱

* n=1
* 모든 토큰이 독립
* 직전에 무슨 토큰이 나오든지 다음 토큰에 영향 X 

## UNK와 혼란도

## 라플라스 평활 Laplace Smoothing
- 모든 경우의 빈도에 1을 추가 

- add-one smoothing = 스무딩을 디스카운팅이라고 함
- discounting이라고 함(관찰된 사례의 확률이 줄어드므로)

### interpolation : 여러 n-gram을 가중평균하여 토큰의 확률을 구함

==========
# 신경망 언어 모형 
## 신경망을 이용한 언어 모형
### 이전의 토큰을 원-핫-인코딩 된 형태로 입력
### 다음의 토큰을 예측(다항 분류 )

==========
# 단어 임베딩 : 단어를 실수 벡터 형태로 표현하는 것 

## 신경망에 임베딩 레이어를 추가하여 단어 임베딩을 얻을 수 있음 

## 임베딩 레이어는 Dense 레이어와 거의 동일함. 
## 입력에 가중치를 곱하여 출력. 
## 입력이 원핫 인코딩이므로, 가중치의 각 행이, 각 단어의 임베딩에 해당함. 


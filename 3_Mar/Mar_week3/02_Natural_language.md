
- 자연어 : 한국어, 영어 등등
- 인공어 : 에스페란토 
- 통제자연어 
- 형식어 : 수식 프로그래밍 언어 등 
================================

### 텍스트 분석으로 할 수 있는 것
- 텍스트에서 정보나 패턴을 추출 
    EX. "어제 서울역에서 사 먹은 김밥이 맛있었다."
        - 개체명 인식(장소, 음식 등에 대한 정보) / 관계 추출/ 감성 분석(태도)

- 대량의 텍스트에 대한 정리/ 통계
    - 논문, 뉴스, SNS 

- 텍스트를 통해 사람을 평가
    - 논술, 자기소개서, 에세이 
    - 객관식은 한계가 많으나 일관성 있는 채점이 가능
    - 텍스트는 일관성 있는 채점이 어려움
    - 텍스트 분석으로 일관성 있고 타당한 채점 


- 인간과 컴퓨터가 자연스럽게 소통 
    - 음성 인식 (빅스비, 시리, 지니 등)
    - 챗봇 

**책추천 : 단어 사생활**
===========================


## 텍스트 분석의 특징 
- 순차적 데이터
    - 데이터의 값들에 순서가 있다.**순서가 중요하다**
    - 어순이 중요함.
    - 의존성: 이전에 나온 말이 이후에 나올 말에 영향
    - 다른 순차적 데이터에 비해 매우 긴 의존성을 가지고 있음


- 이산 변수 
    - 주가 : 순차적 데이터지만 연속적으로 변화함
    - 텍스트 : 각각의 단어는 서로 구별되는 이산변수, 불연속적인 변화
    - 성인이 아는 단어는 평균적으로 2만 ~ 5만 개 
    - 차원(=변수의 수 =단어의 수)이 매우 큼 > 차원의 저주 


- 복잡한 구조 
    - 텍스트에는 보이지 않는 문법적 구조가 존재.
    - 재귀(recursion):하나의 구조 안에 동일한 구조가 포함
    - 긴 의존성의 원인 중 하나

- 모호성(ambiguity)
    - 텍스트에는 거의 항상 모호성이 존재함
    - 동음이의어 : 은행(먹는 은행), bank
    - 문장 구조 : 동생과 고기를 먹었다. 


- 언어의 다양성
    - 전 세계에 수 천개의 언어가 존재(소수 민족이 쓰는 언어까지 수 많음)
    - 언어 간 공통점과 차이점이 있음(예: 피라항어 논쟁) 
    - 주로 텍스트 데이터의 전처리 과정에 큰 차이
    - 한국어의 경우 전처리에 필요한 공개된 자료가 **부족**하다.

*특징들은 분석을 대체적으로 어렵게 만드는 요소들이다. 
============

### 텍스트 분석의 절차 
- 토큰화 
    - 토큰 : 텍스트 분석의 단위 (단어, 형태소 등등)
    - 형태소 : 의미가 있는 최소 단위
    - 단어 : 홀로 쓰일 수 있는 형태소 
    - 단어 분리 : 띄어쓰기를 하지 않는 중국어, 일본어 등 

- lemmatization : 사전에 등재된 형태로 바꾸는 것 
- stemming : 휴리스틱을 이용해 어간을 분리해내는 것 

- 기타정규화
    - 대소문자 정리
    - 불필요한 공백 제거, 특수문자, 문장부호 등 삭제 
    - 축약 표현 
    - 불용어(안 쓰는 단어) 처리(빼버림)

- 데이터 정리
    - **단어 문서 행렬** TDM 
        - 어순을 무시 
        - 문서별로 단어의 출현 빈도를 표 형태로 정리 
    - 토큰들을 출현한 순서대로 정리 

데이터 전처리 이후 
============
지도학습과 비지도 학습 : 기계 학습(machine learning)

* 지도 학습 (supervised learning)
    - X로 Y를 예측 
    - X와 Y, 두 가지 데이터가 필요
    - 보통 X가 텍스트

- 지도학습에서 주의할 점 
    - Y에 해당하는 데이터가 반드시 필요 
        - 예) 맛집 리뷰(x)가 진짜(y)인가 ? 
    - Y를 알 수 없음 
    - Y를 알아낼 수 있는 대안적 방법 모색 

* 비지도 학습 (unsupervised learning) : 머신 러닝이 데이터를 학습하는 방법 중 하나이다. 비지도 학습에는 알고리즘이 자체적으로 이해해야 하는 레이블이 지정되지 않은 데이터가 있습니다. 

ex. 머신 러닝이 자전거 타는 법을 배우는 아이였다면 지도 학습은 자전거를 똑바로 잡고 뒤에서 달리는 부모인 것입니다. 비지도 학습은 자전거를 넘겨주고 아이의 머리를 쓰다듬고 '행운을 빌어요'라고 말하는 것과 같습니다.

=======================
### 텍스트 분석의 절차 : 텍스트 분석의 방법과 절차 
- 파일 / 데이터 베이스 
- 웹스크래핑
- 음성 인식 
- 광학 문자 인식 
* 말뭉치(corpus): 수집된 텍스트 데이터 

===================
2022 - 03 - 14
=======================
# 텍스트 분석의 종류 

## 1. 문서 분류 : 

#### 문서를 미리 정해진 유형으로 분류하는 것 
#### 뉴스 기사나 백과사전 항목 등
#### 가장 널리 사용되는 텍스트 분석의 하나 

## 2. 감성 분석(sentiment analysis) 
#### 문장에 나타난 긍/부정의 태도를 분류 ex. 찬반이나 긍부정. 
#### 기쁨, 슬픔 등 구체적인 감정으로 나누는 것이 정서 분석(emotion analysis)

## 3. 개체명 인식(Named)
#### 사람, 장소, 단체 등 특정한 종류의 이름을 인식
#### 테스트에서 특정한 종류의 정보를 추출하고자 할 때 가장 기본이 됨.
#### 이름은 여러 단어로 되어 있을 수 있고, 계속해서 새로운 이름이 생기기 때문에 사전으로 만들기 어려움 

## 4. 관계 추출 

## 5. 의도 탐지 
#### 주로 챗봇에 사용 
#### 사용자의 의도를 정해진 유형 중에 하나로 분류하고 정해진 정보의 슬롯을 채움 

## 6. 요약(summarization)
#### 긴텍스트를 짧은 텍스트로 요약
#### 중요한 문장을 발췌하는 방법 , 새로운 짧은 텍스트를 만드는 방법. 2가지 
#### 정답이 없기 때문에 평가하기가 어려움 


## 7. 기계번역
#### 한 언어로 된 문장을 다른 언어로 번역 
#### 병렬 말뭉치가 필요.

## 8. 질의 답변


## 9. 상식추론


## 텍스트 분석의 문제점 

- 최근의 자연어 처리 기법은 고도로 발전, 복잡.
- 예측이나 분석결과가 나온 이유를 해석하기가 어려움 . 

- 대부분 Y에 해당하는 데이터가 부족. 
- 영화 줄거리 X로 흥행 Y을 예측? 

- 편향 
    - 데이터가 편향되어 있다면 학습한 패턴도 편향
    - 텍스트에는 다양한 편견과 고정관념이 반영되어 있음
    - 자동화된 자연어 처리 시스템은 학습된 편향을 빠르게 증폭시킬 수 있음 

        - 기억할 점 
            - 텍스트 분석의 문제점을 극복하는 다양한 기법이 발전 중 
            - 분석가는 해결/ 보안할 방법을 모색할 필요가 있음 

### 데이터 부족을 극복하기
- 데이터를 더 많이 모은다. 
    - 사람들에게 작업을 시킴
    - 서비스의 사용자들로부터 데이터를 수집

- 비지도학습으로 패턴을 추출 -> 추출한 패턴으로 지도학습 

================

# 자연어 처리란

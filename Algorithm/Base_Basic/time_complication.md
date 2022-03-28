2022 - 03 - 03

알고리즘의 시간 복잡도 
--------------------
지료형 - =
int, float 같은 것들을 자료형이라고 하고 데이터를 메모리에 저장되는 정수나 실수 같은 것들. 

RAM은 휘발성, 파이썬 파일을 실행하고 끌때까지만 존재

* 자료 구조 == Data Structure
자료 구조는 데이터를 연산하는 기능을 제공하는 것이다. 

데이터를 읽기, 쓰기, 삽입, 삭제, 탐색할 수 있는 연산 기능을 제공한다. 

# 어떤 알고리즘이 좋은 알고리즘인가???

# input을 넣은 후 Ouput이 나오는 시간이 적은 알고리즘이 좋은 알고리즘이다. 
# 그렇다면 시간을 어떻게 재는가?
## 초를 잰다. -> 연산을 센다(횟수)

-------------------

# BIG O 표기법
- 입력 n이 무한대로 커진다고 가정하고 시간 복잡도를 간단하게 표기하는 것. 
= > **최고차항만** 남기고 계수와 상수 제거 

- 다양한 시간 복잡도 종류 
    - 빅오 표기법 => O(n), **O(1)**<입력이 아무리 들어와도 상수시간 안에 끝남/ O(log n), O(n2) 등 
    - 1초에 1억 번 연산으로 계산을 한다. 2초는 2억번.
    - 
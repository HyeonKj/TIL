

## 하루에 했던 일과들을 담는다.
## 복습하면서 기억에 남는 것들과 오류들을 서술하고 오답노트를 작성한다.
## 코드를 이해한다. 
## 비슷한 다른 코드들을 보고 분석한다. 

. **유용한 단축키**

        - `위, 아래 방향키` : 과거에 작성했던 명령어 조회
        - `tab` : 폴더/파일 이름 자동 완성
        - `ctrl + a` : 커서가 맨 앞으로 이동
        - `ctrl + e` : 커서가 맨 뒤로 이동
        - `ctrl + w` : 커서가 앞 단어를 삭제
        - `ctrl + l` : 터미널 화면을 깨끗하게 청소 (스크롤 올리면 과거 내역 조회 가능)
        - `ctrl + insert` : 복사
        - `shift + insert` : 붙여넣기

  4. **VSCODE**

  5. **MARK DOWN /**

     1. 1. 제목

        # 제목

        ## 제목

        ### 제목

        #### 제목

        ##### 제목

        ###### 제목

        ```# 제목 1 ## 제목 2 ### 제목 3 #### 제목 4 ##### 제목 5 ###### 제목 6```

        

        

        * **목록**

          

          - 순서가 없는 목록과 순서가 있는 목록을 표현합니다.

          - 순서가 없는 목록은 `- * +` 를 사용합니다.

        - 순서가 있는 목록은 `1. 2. 3.` 과 같은 숫자를 사용합니다.

        - `tab 키`를 이용해서 들여쓰기를 할 수 있습니다.

        - 작성

          ```markdown
          - 순서가 없는 목록
          	- 서브 목록
          	- 서브 목록
          
          + 순서가 없는 목록
          	+ 서브 목록
          	+ 서브 목록
          
          * 순서가 없는 목록
          	* 서브 목록
          	* 서브 목록
          
          1. 순서가 있는 목록
          	1. 서브 목록
          	2. 서브 목록
          
          1. 혼합 해보기 1
          	- 순서 없음
          	+ 순서 없음
          	* 순서 없음
          2. 혼합 해보기 2
          	1. 순서 있음
          	- 순서 없음
          	2. 순서 있음
          ''
          ```

        - **강조** :

          기울임, 굵게, 취소선

          기울임: *글자* _글자_

          굵게: **글자**

          취소: ~~글자~~

  6. **실습 따라해보기 (샘플)**



# Python



## 1. 개요

![python logo](https://wikidocs.net/images/page/5/pahkey_KRRKrp.png)

파이썬(Python)은 1990년 암스테르담의 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어이다. 귀도는 파이썬이라는 이름을 자신이 좋아하는 코미디 쇼인 "몬티 파이썬의 날아다니는 서커스(Monty Python’s Flying Circus)"에서 따왔다고 한다.

> 인터프리터 언어란 한 줄씩 소스 코드를 해석해서 그때그때 실행해 결과를 바로 확인할 수 있는 언어이다.



## 2. 특징

1. **파이썬은 인간다운 언어이다. 아래 코드는 쉽게 해석된다.**

​		`if 4 in [1,2,3,4]: print("4가 있습니다")`

​		*만약 4가 1, 2, 3, 4 중에 있으면 "4가 있습니다"를 출력한다.* 라고 말이다.



2. 파이썬은 간결하다.

```python
# simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
    	print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
    	print("%6s need compiler" % lang)
    else:
    	print("should not reach here")
```



3. 공식문서가 자세히 제공된다.

​		[파이썬 공식문서 링크](https://docs.python.org/3/)

   

---

1. Git 환경설정 (최초 1번만 하면 됨)
git config --global user.name edukyle
git config --global user.email edukyle.hphk@gmail.com

git config --global --list

2. git 로컬 저장소 만들기
git init

3. git 파일 상태 보기
git status

4.  Working Directory -> Staging Area
git add a.txt

5.  Staging Area -> Commits
git commit -m "commit message"

6. git 커밋 목록 보기
git log
git log --oneline
git log -p

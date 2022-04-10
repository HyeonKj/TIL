# TIL 2022-01-12 (1)

## GIT 특강 1일차 내용

- 1. **WHY**

  2. **CLI VS GUI**

     1. `GUI (Graphic User Interface)` : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
     2. `CLI (Command Line Interface)` : 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

  3. **CLI 기본 명령어들**

     1. `touch`

        - 파일을 생성하는 명령어
        - 띄어쓰기로 구분하여 여러 파일을 한꺼번에 생성 가능합니다.
        - 숨김 파일을 만들기 위해서는 `.`을 파일 명 앞에 붙입니다.

        ```bash
        $ touch text.txt
        ```

     2. `mkdir`

        - make directory
        - 새 폴더를 생성하는 명령어
        - 띄어쓰기로 구분하여 여러 폴더를 한꺼번에 생성 가능합니다.
        - 폴더 이름 사이에 공백을 넣고 싶다면 따옴표로 묶어서 입력합니다.

        ```bash
        $ mkdir folder
        $ mkdir 'happy hacking'
        ```

     3. `ls`

        - list segments
        - 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어
        - `-a` : all 옵션. 숨김 파일까지 모두 보여줍니다.
        - `-l` : long 옵션. 용량, 수정 날짜 등 파일 정보를 자세히 보여줍니다.

        ```bash
        # 기본 사용
        $ ls 
        
        # all 옵션
        $ ls -a
        
        # all, long 옵션 함께 적용
        $ ls -a -l
        
        # 여러 옵션 축약 가능
        $ ls -al
        ```

     4. `mv`

        - move
        - 폴더/파일을 다른 폴더 내로 이동 하거나 이름을 변경하는 명령어
        - 단, 다른 폴더로 이동할 때는 작성한 폴더가 반드시 있어야 합니다. 없으면 이름이 바뀝니다.

        ```bash
        # text.txt를 folder 폴더 안에 넣을 때
        $ mv text.txt folder
        
        # text1.txt의 이름을 text2.txt로 바꿀 때
        $ mv text1.txt text2.txt
        ```

     5. `cd`

        - change directory
        - 현재 작업 중인 디렉토리를 변경하는 명령어
        - `cd ~` 를 입력하면 홈 디렉토리로 이동합니다. (단순히 `cd` 라고만 입력해도 동일합니다.)
        - `cd ..` 를 입력하면 부모 디렉토리로 이동합니다. (위로 가기)
        - `cd -` 를 입력하면 바로 전 디렉토리로 이동합니다. (뒤로 가기)

        ```bash
        # 현재 작업 중인 디렉토리에 있는 folder 폴더로 이동
        $ cd folder
        
        # 절대 경로를 통한 디렉토리 변경
        $ cd C:/Users/kyle/Desktop
        
        # 상대 경로를 통한 디렉토리 변경
        $ cd ../parent/child
        ```

     6. `rm`

        - remove
        - 폴더/파일 지우는 명령어
        - GUI와 달리 휴지통으로 이동하지 않고, 바로 `완전 삭제`합니다.
        - `*(asterisk, wildcard)`를 사용해서 `rm *.txt` 라고 입력하면 txt 파일 전체를 다 지웁니다.
        - `-r` : recursive 옵션. 폴더를 지울 때 사용합니다.

        ```bash
        $ rm test.txt
        $ rm -r folder
        ```

     7. `start, open`

        - 폴더/파일을 여는 명령어
        - `Windows`에서는 start를, `Mac`에서는 open을 사용할 수 있습니다.

        ```bash
        # Windows
        $ start test.txt
        
        # Mac
        $ open test.txt
        ```

     8. **유용한 단축키**

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



----


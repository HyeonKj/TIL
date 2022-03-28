# 2022-01-13
## 특강 2일차

# Git 관련 명령어 한눈에 정리



### 작성자 이름, 메일 등록 (최초 1번만 실행)

git config --global user.name "github username"
git config --global user.email "github email"

### config 정보 출력
git config --global --list

### 일반 폴더 -> 로컬 저장소
git init

### 버전 상태 출력
git status

### Working Directory -> Staging Area
git add [File]
git add .  # 모든 파일 add

### Staging Area -> Commits
git commit -m "commit message" 

### commits 목록 출력

git log
git log --oneline  # 한줄로 보기 옵션
git log -p  # 커밋마다 차이 보기 옵션



### 로컬 저장소와 원격 저장소를 연결
git remote add origin [Github repository URL]

### 연결된 원격 저장소 목록 조회
git remote -v

### 원격 저장소 연결 삭제
git remote rm origin
git remote remove origin

### 로컬 저장소의 commits을 원격 저장소에 반영
git push origin master
git push -u origin master  # -u 옵션을 했다면 이후 push할 때는 git push만으로도 가능

### 원격 저장소를 로컬에 복제
git clone [Github repository URL]

### 원격 저장소의 변경 사항 로컬에 받아오기 (동기화)
git pull origin master

---

---

- 2022-01-13
  - 실습 2인 1조 구성(끝말잇기)
    - 오류 발생 :
      - **홈 폴더에 .git(git이 관리자)이 설정되어 있어서 물결 표시 옆에 ~(master)로 표기되어 있었음.**
      - 해결과정 :
        - - - 홈폴더에 있는 .git을 지우기 위해 [rm -rf] 강제삭제 명령
              - 홈폴더에 git 관리자를 지운 뒤, 해당 끝말잇기 폴더의 부모폴더 또한 .git 관리자 삭제. 
                - **이유** : 왜냐하면 ! 관리자가 둘 이상이 되면 다른 모듈이 되는데 sub 모듈이라고 어려워지는 과정이기 때문에 현재 과정에서는 충돌이나 오류가 일어남. 때문에 홈폴더를 제외하고 아래 자식폴더에만 .git을 각자 가지고 있는 것임. 
                  - **이후** : 끝말잇기 패턴은 간단함.
        - git clone [url]
        - 입력 후 수정 및 저장.
        - git add . 
        - git commit -m "relay - n"
        - git push 무한 반복. 
        - 가져올 땐 git pull origin master 입력 후 add 실시. 
        - clone을 가져올 때 굳이 init 안해도 됨. 이미 되어 있는 상태임. 
  - 2022-01-13 16:33
  - collaboration - > 닉네임 초대 -> 상대방 이메일 수령-> 협업 

-----

#### 소감 

​	에러를 통해서 모르는 것을 알게 되고 한층 더 지식을 쌓을 수 있었다.

// 2022 - 03 - 13 



----


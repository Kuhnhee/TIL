# SSAFY start camp 챗봇 (1일차, 190708)

## 키워드형 챗봇 & 파이썬 기초

### Typora 문법 참고자료

https://ikso2000.tistory.com/60



### 시작하기 전에... 주의사항

1. 대/소문자 구분
2. 띄어쓰기 및 들여쓰기(indent, 4 space, tab)
3. 스펠링



### Python 문법 3형식

1. 저장

   ```python
   dust = 60 #dust라는 상자에 60을 저장
   ```

   무엇을 저장하는가?

    - 모든 숫자

    - 따옴표로 둘러싸인 글자, 숫자

    - 참/거짓

      

   어디에 저장하는가?

   - 변수(variable): 박스

   - 리스트(list): 박스의 리스트

     ```python
     dust = [60, 70, 80]
     location = ["강남구", "서초구"]
     ```

   - 딕셔너리: 견출지 붙인 박스들의 묶음

     ```python
     dust = {"강남구" : 60, "서초구" : 70}
     ```

     

2. 조건

   조건문: 조건의 결과가 True인 경우 실행한다.

   ```python
   if dust > 70:
   	print("over 70")
   elif dust > 50:
   	print("between 50 and 70")
   else:
   	print("lower than 50")
   ```

   

3. 반복

   반복문 (while문, for문): 조건문이 True인 동안 반복 실행한다.

   ```python
   while True:
   	print("Infinite loop")
   ```

   ```python
   n=0
   while n>3:
   	print("Still in loop")
   	n=n+1	# this loop will be executed 3 times.
   ```

   ```python
   friends = ["김강현", "이동원", "김수민"]
   for name in friends:
   	print(name)	
   ```



### API

응용 프로그램에서 사용 가능하도록 OS나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스 (정부 지원 API: data.go.kr)



### 함수

기능들의 묶음. 어떻게 동작하는지 모르더라도, input과 output만 안다면 사용 가능하다.

```python
print("hello")	#hello
abs(-3)			#3
len("umm...")	#6
```

남들이 써놓은 코드를 가져올 때에는 import 사용

```python
import random

numbers = range(10)			# range(10) = [0,1,2,3,4, ... , 9]
how_many = 3
random.choice(numbers)		# choice one from numbers
random.sample(numbers, how_many)	# choice how_many elements from numbers
```



* 오늘의 point: 오픈소스,  API(다른 시스템에 접근할 때 프로그램을 통해 접근하는 것)

* 본 수업에서는 Python 3.7, VS code, git bash 사용할 것



---

### CLI (Command Line Interface)

UNIX 계열에서 쓰는 command line인 **git bash** 사용할 것. 개인용 Laptop에선 **chocolatey** 추천.

- `ls` : 현재 디렉토리의 리스트

- `pwd` : 현재 작업중인 디렉토리

- `cd` : 디렉토리 변경

- `cd ..` : 상위 폴더로 이동

- `cd ~` : 홈 디렉토리로 이동

- `tab` : 자동완성

- `mkdir` : 디렉토리 생성

- `code .` :  현재 폴더에서 VS code 실행

- `rm` : 파일 지우기

- `touch` : 파일 생성

- `exit` : 터미널 종료

  

### git

생활코딩 git 강의 추천

- github repository 생성
- git bash에서 작업 폴더로 이동

- `git init` : initialize

- `git add .` 

- `git config --global user.email "sheva0902@naver.com"`

- `git config --global user.name "Kuhnhee"`

- `git commit -m "1"`

- ```
  git remote add origin https://github.com/Kuhnhee/chatbot-python.git
  git push -u origin master
  ```



### VS code 설정

1. git bash $ home > python (작업 디렉토리)에서 `code .` 입력하여 VS code 실행

`VS code 상에서 ctrl+shift+p > shell 검색 > select default shell > git bash 선택` 

2. Python 새 파일 만들 경우, 추천 extension 설치
3. 파이썬 프로그램 실행 시 우클릭 > Run python file in terminal
4. 혹은 `ctrl+shift+backtick` 으로 커맨드 라인 활성화, python first.py 입력.

---



### Browser 조작

```python
import webbrowser

url = "https://search.daum.net/search?q=아이유"
webbrowser.open(url) # 아이유 검색창을 띄워줌
```

위 코드와 동일하게 작동하지만, 아래와 같이 작성해 놓을 경우 검색어를 바꿀 때 편리하다.

String concatenate를 활용한 예시.

```python
import webbrowser

url = "https://search.daum.net/search?q="
keyword = "아이유"
webbrowser.open(url+keyword) # 아이유 검색창을 띄워줌
```

여러 개의 창을 한 번에 열어보고 싶은 경우, 아래와 같이 반복문을 활용하여 작성할 수 있다.

```python
import webbrowser

url = "https://search.daum.net/search?q="
keywords = ["아이유", "설현", "수지"]
for name in keywords:
    webbrowser.open(url+name)
```










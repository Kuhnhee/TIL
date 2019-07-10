# SSAFY start camp 챗봇 (3일차, 190710)

## Flask

### Flask 설치

```shell
pip install flask
```

```python
# app.py
from flask import Flask
app = Flask(__name__)

# 1.주문 받는 방식(어떻게)
@app.route("/")
# 2. 무엇을 제공할지(무엇)
def hello():
    return "Hello World!"

# 1.주문 받는 방식(어떻게)
@app.route("/hi")
# 2. 무엇을 제공할지(무엇)
def hi():
    return "hi"
```

```shell
flask run	#flask 실행. app.py를 디폴트로 찾는다.
FLASK_APP=app2.py flask run #py 파일의 이름이 app.py가 아닐 경우 실행방법
```

- http://127.0.0.1:5000/ (로컬 5000포트)로 접속 가능 (localhost:5000 과 동일)
- localhost:5000/hi 접속하면 hi 출력

```
http://naver.com:80/ #URL=카페 주문서와 동일
					 #프로토콜 / 이름(도메인 -> IP) / 상세주문
```

- `/`는 컴퓨터에서 root를 의미한다. `~`는 home을 의미한다.

* 포트: 집 -> 네이버 서버에 연결할 때, 네이버 서버(매우 큼)의 문 번호
* http 기본 포트: 80, https 기본 포트: 443, secure shell 포트: 22, 용도에 따라 여러 포트를 사용하면 된다.

#### 미션

```python
#localhost/name에 접속할 때 본인의 영문 이름을 출력
@app.route("/name")
def name():
    return "Kuhnhee Lee"
```



### Variable route

```python
#localhost/name/이름에 접속할 때, 접속한 주소의 이름을 출력 (입력값을 변수화)
@app.route("/hello/<person>")   
def greeting(person):
    return "hello, " + person
	# return "hello, {0}".format(person)
```

#### 미션

```python
#로또번호, 점심메뉴를 추천해주고, 실시간 주가를 알려주는 웹을 만들어라
# random lotto 번호 추천
@app.route("/lotto")
def lotto():
    numbers = range(1,46)
    lotto = random.sample(numbers, 6)
    c = ''.join(str(n) for n in lotto)
    return "오늘의 로또 추천번호는...<h1>{0}</h1>를 추천합니다.".format(c)

# random 점심메뉴 추천
@app.route("/lunch")
def lunch():
    menu = ["김밥", "피자", "햄버거", "삼겹살", "파스타"]
    choice = random.choice(menu)
    return "오늘의 점심 메뉴로는...{0}를 추천합니다.".format(choice)

# /kospi => 현재 네이버 기준 kospi
@app.route("/kospi")
def kospi():
    url = "https://finance.naver.com/sise/"

    response = requests.get(url).text
    document = bs4.BeautifulSoup(response, "html.parser")

    kospi = document.select_one('#KOSPI_now').text
    kosdaq = document.select_one('#KOSDAQ_now').text
    kospi200 = document.select_one('#KPI200_now').text

    msg = "현재 코스피 지수는: {0}<br> 현재 코스닥 지수는: {1}<br> 현재 코스피200 지수는: {2}".format(kospi, kosdaq, kospi200)
    return msg
```

- 문서에 값을 전달하기 위해서는 `print()`가 아니라, 반드시 `return`을 써야 한다.



### datetime 모듈

```python
#만약 오늘이 1월 1일 이라면 예, 아니면 아니요.
from flask import Flask
from datetime import datetime

@app.route("/newyear")
def newyear():
    flag = (datetime.now().month == 1 and datetime.now().day == 1)
    
    if flag:
        return "예"
    else:
        return "아니요"
```



### HTML (HyperText Mark***up*** Language)

기본적인 문서 구조는 다음과 같다.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>홈페이지</title>
    </head>
    <body>
        <h1>건희의 홈페이지</h1>
        <h2>홈페이지에 오신 것을 환영합니다.</h2>
        <h3>반갑습니다.</h3>
        <p>저는 SSAFY에서 파이썬 1반에 있는 이건희입니다.</p>
        <p>라이브 서버 부착했다.</p>
    </body>
</html>
```

링크 걸기

```html
<a href="http://www.google.com">구글로 가기</a> 
<!--http를 붙여주지 않으면, 로컬 기준으로 www.google.com을 찾게되어버림 -->
```

이미지, 영상 첨부하기

```html
<img width=" " height=" " src="주소" alt=" "> <!--img는 닫아줄 필요 없다.-->
<iframe src="주소" frameborder="0"></iframe>
```

배경, 글자 색상 넣어주기

```html
<body style="background-color: green">
    <h1 style="color: yellow">건희의 홈페이지</h1>
</body>
```

리스트 (Unordered list) 넣기

```html
<ul>
    <li>Python</li>
    <li>JAVA</li>
    <li>kotlin</li>
</ul>
```

리스트 (Ordered list) 넣기

```html
<ol>
    <li>자연어</li>
    <li>인공지능</li>
    <li>웹</li>
</ol>
```

- html 기본문서 자동완성:  `!`+`tab` 혹은 `!`+`Enter`



### Template(ex. html)을 만들어 render하기

flask의 기본적 구조 (python의 관례, Django도 마찬가지. 변경 가능)

```shell
./app.py
./templates/xxx.html
```

app.py에서 render_template() 함수를 사용해 template(html) 을 호출하여 화면에 띄워준다.

```python
#app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/greet/<name>")
def greet(name):
    #name에는 "/hello/이름"의 이름이 들어감.
    return render_template('greet.html', username=name)
```

home.html 파일은  templates 폴더 안에 위치한다.

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
	...
</head>
<body>
    <h1>홈페이지 라이브 서버인가? 라이브 서버이다.</h1>
</body>
</html>
```

app.py에서 받은 인자를 template으로 전달하는 것도 가능하다. `{{ 변수 }}` (mustache) 사용

```html
<!-- templates/greet.html -->
<!DOCTYPE html>
<html lang="en">
<head>
	...
</head>
<body>
    <h1>안녕하세요, {{username}}님?</h1>
</body>
</html>
```

#### 미션

```python
# 랜덤으로 메뉴를 출력하며, 그에 해당하는 이미지를 함께 보여주는 웹페이지를 만들어라

# app.py
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/menu")
def menu():
    hamburg = "https://recipes-secure-graphics.grocerywebsite.com/0_GraphicsRecipes/4589_4k.jpg"
    pizza = "https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg"
    taco = "https://cbmpress.com/toronto/wp-content/uploads/sites/3/2017/08/tacomain-01.jpg"
    menu_dict = {"햄버거":hamburg, "피자":pizza, "타코":taco}
    choice_menu = random.choice(list(menu_dict))
    choice_pic = menu_dict[choice_menu]
    return render_template("menu.html", name=choice_menu, pic=choice_pic)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
	...
</head>
<body>
    <h1>안녕하세요, 오늘의 추천 메뉴는 {{name}} 입니다.</h1>
    <img src={{pic}} alt="">
</body>
</html>
```

1. dict 구조와 random 라이브러리를 활용하여, 무작위로 음식 이름과 사진을 선택한다.
2. 이를 name, pic 이라는 변수에 담아 menu.html 에 전달하여 render한다.



#### 미션2

로또 번호 맞추기(지난주 로또 번호 스크래핑 or **API 검색**)

- JSON 파일은 python dictionary로 만들기 굉장히 쉽다.
- JSON -> dictionary 작업도 parsing 이라고 한다. (requests 자체 json parser or JSON 모듈 사용)

- **`set(A) & set(B)` **을 사용해 두 집합의 교집합을 구할 수 있다.

```python
# lotto.py
import requests
import random

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
res = requests.get(url)    #json file을 dict 구조로 바꿔줘야함.

json_lotto = res.text      #json file이 string으로 들어온 것. (이렇게 하면 안돼)
dict_lotto = res.json()    #json file이 dict 구조로 들어온 것.

# winner에 1등 당첨 번호를 넣기
winner = [dict_lotto["drwtNo" + str(i)] for i in range(1,7)]

place = 0
trial = 0
third_count = 0
fourth_count = 0
fifth_count = 0
while(True):
    same_cnt = 0
    trial += 1
    my_lotto = sorted(random.sample(range(1,46), 6))     # 로또 랜덤 추천

    # for i in winner:
    #     for j in my_lotto:
    #         if i == j:
    #             same_cnt += 1
    #             break
    same_cnt = len(set(winner) & set(my_lotto)) # 교집합
    
    if same_cnt==6:
        print("1st place, this was {0}th trial".format(trial))
        print("You've got {0} times of 3rd places, {1} times of 4th places, {2} times of 5th places".format(third_count,fourth_count,fifth_count))
        print("\nYour number is... {0}".format(my_lotto))
        print("Correct num is... {0}".format(winner))
        place = 1
        break;
    elif same_cnt==5:
        third_count += 1
    elif same_cnt==4:
        fourth_count += 1
    elif same_cnt==3:
        fifth_count += 1
    else:
        continue
```

#### 미션4

임의의 로또 번호를 뽑아주고, 지난주 번호와 비교해주는 웹 작성하기

```python
# app.py
from flask import Flask, render_template
import random
import requests

# /lotto 랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능
@app.route("/lotto")
def lotto():

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url) 
    dict_lotto = res.json()    #json file이 dict 구조로 들어온 것.
    
    # winner에 1등 당첨 번호를 넣기
    winner = [dict_lotto["drwtNo" + str(i)] for i in range(1,7)] 

    same_cnt = 0
    my_lotto = sorted(random.sample(range(1,46), 6))     # 로또 랜덤 추천

    same_cnt = len(set(winner) & set(my_lotto)) # 교집합
    
    if same_cnt==6:
        place = "1등"
    elif same_cnt==5:
        place = "2등"
    elif same_cnt==4:
        place = "3등"
    elif same_cnt==3:
        place = "4등"
    else:
        place = "꽝"

    return render_template("lotto.html", winner=str(winner), my_lotto=str(my_lotto), place=place)
```

```html
<!-- ./templates/lotto.html -->
<!DOCTYPE html>
<html lang="en">
<head>
	...
</head>
<body>
    <p>지난 등수: {{winner}}</p>
    <p>당신의 번호: {{my_lotto}}</p>
    <p>당신의 등수는..... {{place}}</p>
</body>
</html>
```



### Live Server extension

VScode -> Extension -> live server 설치

좌측 네비게이터에서 index.html 우클릭 -> Open with live server

서버를 다시 실행시키지 않고도 업데이트 반영이 가능해진다.


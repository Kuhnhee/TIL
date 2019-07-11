# SSAFY start camp 챗봇 (4일차, 190711)

## Flask, Dictionary, Fake sites

### git  특정 파일만 commit하기

```shell
git add (파일주소)
git commit -m "msg"
git push

혹은

git add
git commit -m "msg" (파일주소)
git push
#commit하지 않고자 하는 파일들도 add가 적용되어 commit을 기다리는 상태가 된다.
```

---

### Static page

누가 들어와도 동일한 서비스를 제공하는 페이지 (정적 페이지)

### Dynamic page

flask를 통해서 만들었던 페이지들은 동적으로 서비스들을 제공했었음.

사용자에 맞춰서 정보를 제공하기 위해선서는, 우선 사용자의 **입력값을 처리할 수 있어야 한다.**

- 오늘 교육의 목표는 **Static page를 만들어 배포**하는 것. (via github)
- Dynamic page 배포는 추후에 할 것.

-----

### Fake Google 만들기

form, input, button 태그를 잘 조합하여 검색창을 만들 수 있다.

입력값을 form 태그가 받아서, ~~로 보내는 행위로 검색이 이루어진다.

```html
...
<form action="https://www.google.com/search">
    <input name="q">    <!-- q에 검색값을 저장 -->
    <button>검색</button>
</form>		<!-- form에 의해 https://www.google.com/search?q=검색값" 접속 -->
...
```

### Fake Naver 만들기

```html
...
    <img src="https://logoproject.naver.com/img/img_story_renewal.png" alt="">
    <form action="https://search.naver.com/search.naver">
        <input name="query"> 
        <button>검색</button>
    </form>
...
```

### Fake Daum 만들기

```html
...
    <img src="https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png" alt="">
    <form action="https://search.daum.net/search">
        <input name="q"> 
        <button>검색</button>
    </form>
...
```

---

### 낚시 앱 만들기 ("당신의 전생은..?")

```html
<a href="/pastlife">당신의 전생은....!?</a>
<!--우리 페이지의 /pastlife로 링크 -->
```

가짜 데이터를 생성하기 위한 Faker 라이브러리 사용

```shell
pip install Faker
```

이름을 입력받았을 때 가짜 전생을 알려주는 웹 만들기

- /pastlife에서 입력한 "이름"이 `request.args.get("name")`에 저장된다. 이를 app.py에서 pastlife_result.html로 전달하여 출력시킨다.

```python
# app.py
...

fake = Faker('ko_KR')
nameJob_dict = {}

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

@app.route('/pastlife/result')
def pastlife_result():
    job = fake.job()		#가짜 직업 데이터 출력
    name = request.args.get("name")
    
    # 동일한 이름일 경우 동일한 직업이 출력되도록 하자.
    if name in nameJob_dict:
        job = nameJob_dict[name]
    else:
        job = fake.job()
        nameJob_dict[name] = job
        
    return render_template('pastlife_result.html', job=job, name=name)
```

```html
<!--pastlife.html-->
...
    <h1>당신의 전생은?!</h1>
    <form action="/pastlife/result">
        <p>당신의 이름을 입력하세요</p>
        <input name="name">
        <button>보러가기</button>
    </form>
...
```

```html
<!--pastlife_result.html-->
...
<body>
    <h1>{{name}}님의 전생은 {{job}} 였습니다.</h1>
</body>
...
```

### 낚시 앱 만들기 ("궁합을 알려드립니다.")

/admin 에 들어가서 낚인 사람의 목록을 확인 할 수 있도록 하자.

궁합 결과를 보여주는 동시에, 입력된 두 개의 이름을 저장한다.

```python
# app.py
...
@app.route('/chemistry')
def chemistry():
    return render_template('chemistry.html')

@app.route('/chemistry/result')
def chemistry_result():

    babo = request.args.get("babo")
    you = request.args.get("you")
    
    if babo not in double_dict:
        double_dict[babo] = {}
    if you not in double_dict[babo]:
        double_dict[babo][you] = random.randint(51,100)
    num = double_dict[babo][you]

    return render_template('chemistry_result.html', babo=babo, you=you, num=num)

```

#### 이중 dictionary 구조 (dict in dict)

babo가 you와의 궁합을 확인한 적이 있다면, 이 때의 궁합 정보를 유지시키는 것이 목적일 경우. 아래와 같이 이중 dict 구조를 활용할 수 있다.

```python
# babo: 속는 사람 / you: babo가 궁합을 확인한 상대 / num: babo와 you 사이의 궁합점수
if babo not in double_dict:
    double_dict[babo] = {}
if you not in double_dict[babo]:
    double_dict[babo][you] = random.randint(51,100)
num = double_dict[babo][you]
```

#### 그 외 방법 (tuple을 key로 사용한 경우)

```python
# pair data saved in pair_dict (tuple 사용한 방식)
if (babo,you) in pair_dict:
    num = pair_dict[(babo,you)]
else:
    num = random.randint(51,100)
pair_dict[(babo,you)] = num #fake chemistry number
```

#### app.py, chemistry.html, chemistry_result.html 간 데이터 전달

chemistry.html에서 입력받은 두 개의 이름을 각각 babo, you에 저장한다.

이후 이를 app.py에서 request.args.get("babo"), request.args.get("you")를 통해 불러올 수 있다.

```html
<!--chemistry.html-->
...
<body>
    <h1>궁합을 알려드립니다.</h1>
    <form action="/chemistry/result">
        <p>당신의 이름</p>
        <input name="babo">
        <p>그분의 이름</p>
        <input name="you">
        <button>궁합보기</button>
    </form>
</body>
...
```

request.args.get()을 통해 불러온 babo와 you를 chemistry_result.html로 전달해 출력한다.

```html
<!--chemistry_result.html-->
...
<body>
    <h1>{{babo}}님과 {{you}}님의 궁합 결과는.... {{num}}% 입니다. </h1>
</body>
...
```

#### 낚시당한 사람들의 명단을 /admin 에서 확인하기

double_dict에 저장되어 있는 데이터들을 활용하여 궁합 사이트에 입력된 이름들의 명단을 확인할 수 있다.

- dictionary의 items() 함수를 활용하면 key와 value를 동시에 접근할 수 있다.

```python
# app.py
@app.route('/admin')
def admin():

    msg = ""
    for key, val in double_dict.items():
        val_list = [v for v in val]
        val_string = ",".join(val_list)
        temp_msg = "{0}는 {1}에게 흥미가 있어보인다..\n".format(key, val_string)
        msg += temp_msg
        
    return render_template('admin.html', msg=msg)
```

```html
<!--admin.html-->
...
<body>
    <h1>{{msg}}</h1>
</body>
...
```



### 미션 (dictionary 다루기)

#### (미션1)

```python
# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
print('==== Q1 ====')
vals = list(score.values())
avg = sum(vals)/len(vals)
print("average point is: {0}".format(avg))
```



#### (미션2)

```python
# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 10
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}
print('==== Q2 ====')
a_val = scores['a'].values()
b_val = scores['b'].values()
a_avg = sum(a_val)/len(a_val)
b_avg = sum(b_val)/len(b_val)
print("average of class a is: {}".format(a_avg))
print("average of class b is: {}".format(b_avg))

math_avg = (scores['a']['수학'] + scores['b']['수학']) / len(scores.keys())
lang_avg = (scores['a']['국어'] + scores['b']['국어']) / len(scores.keys())
music_avg = (scores['a']['음악'] + scores['b']['음악']) / len(scores.keys())
print("average of math is: {}".format(math_avg))
print("average of korean is: {}".format(lang_avg))
print("average of music is: {}".format(music_avg))
```



#### (미션3)

```python
# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}
# 3-1. 도시별 최근 3일의 온도 평균은?
print('==== Q3-1 ====')
seoul_avg = sum(city['서울']) / len(city['서울'])
dajeon_avg = sum(city['대전']) / len(city['대전'])
print("서울의 평균 온도는 {}도였다.".format(seoul_avg))
print("대전의 평균 온도는 {}도였다.".format(dajeon_avg))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
print('==== Q3-2 ====')
max_temp = 0
max_temp_city = ""
for key, vals in city.items():
    if max(vals) > max_temp:
        max_temp = max(vals)
        max_temp_city = key

min_temp = 0
min_temp_city = ""
for key, vals in city.items():
    if min(vals) < min_temp:
        min_temp = min(vals)
        min_temp_city = key
print("가장 추운 도시는 {0}로, 온도는 {1}였다.".format(min_temp_city, min_temp))
print("가장 더운 도시는 {0}로, 온도는 {1}였다.".format(max_temp_city, max_temp))

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
print('==== Q3-3 ====')
print(2 in city['서울'])
```



### dict.get(key) 함수

```python
dict.get(key)를 dict[key]보다 권장한다.
```

- 해당 key가 dict에 없을 경우, `dict[key]`는 KeyError가 발생하는 반면, `dict.get(key)`는 default_value를 반환해준다.

```python
dict.get(key)는 (dict[key] or None)과 동일하게 작동한다.
```

---

### OP.GG (scrapping with flask)

#### String 조작

replace()함수, indexing

```python
win = "241W"
win.replace('W', '승') # win = "241승"

#indexing
win = win[0:3]	# win = "241"

#뒤집기
win = win[::-1]
```

/opgg에서 아이디를 입력하면 op.gg에서의 승,패 자료를 스크립핑해 /opgg/search에 출력하는게 목표.

```python
#app.py
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg/search')
def opgg_search():

    ID = request.args.get("ID")
    
    # 1. op.gg에 요청을 보낸다.
    url = "https://www.op.gg/summoner/userName=" + ID

    # 2. html 응답을 받아
    res = requests.get(url)

    # 3. html 안에 있는 정보를 출력
    doc = bs(res.text, "html.parser")
    win_raw = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    lose_raw = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text

    win = win_raw[:len(win_raw)-1]
    lose = lose_raw[:len(lose_raw)-1]

    return render_template('opgg_search.html', ID=ID, win=win, lose=lose)
```

/opgg에서 입력받은 ID값을 request.args.get("ID")로 받아 opgg_search.html로 전달한다.

```html
<!--opgg.html-->
...
    <body>
        <h1>LOL 아이디를 입력하세요</h1>
        <form action="/opgg/search">
            <input name="ID">
            <button>전적검색</button>
        </form>
    </body>
...
```

opgg_search() 함수에서 string indexing을 활용해 승, 패의 숫자 값만을 추출한 뒤 opgg_search.html에 ID와 함께 전달해 rendering한다.

```html
<!--opgg_search.html-->
...
    <body>
        <h1>{{ID}}의 LOL 전적입니다.</h1>
        <h2> {{win}}승 {{lose}}패</h2>
    </body>
...
```






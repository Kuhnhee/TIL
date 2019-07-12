# SSAFY start camp 챗봇 (5일차, 190712)

## Telegram API

1. telegram.org 접속, telegram for windows 설치
2. @botfather 검색
3. bot 이름(kuhnbot), username(kuhnbot_bot) 설정
4. token 받아서 기억해 둘 것
5. `https://api.telegram.org/bot{token}/getMe` 접속하여 json 형식 데이터 확인
6. `https://api.telegram.org/bot{token}/getUpdates`에서 변동기록, 대화기록 확인가능
7. `https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=뭠마`로 "뭠마"라는 메세지를 텔레그램을 통해 전송 가능. chait_id는 6번의 getUpdates를 통해서 확인 가능.

위의 과정을 python을 통해서 하는 것이 오늘의 목표



### Chatbot이 나에게 메세지를 전달하게 하기

'/'에서 'getUpdates'함수를 사용해 chat_id를 가져온 뒤, '/send' 에서 'sendMessage'함수를 사용해 입력받은 메세지를 chat_id에게 텔레그램을 통해 전송해준다.

```python
#app.py
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    msg = request.args.get('msg')

    base = "https://api.telegram.org"
    method_msg = "sendMessage"
    method_update = "getUpdates"

    #chat_id를 가져오는 코드
    #1. getUpdates 메소드로 요청 보내기
    #2. 받아온 응답(json)을 dictonary로 바꿔서 첫번째 메세지의 chat 아이디를 가져온다
    url_upd = f"{base}/bot{token}/{method_update}"
    status = requests.get(url_upd).json()   #json -> dict 변환
    chat_id = status["result"][0]["message"]["chat"]["id"]

    #home에 보내온 msg를 받아 telegram api를 통해 메세지 전송
    url_msg = f"{base}/bot{token}/{method_msg}?chat_id={chat_id}&text={msg}"
    requests.get(url_msg) # 최종 메세지를 보내줌

    return render_template('send.html')
```

home.html에서 입력받은 값을 "msg"에 저장하고, /send로 리다이렉팅한다.

```html
<!--home.html-->
...
<body>
    <h1>텔레그램 메세지 보내기</h1>
    <form action="/send">
        <input name="msg">
        <button>보내기</button>
    </form>
</body>
...
```

send.html로 리다이렉팅된 후, 아래와 같이 메세지를 출력한다.

```html
<!--send.html-->
...
<body>
    <h1>메세지가 전송되었습니다.</h1>
</body>
...
```



### ngrok

우리의 flask를 로컬이 아닌, 외부에 노출되는 서버로 만들자

ngrock은 git-bash보다 cmd로 실행시키는 것이 좋다.

```shell
ngrok http 5000	#ngrok 실행
```

 Forwarding 주소를 통해 누구든지 내 서버(flask)로 접속 가능하다.



### Web Hook

변화하는 값 혹은 신호가 있을 때, 신호를 보내주는 API 

(메세지가 들어왔을 때 telegram이 우리에게 요청(URL)을 보내게끔 하자)

`https://core.telegram.org/bots/api` > setWebhook

1. webhook 등록하기 (app.py에 webhook이 걸리는 URL 구성)

2. ```python
   #method 요청은 2가지(get,post)가 있다.
   #methods의 기본값은 ['GET']
   #민감한, 노출되지 않아야 하는 정보일 경우 'POST'로 요청을 보내야 한다.
   @app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는 주소
   ```

3. `https://api.telegram.org/bot{token}/setWebhook?={ngrok_url}/{token}`  접속: set hook

4. `https://api.telegram.org/bot{token}/deleteWebhook`  접속: delete hook(해제하고 싶을때)

```python
#app.py
@app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는
def webhook():
    '''
    1. 메아리 챗봇
    (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    (2) 그대로 전송
    '''
    print(request.get_json())
    #tuple 형태. 200: 잘 들어오고 있어요~ 라는 상태코드
    return '', 200 
```

git bash 상에서 python app.py 를 통해 서버를 구동한 뒤 챗봇에게 메세지를 전달하면, 아래와 같이 POST... 200 신호가 들어와 webhook이 제대로 이루어지고 있음을 알 수 있다.

![200](C:\Users\student\Desktop\200.jpg)



#### webhook을 사용해 메아리봇 만들기

webhook 신호가 들어왔을 때, 받은 메세지를 챗봇이 send하게 한다.

```python
#app.py
@app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는
def webhook():
    '''
    1. 메아리 챗봇
    (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    (2) 그대로 전송
    '''
    res = request.get_json()
    text = res.get("message").get("text")
    chat_id = res.get("message").get("chat").get("id")

    base = "https://api.telegram.org"
    method_msg = "sendMessage"

    url_msg = f"{base}/bot{token}/{method_msg}?chat_id={chat_id}&text={text}"
    requests.get(url_msg) # 최종 메세지를 보내줌(봇 -> 나)
    
    return '', 200 #tuple 형태. 200: 잘 들어오고 있어요~ 라는 상태코드
```



#### "lotto"를 물어보면 번호를 추천해주는 봇

입력된 메세지가 "lotto"일 경우, 출력 텍스트에 무작위 번호 6개를 출력한다.

```python
#app.py
@app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는
def webhook():
    
	...(생략)...
    chat_msg = res.get("message").get("text")

	...(생략)...

    #lotto를 물어보면 번호를 추첨해주도록 하자.
    numbers = range(1,46)
    lotto = sorted(random.sample(numbers, 6))
    lotto_msg = ','.join(str(n) for n in lotto)

    if (chat_msg == "lotto"):
        text = lotto_msg

    url_msg = f"{base}/bot{token}/{method_msg}?chat_id={chat_id}&text={text}"
    requests.get(url_msg) # 최종 메세지를 보내줌

    return '', 200 #tuple 형태. 200: 잘 들어오고 있어요~ 라는 상태코드
```



#### 파파고 NMT API 활용

1. [https://developers.naver.com](https://developers.naver.com/)에서 API 사용 아이디, 시크릿 발급받기 (.env에 작성)
2. 파파고 NMT API 가이드에 따라, headers와 data dict 선언
3. 두 dict를 `request.post(url, headers= , data=data)`에 삽입



#### 파파고 NMT를 활용해 번역해주는 챗봇

/번역 {문장}을 입력 시, {문장}에 해당하는 문장을 영어로 번역해주는 챗봇을 만든다.

```python
#app.py
@app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는
def webhook():

	...(생략)...

    # /번역 댕댕이 -> 번역결과 출력
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "X-Naver-Client-Id" : config('NAVER_ID'),
        "X-Naver-Client-Secret" : config('NAVER_SECRET')
    }
    data = {
        'source' : 'ko',
        'target' : 'en',
        'text' : chat_msg[4:] #입력 메세지 "/번역 " 이후 값
    }
    trans_data = requests.post(papago_url, headers=headers, data=data).json()
    translated_msg = trans_data['message']['result']['translatedText']
    # pprint(res.json())

    if (chat_msg == "lotto"):
        text = lotto_msg
    elif (chat_msg[:3] == "/번역"):
        text = translated_msg

	...(생략)...
```



#### Clova를 사용해 이미지(파일)이 전송될 경우 face_recognition을 해주는 챗봇

```python
#app.py
@app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는
def webhook():
    '''
    1. 메아리 챗봇
    (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    (2) 그대로 전송
    '''
	...(생략)...

    #lotto를 물어보면 번호를 추첨해주도록 하자.
	...(생략)...

    # /번역 댕댕이 -> 번역결과 출력
	...(생략)...


    # 파일 받았을 때 인식시키기
    # .get()을 사용하면 있을때~ 없을때~ 분기 가능
    if res.get("message").get("photo")[-1].get('file_id') is not None:
        file_id = res.get("message").get("photo")[-1].get('file_id')
        file_res = request.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get("result").get("file_path")
        file_url = f"{base}/file/bot{token}/{file_path}"        # 다운로드 url

        # 파일 다운로드. file stream이 날라올거야~ 명시
        image = requests.get(file_url, stream=True) 
        url = "https://openapi.naver.com/v1/vision/celebrity"
        headers = {
            "X-Naver-Client-Id" : config('NAVER_ID'),
            "X-Naver-Client-Secret" : config('NAVER_SECRET')
        }
        files = {
            'image' : image.raw.read(),
        }
        clova_res = requests.post(url, headers=headers, files=files)
        text = clova_res.json().get('faces')[0].get('celebrity').get('value')

    # 텍스트 메세지인가?
    else:
        if (chat_msg == "lotto"):
            text = lotto_msg
        elif (chat_msg[:3] == "/번역"):
            text = translated_msg
            
    # 메세지 전송
	...(생략)...
```





### token 숨기기 (각종 key)

보안이 필요한 데이터(key)들은 os단계에서 숨겨둬야 한다.

대표적으로, **환경변수**에 저장하곤 한다.

```shell
echo $PATH #terminal의 print 개념. 환경변수 목록 출력
```

- 우리는 **python decouple** 사용할 것

```shell
pip install python-decouple
```

1. 파일 이름 앞에 "."을 추가하여 숨김 파일 .env 생성

2. ```
   #.env
   TELEGRAM_TOKEN = 'bot884275913:AAEt1F_irUBmUAtkiRersxBeNtQeNCJSv-Q'
   ```

3. .env에 담겨있는 정보에 접근하여 telegram token을 가져가도록 한다. 

4. ```python
   #app.py
   from decouple import config
   token = config('TELEGRAM_TOKEN')
   print(token)
   ```



---

### git아... 이 파일은 앞으로 반드시 무시하거라

.env 파일은 github에 업로드되지 않도록 하자

1. .env와 동일한 디렉토리에 .gitignore 생성
2. 한 줄 한 줄 무시하고자 하는 파일명, 폴더명 기입

.gitignore가 **존재하는 폴더~하위폴더 모두에 적용**된다.

---

### json, dict 형태를 이쁘게 출력하기 (pprint)

```python
from pprint import pprint
```


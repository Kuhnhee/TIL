# Deploy

`~/ssafycodes/deploy/modelform` 프로젝트로 배포 연습



`git init` 으로 git 폴더 생성

local server에 있는 코드를 원격 server에 옮기는 과정을 **deploy**라고 한다. 

우리 프로젝트는 github과 같은 원격 저장소에 저장해둔 상태. 이 코드를 원격 서버로 옮겨 **deploy**하는 방법을 사용한다.



Contiguous Integration (CI): 로컬 -> 원격 저장소 저장

(CD): 원격 저장소 -> 원격 서버(clone, pull) (heroku가 해줄 것)

CI와 CD를 합친 것이 DevOps.



배포에 필요한 작업들을 바닥부터 하나하나 직접 할 필요 없게 도와주는 서비스가 Paas.



## Django 서버 배포(Heroku)

### 로컬 -> 원격 저장소

모든 CSS, JS 파일들을 하나로 합쳐주는 과정을 Pipelining이라고 한다. 이는 장고가 자동적으로 해준다. (우리는 `STATIC_ROOT`에 모든 STATIC 파일들을 넣어주면 된다.)

```python
# settings.py
...
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #폴더 이름은 일반적으로 'staticfiles'
```

아래 명령어를 통해 static 파일들을 모아준다.

```bash
$ python manage.py collectstatic
```

django project 내에 `staticfiles`라는 폴더 내에 static 파일들이 한 군데 모아지게 된다.

파일을 변경했으니 git add / commit

```bash
git add .
git commit -m "static file folder"
```

배포용 ignore 파일 추가

```
.vscode
#배포용 ignore
venv
*.sqlite3
.env
*.bak
```

``` bash
git add .gitignore
git commit -m "Add ignore files"
```

gitlab에 `deploy-test` 프로젝트 생성 및 코드 업로드

```
git remote add ...
git push -u origin master
```

`settings.py`에 있는 key를 `.env` 파일에 숨기자, 또, DEBUG=False 명령을 통해 에러가 발생해도 debugging 화면이 출력되지 않도록 한다.(개발 단계에서는 True로 두자)

```
SECRET_KEY='...'
```

`settings.py` 수정

```python
from decouple import config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')
```

```bash
$ git add .
$ git commit -m "add env vars"
```



### 원격 저장소(github, lab) -> 원격 서버

헤로쿠 [공식 홈페이지]( https://www.heroku.com/ ) 

헤로쿠 CLI ([홈페이지]( https://devcenter.heroku.com/articles/heroku-cli )) 설치



헤로쿠 로그인

```basj
heroku login
```

우리의 코드가 올라갈 원격 컴퓨터(다이노) 한 대를 만들자

```bash
heroku create
```

- 도메인 이름을 정해서 만들 수도 있다.(유니크 해야 함)

  ```bash
  heroku create ssafy-jjang
  ```

원격 저장소 리모트 주소도 자동적으로 제공됨을 확인할 수 있다.

```bash
git remote -v
```



heroku(홈페이지) dashboard > 생성된 heroku app 접속

Settings > Config Vars에 key-value의 형태로 SECRET_KEY와 DEBUG값을 지정해둘 수 있다.



**deploy 하기 전 준비물**

`django-heroku` 설치

```bash
$ pip install django-heroku
```

`settings.py`에서 django-heroku import

```python
import django_heroku
django_heroku.settings(locals())
```

`runtime.txt` 

```
python-3.7.4
```

`Procfile`

```
web: gunicorn [프로젝트_이름].wsgi --log-file -
```

gurnicorn 설치

```bash
$ pip install gunicorn
```

현재 pip list그대로를 넣는다.

```bash
$ pip freeze > requirements.txt
```

```bash
$ git add .
$ git commit -m "finish heroku setting"
```

**배포!**

```bash
$ git push heroku master
```

`settings.py` 에 도메인 추가

```
ALLOWED_HOSTS = [
    'sleepy-bayou-12786.herokuapp.com'
]
```

재배포

```bash
$ git add .
$ git commit -m "Allowed hosts add"
$ git push heroku master
```

**원격 서버에서 migration하기**

*VScode에서 터미널 키는 것을 추천*

```bash
$ heroku run python manage.py makemigrations
```

멀캠 5000포트는 막혀있으므로, 헤로쿠 대시보드 > More > Run console 에서 직접 명령을 입력해주자

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```



heroku git remote 바꾸기 (새로운 heroku app으로 연결)

```bash
$ heroku git:remote -a [이름] // git.heroku.com/[이름] 으로 변경
```

`settings.py`의 allowed_hosts의 주소도 변경해주어야 한다.



## Vue 서버 배포(firebase)

firebase console 구글 아이디로 로그인 ([링크]( https://console.firebase.google.com/?hl=ko&pli=1 ))

1. 프로젝트 생성

2. 애널리틱스 허용

3. 좌측 메뉴 [개발] > [Hosting] > [시작하기] 버튼 클릭

4. firbase cli 설치 (우리 프로젝트 폴더에서 진행, 이 예제에서는 `youtube-searcher`예제 프로젝트 사용)

   ` npm install -g firebase-tools ` (-g는 글로벌 설치를 의미)

5. VScode terminal에서 firebase 로그인. 콘솔창에 `firbase login` 입력.

   - Y 입력 후 가입

6. `firbase init` 명령어 입력

   - Y 입력
   - 옵션 선택 -> 'Hosting' (화살표로 내려간 뒤 <space> 키로 선택 후 <enter> 입력)
   - 프로젝트 선택
   -  `dist` 입력 ("dist 폴더를 기본 index.html 페이지 경로로 쓸꺼야~")
   - Vue router를 쓸 경우 반드시 yes. 이외이는 no.

7. `npm run build` 명령어 입력으로 전체 프로젝트 빌드(컴파일)

8. `firebase deploy` 입력



코드 수정 후에는 `빌드`, `디플로이` 해주면 된다.
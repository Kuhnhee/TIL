# django (190813)

- django에서의 root 페이지 설정

  ```python
  #urls.py
  urlpatterns = [
      path('', views.index),
  ]
  ```

  

### 템플릿 상속시키기

1. 공통적으로 쓸 템플릿(코드)을 뽑아낸다.
2. 해당 파일을 따로 만들고,
3. 활용할 다른 템플릿 파일에서 불러와 쓴다.

이전에 만든 템플릿들이 base.html을 상속받도록 하자. base.html은 부트스트랩 navbar가 들어가있는 페이지. (home.html이 base.html을 상속받도록 하자.)

- `{% block body %}`와 `{% endblock %}` 를 body 태그 안에 삽입해둔다. (구멍을 뚫어둠)
- home.html 내에서 base.html과 중복되는 모든 태그 삭제. 최상단에 `{% extends 'base.html' %}`와 `{% block body %}`를 추가, 최 하단에 `{% endblock %}` 추가. (위에 뚫어놓은 구멍에 이 값들을 넣어라)



- 부분적인 렌더링 (partial rendering) 또한 가능하다.

  `{% include '_nav.html' %}`

  ```html
  <!--base.html-->
  <body>
    {% include '_nav.html' %}
  
    {% block body %}
    {% endblock %}
  
    {% include '_footer.html' %}
  </body>
  ```

  ```html
  <!-- _nav.html -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
  	...
  </nav>
  ```

  ```html
  <!-- _footer.html -->
  <footer class="d-flex fixed-bottom justify-content-center">
    <p>Made by 이건희</p>
  </footer>
  ```

  

### ASCII art API 활용한 웹서비스 (artii app 추가생성)

1. /artii/ 에서 입력값을 받는다.
2. 입력값을 이용해 ASCII art API에게 요청을 전달한다.
3. GET을 사용해 API 응답결과를 불러와 출력한다.

```python
#views.py
from django.shortcuts import render
import requests
# Create your views here.
def artii(request):
    url = "http://artii.herokuapp.com/fonts_list"
    response = requests.get(url).text

    context = {
        'list': response,
    }
    return render(request, 'artii.html', context)

def artiiresult(request):
    text = request.GET.get('text')
    url = "http://artii.herokuapp.com/make?text="
    url += text

    response = requests.get(url).text

    context = {
        'show':response,
    }

    return render(request, 'artiiresult.html', context)
```

```html
<!--artii.html-->
  <form action="/result/" method="GET">
    문장을 입력해봐요 <input type="text" name="text">
    <button type="submit">Art!</button>
  </form>
```

```html
<!--artiiresult.html-->
<body>
  <pre>{{show}}</pre>
</body>
```



### 좀 더 DRY하게 django를 쓰자

- "urls.py를 분리하자"

  [artii] app 폴더 내에 urls.py 생성

  "big boss" urls.py가 처리하지 말고~ artii app의 문지기인 urls.py가 처리하도록 하자.

  artii라고 들어오는 url pattern이 나타나면, 본인이 처리하지 말고 artii app 내의 urls.py가 처리하도록 한다.

  ```python
  #first_app > urls.py
  from django.urls import path, include
  
  urlpatterns = [
      path('artii/', include('artii.urls'))
  ]
  ```

  ```python
  #artii > urls.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.artii),    # '' -> 바깥에서 보면 artii/ 와 동일
      path('result/', views.artiiresult),
  ]
  ```

- "공동 templates 관리"

  [first_app] > [templates] 폴더 생성

  공통으로 사용할 템플릿들을 해당 폴더로 이동

  - templates 탐색순서

    1. 자신(app) 폴더 내의 templates 폴더

    2. 다른 app 폴더 내의 templates 폴더

    3. 공통부분인 [first_app]폴더는 찾으려고 하지 않으므로, settings.py를 수정해줘야함.

       이 때, `BASE_DIR` 변수로 현재 프로젝트의 절대경로가 저장되어 있으므로, 이를 활용하면 된다.

    4. ```python
       #settings.py
       TEMPLATES = [
           ...
           'DIR': [os.path.join(BASE_DIR, 'first_app', 'templates')],
           ...
       ]
       ```

       

- "template 이름 중복시 문제 처리"

  본인의 앱 이름과 동일한 폴더를 [templates]내부에 생성

  [templates] > [artii] 안에 template 파일 생성

  대신, views.py에서 html파일을 불러올 때 `render(request, 'artii/artii.html')`와 같이 html 경로를 한 단계 더 깊에 입력해줘야함.



---



### OS 모듈

`os.getcwd()` : 현재 작업경로를 출력

`os.path.join(os.getcwd(), 'templates')` : 폴더들을 합쳐서 하나의 경로를 생성해줌

- C:/Users/.../templates
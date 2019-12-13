# Django Review & URL & Form

### *본 파일은 정윤영님의 [TIL](https://github.com/liza0525/TIL/blob/master/20191014_Django%20Review%20%26%20URL%20%26%20Form.md)을 기반으로 정리한 파일입니다.*



DRY(Do not Repeat Yourself) 하게 코딩하자!



### 향후 학습 계획

- Auth(인증) : 로그인 기능

- CBV(Class Based View) : Django로는 REST 서버 정도로만 쓸 것이기 때문에 생략할 것

- M:N 관계 모델을 쓰도록 할 것임(추천, 좋아요 / 카테고리 등)

- Validation

- 실제 배포 (Deploy) : Docker 활용?

- Javascript

  - 이전에는 Adobe Flash가 유행했으나, 없어지는 추세

  - Javascript의 프레임워크로 현재 가장 유명한 것 : React(made by facebook)

    - **Angular**(made by google)
    - **Vue**
    - Ember, Backbone (옛날에 쓰던 것...)

    

## RECAP(Django 복습)

- 프로젝트 생성 -> app 생성
- settings.py에 app 등록

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True # 자동 번역 기능(internationalization)

USE_L10N = True # localization

USE_TZ = True
```

- 먼저 모델을 정하고 가는 것이 좋다.

- 앞으로 구현할 기능이나 모델을 test하기 위해 tests.py에 코드로 작성

  - 빨간불을 파란불로 만들어 간다!

    따라서 **test 코드를 먼저 짠 후에 개발**을 들어가도록 한다.(**TDD**, Test Driven Development)

- admin.py

```python
from django.contrib import admin
from .models import Article # import 해야 함
# Register your models here.

admin.site.register(Article) # Article 모델에 대한 권한 설정
python manage.py createsuperuser # 사용자 이름과 메일 주소 넣기
```

- runserver 후 admin 페이지에 들어가면 관리할 수 있음
- 만약 admin 내의 model을 attribute별로 확인하고 싶으면, admin.py에 다음과 같이 작성(게임 회사의 서버 사이드에선 자주 할 것임)

```python
from django.contrib import admin
from .models import Article # import 해야 함
# Register your models here.

## 아래의 클래스를 작성하면 해당 Attribute를 확인할 수 있음
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content') # tuple로 적어 보낼 수 있음
    list_display_links = ('title',) # links를 지정 # tuple에선 single element는 꼭 comma를 써야 함

admin.site.register(Article, ArticleAdmin)
```

- urls.py 등록을 해야 함(새끼 urls.py 만들기 위해 include 해야 함)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #return 값은 URLPattern의 instamce
    path('articles/', include('articles.urls')),
]
```

- app에 (app이름 폴더)/urls.py 만들기

```python
from django.urls import path
from . import views

app_name = 'articles' # app name 설정

urlpatterns = [
    path('', view.index, name='index'),
]
```

- views.py에서 index 메소드를 만들어 준다.

```python
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all() # Article 모델 내의 모든 data를 가져옴
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context) # 어떤 templates를 불러올 것인지
```

- templates 폴더를 만들어 (app이름폴더)/index.html를 만들어 준다.
  - 이는 나중에 app 별로 묶여서 작동하기 때문에 (app이름 폴더)를 하나 만들어 주고 그 내에서 관리해야 좋다.

```html
{% extends 'base.html' %}

{% block body %}
<h1>Articles</h1>
<a href="#">새글쓰기</a>

<!-- 모든 Article 들을 보여줌 -->
{% for article in articles %}
  <p>{{ article.pk }}</p>
  <p>{{ article.title }}</p>
  <a href="#">상세보기</a>
{% endfor %}


{% endblock %}
```

- base.html은 프로젝트 내에 templates를 만들어 줌

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  {% block body %}
  {% endblock %}
</body>
</html>
```

- 대신 settings.py 가서 TEMPLATES의 DIR에 탐색 경로 설정해줘야 함

```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'recap', 'templates')],
        'APP_DIRS': True,
```

- create.html과 detail.html templates를 만들어 주고, view함수 지정

## get_absolute_url

- url이 변경되더라도 django의 url reverse가 변경된 url을 추적한다.

```python
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta: # subclass for ordering
        ordering = ['-pk'] # reversed ordering based on pk
        # ordering = ('-pk',) # tuple로 쓰는 방법

    # method도 추가 예정
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk' : self.pk}) # 첫번째 인자 : 어느 view method로 갈 건지 # 두번째 인자 : pk
        # reverse는 django.urls에 있다.
```

## form

- 사용자가 입력한 data를 유효성(validation) 검사하기 위함
- https://docs.djangoproject.com/en/2.2/ref/forms/api/#django.forms.Form
  - django form 공식 문서
- https://github.com/django/django/tree/master/django/forms
  - django github forms
- app 밑에 forms.py 파일 새로 만들기
- 전체적인 코드가 models와 거의 비슷!

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
```

- views.py에서 import하여 create 메소드를 설정해준다.

```python
from .forms import ArticleForm

def create(request):
    if request.method == "POST":
        new_article = Article.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
        )
        return redirect(new_article) # get_absolute_url을 지정하면 해당 객체만 넣어도 redirect가 된다.
    else:
        form = ArticleForm()
        context = {
            'form': form,
        } ## 여기 추가!
        return render(request, 'articles/create.html', context)
```

- 사실 form에게 모두 맡겨버릴 수 있다.

```python
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST) # 이렇게 맡겨버리면 된다.

        # 전송된 데이터가 유효한 값인지 검사 
        # 유효성 검사 하지 않는다면 form.save() 하면 끝이지만
        # 최대한 form의 기능을 쓰기 위해선 다음 같이 해야 한다.
        if form.is_vaild():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
            return redirect(article) # get_absolute_url을 지정하면 해당 객체만 넣어도 redirect가 된다.
        else: # 유효하지 않다면
            return redirect('articles:create')

    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
```

- create.html 파일에서 form 모듈을 불러온다.

```html
{% extends 'base.html' %}
{% block body %}
  <h1>새글쓰기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <!-- {{ form.as_p }} p tag로 감싸진 form을 렌더링 -->
    {% bootstrap_form form %}
  </form>

  <h2>Form 클래스를 통한 HTML Form 생성</h2>
{% endblock %}
```

### Form class의 기능

- **front-end validation** : max_length을 지정한 input은 아예 그 이상의 글이 써지지 않는다.
- **back-end validation** : form이 넘어왔지만 의도하지 않을 때를 방지할 수 있다.

### bootstrap form

- pip 인스톨 먼저 해주고

```python
pip install django-bootstrap4
```

- settings.py 설정

```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4', ## pip는 밑에 써주는 것이 좋음 # 상관은 없음
]
{% extends 'base.html' %}
{% load bootstrap4 %} <!-- 먼저 load 하고 -->
<!-- 매 templates마다 추가해줘야 한다. -->

{% block body %}
  <h1>새글쓰기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %} <!-- 여기 수정 -->
    <button name="submit">제출</button>
  </form>

{% endblock %}
```

- base.html template가 있는 경우에는 다음 코드도 함께 추가해줘야 한다.

```html
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
<!-- 위 세줄 추가해줘야 함!! -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  {% block body %}
  {% endblock %}
</body>
</html>
```

## 기타

- **Youtube** - '실리콘밸리 엔지니어가 말하는 한국 기업 문화가 달라져야 하는 이유'

  - 위계조직 vs 역할조직
  - 미션이 확실한 회사를 찾아가자(그래야 끝없는 발전이 가능)

- Browser

  - html를 browsing 한다.
  - 받은 html를 Render

- Javascript는 Browser를 조작할 수 있다. (요청을 보내는 것이 아닌 page의 모양새를 바꿔준다는 개념)

  - Chrome에서 ctrl+shift+J 치면 JS console창이 뜬다.

  ```python
  document // html 전체를 보여줌
  document.getElementById('title') // html 내의 해당 id가 있는 줄을 보여줌
  print() // 프린트 창이 뜬다.
  ```

- RESTful API

  - https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html
  - url을 알아보기 좋게 만드는 것이라고 생각하면 됨 url은 목적어만 남기고 method로 조작하는 것임(위 문서 내 'REST API 설계 예시' 참고) - 나중에 method로만 바꾸면 된다.
  - Django에서는 PUT, DELETE가 없어 짜기가 좀 어렵다. Django RESTful 프레임워크로
  - HTML 코드에서 쓸 수 있는 것이 아니다, HTML에서 지원하는 것이 아니기 때문. **Javascript에서 지원**한다.

- next=

- 지금까지 온 page의 경로 사항을 저장하여 parameter의 값으로 넘겨줌

- html 파일 내에서

  {{ }} : print out하기 위함

  {% %} : function 이용

### 오늘의 핵심은 재사용성!(=모듈화)
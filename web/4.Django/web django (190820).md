# django (190820)

## C.R.U.D

- table을 이용해 게시판을 만들자 (BOARD 프로젝트 생성)

1. MTV 패턴에서는 Model을 먼저 기획하는게 정석
2. workflow
   - url
   - View
   - Template



### Model 기획

```python
#models.py
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_legth=100)
    content = models.TextField()
    image_url = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



#### app 고유한 namespace 가지기

```python
#[BOARD] > [posts] > urls.py

app_name = 'posts'

urlpatters = [
    path('new/', views.new, name='new')
    path('create/', views.create, name='create')
]
```



#### 반복문을 사용한 테이블 생성



게시판 만들기 -> 글 작성 -> 삭제 & 수정

데이터를 지워도 id는 보존된다 (레퍼런스 관계가 꼬이는 것을 방지하기 위해)
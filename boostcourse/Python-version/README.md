# Boostcourse prj3 Django ver.

본 페이지는 Boostcourse web 과정을 python django로 구현하는 과정을 기록하고자 만든 페이지입니다.



## 1001 

- Django project 생성
- 다운받은 sql파일 2개(테이블 정의, 초기 데이터)를 생성한 Django project와 연동해야 했다.
  - 방법1) Django 자체에서 sql 파일을 line-by-line 읽어오게 하는 시도를 했지만 실패. 한글 String에 의한 에러가 발생한 것으로 추정됨
  - 방법2) MySQL을 설치하여 다운받은 sql파일의 쿼리를 MySQL 상에서 실행. `boostcourse` 라는 db를 만들어 sql파일에 작성된 테이블과 데이터 저장.
    - MySQL에 저장된 데이터와 Django 프레임워크를 연동해줘야 했음. settings.py의 database 설정 변경 후 migrate.
    - models.py에 테이블들에 대한 정의가 되어있지 않으므로, `python manage.py inspectdb` 명령을 사용해 model class들을 자동 생성. 그대로 사용하기에는 잘못된 부분들이 있으므로, 실제로 MySQL에 테이블로 저장되어 있는 클래스들만 남김.
    - 이 때, `managed = False`옵션은 그대로 두어 이미 생성되어 있는 테이블들이 또 생성되는 것을 방지한다.



**예약 생성**

- create_date  & modify_date : 생성시, 수정시 자동적으로 추가되도록 해야함.
  - `auto_now_add=True`, `auto_now=True`
- 


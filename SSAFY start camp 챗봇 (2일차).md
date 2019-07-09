# SSAFY start camp 챗봇 (2일차, 190709)

## 파이썬 기초

### (복습)

### Webbrowser 모듈

```python
webbrowser.open()
webbrowser.open_new()
webbrowser.open_new_tab()
```

---



### 정보 스크랩하기

셀레니움을 이용한 scrapping? -> 심화

자주 확인하는 정보를 (자동)스크랩하기 ex)코스피지수, 부동산가격 등

대부분 다음의 4가지 스텝을 밟게 된다.

1. Naver에 접속
2. 정보를 **검색**
3. **원하는 정보만 복사**한다.
4. 내 컴퓨터에 **저장**한다.



### 서비스

모든 (웹)서비스는 2가지 패턴을 가진다.

- **Request** (Client -> Server): URL 을 통해 이루어짐
- **Response** (Server -> Client): 문서의 형태(html, xml, json)



### Package 다운로드 (pip)

파이썬 패키지 관리 프로그램

```shell
pip list # 가지고 있는 패키지 리스트 확인
pip install pkg_name
```



### Requests 모듈

```python
requests.get(주소)		# 주소에 요청을 전달, 응답을 리턴
requests.get(주소).text	# 응답받은 문서 리턴
requests.get(주소).status
```

* Response [200] : Status code 200(성공) 

* Status code 정리 자료 [https://gracefullight.dev/2017/05/28/HTTP-Status-Code-정리/](https://gracefullight.dev/2017/05/28/HTTP-Status-Code-정리/)

  

### Beautiful Soup4 모듈

문서 내의 정보 검색을 빠르게 해주는 모듈 (추후 자세히 다룰 것)

받아온 문서를 예쁘게 만들자 (파이썬의 입장에서 이쁘게) = parsing

```python
response = requests.get(url).text
document = bs4.BeautifulSoup(response, "html.parser")
```

식별자(HTML ID)를 기준으로 검색이 가능해진다.

```python
kospi = document.select_one('#KOSPI_now').text #CSS Selector로 검색.
```



#### kospi.py 전체 코드

```python
import requests
import bs4

url = "https://finance.naver.com/sise/"

response = requests.get(url).text
document = bs4.BeautifulSoup(response, "html.parser")

kospi = document.select_one('#KOSPI_now').text
kosdaq = document.select_one('#KOSDAQ_now').text
kospi200 = document.select_one('#KPI200_now').text

print('현재 코스피 지수는 : ' + kospi)
print('현재 코스닥 지수는 : ' + kosdaq)
print('현재 코스피200 지수는 : ' + kospi200)
```

최근의 웹들은 javascript가 많이 사용돼 위 방법이 통하지 않는 경우가 많다.



Scrapping 추가 예제

### 네이버 검색어 순위(1위) 가져오기

```python
import requests
import bs4

#1등 검색어 뽑기
url_search = "https://www.naver.com/"
response_search = requests.get(url_search).text
document_search = bs4.BeautifulSoup(response_search, "html.parser")

first_place = document_search.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k').text
print('\n현재 검색어 1등은 : ' + first_place)
```



### 네이버 검색어 순위(1~10위) 가져오기 (select_one 사용한 경우)

```python
#상위 10개 검색어 가져오기 (select_one 사용한 ver.)
base_tag = "#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > "
for i in range(10):
    second_tag = "li:nth-child(" + str(i+1) + ") > a.ah_a > span.ah_k"
    full_tag = base_tag + second_tag
    current_keyword = document_search.select_one(full_tag).text
    print("{0}등 검색어는: {1}".format(i+1, current_keyword))
```



### 네이버 검색어 순위(1~10위) 가져오기 (select 사용한 경우)

```python
#상위 10개 검색어 가져오기 (select 사용한 ver)
keyword_list = document_search.select("span.ah_k")
for i in range(10):
    current_keyword2 = keyword_list[i].text
    print("{0}등 검색어는: {1}".format(i+1, current_keyword2))
```



----

### git (VCS: 코드 관리도구)

git은 사용할 때 항상 현재 상태를 확인하는 습관이 중요 

```shell
git status	#추적되지 않는 파일들 찾아줌
git log		#저장내역

git add		#git add . > 추적되지 않는 것들 다 넣자(저장목록에 파일 추가)
git commit	#commit = save, 실질적인 저장 단계. git commit -m "1" (저장 메세지)
git push	#잔디 심기. git push -u origin master는 처음에만
```

- `add`, `commit`은 로컬에서 일어나는 일, `push`는 원격으로 네트워크에 업로드하는 행위.
- 다운로드 받을 때는 ` clone` 명령 사용 (repository를 복제)

```shell
git clone https://github.com/Kuhnhee/chatbot-python.git
```

- 기본적 원칙 **진실은 깃헙에 있다.**
- pull - push 시나리오
  1. SSAFY 컴퓨터 -> github : push
  2. github ->  집 컴퓨터 : clone
  3. 집 컴퓨터에서 작업한 뒤
  4. 집 컴퓨터 -> github : push
  5. SSAFY 도착, github -> SSAFY : **pull**
  6. SSAFY에서 작업

```shell
git pull origin master
```

- `pull` : repository를 들고 있을 때, 차이를 당겨올 때 사용

- `clone` : repository를 처음 당겨올 때 

  

---



### 파일 조작(파일명 바꾸기...등등)

```python
import os
os.chdir('주소')			#작업하고 있는 위치 변경
os.listdir('주소')		#default: 현재 작업 디렉토리의 파일목록 리스트 형태로 리턴
os.rename('현재이름','바꿀이름')
```

* `mv 현재파일명 바꿀파일명` shell command로도 이름 변경 가능

```python
os.system('ls')			#command창에 ls 입력한 것과 동일
#100번 반복하여 파일을 생성
for i in range(100):
    os.system('touch ./report/report{0}.txt'.format(i))	#삽입 (3.5버전)
    os.system(f'touch ./report/report{i}.txt') #위와 동일 (fstring) (3.6버전 이상)
```

여러개의 파일의 이름을 일괄적으로 변경하기

```python
#200개의 파일의 이름 수정 (report.txt -> samsung_report.txt)
for i in range(200):
    os.rename('./report/report{0}.txt'.format(i), './report/samsung_report{0}.txt'.format(i))
```

```python
#100개의 파일의 이름 수정 (samsung_report.txt -> SSAFY_report.txt)
for i in range(200):
    name_b = './report/samsung_report{0}.txt'.format(i)
    name_after = name_b.replace('samsung', 'SSAFY')
    os.rename(name_b, name_after)
```

파일 열기

```python
f = open('ssafy.txt','w') #open('파일명', '뭐 할건지')
f.write('hell saffy')
f.close()				   #open()과 반드시 쌍으로 존재해야 한다.
```

- open() 모드 중  `'w'`  : 있던 거에 덮어쓴다. 추가만 하고 싶으면 `'a'` 모드로

with - as 문을 사용한 파일 열기 (**사용 뒤 닫을 필요가 없다.**)

```python
with open('ssafy.txt','w') as f:
    for i in range(5):
        f.write('with를 쓸까말까\n')
```

한글 입력하기 (encoding)

```python
with open('ssafy.txt','w', encoding='utf-8') as f:
    for i in range(5):
        f.write('with를 쓸까말까\n')
```

파일 읽기, **readlines()** 사용

```python
with open('ssafy.txt', 'r', encoding='utf-8') as f:
    result = f.readlines()
    print(result)
```



### Task

#### task 1)

```python
# 1 problem.txt 파일을 생성 후, 다음과 같은 내용을 작성
'''
0
1
2
3
'''
with open('problem.txt', 'w') as f:
    for i in range(4):
        f.write(str(i)+'\n')
```

#### task 2)

```python
# 2 problem.txt의 파일 내용을 다음과 같이 변경
'''
3
2
1
0
'''
with open('problem.txt', 'w') as f:
    for i in reversed(range(4)):
        f.write(str(i)+'\n')
```

#### task 3)

```python
# 3 problem.txt의 내용물을 역순으로 바꾸어 reverse.txt에 저장
with open('reverse.txt', 'w') as r, open('problem.txt', 'r') as p:
    text = p.readlines()
    text.reverse()
    for i in range(len(text)):
        r.write(text[i])
```





### 자잘한 팁

`ctrl + /` : 여러 줄 주석

`drag + tab` : 여러 줄 indent

`shift + tab` : indent 해제












# SSAFY python basic (190717)

## Python 기초 (function, 재귀)



### URL 만들기 (kobis API)

```python
import datetime

def my_url(key, dt = None):
    
    if dt == None:
        dt = (datetime.date.today() - datetime.timedelta(days = 1)).isoformat().replace('-','')
    
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    result_url = f'{base_url}key={key}&targetDt={dt}'
    
    return result_url

# (1) 입력 argument들을 dictionary로 받는 방법
data = {
    'key' : 'd976d0eb8db9d4a1387c2c526c90d7cc',
    'dt' : '20190716'
}
my_url(**data)

# (2) dt를 따로 지정해주지 않았을 때, 기본값으로 어제 날짜를 입력한 url을 반환한다.
my_url('d976d0eb8db9d4a1387c2c526c90d7cc') 

# (3) dt를 따로 지정해 줄 경우, 지정된 날짜에 맞는 url을 반환한다.
my_ul('d976d0eb8db9d4a1387c2c526c90d7cc', '190715')
```

### URL 검증

앞서 작성한 my_url 함수를 url_check에서 불러올 때, 요청변수의 양식이 정확한지를 검증한다.

```python
def url_checker(key=None, targetDt=None):
    if key == None:
        return '필수 요청변수가 누락되었습니다.'
    else:
        url = my_url(key, targetDt)
        if targetDt == None:
            return 'API url: {} 어제 날짜로 조회하는 url이 생성되었습니다.'.format(url)
        else:
            return 'API url: {}'.format(url)
    
url_checker('d976d0eb8db9d4a1387c2c526c90d7cc', '190610')
url_checker('d976d0eb8db9d4a1387c2c526c90d7cc') #어제의 날짜가 들어간 url 작성
url_checker()	# '필수 요청변수(key)가 누락되었습니다' 반환
```

함수를 선언할 때, argument값에 None을 기본값으로 설정해 줄 수 있다. 이 경우 해당 함수를 호출할 때, None을 기본값으로 정한 변수의 경우 입력값으로 전달해주지 않더라도 에러가 발생하지 않는다.

```python
def function(val1, val2=None)
	...
    return
function(val1) #val2값을 전달해주지 않더라도 에러가 발생하지 않는다.
```

----

### Scope

파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있으며, **LEGB Rule**을 가지고 있다.

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나가게 된다.

- `L`ocal scope: 정의된 함수
- `E`nclosed scope: 상위 함수
- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

```python
a = 0
print(c)    # x
print(b)    # x
print(a) 

def room():
    b = 0
    print(c)    # x
    print(b)
    print(a)
    
    def toilet():
        c = 0
        print(c)
        print(b)
        print(a)
        print(sum)	# built-in 함수이므로 불러올 수 있다.
```

아래 예제는 greeting 이라는 namespace에 함수가 저장됨에 따라, 기존에 저장된 문자열이 사라졌음을 확인할 수 있다.

```python
greeting = 'hello'
def greeting():
    return 'hi'
print(greeting)
'''
<function greeting at 0x05C24A08>
'''
```

전역에 있는 변수를 바꾸고 싶다면, `global` keyword를 활용할 수 있다. (쓰지 않는 것을 권장) local_scope 함수 내부에서 함수 바깥에 선언되어있는 global_num 변수 값을 변경시킬 수 있다.

```python
global_num = 10
def local_scope():
    global global_num
    global_num = 20
    print(global_num)

local_scope()	#20
print(global_num)	#20	전역변수 global_num이 10에서 20으로 변경되었다.
```

namespace의 생명주기

* built-in scope : 파이썬이 실행된 이후부터 끝까지 

* Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지

* Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할때 까지



---

### 재귀

자기 자신을 호출하는 함수를 의미

```python
#팩토리얼
def factorial(n):
    #재귀를 이용한 팩토리얼 계산에서의 base case는 n이 1일때, 함수가 아닌 정수 반환하는 것이다.
    if n == 1:
        return 1
    return(n * factorial(n-1))
factorial(5)
```

- **재귀는 base case 찾는게 가장 중요하다.**

```python
#피보나치 수열
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib(4)
```

- 재귀함수는 성능상으로 for문에 비해 별로다.


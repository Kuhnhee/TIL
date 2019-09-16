# python basic (190715)

## Python 기초 (저장)

### 디렉토리 준비

```shell
git clone https://github.com/ssafy21/python.git 8ython #8ython 이라는 폴더에 저장됨
```



---



### Python interactive (on git bash)

```shell
python -i
exit()	#나가기
```



---



### Jupyter Notebook

```shell
pip install jupyter
```

```shell
jupyter notebook #현재 디렉토리에서 실행
```

- ipynb 파일의 자료구조 형태는 json 형태
- 크롬 > 설정 > 글꼴 맞춤설정 > Serif > D2Coding 설정하여 폰트 변경 가능
- .md 문법 그대로 적용 가능
- `shift` + `Enter`로 실행 가능



#### 식별자 확인

```python
# 식별자들을 직접 확인해봅시다.
import keyword
keyword.kwlist
```



#### integer -> string 변환

```python
# 5를 string으로 바꿔봅시다.
str(5)
```

```python
# 예시로 str에 값을 할당해보고, 오류를 확인해봅시다.
str = "hello"
str(5)		#error : 사용하던 함수 이름에 억지로 "hello"를 넣었기 때문에 발생
```

상단 Kernel > Restart & Clear Output으로 깔끔하게 초기화 가능



#### 변수 삭제

```python
# 뒤에 코드에 영향이 가니까 변수를 메모리에서 지워줍시다!!!!
del str
```



#### 주석

- 주석은 `#`
- `ctrl`+`/`  단축키
- """ 주석처리하고 싶은 문단 """ (docstring)

```python
# docstring은 다음과 같이 확인할 수 있습니다.
def mysum(a, b):
    """
        난 집에 가고 싶다.
        이 줄은 시행이 되지 않습니다.
        docstring을 쓰는 이유는 __doc__ 을 사용하기 위해
    """
    return a + b


#이 함수에 대한 설명을 docstring을 출력시키는 것으로 확인 가능하다. string type return
mysum.__doc__ 

```



#### 한 줄 쓰기

`;`을 활용하여 한 줄에 여러 함수를 불러올 수 있다. (거의 쓰이지 않는다.)

```python
# print문을 한줄로 이어서 써봅시다. 
print("happy");print("hacking")
```



#### 여러 줄 작성하기

파이썬은 `Enter` 를 치는 순간, 코드가 끝났다고 인식을 하게 된다. 이를 해결하기 위해 `\` 사용

```python
print("\
      파이썬은 쉽다.\
      파이썬은 강력하다.\
      ")
```

 `[]` `{}` `()`는 `\` 없이도 가능하다.

```python
matjip = {
    "짬뽕": "베이징코야",
    "햄버거" : "바스버거",
    "닭도리탕" : "고갯마루",
    "부대찌개" : "대우식당",
    "돼지고기" : "백운봉 막국수"
}
```



#### 변수 및 자료형

3가지 기본 자료형 : 숫자 / 글자 / boolean

* 변수는 `=`을 통해 할당(assignment) 된다. 

* 해당 자료형을 확인하기 위해서는 `type()`을 활용한다.

* 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

같은 값을 여러 변수에 동시에 할당할 수 있다.

```python
x = y = 1004
```

두 개의 변수에 값 두 개를 할당할 수 있다.

```python
# 동시에 두개의 변수에 값 두개를 할당해봅시다
name, age = "john", 27		# (name, age) = ("john", 27)과 본질적으로 같다.
```

다중 할당을 할 때에는, 변수의 개수와 할당하는 값의 개수는 같아야 한다.

```python
#error
a, b = 1
#error
a, b = 1, 2, 3
```

두 변수의 값을 서로 교환하기 (swapping)

```python
# 변수 x와 y의 값을 바꿔봅시다.

# 방법 1
x, y = 5, 10
temp = y
y = x
x = temp

# 방법 2
x, y = y, z
```



#### 수치형(Numbers)

##### int(정수)

- 모든 정수는 `int`로 표현된다.
- 파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 형으로 표기 된다.
- 10진수가 아닌 8진수 : `0o`/2진수 : `0b` /16진수: `0x`로도 표현 가능하다. 

##### Overflow

- 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
- 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

##### arbitrary-precision arithmetic
- 파이썬에서 **아주 큰 정수**를 표현할 때 사용하는 메모리의 크기 변화
- 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 **가용 메모리를 모두** 수 표현에 끌어다 쓸 수 있는 형태.
- 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용 할 수 있게 유동적으로 운용.

```python
# 파이썬에서 가장 큰 숫자를 활용하기 위해 sys 모듈을 불러옵니다.
# 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형에서 오버플로우가 없다.
# arbitrary-precision arithmetic를 사용하기 때문이다. 
import sys
max_int = sys.maxsize
print(max_int)
big_num = max_int * max_int
print(big_num)
```

##### n진수

```python
# n진수를 만들어보고, 출력 해봅시다.
binary_number = 0b10
print(binary_number)

octal_number = 0o10
print(octal_number)

decimal_number = 10
print(decimal_number)

hexadecimal_number = 0x10
print(hexadecimal_number)
```

##### float (부동소수점)

실수는 `float`로 표현된다. 

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, **항상 같은 값으로 일치되지 않는다.** (floating point rounding error)

```python
# 변수에 실수를 넣고 해당 변수의 type을 알아봅시다.
a=3.5
print(a)

# e를 사용할 수도 있습니다.
b = 314e-2
print(type(b))
print(b)
```

정수 + 실수 = 실수

```python
# 실수의 덧셈을 해봅시다.
3 + 3.5		# 6.5
```

**파이썬에서의 부동소수점 연산은 부정확하다.**

```python
# 실수의 뺄셈을 해봅시다.
3.5-3.15	# 0.3500000000000001	(부동소숫점 연산은 정확도에 한계 존재)

# 우리가 원하는대로 반올림을 해봅시다.
round(3.5-3.15, 2)		# 소숫점 둘 째 자리까지

# 두 개의 값이 같은지 확인해봅시다.
(3.5-3.15) == 0.35		# False
```

위 문제를 다음과 같이 처리할 수 있다.

- abs() 사용

- ```python
  a = 3.5-3.15
  b = 0.35
  abs(a-b) <= 1e-10
  ```

- sys module 사용

- ```python
  # sys 모듈을 통해 처리하는 방법을 알아봅시다.
  import sys
  abs(a-b) <= sys.float_info.epsilon
  ```

- math library 사용(3.5버전 이후)

- ```python
  import math
  math.isclose(a,b)
  ```

##### complex(복소수)

```python
a = 3-4j
type(a)#complex
```

허수부, 실수부를 따로 볼 수 있다.

```python
a.image
a.real
```



#### Bool

True, False로 이루어진 타입

숫자 중에서 **0은 False**, 이 외는 True

비어있는 list, dict, string은 False. 비어있지 않으면 True

```python
bool(0)    #False
bool(None) #False
bool([])   #False
bool({})   #False
bool("")   #False
```



#### None

print()는 아무것도 리턴하지 않는 함수. print()가 리턴한 값을 print() 할려고 하면 None 발생

```python
# None의 타입을 알아봅시다.
print(print('hello')) #hello\nNone
```

```python
# 변수에 저장해서 확인해봅시다.
a = None
print(a)    #None
print(type(a))    #<class 'NoneType'>
```



#### 문자형(String)

본 수업에서는 sing quotes(')로 통일해서 진행할 것이다.

```python
# 변수에 문자열을 넣고 출력해봅시다.
pro_says = '김지수 프로님은 얘기했다. "오늘은 종례가 없을 거에요."'
print(pro_says)

# 김지수 프로님은 얘기했다. "오늘은 종례가 없을 거에요."
```

```python
#아래 두 방식은 본질적으로 같은 결과를 출력
print(a, b)
print(a + " " + b)
```

입력함수 `input()`

```python
# 사용자에게 받은 입력은 기본적으로 str입니다
greeting = input('한마디 해주세요')
print(greeting)
```

string 내의 quote를 기호로서 인식시키는 방법, 이스케이프 문자(`\`)

```python
# 오류를 이스케이프 문자와 서로 다른 문장부호를 통해 해결해봅시다.
print('철수가 말했다. \'안녕\'')
```

여러줄의 출력

- `\`를 이용해서 개행할 수 있지만, 권장하지 않는 방식이다.
- 대신, """를 사용한다.

```python
print("""여러줄에
    걸쳐서
    출력하기""")
```

string의 수술/합체

```python
# 물론 string interpolation도 가능합니다.
# 1.Concatenation(합체)
greeting = "안녕하세요," + "저는 " + "kuhn 입니다."

# 2.Interpolation(수술)
name = "kuhn"
greeting2 = f"안녕하세요, 저는 {name}입니다."
print(greeting)
```



#### 이스케이프 문자열

| <center>예약문자</center> |   내용(의미)    |
| :-----------------------: | :-------------: |
|            \n             |     줄바꿈      |
|            \t             |       탭        |
|            \r             |   캐리지리턴    |
|            \0             |    널(Null)     |
|           `\\`            |       `\`       |
|            \'             | 단일인용부호(') |
|            \"             | 이중인용부호(") |

print()함수는 마지막에 기본적으로 개행문자가 들어간다. 이를 바꾸는 방법은 다음과 같다.

```python
# print를 하는 과정에서도 이스케이프 문자열을 활용 가능합니다.
print('내용을 띄워서 출력하고 싶으면', end='\t')
print('다음 줄입니다.')
```

```python
print('위와 같은 개행문자 말고도', end='!')
print('다양한 문자를 넣을 수 있습니다.', end='!')
print('예를 들어 느낌표, 물음표 등등.', end='!')
```



#### String interpolation

1) `%-formatting` 

2) [`str.format()` ](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

`.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.

```python
# %-formatting을 활용해봅시다.
'Hello, 나는 %s입니다. 나이는 %s입니다. 전공은 %s입니다. 주소는 %s입니다.' % (name, age, major, address)

# str.format()을 활용해봅시다.
'Hello, 나는 {0}입니다. 나이는 {1}입니다. 전공은 {2}입니다. 주소는 {3}입니다.'.format(name, age, major, address)

# f-string을 활용해봅시다.
f'Hello, 나는 {name}입니다. 나이는 {age}입니다. 전공은 {major}입니다. 주소는 {address}입니다.'
```

```python
import datetime
today = datetime.datetime.now()
print(today)

#오늘은 xxxx년 xx월 xx일 xx
print('오늘은 {}년 {}월 {}일 {}'.format(today.year, today.month, today.day, today.weekday()))
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%y}일 {today:%A}')
```



#### 연산자

##### 산술 연산자

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| \*     | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| \*\*   | 거듭제곱       |

- `divmod()` 함수

```python
divmod(5, 2) #(2, 1) 몫, 나머지
quotient, remainder = divmod(5, 2)	#quotient = 2, remainder = 1
```

##### 비교 연산자

| 연산자 | 내용     |
| ------ | :------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |

파이썬에서의 정수, 실수 간 비교 주의할 것

```python
# 다른 숫자인지 확인해봅시다.
3.0 == 3	#True
```

파이썬에서 대문자, 소문자는 다르다.

```python
# 문자열도 같은지 확인해봅시다.
"Hi" == "hi"	#False
```

#####  논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

* 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
* 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.

```python
#단축평가(short-circuit evaluation)에 대해서 알아봅시다.
print(3 and 5)	#5 출력
print(3 and 0)	#0 출력
print(0 and 3)	#0 출력
print(0 and 0)	#0 출력
print(False and 3)	#False 출력
print(True and 3)	#3 출력

print(3 or 5)	#3 출력
print(3 or 0)	#3 출력
print(0 or 3)	#3 출력
print(0 or 0)	#0 출력
print(False or 3)	#3 출력
print(True or 3)	#True 출력
```

##### 복합 연산자

| 연산자    | 내용       |
| --------- | ---------- |
| a += b    | a = a + b  |
| a -= b    | a = a - b  |
| a \*= b   | a = a \* b |
| a /= b    | a = a / b  |
| a //= b   | a = a // b |
| a %= b    | a = a % b  |
| a \*\*= b | a = a ** b |

##### 기타 연산자

- Concatenation:
- Containment Test (`in`)
- Identity (`is`)
- Indexing/Slicing (`[]`,`[:]`)

```python
# is는 맛만 봅시다.
# 파이썬에서 -5부터 256까지의 id는 동일합니다.
# ex) -5의 id는 어디서 쓰든 동일하다~ 라는 의미. -5와 255의 id가 같다는 의미가 아니다.
# 빈번하게 쓰이는 숫자들은 동일한 메모리에 미리 올려져있기 때문이다.
id(-5) is id(256) #False
id('hi') is id('hi') #False, 두 'hi'는 서로 다른 메모리에 올려져 있음
id(0) is id(0) #False, 왜? id(0)에 해당하는 숫자는 -5~256를 벗어난 숫자이기 때문에, 앞에서 부른 id(0)과 뒤에서 부른 id(0)은 서로 다른 메모리에 위치하게 된다. id값(정수)은 동일하다.
```



#### 연산자 우선순위

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자
    \*\*
4. 단항연산자 
    +, - (음수/양수 부호)
5. 산술연산자
    \*, /, %
6. 산술연산자
    +, -
7. 비교연산자, `in`, `is`
8. `not`
9. `and` 
10. `or`



#### 암시적 형변환

```python
# int, float, complex를 각각 변수에 대입해봅시다.
int_number = 3
float_number = 5.0
complex_number = 3 + 5j

# int와 float를 더해봅시다. 그 결과의 type은 무엇일까요?
int_number + float_number # 8.0

# int와 complex를 더해봅시다. 그 결과의 type은 무엇일까요?
int_number + complex_number # 6+5j
```



#### 명시적 형변환

```python
#int -> string
str(1) + '등'	#'1등'

#string -> float
b='3.5'
float(b) + 5.0	#8.5

#string '3.5'를 바로 int로 바꿀 순 없다.
int(b) #error
#대신, float로 바꾼 뒤 int로 형변환 가능하다.
int(float(b))


```



#### 시퀀스(sequence) 자료형

파이썬에서 기본적인 시퀀스 타입은 다음과 같다.

1. 리스트(list)

2. 튜플(tuple)

3. 레인지(range)

4. 문자열(string)

5. 바이너리(binary) 



##### list

```python
# 빈 리스트를 만들어봅시다.
l = []
ll = list()
# 원소를 포함한 리스트를 만들어봅시다.
location = ['강남', '강북', '강동', '강서']
# 첫번째 값에 접근해봅시다.
location[0]
```

##### tuple

list와 달리, **immutable(수정 불가)**하고 읽기만 가능하다.

```python
# tuple을 만들어봅시다.
tp = (1,2,3,4,5)
tp2 = 1,2,3,4,5 #괄호를 안 써도 된다.

```

##### range

list로의 형변환이 가능하다.

```python
#range -> list 형변환
r = range(10)
l = [1,2,3,4,5,6,7,8,9]
list(r) == l #True
# 0부터 -9까지 담긴 range를 만들어봅시다.
range(0,-10,-1)
# 0부터 9까지 2씩 증가하는 range
range(0,10,2)
```

##### 시퀀스에서 사용할 수 있는 연산자/함수

| operation  | 설명                    |
| ---------- | ----------------------- |
| x in s     | containment test        |
| x not in s | containment test        |
| s1 + s2    | concatenation           |
| s * n      | n번만큼 반복하여 더하기 |
| s[i]       | indexing                |
| s[i:j]     | slicing                 |
| s[i:j:k]   | k간격으로 slicing       |
| len(s)     | 길이                    |
| min(s)     | 최솟값                  |
| max(s)     | 최댓값                  |
| s.count(x) | x의 개수                |

```python
# 숫자 0이 6개 있는 list를 만들어봅시다.
[0]*6		#[0,0,0,0,0,0]
[1,2,3]*3	#[1,2,3,1,2,3,1,2,3]

# 두번쨰, 세번쨰 값만 가져와봅시다.
location = ['서울','대전','광주','부산','제주','대구']
location[1:3]	#['대전','광주']

#list step
location[1:6:2] #2step씩 ['대전', '부산', '대구']
location[::-1]	#뒤집기, string에도 자주 사용

# 0부터 30까지의 숫자를 3씩 증가시킨 상태로 만들어봅시다.
r = list(range(0,31,3))
# 위에서 만든 list의 길이를 확인해봅시다.
length = len(r)
# 위에서 만든 list의 최솟값, 최댓값을 확인해봅시다.
min(r)
max(r)
# list에 담긴 특정한 것의 개수를 확인할 수도 있습니다.
r.count(31)
```

##### set, dictionary

순서가 없는 자료구조(순서를 기준으로 찾던 list와 본질적으로 다르다.)

##### set

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합집합 |
| a & b             | 교집합 |
| a.difference(b)   | 차집합 |
| a.union(b)        | 합집합 |
| a.intersection(b) | 교집합 |

- set은 중복된 값이 있을 수 없다.

```python
li = [1,2,2,3,3,3,4,4,4,4]
list(set(li))	#[1, 2, 3, 4]
```

##### dictionary

```python
# 비어있는 dictionary를 두가지 방법으로 만들어봅시다.
dict_a = {}
dict_b = dict()
```

dictonary는 key가 중복될 경우, 나중에 선언된 value가 최종적으로 저장된다.

```python
# dictionary는 중복된 key는 존재할 수가 없습니다.
phonebook['서울'] = '01'
phonebook 
'''
    phonebook = {
        '서울':'01',
        '경기':'031',
        '인천':'032'
    }
'''
```

key, value를 추출할 수 있다. 순회 가능한 iterable 자료형을 반환하지만, list처럼 indexing을 할 수는 없다. list로 변환한 뒤에는 indexing 가능하다.

```python
# 딕셔너리의 메소드를 활용하여 key를 확인 해볼 수 있습니다.
phonebook.keys()
# 딕셔너리의 메소드를 활용하여 value를 확인 해볼 수 있습니다.
phonebook.value()
```

- 3.6버전 이후에는 key, value pair 순서가 고정되도록 바뀜. 그 이전 버전은 dictonary를 불러올 때마다 순서가 바뀌었다.
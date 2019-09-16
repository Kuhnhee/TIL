# python basic (190722)

## 모듈

- `hello.py`를 다음과 같이 작성한 뒤, 이를 다른 프로그램에서 모듈로서 호출할 수 있다.

```python
#hello.py
def hi():
	return "안녕하세요"
```

```python
#main_program.py
import hello
hello.hi()	#안녕하세요
```

- 모듈들의 묶음을 패키지라고 한다. 연습을 위해 다음과 같은 폴더 구조를 만든다.

```
- /myPackage
    - __init__.py
    - /math
        - __init__.py
        - formula.py
    - /web
        - __init__.py
        - url.py
```

위 폴더 구조에서 myPackage, math, web이라는 폴더 각각의 기본(default) 파일은 `__init__.py`이다.

- formula.py 내에 my_pi()라는 함수를 선언했을 경우, 다음과 같이 불러올 수 있다.

```python
from myPackage.math.formula import my_pi
```

- Asterisk`*`를 사용하여 모듈 내의 모든 함수, 변수, 클래스를 가져올 수 있다. **하지만**, 우리가 자주 사용하는 변수,함수 명과 동일한 이름의 변수,함수가 import될 우려가 있어 사용을 권장하지 않는다.

```python
from module_name import *
```

- 여러 개의 함수, 변수를 import하고자 할 때에는 다음과 같이 `,`를 사용한다.

```python
from datetime import datetime, date
datetime.now()
date.today()
```

- 이름을 바꿔서 가져올 수도 있다.

```python
import module_name as new_name
```

- 현재 실행되는 python 파일과 동일한 폴더에서 우선적으로 패키지를 찾은 뒤, 없으면 system path를 뒤져서 호출하고자 하는 패키지를 찾는다. (패키지 검색 우선순위는 sys.path를 통해 확인 가능하다.)

```python
import sys
sys.path
```

- python import 참고자료: https://wikidocs.net/1418



### 숫자 관련 함수

`import math`

| 함수                | 비고                            |
| ------------------- | ------------------------------- |
| math.ceil(x)        | 소수점 올림                     |
| math.floor(x)       | 소수점 내림                     |
| math.trunc(x)       | 소수점 버림                     |
| math.copysign(x, y) | y의 부호를 x에 적용한 값        |
| math.fabs(x)        | float 절대값 - 복소수 오류 발생 |
| math.factorial(x)   | 팩토리얼 계산 값                |
| math.fmod(x, y)     | float 나머지 계산               |
| math.fsum(iterable) | float 합                        |
| math.modf(x)        | 소수부 정수부 분리              |

- 내림과 버림은 음수에서 다르게 작용한다.

```python
# 내림
math.floor(-3.5)	# -4
# 버림
math.trunc(-3.5)	# -3
```

- `math.pow()`의 경우, 입력값이 정수더라도 float가 결과로 나온다.

```python
# 제곱
5**2	#25
math.pow(5,2)	#25.0
```

- `random.seed(seed_value)`를 한 값으로 고정해 놓을 경우, 항상 동일한 값이 `random()`의 결과로 나온다. 기본적으로 현재 시간을 seed값으로 사용한다.

---



## 에러

### 문법 에러 (Syntax Error)

- 문법적으로 규칙을 지키지 않은 경우 발생하는 에러
- 정확한 위치를 지정하지 않을 수도 있으므로 앞뒤로 모두 확인을 해봐야 한다.



### 예외 Exceptions

- 문법, 표현식은 맞지만 실행시 발생하는 에러

1. ZeroDivisionError: 0으로 나눈 경우
2. NameError: 정의하지 않는 이름을 부른 경우
3. TypeError: int + string, round('string') 과 같이 변수 타입을 안지킨 경우, 함수 positional argument 갯수 틀린 경우.
4. ValueError: int('3,5') 잘못된 값을 넣은 경우, list에 없는 값을 찾을 경우
5. keyError:  없는 key값을 dict에서 찾을 경우
6. ModuleNotFoundError: import 대상을 찾지 못한 경우
7. ImportError: import하고자 하는 라이브러리의 대소문자를 잘못 쓴 경우
8. KeyboardInterrupt: 프로그램이 실행되는 도중 키보드에 의해 실행 중단된 경우



### try-except

사용자의 입력을 받아 2진수인지 확인하는 코드. 만약 숫자가 아닐 경우, "숫자가 아닙니다."를 출력한다.

```python
# set을 이용한 풀이
num = input()

try:
    float(num)
    if set(num).issubset({'0','1'}):
        print("2진수다")
    else:
        print("2진수 아니다.")
except:
    print("숫자가 아니다.")
```



사용자가 입력한 값으로 100을 나눈 후 출력하는 코드

```python
try:
    num = input()
    print(100/int(num))
except ZeroDivisionError:
    print('0 노노')
except ValueError:
    print('숫자 넣어')
except:
    print('뭔지 모르겠지만 일단 에러 남')
```

- 여기서 중요한 내용은 **에러가 순차적으로 수행됨**으로, 가장 작은 범주부터 시작해야합니다.



에러 메세지를 그대로 출력시키는 것도 가능하다.

```python
try:
    num_list = [1,2,3]
    print(num_list[5])
except IndexError as err:
    print(f'{err} 에러가 났어요')
```



### try-except-else-finally

- else : 예외가 발생하지 않은 경우 거치게 되는 블록
- finally : 예외 발생 여부에 상관 없이 거치게 되는 블록



### 예외 발생시키기(raise)

```python
# 에러를 우리가 통제해서 사용한다.
raise ValueError('에러')
'''
ValueError                         Traceback (most recent call last)
<ipython-input-22-fb527def7d31> in <module>
      1 # 에러를 우리가 통제해서 사용한다.
----> 2 raise ValueError('에러')

ValueError: 에러
'''
```



### 예외 발생시키기 (assert)

```python
assert Boolean expression, error message
```

위의 검증식이 거짓일 경우 AssertionError를 발생한다.

```python
def my_div(num1, num2):
    assert type(num1) == int and type(num2) == int, '정수가 아닙니다.'
    try:
        result = num1/num2
    except ZeroDivisionError as ze:
        print(f'{ze} 에러가 발생했습니다.')
    else:
        return result
    
my_div('1', '2')
my_div(10, 0)
```



--------------------------------------------------



### TDD 방법론 (Test Driven)

- 실패할 수 있는 케이스들을 우선하여 극복하는 방식으로 프로그램 개발










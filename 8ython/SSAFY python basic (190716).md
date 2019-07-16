# SSAFY python basic (190716)

## Python 기초 (control flow, function)



### Jupyter notebook 실행 명령어를 단축시키기

```shell
code .bashrc #home directory
```

```
#.bashrc
alias jn='jupyter notebook'
```

jupyter notebook의 줄임말로 jn이 사용 가능해진다.

```shell
source ~/.bashrc	#방금 작성한 파이을 한 번 실행시켜 줘야함
```



---



### 제어문

**반복문, 조건문**으로 나누어진다.

#### 조건문

- 참/거짓을 판단할 수 있는 조건식을 사용해 분기하는 것
- python의 경우, **들여쓰기**(4 spaces)를 유의해야 한다.

#### 조건식

조건문을 간단하게 한 줄로 작성하고자 할 때 활용

```python
num = -5
value = num if num >= 0 else 0
print(value)
```

#### 반복문

- 조건식이 True일 경우 반복적으로 코드를 실행하는 것
- **종료조건**을 반드시 설정해주어야 한다.

##### for문에는 2가지 컨셉 존재

1. loop(==while문)
2. iterate: 정해진 범위 내(시퀀스)에서 순차적으로 코드를 실행한다. 판별식 없음.

- sequence 자료형? list, range, tuple, String
- **파이썬에서는 제어문 scope 내에서의 변수에 외부에서의 접근이 가능하다. JAVA와 큰 차이** (block based scope가 python에서는 만들어지지 않는다. If, for, while 모두) 단, def는 block을 생성한다.

##### for문과 if문 혼합하기

```python
# 여기에 코드를 작성하세요.
li = [i for i in range(30) if i%2!=0]
print(li) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
```

##### `enumerate()`와 함께 for문 사용하기 (index와 값을 함께 뽑을 수 있다.)

```python
# enumerate()를 활용해서 출력해봅시다.
lunch = ['짜장면', '초밥']
for idx, menu in enumerate(lunch):
    print(idx, menu)
```

- enumerate 자료형을 list로 형변환 하는 것도 가능하다.
- enumerate 객체는 iterable하기 때문에 for문에 사용 가능한 것. iterable 객체는 `__next__`를 포함 

```python
# 숫자를 1부터 카운트 할 수도 있습니다.
list(enumerate(classroom, start=1))
#[(1, '정XX'), (2, '김XX'), (3, '김XX'), (4, '김XX')]
```

##### dict에서의 반복문 활용

```python
# 옆자리 친구의 이름을 활용하여 dictionary를 만들어봅시다.
friend = {
    '이름' : '김XX',
    '여성' : False,
    '주소' : '사X',
    '전공' : 'MaXX'
}
for key, item in friend.items():
    print(f'{key} cd {item}')
```

##### break, continue, else(반복문에서)

- break: 반복문 종료

```python
rice = ["보리", "보리", "보리", "쌀", "보리"]
# 여기에 코드를 작성하세요.
for i in rice:
    if i == '쌀':
        print('쌀\n잡았다!')
        break;
    print('보리')
```

- continue: 다음 loop를 바로 진행

```python
# 여기에 코드를 작성하세요.
age = [10, 23, 8, 30, 25, 31]

for i in age:
    if i<20:
        continue
    print("성인입니다.")
```

- else: **break에 의해 중간에 종료되지 않은 경우에 실행**(끝까지 반복문을 시행한 이후에)

```python
# break가 안되는 상황을 만들어봅시다.
for i in range(3):
    print(i)
    if i == 100:
        print(f'i={i}에서 break 걸림')
        break
else:
    print('break가 안걸림')
    
'''
0
1
2
break가 안걸림
'''
```

```python
numbers = [1, 5, 10]
# 여기에 코드를 작성하세요.
for n in numbers:
    if n == 3:
        print(True)
        break
else:
    print(False)
```



----



### 함수

함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다. 단, **오직 한 개**의 객체만 반환됩니다. 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

- 기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없습니다.

```python
# 에러
def greeting(age, name='john'):
    print(f'{name}은 {age}살입니다.')

# 수정
def greeting(name='john', age):
    print(f'{name}은 {age}살입니다.')
```

#### 키워드 인자

print()함수에는 다양한 인자들이 준재한다.

```python
print('첫번째 문장')
print('두번째 문장', end='_')
print('세번째 문장', '마지막 문장', sep="__중간__", end="끝!")
```

#### 가변 인자 리스트

정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다. **가변인자는 `tuple` 형태로 처리가 되며**, `*`로 표현합니다.

```python
print(*objects, sep=' ', end='\n', ...)
#*objects 에서의 asterisk의 의미 -> 입력값을 list로 받는다.
#따라서 여러개의 string이 입력되어도, 이를 list로 받아 출력시킬 수 있다.
```

```python
# args는 tuple!
def my_sum(*nums):
    print(sum(nums)) 

my_sum(1,2,3,4,5) #15, nums = (1,2,3,4,5)
```

#### 정의되지 않은 인자들 처리 (사용자가 정의해서 쓸 수 있는 인자들), "packing"

가변 인자 리스트와 달리, `dict`의 형태로 입력값이 들어옴

ex) Flask에서 render_template()에 keyword 전달하던 방식

```python
	...
	render_template('home.html', name=name, age=age)

def render_template(XXXX, **kwargs):
```

#### dict를 인자로 넘기기, "unpacking"

```python
def user(username, password, password_confirmation):
    if password == password_confirmation:
        print(f'{username}님, 회원가입이 완료되었습니다.')
    else:
        print('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
        
my_account = {
    'username': '홍길동',
    'password': '1q2w3e4r',
    'password_confirmation': '1q2w3e4r'
}

user(**my_account)	#dict 들어간다~ 입벌려! Asterisk 2개 붙여줘야 한다.
#user(username='홍길동', password='1q2w3e4r', password_confirmation="1q2w3e4r") 동일
```



----



### map function

```python
#입력값을 split한 뒤 int함수를 적용한 다음, a, b에 assign한다.
a, b = map(int, input().split(" "))
```



------



### git

```shell
git remote -v #git 관리 대상 리포지토리 링크 정보 출력
```

```python
rm -rf .git   #.git 폴더 삭제
```

```
# .gitignore
.ipynb_checkpoints		#jupyter notebook 임시파일, git에서 제외하자
```




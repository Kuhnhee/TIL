# python basic (190718)

## Python 기초 (method)

- method와 function의 차이? `duck.run()`과 같이 어떠한 객체**(목적어 or 주어)를 조작하는 방법(동사)**을 method라고 한다. (추후 OOP 파트에서 자세히 다룰 것) 
- `dir()`를 활용해 메소드들을 확인 가능하다.
- method에는 2가지 방식이 있다.

1. Destructive : 원본 변경. 대부분 return을 하지 않는다.
2. Non-destructive : 원본 변경 X. 

---

### 변형

- `.capitalize()` : 문장의 앞글자만 대문자로 변환. 단, 뒤따라 있는 다른 대문자들이 소문자로 변환됨을 주의해야 한다. Non-destructive.
- `.title()` : 어포스트로피/공백 이후 문자를 대문자로 변환.  Non-destructive.
- `.upper()` : 모두 대문자로 변환. Non-destructive.

- `lower()` : 모두 소문자로 변환.
- `swapcase()` : 대-소문자 변환. Non-destructive.

- **`join(iterable)`** :  **string**에다가 join을 해야한다. `' '.join(list_name)` 형식. Non-d
- **`split()`** : `'010-8609-1418'.split('-')` => `['010','8609','1418']`
- `.replace()` : `string_name.replace('i', 'e')`. Non-d
- `.strip()` : **특정한 문자들을 지정**하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip) 오른쪽을 제거합니다(rstrip). 주로 줄바꿈 문자 `\n`를 제거할 때 사용된다. `'this is strip.\n'.strip('\n')`  => 끝에 개행문자 삭제.
- `.find(x)` : x의 첫 번째 위치를 반환. (중복되는 문자의 경우에도 첫 번째의 위치만 반환한다.) **없는 문자를 찾으려 할 경우, -1을 반환**
- `.index(x)` : x의 첫 번째 위치를 반환. (중복되는 문자의 경우에도 첫 번째의 위치만 반환한다.) 단, **없는 문자를 찾으려 할 경우 오류가 발생한다.**

---

### 다양한 확인 메소드

```python
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()
```

---

### List 메소드

#### 값 추가 / 삭제

- `.append(x)` : 리스트의 뒤에 값을 추가한다. Destructive
- `.extend(iterable)` : **리스트에 iterable(list, range, tuple, string*유의*) 값을 붙일 수가 있습니다.** list와 list를 붙인다는 개념(+와 동일하게 작동). Destructive
- `.insert(i, x)`  : 정해진 위치 `i`에 값을 추가한다. 길이를 넘어서는 인덱스는 무조건 마지막에 하나만 붙게 된다. Destructive
- `.remove(x)` : 중복되는 값이 있을 경우, **첫 번째 값만 삭제한다.** remove는 삭제하고자 하는 값이 이미 존재하지 않을 경우, 오류가 발생한다.
- `.pop(i)` : 정해진 위치 `i`의 값을 **삭제하면서 반환한다. Destructive 하면서 return 값 존재.**

#### 탐색 및 정렬

- `.index(x)` : x값을 찾아 그 index를 반환
- `.count(x)` : x값의 갯수를 확인하여 반환
- `.sort()` : `sorted(list_name)`와는 다르게 **Destructive하며 return값 x** `.sort(reverse=True)`를 할 경우 내림차순으로 정렬
- `.reverse()` : `reversed(list_name)`와는 다르게**Destructive하며 return값 x**
- `.clear()` : 리스트의 모든 항목 삭제

원본을 파괴하지 않는 `sorted(), reversed()`를 활용하는 것을 권장한다.

#### 복사

* 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다. 

```
num = [1, 2, 3]
```

* 위와 같이 변수를 생성하면 num이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.

* 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

```python
numbers = [1,2,3]
numbers2 = numbers
```

위와 같이 list를 복사하려고 할 경우, 주소만 복사되어 numbers2에 저장되기 때문에 numbers와 numbers2는 동일한 데이터의 주소를 가지게 된다.

```
numbers2[0] = 0
# numbers = [0,2,3]
```

numbers2의 값을 바꾸려고 해도, numbers의 값 까지 변하게 된다.

- immutable 값의 경우 값 자체가 그대로 복사가 되지만, mutable은 위와 같이 주소를 복사하게 된다.



내용물을 복사하기 위한 방법들은 다음과 같다.

```python
num = [1,2,3]

# 방법 1 (Shallow copy)
num2 = num[:]

# 방법 2 (Shallow copy)
num2 = list(num)

# deep copy
import copy
matrix = [
    [1,2,3],
    [4,5,6]
]

matrix2 = copy.deepcopy(matrix)
```

---

### List Comprehension

#### 세제곱리스트

```python
cubic_list = [i**3 for i in range(1,11)]
```

#### 짝수리스트

```python
even_list = [i for i in range(1,11) if i%2==0]
```

#### 곱집합

두 list의 가능한 모든 조합을 담은 pair 리스트 만들기

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
pair = [(girl_name, boy_name) for boy_name in boys for girl_name in girls]
```

#### 피타고라스 정리

```python
pita = [(x,y,z) for x in range(1,50) for y in range(x,50) for z in range(y,50) if ((x**2 + y**2) == z**2)]
```

#### 모음 제거하기

```python
words = 'Life is too short, you need python!'
word_changed = ''.join([c for c in words if c not in 'aeiouAEIOU'])
```

---

### Dictionary 메소드 활용

- `.pop(key[, default])` : key가 존재한다면 그 값을 **제거&반환**한다. key가 없다면 에러. 만약 default를 지정해줬다면 default 값을 반환

```python
my_dict = {'apple' : '사과', 'banana' : '바나나'}
my_dict.pop('apple')

my_dict.pop('apple', '키 없음') #'apple'이 없을 경우 '키 없음' 반환
```

- `.update(**args)` :  my_dict[key]=new_value와 달리, 여러개의 key값의 value를 한 번에 변경할 수 있다.

```python
my_dict = {'apple' : '사과', 'banana' : '바나나', 'melon' : '멜론'}
my_dict.update(apple='사과와아아', banana='바나나아아아', melon='멜로오오온')

new_dict = {'apple':'사과와아아', 'banana':'바나나아아아', 'melon':'멜로오오온'}
my_dict.update(new_dict)
```

- `.get(key[, default])` : key를 통해 value를 가져온다. key가 없어도 error가 발생하지 않고, None이 반환된다.

---

### Dictionary Comprehension

```python
#cubic dict
cubic_dict = {x:x**3 for x in range(1,11)}
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
```

- dictionary, list comprehension 내에서 else, elif문의 사용은 일반적인 if, else 한줄쓰기와 다르다. 조건문이 하나(if) 있을 때에는 조건문을 맨 뒤로 보내도 되지만, else까지 사용할 경우 for문 앞으로 와야 한다.

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

# 미세먼지 농도가 80 초과 지역만 뽑아 봅시다.
# 예) {'대전': 82, '중국': 200}
high = {key:value for key,value in dusts.items() if value>80}
print(high)

# 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꿔봅시다.
dust_new = {key:"나쁨" if val>80 else "보통" for key,val in dusts.items()}
print(dust_new)

# elif 도 사용할 수 있습니다.
# elif문을 사용할 수는 없으며, else문 다음 if-else 조건을 다시 한 번 걸어주는 방식으로 구현할 수 있다.
dust_new = {key: "나쁨" if value > 80 else "보통" if 50 <= value <80 else "좋음" for key, value in dusts.items()}
print(dust_new)
```

---

### Set 메소드 활용

- `.add(elem)` :  elem을 set에 추가한다. 중복은 제외

```python
fruits = {'사과','바나나','수박'}
fruits.add('천도복숭아')
fruits.add('자두')
#{'사과','바나나','수박','천도복숭아','자두'}
```

- `.update(*others)` : 여러가지 값들을 추가한다. 이 때, 반드시 **iterable(for문을 사용할 수 있는)**한 값을 넣어야 한다. 중복은 제외

```python
fruits = {'사과','바나나','수박'}
fruits.update(['천도복숭아','사과'])
```

- `.remove(elem)` : 특정 elem을 set에서 삭제하고, 없으면 에러 발생

- `.discard(elem)` : elem을 set에서 삭제하고, 없어도 에러가 발생하지 않는다.
- `.pop()` : **임의의 원소**를 제거해 반환한다.

----

### 정리

|      | String | List | Dictionary | Set                                       |
| ---- | ------ | ---- | ---------- | ----------------------------------------- |
| C    |        |      |            | `add()`                                   |
| R    |        |      |            |                                           |
| U    |        |      |            | `update()`                                |
| D    |        |      |            | `remove()`, `discard()`, `pop()` : 무작위 |

---

### map(), zip(), filter()

- `map(function, iterable)` : iterable 자료의 모든 원소에 function을 적용한 후, 그 결과를 map object로 반환한다. 이를 사용하기 위해서 list형으로 변환을 해줘야 한다.

```python
chars = ['1', '2', '3']
# 위의 코드를 [1, 2, 3]으로 만들어봅시다.
list(map(int,chars))
```

- `zip(*iterables)` : 복수의 iterable한 것들을 모아준다. 튜플의 모음으로 구성된 zip object를 반환한다. **zip은 반드시 길이가 같을 때 사용해야 한다.** 길이가 다를 경우, 짧은 것을 기준으로 구성하게 된다.

```python
#matching 문제의 경우
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
dict(zip(girls,boys)) #{'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
list(zip(girls,boys)) #[('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
```

- `filter(function, iterable)` : iterable에서 function에 반환된 결과가 `True`인 것들만 구성하여 반환한다.

```python
#짝수인지 판단하는 함수의 작성
numbers = list(range(1,31))

#for 버전
evens = []
for num in numbers:
    if not num%2:
        evens.append(num)

#comprehension 버전
evens = [num for num in numbers if not num%2]


#filter 버전
def even(n):
    return not n%2
list(filter(even,numbers))
```

---

### Problem set

#### 최대공약수, 최소공배수 구하기

```python
#유클리드 호제법 (최대공약수)
def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b
```

```python
#최소공배수
def lcm(a, b):
    return a*b//gcd(a,b)
```

#### 덧셈 기호 없이 더하기

```python
def Add(x, y): 
  
    # Iterate till there is no carry  
    while (y != 0): 
      
        # carry now contains common 
        # set bits of x and y 
        carry = x & y 
  
        # Sum of bits of x and y where at 
        # least one of the bits is not set 
        x = x ^ y 
  
        # Carry is shifted by one so that    
        # adding it to x gives the required sum 
        y = carry << 1
      
    return x 
```




# python basic (190723,24)

## OOP basic

이전의 프로그래밍(절차지향)이 순서도에 가까웠다면, 이를 주어+동사 형태의 직관적인(상식적인) 형태로 발전시킨 것이 객체지향 프로그래밍이다.

- 클래스: 동일한 종류, 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것
- 인스턴스: 클래스에 속하는 예시. Object와 동의어로 사용
- 속성: 클래스/인스턴스가 가지고 있는 속성
- 메서드: 클래스/인스턴스가 할 수 있는 행위



- class 내에서 함수 선언시, 혹은 변수 사용시 `self` 를 사용해야 함에 유의해야 한다.
- `self`: 인스턴스 객체 자기자신. 메서드는 인스턴스 객체가 함수의 첫번째 인자로 전달되도록 되어있다. **반드시 self를 쓰지 않아도 되며, 다른 이름으로 써도 가능하다.**



- `__str__` 를 override할 경우, 아래와 같이 사용할 수 있다.
- `__repr__`: 객체가 표현될 때 쓰이는 '문자열'

```python
class Phone
	model = 'galaxy'

	def __str__(self):
		return self.model
   	
    def __repr__(self):
        return "hello!"
    
myphone = Phone()
print(myphone)	# 'galaxy'
myphone	# 'hello!'
```



### 용어 정리

```python
class Person:                     #=> 클래스 정의(선언) : 클래스 객체 생성
    name = 'unknown'              #=> 멤버 변수(data attribute)
    def greeting(self):           #=> 멤버 메서드(메서드)
        return f'{self.name}' 
```


```python
richard = Person()      # 인스턴스 객체 생성
tim = Person()          # 인스턴스 객체 생성
tim.name                # 데이터 어트리뷰트 호출
tim.greeting()          # 메서드 호출
```



### 생성자 `__init__(self)`, 소멸자 `__del__(self)`

* 클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다. 
* 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다. 
* 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.
* 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 => 클래스 순으로 탐색을 한다.

객체가 가지는 변수의 이름공간을 분리하기 위해, 생성자를 사용해야 한다. 또, 객체가 소멸될 때의 행동을 소멸자를 사용해 정의할 수 있다.

```python
class Person:
	def __init__(self, name):
		self.name = name
        
   	def __del__(self):
        print('나는 간다.')
```

---



## OOP advanced

### 클래스 변수

- 클래스의 속성입니다.
- 클래스 선언 블록 최상단에 위치합니다.
- `Class.class_variable` 과 같이 접근/할당합니다.



### 인스턴스 변수

- 인스턴스의 속성입니다.
- 메서드 정의에서 `self.instance_variable` 로 접근/할당합니다.
- 인스턴스가 생성된 이후 `instance.instance_variable` 로 접근/할당합니다.



### 클래스 메서드

- 인스턴스 메서드와 동일하게 선언하지만, `def` 바로 위에 데코레이터 `@classmethod`를 반드시 붙여줘야 한다.
- **첫 번째 인자로 cls 를 받도록 정의합니다. 이 때, 자동으로 클래스 객체가 cls 가 됩니다.**
- 인스턴스 입장에서도 접근이 가능하다. 이 때, **인스턴스 입장에서도 함수를 호출한 것은 클래스 인자이다.**



### 인스턴스 메서드

- **정의 위에 어떠한 데코레이터도 없으면, 자동으로 인스턴스 메서드가 됩니다.**

- **첫 번째 인자로 self 를 받도록 정의합니다. 이 때, 자동으로 인스턴스 객체가 self 가 됩니다.**



### 스태틱(정적) 메서드

- **정의 위에 @staticmethod 데코레이터를 사용합니다.**
- **인자 정의는 자유롭게 합니다. 어떠한 인자도 자동으로 넘어가지 않습니다.**
- 데이터에 접근하지 않는 메소드(주로 연산)를 쓸 때 사용

```python
class MyClass:
    
    def instance_method(self):
        return '저는 인스턴스 메서드입니다.'
    
    @classmethod
    def class_method(cls):
        return f'저는 클래스 메서드입니다. 저를 호출한 사람은 {cls}입니다.'
    
    @staticmethod
    def static_method():
        return '저는 스태틱 메서드입니다.'
    
mc = MyClass()
mc.instance_method()	# '저는 인스턴스 메서드입니다.'

MyClass.class_method()  # '저는 클래스 메서드입니다.'저를 호출한 사람은 <class '__main__.MyClass'>입니다."
mc.class_method()		# '저는 클래스 메서드입니다.'저를 호출한 사람은 <class '__main__.MyClass'>입니다."

MyClass.static_method()	# 저는 스태틱 메서드입니다.
mc.static_method()		# 저는 스태틱 메서드입니다.
```

#### 정리
- 인스턴스는, 3가지 메서드 모두에 접근할 수 있습니다.
- 하지만 인스턴스에서 클래스메서드와 스태틱메서드는 호출하지 않아야 합니다. (가능하다 != 사용한다) 
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계합니다.



- 클래스는, 3가지 메서드 모두에 접근할 수 있습니다.
- 하지만 클래스에서 인스턴스메서드는 호출하지 않습니다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계합니다.
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 클래스메서드로 정의합니다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면 스태틱메서드로 정의합니다

### 

### 오버로딩

- 객체 간의 대소관계, 연산관계를 정의할 수 있다.

```
+  __add__   
-  __sub__
*  __mul__
<  __lt__
<= __le__
== __eq__
!= __ne__
>= __ge__
>  __gt__
```

- `__gt__`를 정의할 경우, `__lt__`는 새로 정의해 줄 필요 없다. `__eq__`과 `__ne__`도 마찬가지 관계.



### 상속

Person class로부터 상속받은 Student class를 만들어보자.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'{self.name} 입니다. 반갑습니다!')
```

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id
        
    def study(self):
        print('공부중')
        
    def greeting(self):
        print(f"안녕하세요, {self.student_id}학번 {self.name}입니다.")
```

#### super()

- 자식 클래스에 메서드를 추가 구현할 수 있습니다.
- 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있습니다.

#### 상속관계에서의 이름공간

- 기존에 인스턴스 -> 클래스순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됩니다.
- instance => class => global
- **인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역**


























# SSAFY python basic (190723)

## OOP(1)

이전의 프로그래밍(절차지향)이 순서도에 가까웠다면, 이를 주어+동사 형태의 직관적인(상식적인) 형태로 발전시킨 것이 객체지향 프로그래밍이다.

- 클래스: 동일한 종류, 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것
- 인스턴스: 클래스에 속하는 예시. Object와 동의어로 사용
- 속성: 클래스/인스턴스가 가지고 있는 속성
- 메서드: 클래스/인스턴스가 할 수 있는 행위



- class 내에서 함수 선언시, 혹은 변수 사용시 `self` 를 사용해야 함에 유의해야 한다.
- `self`: 인스턴스 객체 자기자신. 메서드는 인스턴스 객체가 함수의 첫번째 인자로 전달되도록 되어있다. **반드시 self를 쓰지 않아도 되며, 다른 이름으로 써도 가능하다.**



- `__str__` 를 override할 경우, 아래와 같이 사용할 수 있다. (`__repr__`도 유사한 기능)

```python
class Phone
	model = 'galaxy'

	def __str__(self):
		return self.model
    
myphone = Phone()
print(myphone)	# 'galaxy'
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



객체가 가지는 변수의 이름공간을 분리하기 위해, 생성자를 사용해야 한다.

```python
class Person:
	def __init__(self, name):
		self.name = name
```














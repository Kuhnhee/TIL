# Python

**파이썬에서 추상 클래스 어떻게 구현하지?**

`abc` (abstract base class)를 사용한다... ([링크](https://wayhome25.github.io/cs/2017/04/10/cs-11/))

```python
# character.py
from abc import * # Abstract Base Class

class Character(metaclass = ABCMeta):
  def __init__(self):
    self.hp = 100
    self.attack_power = 20

  def attack(self, other, attack_kind):
    other.get_damage(self.attack_power, attack_kind)

  @abstractmethod # Character 클래스를 상속받는 모든 클래스는 하기 함수를 오버라이딩으로 구현해야 인스턴스 생성이 가능하다.  
  def get_damage(self, attack_power, attack_kind):
    pass

# 테스트코드    
if __name__ == '__main__':
    ch1 = Character()  # TypeError 발생 (Can't instantiate abstract class Character with abstract methods get_damage)
```

**파이썬 List가 내부적으로 어떻게 구현되어 있는지 알아요?**

Linked-List로 구현되어 있대요~



## GIL

참고자료: [링크1](https://wangin9.tistory.com/entry/pythonthreadGIL) [링크2](https://brownbears.tistory.com/215) 

파이썬에서는 GIL에 의해 멀티 스레딩을 할 경우 오히려 속도가 느려지는 현상이 발생한다. GIL에 의해 자원에 접근할 수 있는 스레드가 한 개로 제한되기 때문이다. (어느 시점이든 하나의 Bytecode만이 실행되도록 강제한다. 각 스레드는다른 스레드에 의해 GIL이 해제되길 기다린 후에야 실행될 수 있다. 즉, 멀티 스레드로 만들었어도 본질적으로 싱글 스레드로 동작한다.)

압축, 정렬, 인코딩 등 수행시간에 CPU 영향이 큰 작업(CPU bound)으 멀티 스레드로 수행하도록 한 경우 성능 문제가 대두된다. 이 경우 GIL로 인해 멀티 스레드로 작업을 수행해도 싱글 스레드일 때와 별반 차이가 나지 않는다. 따라서 **멀티 스레드는 파일, 네트워크 I/O같은 I/O bound 프로그램에 사용**하고, 이외에는 멀티 프로세스를 활용해야한다.

![gil1](./img/gil1.png)

![gil2](./img/gil2.jpg)

**그렇다면, GIL을 왜 쓰는거지?**

- GIL을 도입하면 인터프리터의 구현이 쉬워지고, Garbage Collector을 만들기 좋아며, C/C++ 확장 개발에 용이하다. 또한 프로그램이 I/O를 많이 쓸 경우 대부분 I/O bound 이기 때문에 파이썬의 스레드를 사용하는 것이 좋은 경우도 있다.
- GIL을 활용한 멀티 스레드가 그렇지 않은 멀티 스레드보다 구현이 쉬우며, 레퍼런스 카운팅을 사용하는 메모리 관리 방식에서 GIL 덕분에 오버헤드가 적어 싱글 스레드일 떄 **fine grained lock** 방식보다 성능이 우수하다. 
- C extension을 활용할 때 GIL은 해제되므로 C library를 사용하는 CPU bound 프로그램을 멀티 스레드로 실행하는 경우 성능향상을 기대할 수 있다.

**파이썬에서 병렬작업은 못하는 건가?**

- 쓰레드 대신 프로세스를 만들어주는 라이브러리 `multiprocessing` 모듈을 사용하면 된다. (쓰레드 대신 프로세스를 띄워준다.) 즉, 하나의 인터프리터를 쓰는게 아니라 여럿의 프로세스를 구동시키는 것이다. 이 경우 **프로세스의 관리는 OS에서 하기 때문에, OS에서 적절하게 프로세스를 코어별로 할당을 하게 해서, 전체적으로 성능을 향상시키게 된다.** 
- `multiprocessing` 모듈은 `fork()`를 통해 동시에 여러 프로세스에 원하는 작업을 실행할 수 있도록 도와주는 모듈이다. 파이썬에서는 OS 모듈에 속한 `fork()`함수를 사용해 여러 프로세스를 생성할 수 있다. `fork()`를 통해 생성된 프로세스의 복사본은 모든 데이터와 코드를 부모 프로세스로부터 가져오며, 운영 체제에서 자체 PID를 얻는 완전히 독립적인 프로세스로 수행된다. **IPC(프로세스 간 통신)**에서 손해가 발생하지만, 이를 지원하는 각종 메커니즘이 존재하며 쓰레드와 똑같이 사용할 수 있다.

![multiprocessing1](./img/multiprocessing1.jpg)

- `multiprocessing` 패키지에는 `threading` 모듈에 없는 API가 포함되어 있다. 예를 들어, 여러 입력에서 함수 실행을 병렬화하는 데 사용할 수 있는 깔끔한 `Pool` 클래스가 있다. [참고자료](https://hamait.tistory.com/755) 
- `threading` 모듈을 사용한 멀티쓰레드 구현 또한 가능하다. (But, 여전히 GIL의 영향을 받음에는 변함이 없다.)

**그렇다면, 파이썬은 멀티스레딩이 좋을까, 멀티프로세싱이 좋을까?**

- 쓰레드는 가볍지만 GIL로 인해 계산 처리를 하는 작업은 한 번에 하나의 쓰레드에서만 작동하여 **CPU 작업이 적고 I/O 작업이 많은** 병렬 처리 프로그램에서 효율적이다. (파일 읽기/쓰기, 네트워크와의 상호작용, 디스플레이같은 장치와의 통신 동 **Blocking I/O**작업을 할 경우, 스레드는 운영체제가 이런 요청에 응답하는데 드는 시간을 프로그램과 분리하므로 유용하다.)

  또, 멀티스레드를 사용할 경우 프로그램이 동시에 여러 작업을 하는 것처럼 보이게 만들기 용이하다. 함수를 마치 병렬로 실행하는 것처럼 애주는 일을 파이썬에게 맡길 수 있다. (비록 GIL 때문에 한 번에 한 쓰레드만 진행하지만, CPython은 파이썬 스레드가 어느정도 공평하게 실행됨을 보장한다.)

- 프로세스는 각자가 **고유한 메모리 영역을 가지기 때문에 더 많은 메모리**를 필요로 하지만, 각각 프로세스에서 병렬로 CPU 작업을 할 수 있고 이를 이용해 여러 머신에서 동작하는 **분산 처리** 프로그래밍도 구현할 수 있다. 

**추가**

- Blocking I/O를 처리하는데 스레드 대신 내장모듈 `asyncio`를 사용할 수 도 있다. (멀티 스레드와 비동기 처리는 다르다.)



## Garbage Collector

파이썬에서는 기본적으로 **garbage collection**과 **reference counting**을 통해 할당 된 메모리를 관리한다. 기본적으로 참조 횟수가 0이 된 객체를 메모리에서 해제하는 레퍼렁스 카운팅 방식을 사용하지만, 참조 횟수가 0이 아님에도 도달할 수 없는 상태인 **reference cycle(순환 참조)**가 발생했을 때는 garbage collection으로 그 상황을 해결한다. (엄밀히는 레퍼런스 카운팅 방식이 가비지 컬렉션의 한 형태.)

어떤 객체의 레퍼런스 카운트를 보고 싶다면 `sys.getrefcount()`로 확인할 수 있다.

가비지 컬렉터의 경우 파이썬의 `gc` 모듈을 통해 직접 제어할 수 있다. 이 모듈은 cyclic garbage collection을 지원하여 순환 참조를 해결할 수 있다. **`gc` 모듈은 오로지 순환 참조를 탐지하고 해결하기 위해 존재한다.** 

### 가비지 컬렉션의 작동 방식

**가비지 컬렉션이 발생하는 기준**

- GC는 내부적으로 generation(세대)과 threshold(임계값)로 가비지 컬렉션 주기와 객체를 관리한다. 세대는 0, 1, 2세대로 구분되며, 최근에 생성된 객체는 0세대(young)에 들어가고 오래된 객체일수록 2세대(old)에 존재한다. **더불어 한 객체는 단 하나의 세대에만 속한다. 가비지 컬렉터는 0세대일수록 더 자주 가비지 컬렉션을 하도록 설계되어 있다.** 이는 *generational hypothesis*에 근거한다. ([링크](https://www.memorymanagement.org/glossary/g.html#term-generational-hypothesis)) 
  - *generation hypothesis*의 두 가지 가설
    1. 대부분의 객체는 금방 도달할 수 없는 상태(unreachable)가 된다.
    2. 오래된 객체(old)에서 젊은 객체(young)로의 참조는 아주 적게 존재한다.

- 주기는 threshold와 관련되며, `gc.get_threshold()`로 확인해 볼 수 있다.

  ```python
  >>> gc.get_threshold()
  (700, 10, 10)
  ```

  각각 `threshold 0`, `threshold 1`, `threshold 2`를 의미한다. `n`세대에 객체를 할당한 횟수가 `threshold n`을 초과하면 가비지 컬렉션이 수행되며 이 값은 변경될 수 있다.

  0세대의 경우 메모리에 객체가 할당된 횟수에서 해제된 횟수를 뺀 값, 즉 객체 수가 `threshold 0`을 초과하면 가비지 컬렉션이 실행된다. 

  0세대 가비지 컬렉션이 일어난 후 0세대 객체를 1세대로 이동시킨 후 *카운터*를 1 증가시킨다. 이 1세대 카운터가 `threshold 1`을 초과한다면 그 때 1세대 가비지 컬렉션이 일어난다. (위의 threshold 값들을 기준으로, 0세대 가비지 컬렉션이 객체 생성 700번 만에 일어난다면 1세대는 7000번 만에, 2세대는 70000번 만에 일어난다는 뜻이다.)

### 라이프 사이클

1. 새로운 객체가 만들어질 때 파이썬은 객체를 메모리와 0세대에 할당한다. 만약 0세대의 객체 수가 `threshold 0`보다 크면 `collect_generations()`를 실행한다. 

   `collect_generations()`가 호출되면 모든 세대(기본적으로 3개의 세대)를 검사하는데 가장 오래된 세대(2세대)부터 역으로 확인한다. 해당 세대에 객체가 할당된 횟수가 각 세대에 대응되는 `threshold n`보다 크면 `collect()`를 호출해 가비지 컬렉션을 수행한다.

2. `collect()` 메소드는 **순환 참조 탐지 알고리즘**을 수행하고 특정 세대에서 도달할 수 있는 객체(reachable)과 돋라할 수 없는 객체(unreachable)를 구분하고 도달할 수 없는 객체 집합을 찾는다. 도달할 수 있는 객체 집합은 다음 상위 세대로 합쳐지고 (0세대에서 수행되었으면 1세대로 이동), 도달할 수 없는 객체 집합은 콜백을 수행한 후 메모리에서 해제된다.

**가비지 컬렉터가 어떻게 순환 참조를 발견하는가?**

- 먼저 순환 참조는 컨테이너 객체(`tuple`, `list`, `set`, `dict`, `class`)에 의해서만 발생할 수 있음을 알아야 한다. 컨테이너 객체는 다른 객체에 대한 참조를 보유할 수 있다. 그러므로 `정수`, `문자열`은 무시한 채 컨테이너 객체에만 관심을 집중한다.
- 모든 컨테이너 객체를 추적하는 게 아이디어다. 객체 내부의 링크 필드에 더블 링크드 리스트를 사용하는 방법이 가장 좋다. 이렇게 하면 추가적인 메모리 할당 없이도 **컨테이너 객체 집합**에서 객체를 빠르게 추가하고 제거할 수 있다. 컨테이너 객체가 생성될 때 이 집합에 추가되고 제거될 때 집합에서 삭제된다.
- 모든 컨테이너 객체에 접근할 수 있게 되었으니 아래와 같은 방법으로 순환 참조를 찾을 수 있어야 한다.
  1. 객체에 `gc_refs` 필드를 레퍼런스 카운트와 같게 설정한다.
  2. 가 객체에서 참조하고 있는 다른 컨테이너 객체를 찾고, 참조되는 컨테이너의 `gc_refs`를 감소시킨다. 
  3. `gc_refs`가 0이면 그 객체는 컨테이너 집합 내부에서 자기들끼리 참조하고 있다는 뜻이다.
  4. 그 객체를 unreachable하다고 표시한 뒤 메모리에서 해제한다.



## Generator

**제너레이터와 이터레이터의 관계**

![generator](./img/generator.png)

Generator는 제너레이터 함수가 호출될 때 반환되는 iterator의 일종이다. `yield`구문을 사용해 데이터를 원하는 시점에 반환하고 처리를 진행할 수 있다. 진입점이 여러개인 함수라고 생각해도 되며, 이러한 특성으로 인해 원하는 시점에 원하는 데이터를 받을 수 있게 된다.

**동작과정**

1. `yield`문이 포함된 제너레이터 함수가 실행되면 **제너레이터 객체**가 반환. 아직 함수의 내용이 실행되지는 않는다.

2. 빌트인 메소드인 `next()`를 통해 **제너레이터 객체**를 실행시킬 수 있다. 메소드 내부적으로 이터레이터를 인자로 받아 이터레이터에 정의되어 있는 `__next__()`메서드를 실행시킨다.

   ```python
   def generator():
       yield 1
   >>> gen = generator()
   >>> next(gen)
   ```

3. 처음 `__next__()` 메소드가 실행되면 제너레이터의 함수 내용을 실행하다가 `yield`문을 만났을 때 처리를 중단한다.

4. 이 때 모든 local state는 중단되는데, 변수의 상태, 명령어 포인터, 내부 스택, 예외 처리 상태를 포함한다.

5. 이후 제어권을 상위 컨텍스트로 양보(yield)하고, 또 `__next__()`가 호출되면 중단되었던 시점부터 다시 시작한다.

**왜 제너레이터를 쓰는걸까?**

`List`, `Set`, `Dict`과 같은 컨테이너들은 이터러블하기에 유용하지만, 담고 있는 모든 값을 메모리에 저장하고 있어야 하기에 큰 값을 다룰 때에는 효율적이지 못하다. 이 때 제너레이터를 사용하면 `yield`를 통해 그때그때 필요한 값만을 받아 쓰기때문에 모든 값을 메모리에 저장해둘 필요가 없게 된다.

혹은 지속적으로(무한히) 제공받아야 할 데이터가 있거나, 모든 값을 한 번에 계산하기에는 소모값(시간, 자원)이 커 그때그때 필요한 만큼만 계산하고 싶을 때 유용하다.

**제너레이터는 단점이 없을까?**

그때그때 필요한 값을 던져줄 뿐 기억해두지는 않기 때문에, 여러 번 반복적으로 사용되어야 하는 자료의 경우 사용하기 어렵다.

*추가: `range()`는 이터레이터, 혹은 제너레이터인가?*

- *`range()` 함수는 제어레이터, 이터레이터 모두 아니다. range 객체를 반환하는 함수이며, 다만 내부 구현상 제너레이터를 사용한 것 처럼 **메모리 사용에 있어 이점이 있다.*** 



## 파이썬에서 비동기 프로그래밍의 이해

참고자료: [링크1](https://blog.humminglab.io/python-coroutine-programming-1/) [링크2](https://blog.humminglab.io/python-coroutine-programming-2/) [링크3](https://sjquant.tistory.com/13?category=797018)(이 시리즈를 강력하게 추천)  

언제 비동기 프로그래밍을 하는게 좋을까?

- 여러 사이트들에 request를 보낼 때, 동기적으로 프로그래밍 할 경우 매번 response를 기다린 다음 이어지는 request를 전송한다. 하지만 비동기적으로 프로그래밍할 경우 response를 기다릴 필요 없이 다음 request를 전송할 수 있다. ([링크](https://sjquant.tistory.com/15?category=797018)) 

`asyncio`를 이해하기 위해서는 `coroutine`에 대한 이해가 필요하고, 이를 이해하기 위해서는 `generator`에 대한 이해가 필요하다.

python의 coroutine은 itertator부터 시작하여 generator를 확장한 것.

### Iterator

- python의 `for` 루프는 객체에 `__iter__()` 메소드가 있으면 이를 이용해 iterator를 얻는다.
- Iterator의 `__next__()`로 StopIteration exception이 발생할 때 까지 반복하여 값을 얻어 loop를 반복 수행
- 동일한 동작은 built-in 함수인 `next()`를 이용하여 사용 가능

### Generator(yield 키워드가 있는 함수)

- Iterator를 좀 더 편하게 이용하기 위해, 다른 언어처럼 `yield`를 이용하여 `coroutine`을 지원한 것이 `generator`이다.

- 호출 시 Generator가 실행되는 것이 아니라 함수를 감싸는 `generator` 객체가 리턴된다. 이 객체는 iterator와 동일하게 `__next__()`를 가진 객체이다.
- `yield` 키워드를 사용하여 중간에 멈추가 결과를 받는 용도로, iterator를 쉽게 만드는 데에 사용된다.

### Yield 기반의 coroutine(updated generator)

- `send()` 함수를 사용해 generator에서 `caller`와 `calle`간에 데이터를 양방향으로 전달할 수 있게 되었다. (`send(None)`은 `next()`와 동일.)

  ```python
  def coroutine1():
      print('callee 1')
      x = yield 1
      print('callee 2: %d' % x)
      x = yield 2
      print('callee 3: %d' % x)
      
  task = coroutine1()
  i = next(task)		# callee 1 출력, i는 1이 됨
  i = task.send(10)	# callee 2: 10 출력, i는 2가 됨
  task.send(20)		# callee 3: 20 출력 후 StopIteration exception 발생
  ```

  ![coroutine1](./img/coroutine1.JPG)

- Coroutine은 yield에서 값을 받을 수 있다는 것을 제외하고 generator와 동일하다.
- generator에서 yield문은 try-finally로 감쌀 수 없었으나, python 2.5부터는 이를 지원한다. 따라서 coroutine -> caller로의 예외 전달이 가능해졌다.
- Caller에서 `throw(type, value, traceback)`을 사용해 yield로 멈춰있는(또는 생성 직후) coroutine에 exception을 전달할 수 있다.
- Caller에서 coroutine을 종료 시킬 수 있는 `close()`도 추가되었다. 이는 내부적으로 `throw()`를 이용하여 `GeneratorExit` exception을 coroutine에게 전달하는 방식으로 구현되어 있다.

위와 같이 exception과 종료 기능이 추가되면서, 비동기 프로그래밍을 위한 준비가 완료되었다.

### yield from

다음과 같이 coroutine이 sub-coroutine을 호출하는 구조를 상상해보자.

```python
def subcoroutine():
    yield 1
    yield 2
   
def coroutine():
    for v in subcoroutine():
        yield v
       
x = coroutine()
print(next(x))	# 1 출력
print(next(x))	# 2 출력
next(x)			# StopIteration
```

위 코드에서 `send()`, `throw()`, `close()`를 지원하기 위해서는 아래와 같이 `coroutine()`을 수정해야 한다.

```python
def subcoroutine():
    print("Subcoroutine")
    x = yield 1
    print("Recv:" + str(x))
   	x = yield 2
    print("Recv:" + str(x))
    
def coroutine():
    _i = subcoroutine()
    _x = next(_i)
    while True:
        _s = yield _x
        
        if _s is None:
            _x = next(_i)
        else:
            _x = _i.send(_s)
            
>>> x = coroutine()
>>> next(x)
Subcoroutine
1

>>> x.send(10)
Recv: 10
2

>>> x.send(20)
Recv: 20
StopIteration
```

위의 복잡한 코드를 한 줄로 바꿔주는 역할을 하는게 `yield from`이다. caller <-> sub-coroutine이 데이터를 주고 받게 하려면 아래와 같이 간단하게 작성할 수 있다.

```python
def subcoroutine():
    print("Subcoroutine")
    x = yield 1
    print("Recv: " + str(x))
    x = yield 2
    pprint("Recv: " + str(x))
    
def coroutine():
    yield from subcoroutine()
```

`yield from`의 오른쪽에 들어갈 수 있는 것은 iterable과 generator이다.

generator에서 return이 지원됨에 따라, 아래와 같이 `yield from`에서 직접 값을 받는 것이 가능해졌다.

```python
def sum(max):
    tot = 0
    for i in range(max):
        tot += i
        yield tot
    return tot

def coroutine():
    x = yield from sum(10)
    print('Total: {}'.format(x))
```

### Asyncio

Python 3.4에서 추가된 event loop 방식의 비동기 프로그래밍 표준 라이브러리.

Coroutine과 같이 사용한다면 단일 thread에서 마치 multi-tasking을 하는 것과 유사한 기능을 수행할 수 있게 된다. 이를 이해하기 위해서는 python 3.2에서 추가된 future를 이해할 필요가 있다.

*future?*

- *work thread(process)의 핸들이라고 볼 수 있다. `future.result()`와 같이 종료가 끝날 때까지 기다리게 되면, 해당 work function에서 결과를 완료하거나, exception이 발생한 경우 이를 받을 수 있다.*

- *예제 코드*

  ```python
  from concurrent import futures
  import urllib.request
  
  URLS = ['http://www.foxnews.com/',
         'http://www.cnn.com/',
         'http://some-made-up-domain.com/']
  
  def load_url(url, timeout):
      return urllib.request.urlopen(url, timeout=timeout).read()
  
  def main():
      with futures.ThreadPoolExecutor(max_workers=5) as executor:
          future_to_url = dict(
          	(executor.submit(load_url, url, 60), url)
          	for url in URLS)
          
          for future in futures.as_completed(future_to_url):
              url = future_to_url[future]
              try:
                  print('%r page is %d bytes' % (
                  	url, len(futures.result())))
              except Exception as e:
                 	print('%r generated an exception: %s' % (
                  	url, e))
  ```

- *`executor.submit()`으로 thread pool에서 돌릴 함수를 등록하면 future를 리턴한다. 등록된 함수는 trhead pool에서 비동기로 실행된다.*

- *`futures.as_completed()`처럼 결과가 완료된 순서대로 리턴되는 generator를 리턴 받을 수 있다. 위와 같이 `for`문에 넣어 loop를 돌릴 수 있다. 완료되거나 비정상 종료된 future가 차레대로 나오게 된다.*

- *`future.result()`로 결과를 받을 수 있다. 만일 future 내의 함수(`load_url()`) 에서 exception이 발생한 것도 future를 통하여 호출한 thread에서 받을 수 있게 된다. 위의 예제와 같이 `future.result()`가 `try-except`문으로 감싸서 해당 작업에서 발생한 예외도 받을 수 있다.*

- *결과적으로 future를 사용해 childe thread에서 발생한 exception도 쉽게 처리가 가능해진다.*

`send()`를 반복적으로 호출하는 것을 `asyncio`의 `event loop`에서 한다고 보면 된다. 이렇게 되면 coroutine도 event loop에서 마치 별도의 thread에서 도는 것과 같이 실행되는 셈이다. 이들 coroutine을 event loop에서 관리 하기 위해 future에서 상속받은 task를 사용한다. 일반 콜백 함수는 `call_later()`를 이용하여 event loop에 등록하고, coroutine은 `ensure_future()`나 `loop.create_task()`를 사용하여 등록한다.

여기에 추가적으로, `yield from`에 iterator, generator와 더불어서 future 또한 사용 가능해졌다. 다음은 async/await을 사용하지 않고 callback/coroutine을 혼용하여 사용한 예다.

```python
import asyncio

@asyncio.coroutine #documentation이 목적인 데코레이터
def print_every_second_coroutine(type):
    "Print seconds"
    while True:
        for i in range(10):
            print(i, 's (coroutine {})'.format(type))
            yield from asyncio.sleep(1)
        loop = asyncio.get_event_loop()
        loop.stop()

def print_every_seconds_callback(i):
    print(i, 's (callback)')
    loop = asyncio.get_event_loop()
    loop.call_later(1.0, print_every_seconds_callback, i+1)
    
def print_every_seconds_callback_to_coroutine():
    asyncio.ensure_future(print_every_second_coroutine('B'))
    
loop = asyncio.get_event_loop()
loop.call_soon(print_every_seconds_callback, 0)
loop.call_soon(print_every_seconds_callback_to_coroutine)
asyncio.ensure_future(print_every_second_coroutine('A'))

loop.run_forever()
loop.close()
'''
0 s (callback)
0 s (coroutine A)
0 s (coroutine B)
1 s (callback)
1 s (coroutine A)
1 s (coroutine B)
...
'''
```

- `asyncio.ensure_future()`를 통해 default event handler에 coroutine 등록(generator인 `print_every_second_coroutine('A')`를 등록)
- callback으로는 `print_every_seconds_callback`과 같이 함수의 이름을 전달. `call_later()`등의 메소드를 통해 반복해서 호출한다.
- `print_every_seconds_callback_to_coroutine()`과 같은 일반 callback 함수에서는 coroutine 직접 호출 불가. (직접 호출하려면 이 함수가 `next()`를 반복해서 호출하여야 하기 때문에 event loop가 blocking된다.) 대신, coroutine을 등록 하는 것과 동일하게 `asyncio.ensure_future()` (또는 `loop.create_task()`)를 사용한다.

### async, await

Python 3.5에서 coroutine을 명시적으로 지정하는 **async**와 yield를 대체하는 **await** 키워드가 추가.

기존의 `yield`를 사용하는 generator based coroutine과 비교하기 위해 **native coroutine**이라고 한다. native coroutine은 **함수 앞에 async def 키워드**를 붙여서 사용한다.

```python
async def read_data(db):
    pass
```

기존 문법인 `yield`, `yield from`을 사용할 수 없고, `await`를 사용한다. (`await`를 사용하지 않더라도, `async def`로 정의된 함수는 coroutine이 된다.) 최신 버전에서는 `yield`도 사용 가능한다.

`await`의 오른쪽에 올 수 있는 값들은 다음과 같다.

- native coroutine object
- generator based coroutine object
- `__await__` 메소드를 가진 object를 리턴하는 iterator
- CPython API를 위한 `tp_as_async.am_await`



## 클래스 상속시 메서드 실행 방식

상속시 메소드를 가져오는 순서는 `__mro__`를 따른다. MRO(Method Resolution Order)는 메소드를 확인하는 순서로 python 2.3 이후 C3 알고리즘이 도입되어 있다. 단일/다중 상속시 어떤 순서로 메소드에 접근할지는 해당 클래스의 `__mro__`에 저장되는데 왼쪽에 있을수록 우선순위가 높다. B, C를 다중상속받은 D 클래스가 있고, B와 C는 각각 A를 상속받았을 때, D의 mro를 조회하면 볼 수 있듯이 부모클래스는 반드시 자식클래스 이후에 위치해있다. 최상위 object 클래스까지 확인했는데도 적절한 메소드가 없으면 `AttributeError`를 발생시킨다.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

>>> D.__mro__
(__main__.D, __main__.B, __main__.C, __main__.A, object)
```



## PyPy / CPython 비교

CPython은 일반적인 인터프리터임에 반해,  PyPy는 **실행 추적 JIT 컴파일(Tracing Just-In-Time)**을 제공하는 인터프리터이므로 PyPy가 더 빠르다. (JIT: 한 줄 한 줄 읽다가, 적절한 시기에 전체를 컴파일.)

### PyPy

*파이썬으로 만들어진* 파이썬 인터프리터. 파이썬으로 구현되어 있음에도 CPython보다 빠르다.

- 엄밀히는, RPython 언어로 동적 언어의 인터프리터를 구현할 수 있게 해주는 프레임워크([링크](https://blog.hongminhee.org/2011/05/02/5124874464/))

### 실행 추적 JIT 컴파일

메소드 단위로 최적화 하는 전통적인 JIT와 다르게 런타임에서 *자주 실행되는 루프를 최적화*한다.

### RPython (Restricted Python)

동적 언어인 Python에서 표준 라이브러리와 문법에 제약을 가해 **변수의 정적 컴파일**이 가능하도록 만들어진 언어. *동적 언어 인터프리터를 구현하는데 사용된다.*

RPython으로 인터프리터를 작성하고 툴체인으로 힌트를 추가하면 인터프리터에 실행추적 JIT 컴파일러를 빌드한다. 이렇게 언어 사양(파이썬 언어 규칙, BF 언어 규칙 등)과 구현(인터프리터 제작)을 분리함으로써 **어떤 동적 언어에 대해서라도 자동으로 JIT 컴파일러를 생성할 수 있게 되었다.**

*동적 언어(타입) / 정적 언어(타입)*

- *정적 타입: 컴파일 시에 타입에 대한 정보를 결정하기 때문에 속도 상승. 타입 엘로 인한 문제점을 초기에 발견할 수 있어 타입의 안정성 상승.*
- *동적 타입: Run time까지 타입에 대한 결정을 끌고 갈 수 있기 때문에 많은 선택의 여지가 있다. But, 예상치 못한 Type Error 가능성 존재.*

- *정적 타입 언어가 **항상** 더 빠를것이라 말할 수 있을까?*
  - *GC와 같은 다른 요소들에 대한 고려도 필요할 것 같아.*



## Duck Typing

동적 타입을 가지는 프로그래밍 언어에서 많이 사용되는 개념으로, 객체의 실제 타입보다는 객체의 변수와 메소드가 그 객체의 적합성을 결정하는 것을 의미한다. 

동적 타입 언어인 파이썬은 메소드 호출이나 변수 접근시 타입 검사를 하지 않으므로 duck typing을 넓은 범위에서 활용할 수 있다. 다음은 간단한 duck typing 예시다.

```python
class Duck:
    def walk(self):
        print('뒤둥뒤뚱')

    def quack(self):
        print('Quack!')

class Mallard: #청둥오리
    def walk(self):
        print('뒤뚱뒤뚱뒤뚱')

    def quack(self):
        print('Quaaack!')

class Dog:
    def run(self):
        print('타다다다')
    
    def bark(self):
        print('왈왈')

def walk_and_quack(animal):
    animal.walk()
    animal.quack()

walk_and_quack(Duck())
walk_and_quack(Mallard())
walk_and_quack(Dog())
```

`Duck`와 `Mallard`는 `walk()`와 `quack()`을 구현하고 있기 때문에 `walk_and_quack()`이라는 함수의 인자로 **적합하다.** 그러나 `Dog`는 두 메소드가 구현되어 있지 않으므로 해당 함수의 인자로서 **부적합하다**. 즉, `Dog`는 적절한 **duck typing에 실패**한 것이다.

Python에서 duck typing이 활용되는 예시

1. `__len__()` 을 구현하여 *길이가 있는 무언가*를 표현
2. `__iter__()` 와 `__getitem__()`을 구현하여 iterable을 duck-typing할 수 있다. 굳이 `Iterable` 인터페이스를 상속받지 않고도 `__iter__()`와 `__getitem__()`을 구현하기만 하면 `for ~ in ~` 문법에서 바로 활용할 수 있게 된다.

이러한 방식은 인터페이스를 구현하거나 클래스를 상속하는 방식으로 인자나 변수의 적합성을 **Run time 이전**에 판단하는 정적 타입 언어들과 비교된다. 





## 메모리 누수

참고자료: [링크](https://soooprmx.com/archives/5074) 

Reference counting에 의해, 참조 회수가 0이 될 경우 해당 객체의 `__del__()` 메소드가 호출된다. 어떤 경우, 개발자가 이 `__del__()`메소드를 변경해서 객체가 제거되는 시점에 필요한 리소스 정리를 할 수 있다.(기본적으로는 파이썬에서 자동적으로 지원해 주므로 할 필요 없다.)

아래 코드는 Foo() 함수의 인스턴스가 참조회수가 0이 되자 자신의 `__del__()` 함수를 호출하는 모습이다.

```python
class Foo:
  def __init__(self):
    self.value = 1
    self.friend = None
  def __del__(self):
    print(f'Object({id(self)}:{self.__class__}) is being destroyed.')
    
>> a = Foo()
>> a = 1  ## 1)
Object(1087b819c18:<class '__main__.Foo'>) is being destroyed.
```

한 단계 나아가, 아래와 같이 `a`, `b` 두 개의 Foo() 함수 인스턴스를 선언한 뒤 `a`의 속성값이 `b` 객체를 참조하도록 해보자. 이후 `b` 변수에 다른 객체를 바인딩할 경우 여전히 `a` 객체에 의해 참조되고 있으므로 삭제되지 않음을 확인할 수 있다. 하지만 `a` 변수의 바인딩을 바꿀 경우, 최초에 만들었던 두 개의 Foo()함수 인스턴스가 모두 참조를 잃었음에도 불구하고 `a`에 바인딩 되어있던 인스턴스만 삭제됨을 확인할 수 있다.

```python
>> a, b = Foo(), Foo()
>> a
<__main__.Foo object at 0x000001D953A38BE0>
>> b
<__main__.Foo object at 0x000001D953A38BA8>
>> a.friend = b  ## 1
>> b = None      ## 2
>> a = None      ## 3
Object(at 1d953a38be0, <class '__main__.Foo'>) is being destroyed. 
```

이는 `a`에 바인딩 되어있던 객체를 제거하는 과정에서 `a.friend`에 대한 참조를 제거하는 작업이 이뤄지지 않았기 때문이다.

클래스 인스턴스의 속성이 만약 다른 클래스의 인스턴스를 참조하거나, 동일 클래스의 다른 인스턴스를 참조할 가능성이 높다면 이는 메모리 누수가 발생할 가능성이 매우 높은 지점이 된다. 기본적으로 파이썬 프로그램의 생애주기는 짧기 때문에 문제가 되지 않을 수 있지만, **서버**와 같이 생애 주기가 길거나, 많은 인스턴스를 생성하고 연결하는 동작을 하는 경우에 메모리 누수는 큰 문제가 될 수 있다.

파이썬에서는 이러한 문제를 처리하기 위해 **약한 참조**를 제공한다. 대상 객체를 참조하기는 하지만, 대상 객체에 대한 소유권을 주장하지는 않는, 즉 **reference count를 올리지 않는** 참조를 말한다.

약한 참조는 `weakref`모듈의 `ref` 클래스를 통해서 생성할 수 있다. 기본적인 사용법은 이렇다.

1. 특정 대상에 대해 약한 참조를 만들 떄는 `weakref.ref(target)`과 같이 `ref()` 함수에 인자를 넘겨 약한참조 객체를 생성한다.
2. 생성된 약한참조로부터 참조대상을 얻으려 할 때는 약한참조 객체를 호출한다.

만약 참조대상이 파괴되었다면 약한참조는 참조 대상에 대한 액세스를 요청받을 때 `None`을 리턴한다.

```python
class Foo:
  def __init__(self):
    self.value = 1
    self.friend = None
  def __del__(self):
    ## 여기서 딱히 friend 속성을 정리하지 않는다.
    print(f'Object({id(self):x}) is being destroyed.')

## 테스트
>> import weakref
>> a, b = Foo(), Foo()
## 각각의 객체를 약한 참조를 이용해서 할당한다.
>> a.friend = weakref.ref(b)
>> b.friend = weakref.ref(a)
## 객체를 지워본다.
>> b = None
Object(2520efedc18) is being destroyed.
>> a.friend()    ## 제거된 대상을 액세스하려하면 None이 리턴된다.
>> a = None
Object(2520efc8ba8) is being destroyed.
## 자가 참조에 대해서도 테스트
>> c = Foo()
>> c.friend = weakref.ref(c)
>> c = None
Object(2520efed518) is being destroyed.
```

**그래서 약한 참조를 언제 쓴다고?**

- 한 개 이상의 객체가 참조 순환 고리를 만드는 경우에 메모리 누수를 방지하기 위해서 주로 사용한다.

- 캐싱에 사용하는 경우도 있다. 예를 들어 어떤 객체들이 비용이 많이 드는 연산을 통해서 생성된다고 생각해보자. 반복계산에 소요되는 비용을 줄이기 위해서 이들을 **사전**에 추가해서 캐싱할 수 있다.

  사전을 이용한 캐싱은 속도를 높이는데 좋지만, 만약 이 객체들이 메모리를 많이 사용하는 큰 덩치라면, 캐시를 위한 사전을 유지하는 것 자체가 큰 부담이 될 수 있다.

  따라서 '비교적 짧은 시간 내에 재사용되는 경우'에만 속도를 높이기 위해 사용할 수 있고, 캐시에 객체 그 자체를 저장하는 것이 아니라 객체에 대한 약한 참조만을 저장하여 캐싱이 메모리 관리를 방해하지 않도록 할 수 있다.

**조금 더 편리하게 쓸 수 없을까?**

매번 `weakref.ref(x)`를 쓰는 과정은 피곤하다. **객체 프로퍼티를 사용해 접근자를 호출**하는 식으로 우회하여 이 문제를 개선할 수 있다.

```python
import weakref

class ConvenientFoo:
  def __init__(self, value):
    self.value = value
    self._friend = None
  
  @property
  def friend(self):
    if self._friend is None:
      return None
    return self._friend()

  @friend.setter
  def friend(self, target):
    self._friend = weakref.ref(target)

  def __del__(self):
    print(f'{id(self):x} is being destroyed.')

## 테스트
>> a, b, c = [ConvenientFoo() for _ in range(3)]
>> a.friend = b
>> b.friend = a
>> c.friend = c
>> a = None
2520efc8ba8 is being destroyed.
>> b = None
2520efedc18 s being destroyed
>> c = None
2520efed518 is being destroyed
```

**가비지 콜렉터 Remind**

메모리 누수는 생성된 이후 참조가능한 위치를 모두 잃어버렸지만, 참조수를 유지하고 있는 객체들 때문에 발생한다. 상호간에 참조를 갖는 두 객체나 참조 사이클을 만드는 3개 이상의 객체, 혹은 자기 스스로를 참조하는 객체 등은 그 객체에 대한 이름을 잃게 되더라도 파괴되지 않고 그 메모리를 점유한다.

가비지 콜렉터는 이렇게 누수가 발생한 경우, **고립된 객체를 찾아서 제거하는 기능이다(Reference counting만으로 제거하지 못한 객체들)**. 따라서 프로세스가 사용하는 모든 힙 메모리 공간을 다 뒤져서 살아있는 객체를 찾은 다음, 이 객체를 외부에서 사용 가능한지를 검사한다. 만약 특정 객체 혹은 객체 그룹이 외부로 부터 고립되어 있는것을 발견하면 가비지 콜렉터는 해당 객체들을 제거하고, 메모리를 회수한다.

수많은 객체들을 전수조사해야하고, 그 객체에 대한 명시적이지 않은 모든 참조를 찾아야 하니, 엄청난 리소스를 소모해야 하는 작업이 된다. 일부 서비스에서는(*ex. 인스타그램 서버*) 가능한 명시적인 참조만을 사용하여 가비지 콜렉터의 도움 없이 서비스를 만들고, 아예 GC를 꺼놓기도 한다.




# Java



## JVM & garbage collector

참고자료: [링크1](https://asfirstalways.tistory.com/158) [링크2](https://asfirstalways.tistory.com/159)

### JVM에서 Thread의 의미?

**JVM은 하나의 프로세스로 실행된다.** 즉, 자바 어플리케이션이 기본적으로 하나의 메인 쓰레드를 가진다는 것이다. JAVA 프로그램을 실행시키기 위해 Main Thread는 main() 메소드를 실행한다. (`public static void main` 는 메인 쓰레드의 시작점을 선언하는 것.)

JAVA 어플리케이션을 더 빠르고 효율적으로 동작할 수 있도록 Multi-thread 프로그래밍을 지원한다.



### JVM이란?

*가상머신이란?: 프로그램을 실행시키는데 필요한 물리적 머신과 유사한 환경을 소프트웨어로 구현한 것*

1. JAVA 어플리케이션을 **클래스 로더**를 통해 읽어 들여 **Java API**와 함께 **실행**시키는 역할
2. JAVA와 OS 사이에서 **중개자** 역할. JAVA가 OS에 구애받지 않고 재사용을 가능하게 해준다.
3. **메모리 관리, Garbage collection**을 수행한다.
4. **스택** 기반의 가상머신. (ARM 아키텍쳐는 레지스터 기반) 



### 왜 JVM을 알아야 하는가?

1. 한정된 메모리를 효율적으로 사용하여 최고의 성능을 내기 위해, 그 메모리 구조를 파악해야 하기 때문.



### JAVA 프로그램의 실행과정

1. 프로그램이 실해되면 JVM은 OS로부터 해당 프로그램이 필요로 하는 **메모리를 할당**받는다. JVM은 이 메모리를 용도에 따라 여러 영역으로 나누어 관리한다.
2. 컴파일러(javac)가 소스코드(.java)를 읽어들여 **바이트코드(.class)로 변환**시킨다.
3. Class loader를 통해 **class 파일들을 JVM으로 로딩**한다.
4. 로딩된 class파일들은 Execution engine을 통해 해석된다.
5. 해석된 바이트코드는 Runtime Data Areas에 배치되어 실질적인 수행이 이루어지게 된다. 

위의 실행과정 속에서 JVM은 필요에 따라 *Thread Synchronization*, *GC*와 같은 관리작업을 병행한다.



### JVM 구성

**Class Loader(클래스 로더)**

- 클래스 파일을 JVM으로 로드하고, 링크를 통해 배치하는 작업을 수행하는 모듈. **Rutime**시에 동적으로 클래스를 로드한다. jar파일 내 저장된 클래스들을 JVM 위에 탑재하고 사용하지 않는 클래스들은 메모리에서 삭제한다. 자바는 동적 코드이므로 **컴파일 타임이 아니라 런타임에 참조한다.** 즉, 클래스를 처음 참조할 때 해당 클래스를 로드하고 링크한다. 그 역할을 클래스 로더가 수행한다.

**Execution Engine(실행 엔진)**

- 클래스를 실행시키는 역할. Class Loader가 JVM 내의 Runtime Data Area에 바이트 코드를 배치시키고, 이것은 Execution engine에 의해 실행된다. 이 과정에서 실행 엔진은 바이트코드를 JVM 내부에서 기계가 실행할 수 있는 형태로 변경한다. *(인터프리터, JIT 두 가지 방식이 존재한다.)*

**Interpreter(인터프리터)**

- (실행 엔진이) 자바 바이트 코드를 명령어 단위로 읽어서 실행한다.
- 인터프리터 언어의 단점을 그대로 갖게 된다. (한 줄씩 수행하기 때문에 느리다.)

**JIT(Just-In-Time)**

- 인터프리터 방식의 단점을 보완하기 위해 도입된 JIT 컴파일러
- 인터프리터 방식으로 실행하다가, 적절한 시점에서 바이트코드 전체를 컴파일하여 *네이티브 코드*로 변경하고,  더 이상 인터프리팅하지 않고 네이티브 코드로 직접 실행하는 방식.
- 네이티브 코드는 **캐시에 보관**하기 때문에 한 번 컴파일된 코드는 빠르게 수행하게 된다.
- JIT 컴파일러가 컴파일하는 과정은 인터프리팅보다 훨씬 오래걸리므로, **한 번만 실행되는 코드라면 인터프리팅이 유리하다.**
- 따라서 JIT 컴파일러를 사용하는 JVM들은 내부적으로 해당 메서드가 얼마나 자주 수행되는지 체크하고, 일정 정도를 넘을 때에만 컴파일을 수행한다. 

**Garbage Collector**

- GC를 수행하기 위한 모듈 (스레드)

**Runtime Data Area**

- 프로그램을 수행하기 위해 OS에서 할당받은 메모리 공간(실질적인 수행이 이루어지는 공간)

  1. PC Register

     *스레드가 시작될 때* 생성되며 생성될 때마다 생성되는 공간으로 스레드마다 하나씩 존재한다. 스레드가 **어떤 부분을 어떤 명령으로 실행해야할 지에 대한 기록**을 하는 부분으로 현재 수행 중인 JVM 명령의 주소를 갖는다.

  2. JVM Stack

     프로그램 실행과정에서 **임시로 할당**되었다가 메소드를 빠져나가면 소멸되는 특성의 데이터를 저장하기 위한 영역. 각종 형태의 **변수나 임시 데이터, 스레드나 메소드의 정보**(메소드 안에서 사용되는 매개변수, 지역변수, 리턴 값 등)를 저장한다.

     *메소드 호출 시* 각각의 스택 프레임(해당 메서드를 위한 공간)이 생성된다. 메소드 수행이 종료될 경우 스택 프레임 별로 삭제된다.

  3. Native method stack

     (바이트 코드가 아닌) 실제 실행할 수 있는 기계어로 작성된 **프로그램을 실행시키는 영역**. JAVA가 아닌 다른 언어로 작성된 코드를 위한 공간. JAVA Native Interface를 통해 바이트 코드로 전환하여 저장하게 된다. 일반 프로그램처럼 **커널이 스택을 잡아 독자적으로 프로그램을 실행시키는 영역**. 이 부분을 통해 C code를 실행시켜 kernel에 접근할 수 있다.

     (여기까지 각 thread 별로 생성되는 영역)

     ---

     (여기부터 thread간에 공유하는 영역)

  4. Method Area (= Class area = Static area)

     클래스 정보를 처음 메모리에 올릴 때 **초기화되는 대상을 저장하기 위한 메모리 공간**. 올라가게 되는 메소드의 바이트 코드는 프로그램의 흐름을 구성하는 바이트 코드이다. 자바 프로그램은 main 메소드의 호출에서부터 **계속된 메소드의 호출로 흐름을 이어가기 떄문**.

     **Runtime Constant Pool**이라는 별도의 관리 영역이 존재. 상수 자료형을 저장하여 참조하고 중복을 막는 역할을 수행한다.

     Method Area에 올라가는 정보의 종류는 다음과 같다.

     1. Field Information

        멤버변수의 이름, 데이터 타입, 접근 제어자에 대한 정보

     2. Method Information

        메소드의 이름, 리턴타입, 매개변수, 접근제어자에 대한 정보

     3. Type Information

        class인지 interface인지의 여부 저장. Type의 속성, 전체 이름, super class의 전체 이름(interface 이거나 object인 경우 제외)

     *Method Area는 클래스 데이터를 위한 공간, Heap 영역은 객체를 위한 공간. 두 공간 모두 GC의 관리 대상에 포함된다.*

  5. Heap

     **객체를 저장하는 가상 메모리 공간**. `new` 연산자로 생성된 객체와 배열을 저장한다. (이 때, Class area에 올라온 클래스들만 객체로 생성할 수 있다.) 'New/Young Generation', 'Tenured Generation', 'Permanent Generation'의 세 가지 영역으로 구성된다.

     1. Permanent Generation

        생성된 객체들의 정보의 주소값이 저장된 공간.

        Class Loader에 의해 로드되는 Class, Method 등에 대한 Meta 정보가 저장되는 영역이고 JVM에 의해 사용된다. Reflection을 사용하여 동적으로 클래스가 로딩되는 경우에 사용된다.

     2. New/Young 영역

        - Eden: 객체들이 최초로 생성된 공간
        - Survivor 0 / 1: Eden에서 참조되는 객체들이 저장되는 공간

     3. Old 영역(Tenured)

        New/Young 영역에서 일정 시간 참조되고 있는, **살아남은 객체들이 저장되는 공간**.

        Eden 영역에 객체가 가득차게 되면 첫 번째 GC(minor GC)가 발생하여 Eden 영역에 있는 값들을 Survivor 1 영역에 복사하고, 이 영역을 제외한 나머지 영역의 객체를 삭제한다.

     인스턴스는 소멸 방법과 시점이 지역 변수와는 다르기에 힙이라는 별도의 영역에 할당된다. JVM은 더이상 인스턴스의 존재 이유가 없을 때 소멸시킨다.



### GC (Naver D2 참고: [링크](https://d2.naver.com/helloworld/1329))

**Minor GC**

- 새로 생성된 객체들이 대부분 Eden 영역에 위치된 뒤, Eden 영역에서 GC가 한 번 발생한 후 살아남은 객체는 Survivor 영역 중 하나로 이동된다. 이 과정을 반복하다가 계속해서 살아남는 객체는 일정시간 참조되고 있었다는 뜻이므로 Old 영역으로 이동시킨다. 

**Major GC**

- Old 영역에 있는 객체들을 검사하여 참조되지 않은 객체들을 한꺼번에 삭제한다. **시간이 오래 걸리고, 실행 중 프로세스가 정지된다.** 이것을 **'stop-the-world'**라 하는데, Major GC가 발생하면 **GC를 실행하는 스레드를 제외한 나머지 스레드는 모두 작업을 멈춘다.** GC 작업을 완료한 이후에야 중단됐던 작업을 다시 시작한다.



***GC는 어떤 원리로 소멸시킬 대상을 선정하는가?***

- Heap 내의 객체 중에서 Garbage를 찾아내고, 찾아낸 가비지를 처리해서 힙의 메모리를 회수한다. 참조되고 있지 않은 객체를 가비지라고 하며, 객체가 가비지인지 아닌지 판단하기 위해서 **reachability**라는 개념을 사용한다. 힙 영역에 할당된 객체가 유효한 참조가 있다면 **reachability**, 없다면 **unreachability**로 판단한다. 

- 객체 간에는 참조 사슬이 형성될 수 있는데, 이 참조 사슬 중 최초에 참조한 것을 **Root Set**이라 칭한다. 힙 영역에 있는 객체들은 총 4가지 경우에 대한 참조를 하게 된다.

  1. 힙 내의 다른 객체에 의한 참조
  2. JAVA 스택, 즉 JAVA 메소드 실행 시에 사용하는 지역변수와 파라미터들에 의한 참조
  3. 네이티브 스택 (JNI, Java Native Interface)에 의해 생성된 객체에 대한 참조
  4. 메소드 영역의 정적 변수에 의한 참조

  이 중 2,3,4는 **Root Set**에 해당한다.

- 인스턴스가 GC의 대상이 되었다고 해서 바로 소멸이 되는 것은 아니다. 빈번한 GC의 실행은 시스템에 부담이 될 수 있기에 추가적인 알고리즘을 통해 GC의 실행 타이밍을 계산한다.



### 메모리 누수

메모리 누수(Memory Leak)는 프로그램이 필요하지 않은 메모리를 계속 점유하고 있는 현상이다.

기본적으로 JAVA는 가상머신이 메모리를 관리해주어(+GC) OS 레벨에서의 메모리 누수가 방지된다.

JAVA 프로그램 실행시 JVM 옵션을 주어서 OS에 요청한 사이즈 만큼의 메모리를 할당 받아서 실행하게된다. 할당받은 이상의 메모리를 사용하게 되면 에러가 나면서 자동으로 프로그램이 종료된다. 그러므로 현재 프로세스에서 메모리 누수가 발생하더라도 **실행중인 것만 죽고, 다른 것에는 영향을 주지 않는다.**

참고자료: ([링크](https://118k.tistory.com/608))

JAVA에서 메모리 누수는 더이상 사용하지 않는 객체가 GC에 의해 회수되지 않고 계속 누적되는 현상이다. Old 영역에 누적된 객체로 인해서 GC가 빈번하게 발생하게 되고, 프로그램의 응답속도가 늦어지다 결국 OOM(OutOfMemory) 오류로 프로그램이 종료된다.

주로 빈번한 전역변수의 선언이나, `list`, `hashmap`같은 콜렉션에 저장한 객체를 해제하지 않고 계속 유지하레 되면서 발생한다. 아래는 메모리 유수가 발생하는 대표적인 예시들이다. ([링크](https://dzone.com/articles/memory-leak-andjava-code))

1. `Integer`, `Long`같은 래퍼 클래스(Wrapper)를 이용하여, 무의미한 객체를 생성하는 경우
2. `map`에 캐쉬 데이터를 선언하고 해제하지 않는 경우
3. 스트림 객체를 사용하고 닫지 않는 경우
4. `map`의 키를 사용자 객체로 정의하면서 `equals()`, `hashcode()`를 재정의하지 않아, 같은 키로 착각하여 데이터가 계속 쌓이게 되는 경우
5. `map`의 키를 사용자 객체로 정의하면서 `equals()`, `hashcode()`를 재정의 하였지만, 키값이 불변(immutable) 데이터가 아니라서 데이터 비교시 계속 변하게 되는 경우

6. 자료구조를 생성하여 사용하면서, 구현 오류로 인해 메모리를 해제하지 않는 경우



## Java Thread

**Thread Life Cycle**

참고자료: [링크1](https://zion437.tistory.com/133) [링크](https://sjh836.tistory.com/121)

**Thread Pool**

참고자료: [링크1](https://blog.naver.com/PostView.nhn?blogId=zion830&logNo=221393808512) 

실행될 쓰레드의 개수가 많아지면 쓰레드의 생성과 스케줄링 등에 소모되는 비용으로 인해 CPU에 부하가 발생할 수 있다. 이로 인해 발생할 퍼포먼스 저하를 방지하기 위해 고안된 것이 **Thread Pool(쓰레드 풀)** 이다.

쓰레드 풀은 제한된 개수의 쓰레드를 JVM에 맡기는 방식으로, 동시에 실행되는 쓰레드의 개수를 제한한다. 실행할 작업을 풀에 전달하면 개발자가 쓰레드를 딕접 생성할 필요 없이 **JVM이 풀의 쓰레드 중 하나를 선택해** (이 때 선택 가능한 쓰레드를 Idle Thread라고 한다.) 실행한다.



## Multi Thread 환경에서의 개발

### Field Member

`필드(field)`란 클래스에 변수를 정의하는 공간을 의미한다. 이곳에 변수를 만들 경우 메소드 끼리 변수를 주고 받는 데 있어서 참조하기 쉬우므로 정말 편리한 공간 중 하나이다. 하지만 객체가 여러 스레드가 접근하는 **싱글톤 객체**라면 `field`에서 상태값을 가지고 있으면 안된다. 모든 변수를 parameter로 넘겨받고 return하는 방식으로 코드를 구성해야 한다.

### 동기화(Synchronized)

필드에 `Collection`이 불가피하게 필요할 때, JAVA에서는 `synchronized` 키워드를 통해 스레드 간 **race condition**을 통제한다. 이 키워드를 기반으로 구현된 `Collection`들도 많이 존재한다. `List`를 대신하여 `Vector`를 사용할 수 있고, `Map`을 대신하여 `HashTable`을 사용할 수 있다. 하지만 이 `Collection`들은 제공하는 API가 적고 성능도 좋지 않다.

기본적으로는 `Collections` util 클래스에서 제공하는 `static` 메소드들을 통해 이 문제를 해결한다. `Collections.synchronizedList()`, `Collections.synchronizedSet()`, `Collections.synchronizedMap()` 등이 존재한다.

### ThreadLocal

**스레드 사이에 간섭이 없어야 하는 데이터**에 사용한다. 멀티스레드 환경에서는 클래스의 필드에 멤버를 추가할 수 없고 매개변수로 넘겨받아야 하기 때문이다. 즉, **스레드 내부의 싱글톤을 사용하기 위해 사용**한다. 주로 *사용자 인증, 세션 정보, 트랜잭션 컨텍스트*에 사용한다.

Thread Pool 환경에서 ThreadLocal을 사용하는 경우 ThreadLocal 변수에 보관된 데이터의 사용이 끝나면 반드시 해당 데이터를 삭제해 주어야 한다. 그렇지 않으면 이후 쓰레드가 재사용될 때 올바르지 않은 데이터를 참조할 수 있다.

ThreadLocal을 사용하는 방법

1. ThreadLocal 객체를 생성한다.
2. ThreadLocal.set() 메서드를 이용해서 **현재 스레드의 로컬 변수에 값을 저장**
3. ThreadLocal.get() 메서드를 이용해서 **현재 스레드의 로컬 변수 값을 읽어온다.**
4. ThreadLocal.remove() 메서드를 이용해서 **현재 스레드의 로컬 변수 값을 삭제한다.**



## Generic

JAVA의 안정성을 담당한다. **다양한 타입의 객체**들을 다루는 메소드나 `Collection` 클래스에서 사용하는 것으로, **컴파일 과정에서 타입체크를 해주는 기능**이다. 객체의 타입을 컴파일 시에 체크하기 때문에 객체의 타입 안정성을 높이고 형변환의 번거로움을 줄여준다. 

자연스럽게 코드도 간결해진다. 예를 들어, **`Collection`에 특정 객체만 추가될 수 있도록**, 또는 특정한 클래스의 특징을 갖고 있는 경우에만 추가될 수 있도록 하는 것이 제네릭이다.

이로 인한 장점은 `Collection`에 들어온 값이 내가 원하는(의도한) 값인지 별도의 로직처리를 구현할 필요가 없어진다. 또한 API를 설계하는데 있어서 보다 명확한 의사전달이 가능하다.

*Remind) Python과 같은 동적 타입 언어들은 런타임에 변수 타입을 체크한다.*



## Wrapper class

참고자료: [링크](https://hyeonstorage.tistory.com/168) 

예) `Integer` 클래스로부터 생성된 객체는 하나의 `int` 값을 저장할 수 있다.

```java
Integer age = new Integer(30);
Double avg = new Double("3.145");
```

기본 자료형(Primitve data type)에 대한 클래스 표현을 Wrapper class라 한다. `Integer`, `Float`, `Boolean` 등이 Wrapper class의 예다. `int`를 `Integer`라는 객체로 감싸서 저장해야 하는 이유가 있을까? 일단 컬렉션에서 **제네릭**을 사용하기 위해서는 Wrapper class를 사용해줘야 한다. 또한 `null`값을 반환해야만 하는 경우에는 return type을 Wrapper class로 지정하여 `null`을 반환하도록 할 수 있다. 하지만 이러한 상황을 제외하고 일반적인 상황에서 Wrapper class를 사용해야 하는 이유는 객체지향적인 프로그래밍을 위한 프로그래밍이 아니고서야 없다. 일단 해당 값을 비교할 때, Primitive data type인 경우에는 `==`로 바로 비교해줄 수 있다. 하지만 Wrapper class인 경우에는 `.intValue()`메소드를 통해 해당 Wrapper class의 값을 가져와 비교해줘야 한다.

*Wrapper class 명단*

- *Byte | Short | Integer | Long | Float | Double | Character | Boolean | Void*

*Wrapper class 기본 메소드 명단*

- byteValue() | shortValue() | intValue() | longValue() | floatValue() | charValue() | doubleValue() | booleanValue()

*JAVA Primitive Data Types* ([링크](https://www.w3schools.com/java/java_data_types.asp))

*(Integer types)*

- byte | 1byte | -128 ~ 127
- short | 2bytes | -32,768 ~ 32,768
- int | 4bytes | -2,147,483,648 ~ 2,147,483,647
- long | 8bytes | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807

*(Floating point types)*

- float | 4bytes | 6~7 decimal digits
- double | 8bytes | 15 decimal digits

*(Others)*

- boolean | 1bit | true or false
- char | 2bytes | single character/letter or ASCII values

**Boxing & Unboxing**

Wrapper class는 산술연산을 위해 정의된 클래스가 아니기 때문에, 이 클래스의 인스턴스에 저장된 값은 변경이 불가능하며, 값을 저장하는 새로운 객체의 생성 및 참조만 가능하다.

- Boxing: 기본 자료형을 Wrapper class의 객체로 변경하는 과정

  ```java
  Integer age = new Integer(30);
  ```

- Unboxing: 각각의 객체를 기본 자료형으로 변경하여 사용하는 과정

  ```java
  int age2 = age.intValue()
  ```

**AutoBoxing**

Wrapper class에 상응하는 Primitive data type일 경우에만 가능하다.

아래 예에서 `Integer`라는 Wrapper class로 설정한 collection에 데이터를 add할 때 `Integer`객체로 감싸서 값을 넣을 필요 없이, JAVA 내부에서 자동적으로 `AutoBoxing` 해준다.

```JAVA
List<Integer> lists = new ArrayList<>();
lists.add(1);
```



## Annotation

참고자료: [링크](https://asfirstalways.tistory.com/309) 

**요약**

주석처럼 코드에 달아 클래스에 특별한 의미를 부여하거나 기능을 주입할 수 있다. *유지 정책(retention policy)*를 통해 유지되는 기간을 지정할 수도 있다. 크게 JDK에 내장되어 있는 `built-in annotation`, 어노테이션에 대한 정보를 나타내기 위한 어노테이션인 `Meta annotation`, 개발자가 직접 만들어 내는 `Custom Annotation`이 있다.

**역할**

기존의 JAVA Web App들은 구성과 설정값들을 외부의 XML 설정 파일에 명시하는 방법으로 프로그래밍 되었다. 따라서 재컴파일 없이도 쉽게 변경사항을 적용할 수 있었지만, 프로그램 작성을 위해 매번 많은 설정을 작성해야 한다는 불편함이 존재했다. 이후 웹 앱의 규모가 커짐에 따라 이러한 불편함은 더 커졌고, 이를 해결하기 위해 고안된 것이 어노테이션이다.

이를 사용하면 데이터에 대한 유효성 검사조건을 어노테이션을 사용하여 직접 명시함으로써 유효조건을 쉽게 파악할 수 있게 되며 코드가 깔끔해진다. 단순히 부가적인 표현 뿐만 아니라, `reflection`을 이용하면 어노테이션 지정만으로 원하는 클래스를 주입할 수도 있다.

어노테이션은 크게 *문서화*, *컴파일러 체크*, *코드 분석*을 위한 용도로 사용된다. 본질적인 목적은 *소스 코드에 메타데이터를 표현하는 것*이다.

### `Built-in Annotation`

JAVA에 내장되어 있는 어노테이션. 주로 컴파일러를 위한 것으로, 컴파일러에게 유용한 정보를 제공.

**@Override**

메소드 앞에만 붙일 수 있으며, 현재 메소드가 **수퍼클래스의 메소드를 오버라이드한 메소드임을 컴파일러에게 명시**한다. 오버라이딩 할 때 메소드 명에서 오타가 발생할 수 있는데, 이 경우 어노테이션을 통해 오타가 발생할 수 있는 부분을 잡아줄 수 있다.

**@Deprecated**

차후 지원되지 않을 수 있기에 사용을 지양해야 할 메소드를 나타낸다.

**@SupressWarning**

경고를 제거

**@FunctionalInterface**

컴파일러에게 다음의 인터페이스는 함수형 인터페이스라는 것을 알린다. 이 또한 오버라이딩 어노테이션과 같이 실수를 미연에 방지하기 위해 사용된다.

### `Meta-Annotation`

어노테이션에 사용되는 어노테이션. **해당 어노테이션의 동작대상을 결정**한다. 주로 새로운 어노테이션을 정의할 때 사용한다.

**@Target**

어노테이션이 적용가능한 대상을 지정하는데 사용한다. 여러 값을 지정할 때는 배열처럼 `{}`를 사용한다.

**@Retention**

어노테이션이 유지되는 기간을 지정한다.

1. **SOURCE**

   *소스 파일*에만 존재하며, 클래스 파일에는 존재하지 않는다. @Override, @SupressWarning같은 **컴파일러에 의해 사용되는 어노테이션** 유지 정책이  SOURCE에 해당한다. 컴파일러를 직접 작성할 게 아니면 사용할 일이 없다.

2. **CLASS**

   *클래스 파일*에 존재하지만 런타임 시에 사용이 불가능하다. @Retention의 default 값이지만, 런타임에 사용이 불가능해 잘 사용되지 않는다.

3. **RUNTIME**

   ***클래스 파일***에 존재하며 ***런타임***에도 사용 가능하다. 런타임 시에 Reflection을 통해 클래스 파일에 저장된 어노테이션 정보를 읽어서 처리할 수 있게 된다.

**@Documented**

어노테이션에 대한 정보가 javadoc으로 작성한 문서에 포함되도록 할 때 사용하는 어노테이션. `built-in-annotation` 중 @Override와 @SuppressWarnings를 제외학는 모두 이 메타 어노테이션이 붙어있다.

```java
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
public @interface FunctionalInterface() {}
```

**@Inherited**

어노테이션이 자손 클래스에도 상속되도록 하는 어노테이션이다. 조상 클래스에 붙여놓을 경우 자손 클래스에도 이 어노테이션이 붙은 것과 같이 인식된다.

**@Native**

네이티브 메서드에 의해 참조되는 상수필드에 붙이는 어노테이션이다. 네이티브 메서드란 JVM이 설치된 **OS의 메서드**를 말한다. 네이티브 메서드는 보통 C언어로 작성되어 있으며 JAVA에서는 메서드의 선언부만 정의하고 구현은 하지 않는다. Object 클래스의 메서드들은 대부분 네이티브 메서드이다. 우리는 **JAVA라는 언어를 통해 OS의 메서드를 호출하고 있는 것과 마찬가지이다.** 네이티브 메서드와 자바에 정의된 메서드를 연결하는 것을 **JNI(JAVA Native Interface)**라고 한다. (JVM, GC 파트 remind)

### `Custom-Annotation`

```java
public @interface MyAnnotation {}
```

어노테이션 타입의 선언은 '특별한' 종류의 인터페이스 선언이다. 단, 일반적인 인터페이스 선언과 구분하기 위해 예약어 `interface` 앞에 `@`를 붙여준다. 어노테이션 타입은 암묵적으로 `java.lang.annotation.Annotation`을 확장하기 때문에 **extends 절을 가질 수 없다.**

다음과 같은 형식을 갖는다.

```pseu
@interface [어노테이션 이름] {
	타입 요소이름();
	...
}
```



어노테이션은 메타데이터 저장을 위해 **클래스처럼 멤버를 가질 수 있다.** 어노테이션 내에 선언된 메소드를 어노테이션의 **요소(element)**라고 한다. 요소의 개수에 따라 Maker 어노테이션, Single-value 어노테이션, Full 어노테이션으로 분류할 수 있다.

**Maker 어노테이션**

- 요수 개수: 0

  단순히 표식으로서 상요되는 어노테이션. 컴파일러에게 어떤 의미를 전달하는데 사용된다.

**Single-value 어노테이션**

- 요소 개수: 1

  요소로 단일 변수만을 갖기 때문에 값만을 명시하여 데이터를 전달할 수 있다.

  ```java
  @interface TestInfo {
      String value();
  }
  @TestInfo("passed") // @TestInfo(value="passed") 와 동일
  class MyClass{...}
  ```

**Full 어노테이션**

- 요소 개수: 2 이상

  데이터를 배열 안에 key-value 형태로 전달한다.

  ```java
  @AnnotationName(element1=value1, element2=value2, ...)
  ```

  *이 요소에는 일정 규칙이 존재한다.*

  1. 요소의 타입은 기본형, String, enum, 어노테이션, Class만 허용한다.
  2. 요소의 `()` 안에 매개변수를 선언할 수 없다.
  3. 예외를 선언할 수 없다.
  4. 요소를 타입 매개변수로 정의할 수 없다. (제너릭의 타입?)
  5. 어노테이션의 각 요소는 기본값(`default`)을 가질 수 있다.

  ```java
  @interface TestInfo {
      int count() default 1;
  }
  @TestInfo("passed") // @TestInfo(count=1)와 동일
  class myClass{...}
  ```



***[추가) enum이 뭐지?](#Enum)***





## final keyword

- final class

  다른 클래스에서 **상속하지 못한다.**

- final method

  다른 메소드에서 **오버라이딩하지 못한다.**

- final variable

  변하지 않는 **상수값이 되어** 새로 할당할 수 없는 변수가 된다.

*혼동 주의*

- finally

  `try-catch` 혹은 `try-catch-resource` 문을 사용할 때, 작업 성공 여부와 관계없이 마무리 해줘야하는 작업이 존재할 경우 작성하는 코드 블록

- finalize()

  `GC`에 의해 호출되는 메소드로 함부로 사용하지 말 것.



## Overriding vs Overloading

- 오버라이딩(Overriding)

  상위 클래스에 존재하는 메소드를 **하위 클래스에서 필요에 맞게 재정의**하는 것

- 오버로딩(Overloading)

  상위 클래스의 메소드와 **이름, return 값은 동일하지만, 매개변수만 다른 메소드**를 만드는 것을 의미한다. 다양한 상황에서 메소드가 호출될 수 있도록 한다. (ex. 생성자)



## Access Modifier

변수 혹은 메소드의 접근 범위를 설정해주기 위해서 사용하는 JAVA의 예약어를 의미하며 총 네 가지 종류가 존재한다.

- public

  어떤 클래스에서라도 접근이 가능

- protected

  클래스가 정의되어 있는 **패키지 내**, 혹은 해당 클래스를 **상속받은 외부 패키지**의 클래스에서 접근 가능

- (default)

  클래스가 정의되어 있는 **패키지 내에서만** 접근 가능

- private

  정의된 해당 클래스에서만 접근이 가능



## Enum

참고자료: [링크1](http://woowabros.github.io/tools/2017/07/10/java-enum-uses.html) [링크2](https://limkydev.tistory.com/50) 

클래스의 하나로. 열거형 타입(Enumerated type)이라고도 부른다. **서로 연관된 상수들의 집합**이기도 하다.

아래 두 표현식은 동일한 의미를 가진다.

```java
enum Fruit {
    APPLE, PEACH, BANANA;
}
```

```java
class Fruit {
    public static final Fruit APPLE = new Fruit();
    public static final Fruit PEACH = new Fruit();
    public static final Fruit BANANA = new Fruit();
    private Fruit(){} //생성자가 private -> Fruit 클래스를 인스턴스로 만들 수 없다.
}
```

Enum을 통해 얻는 장점:

- 코드가 단순해진다.

- 인스턴스 생성과 상속을 방지한다.

- `enum` 키워드를 통해 구현의 의도가 *열거*임을 분명하게 나타낼 수 있다.

  ---

- IDE의 적극적인 지원(자동완성, 오타검증, 텍스트 리팩토링)

- 허용 가능한 값들을 제한할 수 있다.

- 리팩토링시 변경 범위가 최소화 된다.
  - 내용의 추가가 필요하더라도, Enum 코드 외에 수정할 필요가 없다.

JAVA의 Enum은 여기서 더해, 다음과 같은 장점이 있다.

- C/C++의 Enum은 결국 int값이지만, JAVA의 Enum은 완전한 기능을 갖춘 **클래스**이다.



### 1. 데이터들 간의 연관관계 표현







*python에서의 enum은 어떨까?*
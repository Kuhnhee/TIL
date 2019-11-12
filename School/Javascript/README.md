# Javascript









## Node.js

*다음 [링크](https://sjh836.tistory.com/79)의 글을 참고하여 정리한 내용입니다.*

*브라우저 바깥의 JS 동향 및 전망. [링크](https://d2.naver.com/helloworld/7700312)*

*2019년과 이후 JS의 미래 [링크1](https://d2.naver.com/helloworld/4007447) [링크2](https://d2.naver.com/helloworld/2108442)*



구글 V8 JavaScript 엔진 기반, 싱글스레드 기반으로 비동기 이벤트 위주 I/O를 사용하는 시스템.

- 오픈 소스 JIT 가상 머신 형식의 JS 엔진. JS를 바이트코드로 컴파일하거나 인터프리트하는 대신 실행하기 전 직접적인 **기계어로 컴파일**하여 성능을 향상. 추가적으로 **인라인 캐싱**과 같은 최적화 기법을 도입.



**특징**

- 싱글 스레드: 문맥 교환으로 인한 오버헤드 없음
- 비동기 I/O: CPU time loss 회피, I/O 요청이 있으면 **worker**에게 맞기고 쓰레드는 다른 일을 계속 받는다.
- 이벤트 기반: epool or kqueue 사용
- 경량형 프레임워크
- 풍부한 라이브러리, 모듈
- 서버와 클라이언트에서 사용하는 언어 (JS)가 같음

![node1](./img/node1.jpg)



## 싱글스레드?

1. 싱글스레드 기반의 **이벤트 루프**가 돌면서 요청을 처리한다. I/O 요청이 있는 경우, 스레드 풀에 요청을 전달한다. 이 스레드 풀에는 워커들이 여럿 존재한다. 즉, **이벤트 루프**만 싱글 스레드라서 request, response가 싱글스레드일 뿐 뒤에서 일하는 워커들(I/O처리)은 멀티 스레드로 동작한다.

2. 기본적으로 NodeJS는 event loop를 돌리는데 하나의 쓰레드를 사용한다. 그러나 CPU를 많이 사용해야 하는 일들을 이 main thread에서 모두 처리할 경우 다른 일을 처리할 수 없게 된다. 따라서 nodejs는 기본적으로 CPU Intensive한 작업들은 다른 쓰레드에서 처리한다. 예를 들어, nodejs 모듈 중 **crypto** 모델의 **pbkdf2()**라는 암호 생성 함수는 CPU Intensive하기 때문에 event loop가 돌아가는 main thread가 아닌 다른 thread에서 돌아간다.**(Event loop가 block될 수 있기 때문에)**

3. **Event Loop**와 내가 작성한 JS 코드를 실행할 때에만 "nodejs는 싱글스레드"이다.

   비동기 file I/O를 하는 경우 OS가 비동기적으로 지원하지 않기 때문에 추가적인 thread를 사용한다.

   nodejs의 비동기 I/O인 추상화 라이브러리인 Libuv는 기본적으로 4개의 thread를 가지고 있다(변경 가능). 이용자가 fs모듈의 `readFile()`함수 혹은 crypto 모듈의 `pbkdf2()`함수를 사용할 경우 내부적으로 이런 작업들을 thread를 사용해 처리하게 된다.

**싱글스레드로 여러 요청을 어떻게 받지?**

- 멀티플렉싱



## Network I/O 작업은 다르게 동작한다?

위에서 언급한 **pbkdf2()**와 같은 **file system I/O** 작업이 병렬처리 되는 것과 같이, **network I/O**작업 또한 병렬 처리 된다. 하지만, 위와 같이 **thread pool** 안에 있는 여러 thread들을 사용하는게 아니라 운영체제의 **Process** 안에서 병렬로 처리하게 된다.



## Event-loop 

**참고자료: [링크](https://medium.com/@rpf5573/nodejs-event-loop-part-1-big-picture-7ed38f830f67)  **

서버가 많은 클라이언트로부터 I/O요청을 받게 될 경우, 처리해야 할 callbak funciton 또한 많아지게 된다. Nodejs에서는 **event queue**와 **event loop**을 사용해 callback function들을 처리한다.

서버는 I/O 요청을 받아서 disk나 network device에게 일을 시키고 일이 끝나면 **event queue**에 설정해 놓은 **callback function**을 순서대로 담고, **event loop**는 그 **callback function**을 하나하나 빼서 실행한다.

이 때, 네트워크 관련 I/O 작업들은 OS를 통해 OS의 프로세스 자원을 사용하여 처리하며, 파일 입출력/암호만들기 등은 **libuv** 비동기 I/O처리 라이브러리의 **thread pool**안에 있는 thread에서 처리를 한다.

타이머는 **Event loop** 안에서 정해진 시간이 지났는지를 계속 체크한다.



**여러 Event Queue들**

1. timers: `setTimeout()`, `setInterval()`로 등록한 callback 함수와 호출 시간이 들어 있다. **Event loop**는 timers queue에 들어있는 타이머 아이템(callback 함수, 호출시간)에 설정된 호출시간이 지났는지 판단해서 callback 함수를 호출한다.
2. I/O events: I/O작업이 끝난 후에 호출될 callback 함수가 들어있다.
3. Immediates: `setImmediate()`로 설정된 callback 함수가 들어있다.
4. close handler: `*.on('close')`로 설정된 callback 함수가 들어있다.



**Event loop phase**

Event loop는 아래와 같은 순서대로 호출된다.

1. timers: **timer event queue**를 한 바퀴 돌면서 지연 시간이 지난 타이머들의 callback 함수를 호출한다.
2. pending callbacks(I/O Callbacks): **pending queue**에 있는 callback 함수들을 처리한다. TCP 오류 같은 시스템 작업의 callback을 반환한다. **poll**단계에서 처리하지 못하고 다음 루프로 지연된 callback 함수들 또한 이곳에 담겨있을 것이다. 
3. idle: `uv_idle_{init, start, stop}` API를 사용해 idle queue에 등록된 callback 함수를 호출한다.
4. prepare: `uv_prepare_{init, start, stop}` API를 사용하여 prepare queue에 등록된 calback 함수를 호출한다. **Poll** 단계에서 event loop가 잠시 *block*될 수 있기 때문에, *block*되기 전에 실행할 것들이 이 단계에서 실행된다.
5. poll: 여유가 있다면 I/O 작업이 끝나기를 기다린다. 작업이 끝나면 **pending queue**에 넣지 않고 여기서 바로 실행한다. 예를 들어, 다음 타이머가 실행되기 까지 10초가 남았고 다른 큐에는 할일이 없다면, 10초동안 I/O 작업(파일 Read/Write)이 끝나기를 기다린다. 
6. check: `setImmediate()`로 설정된 callback 함수들을 호출한다.
7. close callbacks: `*.on('close')`로 설정된 callback 함수들을 호출한다.
8. 각 단계 사이사이 **next tick queue**와 **micro task queue**에 들어있는 callback 함수들을 호출한다.



## Blocking vs Non-Blocking

**Blocking**

JS 코드가 line-by-line으로 실행되는 도중, I/O 관련 작업이나 네트워크 통신을 하는 코드를 CPU(nodejs의 single-thread에 할당된 CPU 자원)가 마주쳤을 때, OS에게 해당 작업을 맡긴다. 이 때 CPU는 잠시 대기상태로 전환되어 결과를 기다린다. OS로부터 작업이 끝났다는 신호를 받으면, 바로 다음 JS 코드를 한 줄씩 실행한다. 이와 같이 **CPU가 잠시 쉬면서 OS로부터의 신호를 기다리는 상태를 Blocking이라고 한다.**

**Non-Blocking**

**CPU를 쉬게 냅두지 않는다.** I/O관련 작업이나 네트워크 통신 관련 일을 하라는 코드를 만났을 때, OS에게 일을 맡기고, **다시 자기가 하던 일을 한다.** 이후 OS에게 맡긴 일이 끝났을 때 CPU에게 이를 알리도록 설정한다.

Node.js에서는 non-blocking 방식으로 일을 처리하기 위해서 **Event-loop**와 **Event-Queue**를 만들어 사용한다. CPU는 OS에게 일을 맡기면서, 작업이 끝날 경우 '특정 코드 블락'(=**Callback Function**)을 Event-queue 안에 넣도록 시킨다. 이후 해당 queue(Event-queue)를 감시하면서 뭔가(callback function) 들어있으면 해당 코드를 실행시킨다.



## 비동기의 장점?

I/O 요청이 발생했을 때 워커들에게 일을 맞기고, CPU는 쉬지않고 계속 다른 요청들을 받는다. I/O처리가 끝나면 워커가 콜백함수와 함께 파일쓰기가 끝났다고 알려준다. CPU 효율의 입장에서 큰 차이를 만든다.





## 기존 웹서버와이 차이?

Apache와 같은 웹서버는 웹 리소스가 요청될 때마다 이를 처리하기 위한 별도의 스레드를 매번 생성하거나, 새 프로세스를 호출한다. 이로 인해 **request가 많아질 경우 병목 현상**이 발생하는 경우가 많다. Synchronous 방식에서는 이를 해결하기 위해 흔히 멀티스레드에 스케일아웃하고 로드밸런싱을 한다.

하지만 **Node와 같이 비동기 처리**를 지원할 경우, Non-blocking으로 요청을 처리할 수 있기 때문에 훨씬 가벼우면서도 빠르다.

Node는 **싱글 스레드이기 때문에 오버헤드가 적어** 어플리케이션 확장성을 쉽게 얻을 수 있다. 또한 **리소스 사용을 최소화**했기 때문에 굳이 멀티스레드로 만들 필요가 없다.


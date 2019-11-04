# Node.js

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

싱글스레드 기반의 **이벤트 루프**가 돌면서 요청을 처리한다. I/O 요청이 있는 경우, 스레드 풀에 요청을 전달한다. 이 스레드 풀에는 워커들이 여럿 존재한다. 즉, **이벤트 루프**만 싱글 스레드라서 request, response가 싱글스레드일 뿐 뒤에서 일하는 워커들(I/O처리)은 멀티 스레드로 동작한다.

**싱글스레드로 여러 요청을 어떻게 받지?**

- 멀티플렉싱



## 비동기의 장점?

I/O 요청이 발생했을 때 워커들에게 일을 맞기고, CPU는 쉬지않고 계속 다른 요청들을 받는다. I/O처리가 끝나면 워커가 콜백함수와 함께 파일쓰기가 끝났다고 알려준다. CPU 효율의 입장에서 큰 차이를 만든다.



## 기존 웹서버와이 차이?

Apache와 같은 웹서버는 웹 리소스가 요청될 때마다 이를 처리하기 위한 별도의 스레드를 매번 생성하거나, 새 프로세스를 호출한다. 이로 인해 **request가 많아질 경우 병목 현상**이 발생하는 경우가 많다. Synchronous 방식에서는 이를 해결하기 위해 흔히 멀티스레드에 스케일아웃하고 로드밸런싱을 한다.

하지만 **Node와 같이 비동기 처리**를 지원할 경우, Non-blocking으로 요청을 처리할 수 있기 때문에 훨씬 가벼우면서도 빠르다.

Node는 **싱글 스레드이기 때문에 오버헤드가 적어** 어플리케이션 확장성을 쉽게 얻을 수 있다. 또한 **리소스 사용을 최소화**했기 때문에 굳이 멀티스레드로 만들 필요가 없다.

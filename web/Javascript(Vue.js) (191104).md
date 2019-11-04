# Vue.js

우리가 JS를 쓰는 이유?

- **Client Side Rendering**을 하기 위한 것
  - 클라이언트는 Browser라는 프로그램을 통해서 서버에 접근을 한다. Rendering의 주체가 Django가 아닌, 클라이언트의 Browser가 되도록 하자. (우리가 지금까지 해온 방식은 Server Side Rendering, Django가 rendering 해왔다. 요청&응답이 있는 구조였다.)
  - Page load가 없이 (새로운 요청을 보내지 않고), 클라이언트 측에서 화면이 바뀌도록 하기 위해. (좋아요, 팔로우, 댓글, 글쓰기 ... )
  - *사용자의 경험을 향상시키자!* 가 목적



Vue.js와 같은 FE framework를 쓰는 이유?

- 어플리케이션을 만들기가 **쉬워지기 때문**
- 공식문서 [링크](https://kr.vuejs.org/v2/guide/) 



## RECAP

문서(html)을 객체로 다룰 수 있도록 하는 것이 DOM. 각각의 태그가 오브젝트화 되어있다. 이 오브젝트들을 조작하는게 JS.

JS의 `this`는 JAVA의 `this`와 다르다. `addEventListner`의 콜백 함수로 arrow function을 쓰지 않는 이유. (arrow function이 `this`의 context를 바꾼다.)



**검색창 밑에 검색값 보여주기**

`input` 이벤트는 입력값이 입력되는 순간 바로 발생

```html
<body>
  <h1>댓글달기</h1>
  <input id="userInput" type="text">
  <p id="inputArea"></p>

  <script>
    const userInput = document.querySelector('#userInput')
    const inputArea = document.querySelector('#inputArea')
    
    userInput.addEventListener('input', function(event) {
      inputArea.innerText = event.target.value
    })
  </script>
</body>
```

좋아요 갯수 카운트(단순 카운터)

```html
<body>
  <h1>댓글달기</h1>
  <input id="userInput" type="text">
  <p id="inputArea"></p>

  <h2>좋아요</h2>
  <p id="likeCountArea">좋아요 갯수:</p>
  <button id="likeButton">좋아요</button>

  <script>
    const userInput = document.querySelector('#userInput')
    const inputArea = document.querySelector('#inputArea')
    const likeButton = document.querySelector('#likeButton')
    const likeCountArea = document.querySelector('#likeCountArea')
    let likeCount = 0 //좋아요 카운트
    
    userInput.addEventListener('input', function(event) {
      inputArea.innerText = event.target.value
    })

    likeButton.addEventListener('click', function(event) {
      // 좋아요 갯수를 한 개 중가시킴
      likeCount++
      // p태그의 값을 변경시킴
      likeCountArea.innerText = `좋아요 갯수: ${likeCount}`
    })
  </script>
```

기능을 추가할 때마다 object를 잡아주고, event를 핸들링해주고, 코드가 너무 복잡해지고 길어진다. 이를 정리하기 위해서 (maintain을 용이하게 하기 위해) 등장한게 JS framework들.



**위의 코드를 vue.js로 작성할 경우**

1. vue 객체 생성
   - `el`: 이 객체가 실행될 위치 지정
   - `data`: 이 객체가 사용할 데이터들 (정적 데이터) 정의
   - `methods`: 이 객체가 사용할 함수들 정의
2. 선언한 vue 객체가 역할을 수행할 영역 생성 (아래 코드에서는 `<div id='app'>`)
3. Vue directive를 사용해 Vue 객체가 할 행위를 지정(바인딩, 이벤트 핸들링 등). Mustache `{{ }}` 문법을 사용해 값 전달.

```html
<body>
  <!-- vue instance를 마운트할 위치 -->
  <div id='app'>
    <h1>댓글달기</h1>
    <!-- vue directive 사용해서 실시간으로 연결 -->
    <input type="text" v-model="msg">
    <p>{{ msg }}</p>
      
    <h2>좋아요</h2>
    <p>좋아요 갯수: {{ likeCount }}</p>
    <button v-on:click="like()">좋아요</button> <!-- v-on: button이 ~를 하면~ -->
  </div>

  <script>
    // rendering은 vue 너가 해~ 난 어떻게 할지만 알려줄게!
    // vue 객체 생성
    const app = new Vue({
      el: '#app', // ~에서 하면 돼! 라고 위치를 알려주는 것
      data: { // vue 인스턴스가 사용할 데이터들. Django에서 render때의 context와 동일한 역할
        msg: '와 vuejs 시작했다!',
      },
      methods: {
        like: function() {
          this.likeCount++
        }
      },
    }) 
  </script>
</body>
```

- `v-model="msg"` : 폼 입력 바인딩
- `v-on:click="like"` : 클릭 이벤트 발생시 `app`의 `like` 함수 실행. 추후 배우겠지만`@click="like"`와 동일. (short hand expression)

- Django에서 app들을 쪼개놓듯이, Vue에서는 componnt별로(검색창, 내비게이터, ...) 객체를 분리해(각각의 용도를 위한 vue 객체를 생성해) 관리한다.
- vue.js는 선언적 프로그래밍 패러다임
  - = Discriptive Programming (묘사를 한다!)
  - 명령적으로 프로그래밍하는 것보다 훨씬 명시적으로 할 수 있다.



## Vue.js

### SPA(Single Page Application)

- 페이지 로드 없이, 한 번에 한 페이지 안에서 모든걸 할 수 있는 어플리케이션
  - 이를 위해서는 JS를 통핸 Client Side Rendering을 할 수 밖에 없다.

![vue1](./img/vue1.PNG)

위의 MVC(MTV) 패턴에서 아래의 형태로 변화

![vue2](./img/vue2.PNG)



### 시작하기

VScode extension 'Vetur', 'Vue VSCode Snippets' 설치.

Chrome extension 'Vue.js devtools' 설치. (Vue가 사용되는 page에 들어가면 초록색으로 변한다. 또, 개발자 도구 창에 Vue 항목 생긴다.)



bootstrap에서의 Responsive(반응형)과 JS에서의 Reactive(반응형)은 다른 의미

- Reactive: 데이터의 변화에 반응형. **자동 적용(반영)**
- Responsive: Device의 화면크기에 반응형. 



**CDN 추가**

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```



**Vue 인스턴스 mount 위치 지정**

```html
<div id="app"></div>

<script>
    const app = new Vue({
        el: '#app'
    })
</script>
```



**Data 선언 및 전달**

 Mustache 문법 (`{{ }}`) 사용

선언 시 `$` 혹은 `_`은 어지간해서는 쓰지 않는다. (시스템이 예약어로 사용하고 있는 경우가 많아)

```html
<div id="app">
    <p>{{ message }}</p>
    <p>{{ name }}</p>
</div>

<script>
    const app = new Vue({
        el: '#app',
        data: {
            message: '안녕 Vue.js',
            name: '건희',
        },
    })
</script>
```



**Vue 객체에 선언된 함수를 통해, Data를 입력되는 값으로 변경하기**


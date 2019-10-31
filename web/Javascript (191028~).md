# Javascript

*본 리포지토리는 [정윤영](https://github.com/liza0525/TIL/blob/master/20191029_Fundamental_of_Javascript.md)님과 [이수진](https://github.com/sigk218)님의 TIL을 참조했습니다.*

Javascript는 browser 조작 언어로 시작됨

- node.js: browser 뿐만 아니라, 상용 프로그래밍 언어로도 사용하도록 도입 

규격 통일이 필요해져 ECMA에서 **ECMA Script** 정의

- ES2015 즈음부터 Chrome이 따르기 시작
- firefox는 이전부터 ECMA를 따라 왔음, IE는 별개로

언어적 업그레이드가 ES2015(ES6)부터 급격히 이루어짐

Javascript 기본 타입에 관하여.... ([링크](https://nooheat.github.io/자바스크립트-타입과-typeof-정확히-알기/))



**개발자 도구 - Console 창**

- `window`: 브라우저 자체를 하나의 객체로 표현한 것
- `window.history`
- `window.document.getElementsByTagName('p')`
- `window.print`
- `ctrl+l`: 모든 line 삭제



## node.js

JS를 Fully functional programming language로 사용

Google이 개발, 현재는 Linux foundation이 관리

**설치** ([링크](https://nodejs.org/ko/))

```shell
# 12.13.0 LTS 버전 설치
# 버전 확인
node -v

# npm 버전 확인
npm --version

# 파일 실행
node file_name.js
```



## 저장

`무엇을 (자료형)` | `어디에 (identifier, Container type)` | `어떻게(=)`

**선언과 할당**

JS에서 assignment(할당)과 declare(선언)은 한 번만 가능

`let`: 변수 선언 ( *block-scoped* ). 재선언 불가

`const`: 상수 선언 ( *block-scoped* ). 재선언/재할당 불가

`var`: ES6 이전에 지역변수 선언 방식 (legacy code, *function-scoped* )



**자료형**

- 파이썬과 비교

```
				python 				Js
				type()				typeof(키워드, 메서드 X)
숫자 			   숫자				   숫자 
글자 			   '', ""			   '', "", ``
boolean 		True, False			true, false
Empty Value 	None 				undefined(default), null
```

- `string`

  ```javascript
  'hello'.length // 5
  'hello'.toUpperCase() // 'HELLO'
  
  const MY_FAV = 4
  // concatenation
  console.log('내가 좋아하는 숫자는 ' + MY_FAV)
  
  // interpolation
  console.log(`내가 좋아하는 숫자는 ${MY_FAV}`)
  ```

- *undefined, null, NaN (not a number)*

  ```javascript
  typeof undefiend //'undefined'
  typeof null //'object'
  typeof NaN // number
  ```

- `==` 와 `===`

  `==`: Value만 비교

  `===`: 객체 타입 비교 후, 주소 값 비교

  ```javascript
  // ex1 
  null == undefined // true
  null === undefined // false
  
  // ex2
  [] == [] // false; array 클래스의 인스턴스. 다른 객체로 인식
  [] === [] // false; 주소값이 다름.
  ```

- Javascript Convention

  - 상수명: ALLCAP
  - 변수명, 함수명, camelCase
  - 클래스: PascalCase



## 조건/반복문

입력

- ```javascript
  const UserName = prompt('당신의 이름을 입력해주세요.')
  ```

조건문

- ```javascript
  if (UserName.length >= 3){
      alert('이름이 3글자 이상입니다.')
  } else{
      alert('이름이 3글자 미만입니다.')
  }
  ```

반복문

- ```javascript
  let menus = ['대우식당', '바스버거', '세븐브릭스', '진가와']
  
  menus[0] // '대우 식당'
  
  // version 1 
  for (let i = 0; i< menus.length; i++){
      console.log(menus[i])
  }
  
  // version 2
  for [변수] (let menu of menus){
      console.log(menu)
  }
  
  // version 3
  menus.forEach(function(menu){ //python lambda - function 
                console.log(menu)
                })
                
  // verison 3-short
  menus.forEach(menu => {
      console.log(menu)
  })         
  ```

논리 연산자

- ```
  연산자		python 			JS
  곱		  and 			 &&
  합		  or 			 ||
  		  				  |
  		  not, !		  !
  3항		참/거짓 ? [참 일때]:[거짓일 때]
  ```



## 함수

**함수의 선언**

```pseudocode
function [함수명](인자){
    내용
    return 
}
```

변수를 선언하고, 함수 표현식을 써준다.함수 표현식으로 쓰면 실행되기 이전 시점에 함수를 선언을 하고 코드를 읽게 된다.(hoisting 발생)

```javascript
// 2.function Expression
const sub = function (num1, num2){
    return num1 - num2 
}
```

Arrow function notation(ES6) 방식

```javascript
const mul = (x, y) => {
    return x * y
}
// 인자가 하나인 경우 괄호 생략 가능. e는 보통 event 의미
e => {
    
}
```



## 객체

JS의 객체는 인자로 Value, function을 사용하는게 가능하며, 객체 안에 객체를 저장할 수 있다.

```javascript
const me = {
    name: 'john', 
    sleep: function(){
        console.log('쿨쿨')
    },
    applProducts:{
        macBook: '2018pro',
        iPad:'2018pro',
    }
}

// 객체 선언시 'name', name 모두 가능.(str이 아니여도 됨)
// 불러올 때 KEY 값은 문자열만 가능.
console.log(me['name']) // console.log(me[name]) (X)
console.log(me.name)
console.log(me.sleep()) //'.'으로 참조도 가능함.
console.log(me.applProducts.macBook)// 중첩도 가능.
```



## 파일 Read / Write

파일 불러오기

```javascript
const fs = require('fs') // file system library import (node js)
```

JS 객체를 JSON파일로 만들기

```javascript
//JSON(Javascript Object Notation)
//object - > JSON
const meJSON = JSON.stringify(me)
console.log(typeof(meJSON)) //string 
// fs.writeFile('me.json', meJSON, err =>{}) //callback함수 필요
fs.writeFileSync('me.json', meJSON) //동기적으로 만든 것
```

JSON 파일을 불러와 객체로 저장하기

```javascript
//JSON(string) - > obejct
const meObject = JSON.parse(meJSON)
console.log(typeof meObject)
console.log(meObject)
console.log(meJSON)
```

Callback 함수: 작동 하다가 error가 났을때 무엇을 할 지 알려줌



## Event 핸들링 (Dino)

크롬 콘솔창에서 공룡 집기

```javascript
const dino = document.querySelector('#dino')
```

`dino` 객체의 margin값에 접근하기

```javascript
dino.style.marginRight = '20px' //오른쪽 margin 20px 지정
dino.style.marginLeft = ...
```

`dino`를 클릭했을 때 `alert` 띄우기

```javascript
const dino = document.querySelector('#dino')
dino.addEventListener('click', event => {
    alert('아야')
    console.log(event)
})
```

화살표 키로 dino 움직이기 (margin 추가하는 방식으로)

`keydown` : 키보드를 누를 때. `keyup` : 키보드에서 손을 뗄 때.

```javascript
document.addEventListener('keydown', e => {
    // margin을 주는 방식으로 공룡을 움직여보자
    if (e.keyCode === 37) {
        console.log('왼쪽으로 이동')
        x -= 40
        dino.style.marginLeft = `${x}px`
    } else if (e.keyCode === 38) {
        console.log('위쪽으로 이동')
        y -= 40
        dino.style.marginTop = `${y}px`
    } else if (e.keyCode === 39) {
        console.log('오른쪽으로 이동')
        x += 40
        dino.style.marginLeft = `${x}px`
    } else if (e.keyCode === 40) {
        console.log('아래쪽으로 이동')
        y += 40
        dino.style.marginTop = `${y}px`
    } else {
        alert('잘못된 키를 누르셨어요. 방향키를 눌러주세요')
    }
})
```

전체 코드

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <title>Dino</title>
  <style>
    .bg {
      background-color: #f7f7f7;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
  </style>
</head>

<body>
  <div class="bg">
    <img id="dino" width="100px" heigth="100px"
      src="https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg"
      alt="dino" />
  </div>

  <script>
    const dino = document.querySelector('#dino')
    dino.addEventListener('click', event => {
      alert('아야')
      console.log(event)
    })

    let x = 0
    let y = 0

    document.addEventListener('keydown', e => {
      // console.log(e)
      // console.log(e.key)
      // console.log(e.keyCode)

      // margin을 주는 방식으로 공룡을 움직여보자
      if (e.keyCode === 37) {
        console.log('왼쪽으로 이동')
        x -= 40
        dino.style.marginLeft = `${x}px`
      } else if (e.keyCode === 38) {
        console.log('위쪽으로 이동')
        y -= 40
        dino.style.marginTop = `${y}px`
      } else if (e.keyCode === 39) {
        console.log('오른쪽으로 이동')
        x += 40
        dino.style.marginLeft = `${x}px`
      } else if (e.keyCode === 40) {
        console.log('아래쪽으로 이동')
        y += 40
        dino.style.marginTop = `${y}px`
      } else {
        alert('잘못된 키를 누르셨어요. 방향키를 눌러주세요')
      }
    })
  </script>
</body>

</html>
```



## Shopping list (MDN 코드 기반)

장바구니에 항목을 추가했을 때, 페이지 리로드 없이 목록이 생성되도록 만들자.

우선, 컨트롤 해야하는 html 태그들을 가져오자

```html
...
  <h1>My Shopping List</h1>
  Enter a new item: <input id="item-input" type="text">
  <button id="add-button">Add Item</button>
  <ul id="shopping-list">
  </ul>
...
<script>
    //input, button, shoppinglist(ul) 태그 가져오기
    const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')
</script>
```

`click`이벤트가 `button`에서 발생했을 때, 입력된 값을 가져오자

```javascript
    button.addEventListener('click', e => {
      const itemName = input.value //input 객체 안에 들어간 value값을 가져온다.
    })
```

`ul` 태그 안에 값들을 추가해주자 (`li` 태그를 추가해주자). `createElement`(태그 생성), `innerText`(값 삽입), `appendChild`(자식으로 추가) 사용.

```javascript
	const item = document.createElement('li') //li태그 생성
    item.innerText = itemName //li태그에 값 삽입
    shoppingList.appendChild(item) //ul태그의 자식으로, 생성한 li태그를 추가
```

`Add item` 버튼을 누르는 순간, 입력창을 비우자

```javascript
	input.value = ''
```

**항목 삭제 기능도 추가하자**

삭제를 위한 `button` 태그 생성

```javascript
      const deleteButton = document.createElement('button') //button태그 생성
      deleteButton.innerText = 'delete'
      item.appendChild(deleteButton) //li태그 안에 삭제 버튼 추가
```

`delete` 버튼이 클릭되었을 때의 행동을 `addEventListner`로 추가.

`remove()` 함수로 생성한 `item` (`li`태그) 삭제

```javascript
      deleteButton.addEventListener('click', e => {
        item.remove()
      })
```

전체 코드

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>My Shopping List</h1>
  Enter a new item: <input id="item-input" type="text">
  <button id="add-button">Add Item</button>
  <ul id="shopping-list">

  </ul>

  <script>
    const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')

    button.addEventListener('click', e => {
      const itemName = input.value //input 객체 안에 들어간 value값을 가져온다.
      input.value = '' //입력창 비우기

      const item = document.createElement('li') //li태그 생성
      item.innerText = itemName //li태그에 값 삽입

      const deleteButton = document.createElement('button') //button태그 생성
      deleteButton.innerText = 'delete'
      deleteButton.addEventListener('click', e => {
        item.remove()
      })
      item.appendChild(deleteButton) //li태그 안에 삭제 버튼 추가

      shoppingList.appendChild(item) //ul태그의 자식으로, 생성한 li태그를 추가
    })

  </script>
</body>
</html>
```

훗날 MTTM (MVC에서 MVVM) 모델을 사용할 것. MTV의 View가 TM(Template+Model)으로 바뀜. Template과 Model이 직접적으로 데이터를 주고받음



## giphy 붙이기 (python 없이 template에서 바로)

**python은 함수를 선언하기 전 사용하면 에러가 나지만, JS는 파일 전체가 한꺼번에 로드되기 때문에 선언과 호출의 순서를 지킬 필요가 없다.**



python의 `requests`의 역할을 JS에서는 `XMLHttpRequest` 클래스의 인스턴스가 해준다.

```javascript
const API_KEY = '...'
let keywod = 'samsung' //나중에 안 쓸 값
const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`

const GiphyAPICall = new XMLHttpRequest()
GiphyAPICall.open('GET', URL)
GiphyAPICall.send()
```

응답이 제대로 도착했을 경우의 event를 `load`라고 한다.

```javascript
GiphyAPICall.addEventListener('load', e => {
    const parsedData = JSON.parse(e.target.response)
    // e.target.response = raw json data
    pushToDOM(parsedData)
}) 
```

전달받은 `paredData`를 `pushToDOM`에서 `forEach`문을 사용해 출력해주자

```javascript
const pushToDOM = (data) => {
    const dataSet = data.data
    dataSet.forEach(data => {
        resultArea.innerHTML += `<img src="${data.images.original.url}">`
    })
}
```

`innerHTML`말고, `createElement`로 구현하면 더 깔끔하게 할 수 있다.

```javascript
const pushToDOM = (data) => {
    resultArea.innerHTML = null; //초기화 (출력되어있는 값들 지움)
    const dataSet = data.data
    dataSet.forEach(data => {
        const elem = document.createElement('img') //img 태그 생성
        elem.src = data.images.original.url //img태그의 src값 지정
        elem.className = 'container-image' //css파일의 .container-image 디자인 적용
        resultArea.appendChild(elem) //resultArea에 img 태그 삽입
    })
}
```

검색한 값을 바탕으로 검색이 이루어지도록 함수 `searchAndPush`를 추가한다.

```javascript
button.addEventListener('click', e => {
    // console.log(`click 됐어요: ${inputArea.value}`)
    searchAndPush(inputArea.value)
})

inputArea.addEventListener('keydown', e => {
    if (e.keyCode === 13) {
        // console.log(`Enter 쳤어요: ${inputArea.value}`)
        searchAndPush(inputArea.value)
    }
})

const searchAndPush = (keyword) => {
    const API_KEY = 'm70jiv4KpdsmCelE47R0DvVEhV35xYcY' //이상태로 github에 올리지 마
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`
    
    const GiphyAPICall = new XMLHttpRequest()
    GiphyAPICall.open('GET', URL) //http method, url을 넣어줌
    GiphyAPICall.send() //요청을 보냄
    
    //응답이 제대로 왔을 때의 event를 'load'라고 함
    GiphyAPICall.addEventListener('load', e => {
        const parsedData = JSON.parse(e.target.response)
        pushToDOM(parsedData)
    }) 
}
```



## Asynchronous

python 코드

```python
from time import sleep

def sleep_3s():
    print("3초 쉬자.")
    sleep(3)
    print("3초 지났다.")

print("시작")
sleep_3s()
print("종료")

>>>시작
>>>3초 쉬자
>>>3초 지났다.
>>>종료
```

JS 코드

```javascript
const nothing = () => {
    console.log('3초 끝남')
}

console.log('start')
setTimeout(nothing, 3000)
console.log('end')

>>>start
>>>end
>>>3초 끝남
```



python은 synchronous 하면서 blocking 성격을 가지는 코드이다. 코드가 순차적으로 진행된다.

**반면, JS는 부분적으로 asynchronous하여 순서를 지키지 않는다. (non-blocking)**

- 기본적으로는 동기적, 부분적으로만 비동기적.
- 비동기함수는 잘 handling 해줘야 한다. (callstack이 받아놓고, eventloop가 알려준다.)

- 동기적으로 사용하고 싶다면, **Callback**을 잘 사용하자. (함수 안에 함수)
  - 예를 들어, `addEventListner` 내부의 callback 함수는 event가 발생했을 때에 동작한다.

- 출생이 *브라우저 조작* 이기 때문에 이렇게 만들어 진 것.



```javascript
const sleep = sec => {
    const startTime = new Date().getTime()
    while(new Date().getTime() - startTime < sec*1000){ //sec은 초단위, getTime()은 ms
    }
}
>>> sleep(10)
```

위 코드를 실행시, 10초동안 이용자는 브라우저를 통해 아무것도 할 수 없어(while문이 동작하는 순간 다른 일을 할 수 없게 됨). 이런 일을 방지하기 위해 JS는 비동기적으로 설계된 것. 특정 작업이 다른 작업을 막는 것을 예방하는게 목적.

과거 브라우저는 single-thread였음(tab이 한 개). 그 안에서 오래 걸리는 코드가 존재하면 다른 기능이 실행되지 못했음. 이럴 경우 사용자 경험이 좋지 않으므로, **종료를 예측할 수 없는(혹은 시간이 아주 오래 걸리는; XMLHttpRequest, addEventListner 등)** 작업이 있는 경우 비동기적으로 작동한다. 

JS는 싱글 스레드인가? X

- JS가 실행되는 context가 싱글 스레드인 것. (내부적으로는 멀티 스레드)

- 코드가 진행되는 방식이 싱글 스레드인 것.

  - 싱글 스레드라고 생각하고 프로그래밍 할 수 있도록 만들어진 것

  - 프로그래머 입장에서 편해짐

- 실행되는 맥락을 잘 추상화했기 때문에 JS가 각광받는 것 (멀티 스레딩 언어보다 좋다!)

  비동기적 기능때문에 서버 단에서도(node.js) 성능이 좋다고 인정받음.

JS는 비동기 언어다? X

- 부분적으로 비동기적인 함수가 존재할 뿐이다.



**비동기 함수를 어떻게 처리할까?**

- **Callback**

  비동기적함수는 `비동기적함수( , function)`의 형태를 가짐. 여기서 `function`이 Callback 함수.

  code readability가 매우 떨어짐.

- **Promise**

  JS에서 공식적으로 제공하는 비동기 함수 처리방법

- **async/wait**



파일 Read/Write는 대표적인 비동기 함수

```javascript
const fs = require('fs') // file system library import (node js)

console.log('파일 읽기 전')

fs.readFile('me.json', () => {
    console.log('파일 읽기')
})

console.log('끝')
>>>
파일 읽기 전
끝
파일 읽기
```

파이썬 스타일로 변수에 저장해도 읽을 수 없다. (비동기 함수이기 때문)

```javascript
let content = ''
content = fs.readFile('me.json', () => {
    console.log('파일 읽기')
})
console.log(content)
>>>
undefined
파일 읽기
```

Callback 함수를 이용한 `readFile` 처리. Callback 함수의 parameter로 `err`, `data`를 전달한다.

```javascript
fs.readFile('me.json', (err, data) => {
    console.log(JSON.parse(data))
})
```

Callback함수 안에 다른 함수를 nesting 가능하다. (이걸 반복하다 보면 가독성이 매우 떨어져)

```javascript
fs.readFile('me.json', (err, data) => {
    setTimeout(() => {
        console.log(JSON.parse(data))
    }, 10000)
})
```

`readFileSync`는 `readFile`과 달리 동기적으로 파일을 읽을 수 있는 함수다.

```javascript
let content = ''
content = fs.readFileSync('me.json')
console.log(JSON.parse(content))

>>>
{
  name: 'john',
  appleProducts: { macBook: '2018pro', iPad: '2018pro' }
}
```





**axios (python requests같은 역할. XMLHttpRequest와 유사)** [링크](https://github.com/axios/axios)

axios cdn으로 추가

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

`XMLHttpRequest`는 절차가 복잡 (매번 request 때마다 객체를 만들고, event listner로 핸들링 해줘야 했다.)

`open()` `send()` `addEventListner()`의 세 단계를 하나로 줄여주는 것이 `axios`.

`axios`도 **비동기 함수**이지만, callback을 사용하지 않는다. 대신, `then`이라는 메소드로 핸들링 할 수 있도록 만들어놨다.

```javascript
const URL = 'https://dog.ceo/api/breeds/image/random'
axios.get(URL).then(function(){})
```

여기서 `axios.get(URL)`은 `Promise` 객체를 반환한다. (python의 `request` 객체와 유사)

`Promise` 객체는 다음에 행할 행동을 정해줘야 한다.

```javascript
const URL = 'https://dog.ceo/api/breeds/image/random'

// 1. Pormise 객체 (resolved)
const result = axios.get(URL)

// 2. Promise 객체를 까보기 위해서 .then()으로 메소드를 연결
result.then((result) => {
    console.log(result.data.message)
})

// 위 과정을 한 줄로
axios.get(URL)
    .then(result => console.log(result.data.message)) //이미지 url 출력
```



Dog 버튼을 눌렀을 때 랜덤한 개 사진이 출력되도록 하자

```javascript
const URL = 'https://dog.ceo/api/breeds/image/random'
const dogButton = document.querySelector('#dog')
const catButton = document.querySelector('#cat')

const getDogAndPush = () => {
    axios.get(URL)
        .then(response => {
            // showroom 초기화
            document.querySelector('#showroom').innerHTML = ''
            // <body> 아래에 <img> 태그 삽입
            const imgURL = response.data.message
            const imgTag = document.createElement('img')
            imgTag.src = imgURL
            document.querySelector('#showroom').appendChild(imgTag)
        })
}

//버튼이 눌려졌을 때 (getDogAndPush)
// 1. axios -> dog 사진 요청
// 2. <body> 아래에 <img> 받아온 사진 보여주기
dogButton.addEventListener('click', getDogAndPush)
```

이미지 크기 고정하기

```html
<style>
    img {
        width: 300px;
        height: 300px;
    }
</style>
```



---



## JS로 좋아요 기능 구현하기

Django를 backend로 사용하고, DTL을 통해 Javascript를 사용해보자

*RECAP* 프로젝트를 재활용한다.

*eventListner의 callback function은 arrow function을 쓰지 않는다.*

- *this*의 binding이 달라지기 때문.

```html
<!--[articles] > [detail.html] -->

<!--button 안에 현재 article의 pk값을 숨겨놓자 -->
{% if user in article.like_users.all %}
<button data-id="{{ article.pk }}" class="btn btn-outline-primary" id="like-button">
    좋아요 취소
</button>
{% else %}
<button data-id="{{ article.pk }}" class="btn btn-primary" id="like-button">
    좋아요
</button>
{% endif %}
```

`button` 태그 안에 `data-id`라는 값을 지정해 주면, `dataset`이라는 영역에 `id`라는 key를 가진 값이 저장된다. `e.target.dataset`에 들어가면, `id`라는 이름을 가진 영역에 `articke.pk`가 들어가있다. 여기서 `target`은 `likeButton`을 의미한다. (`data-hi = "{{ article.title }}"` 을 `button` 태그 안에 입력할 경우, `dataset` 영역 안 `hi`라는 키값에 `article.title`이 저장된다.)

`axios.get()`명령을 통해 돌아온 response(`Promise` 객체)는 html 페이지를 담고 있을 것. (views.py의 like 함수가 article 상세보기 페이지를 반환하므로) like 함수가 JSON을 반환할 수 있도록 views.py를 바꿔보자

```python
# [articles]>[views.py]>like
from django.http import Http404, HttpResponse, JsonResponse
#python response를 Json형식으로 바꿔주는게 JsonResponse
def like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True
    context = {
        'liked': liked,
        'count': article.like_users.count(),
    }
    return JsonResponse(context)
```

좋아요 버튼 변경을 위한 스크립트

```javascript
<script>
    // 좋아요 버튼을 클릭하면, 좋아요 DB를 업데이트하고, 버튼을 바꾼다. (EventListner 사용)
    const likeButton = document.querySelector('#like-button')
likeButton.addEventListener('click', function(e){
    // 좋아요 DB를 업데이트 == articles/:id/like url로 요청을 보냄
    // console.log(e.target.dataset.id)  //target = likeButton, data로 시작하는 모든 값들은 dataset에 저장됨
    const articleId = e.target.dataset.id
    axios.get(`/articles/${articleId}/like/`)
        .then(response => {
        // console.log(response.data.liked) //false or true
        // 버튼을 '좋아요 취소'로 변경
        if (response.data.liked) {
            // 테두리 변경 (클래스 삭제, 추가)
            e.target.classList.remove('btn-primary')
            e.target.classList.add('btn-outline-primary')
            // 내용 변경
            e.target.innerText = '좋아요 취소'
        } else {
            e.target.classList.remove('btn-outline-primary')
            e.target.classList.add('btn-primary')
            e.target.innerText = '좋아요'
        }
    })
})
</script>
```

좋아요 카운트 변경을 위한 스크립트

```html
<!--[articles] > [detail.html] -->
    <p>좋아요: <span id="like-count">{{ article.like_users.count }}</span></p>
```

```javascript
const likeCount = document.querySelector('#like-count')
...
              // 카운트 반영
              likeCount.innerText = response.data.count
```

좋아요 누른 사람의 명단을 위한 스크립트


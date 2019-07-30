# SSAFY Web (190729)

## Intro to Web service

### trello

- Kanban 식 프로젝트 관리 (agile)
- To do / Doing / Done 3 개의 리스트 관리

---

### Web

- 모든 서비스에는 주문(요청)과 응답이 존재한다.
- 요청의 종류 2가지 : 1. 줘라(Get), 2. 받아라(Post)
- **우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.**
- 웹 교과서: https://developer.mozilla.org/ko/

### Static web

- 특정한 요청에 대해 동적으로 대답하지 못하는 웹 서비스의 형태.
- **어떠한 요청**이 들어오더라도 **동일한 컨텐츠**를 보여준다.
- 예시) 일반적인 블로그, 포트폴리오 페이지
- 오늘 강의 목표는 static web을 만들어 github pages에 업로드하는 것.

도메인 구매 -> 'aws route 53' or 'godaddy'

### 면접 단골질문

사용자가 Daum.net을 입력했을 때, 어떤 일이 이루어지는가?

### Web developer extension

웹 개발자를 위한 필수 크롬 익스텐션

### 접근성(Accessibility)

어떻게 해야 더 많은 사람들이 더 쉽게 웹에 접근할 수 있을까? 최근의 핫이슈

네이버 웹 접근성 페이지 참조(https://accessibility.naver.com/)

- ex) html 페이지의 `<html lang="ko">`

### 포트폴리오 페이지 만들기

- repository name -> Kuhnhee.github.io

- .../ssafycodes/portfolio/index.html

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>포트폴리오 페이지</title>
  </head>
  <body>
      <h1>나의 포트폴리오 페이지</h1>
  </body>
  </html>
  ```

- ```shell
  git init
  git add index.html
  git commit -m "first commit"
  git remote add origin https://github.com/Kuhnhee/Kuhnhee.github.io.git
  git push -u origin master
  ```

- kuhnhee.github.io에 접속하면 포트폴리오 페이지 접속 가능하다.



---

### HTML

Hypter Text Markup Language

- 웹 페이지를 작성하기 위한 역할 표시 언어

- Hyper Text를 주고받는 규칙: http
- http의 보안, 속도를 강화: https
- 왜 https가 http보다 속도가 빠른가? (https://tech.ssut.me/https-is-faster-than-http/)

#### DOCTYPE 선언부

사용하는 문서의 종류를 선언하는 부분. 보통 html을 사용

#### html 요소 `<html></html>`

HTML 문서의 최상위 요소로 문서의 root를 뜻한다. head와 body 부분으로 구분된다.

#### head 요소 `<head></head>`

- `<meta property="og:....">` 카톡 링크 걸었을 때 나타나는 대표 이미지 결정 가능 (Open graph)

#### body 요소 `<body></body>`

브라우저 화면에 나타나는 정보로 실제 내용에 해당한다.



### Tag와 DOM TREE

#### (Document *Object* Model)

html은 모든 것을 *객체*로 본다.

html 문서는 "tree"형태와 같이 *계층 구조*를 가지고 있다.

-> 검색에 용이하다.

#### Tag

- html은 2 space가 convention.
- 태그는 대소문자를 구별하지 않으나, 소문자로 작성하는게 규칙이다.
- 닫는 태그가 없는 태그도 존재한다. `<img..>`

```html
<img src="~" alt="네이버로고">
```

- img 태그에서 src의 이미지가 없을 경우, alt 값이 대신 표현된다.

- instagram의 screen reader: 인공지능을 활용, 시각장애인들을 위해 alt값으로 이미지에 대한 정보를 알려주는 시스템 -> **"접근성"** 키워드와 연관

- 태그에는 속성이 지정될 수 있다.

  ```html
  <a href="https~"/>
  ```

- 속성에는 ""를 사용하며, 공백은 사용하지 않는다.

#### DOM TREE

```html
<body>
    <h1> 웹 문서 </h1>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

- body 태그와 h1태그는 부모-자식 관계
- 태그는 중첩되어 사용 가능하다.
- h1 태그와 ul 태그는 형제 관계(sibling)

#### Semantic Tag

- `<div></div>` : 공간을 분할할 뿐 의미는 없다.(non semantice)
- header, nav, aside, section, article, footer
- html 내에서 어떠한 역할을 하는지 의미적으로 분류해 놓은 것을 semantic tag라 한다.
- **개발자 및 사용자 뿐 아니라 검색엔진 등에 *"의미 있는 정보의 그룹"*을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 의미를 가지는 캐그들을 활용하기 위한 노력이 중요하다.**

#### 검색 엔진 최적화 (SEO)

- 개발한 서비스가 검색엔진에 효과적으로 노출되도록 하는 것.

- 구글에 검색했을 때, "네이버"의 검색결과와 "멀티캠퍼스"의 검색결과를 비교해보면 차이가 명확. 구글 검색엔진이 자동적으로 해당 사이트의 정보들을 긁어올 수 있도록 하는게 중요하다.

- 페이지 빌딩 단계에서부터, SEO를 고려하는 것이 중요하다.



----

### 직접 태그 사용해보기

- vscode tab 2space로 바꾸기 (html, css파일에 대해서)

  ctrl+shift+p -> open settings(JSON)

  ```json
  {
  	...
      "[html]": {
          "editor.tabSize": 2
      },
      "[css]":{
          "editor.tabSize": 2
      }
  }
  ```

  한 번에 li 태그를 여러개 만드는 방법은 다음과 같다.

- ```html
  <!-- ol>li*4 -->
  <ol>
    <li>int</li>
    <li><em>float</em></li>	<!--글자 emphasize-->
    <li><i>complex</i></li>	<!--글자 기울이기-->
    <li><s>str</s></li>	<!--글자 중간에 줄긋기-->
  </ol>
  ```

- `<hr>`태그로 줄 긋기 가능하다.

- list의 bullet 모양 바꾸기

  ```html
  <ul style="list-style-type:circle">...</ul>
  ```

- 항목 이동 기능을 추가할 수 있다.

  ```html
  <a href="#python">파이썬</a> <a href="#web">웹</a>
  
  <section id="python">
      ...
  </section>
           
  <section id="web">
  	...
  </section>
         
  ```

- table tag를 사용해 표를 추가할 수 있다.

- ![0729_1](C:\Users\student\TIL\web\img\0729_1.jpg)

  ```html
  <style>
      table, tr, td, th {
        border:1px solid black;
      }
  </style>
  ...
  <table>
      <tr>
          <th></th>
          <th>월</th>
          <th>화</th>
          <th>수</th>
      </tr>
      <tr>
          <td>A코스</td>
          <td rowspan="2">짬뽕</td>
          <td colspan="2">초밥</td>
      </tr>
      <tr>
          <td>B코스</td>
          <td>김치찌개</td>
          <td>삼계탕</td>
      </tr>
  </table>
  ...
  ```

  




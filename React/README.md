# React 노트

> react 개발을 하며 발생했던 이슈들을 정리합니다.



## Routing 하며 props 넘기기

**목표) SourceComponent에서 링크를 통해 TargetComponent로 라우팅 할 때, 특정 값을 전달해 주고 싶다.**

 **index.js**

```js
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom';

export default class App extends Component {
  render() {
    return (
      <BrowserRouter>
				...
        <Route path="/" exact component={SourceComponent} />
        <Route path="/project/:projectId" component={TargetComponent} />
      </BrowserRouter>
    );
  }
}
```

**SourceComponent.jsx**

```jsx
import { Link } from 'react-router-dom';
...
  <Link to={`/project/${id}`}>...</Link>
```

**TargetComponent.jsx**

```jsx
export default function TargetComponent({ match }) {
  	// 전달받은 props는 match.params 안에 있다.
    const { projectId } = match.params;
}
```

참고자료: [React Router를 이용하여 component간에 props 넘겨주기](https://medium.com/@ghur2002/react-router를-이용하여-component간에-props-넘겨주기-610de3511c67)

---



## Redux로 데이터 관리하기



---



## Context로 데이터 관리하기



---



## Next.js를 사용한 SSR



---


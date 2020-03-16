# Typescript 스터디

> 참고서적: [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/)

## 개요

Typescript는 JS로 컴파일되어 실행된다.

- 따라서 TS compiler가 필요하다. 

  ```shell
  npm install -g typescript@next
  ```

  이제 `tsc` 명령어를 사용 가능하다.



**Types can be Implicit**

```ts
var foo = 123;
foo = '456'; // Error: cannot assign 'string' to 'number'
```

위와 같이 작성할 경우 이후 코드에서 `foo` 가 `string` 인지 `number` 인지 확실히 알 수 없어.



**Types can be Explicit**

annotation syntax를 통해 타입을 명시할 수 있다.

```ts
var foo: number = 123;
```

아래와 같이 입력할 경우 에러가 발생할 것.

```typescript
var foo: number = '123'; //Error: cannot assign a 'string' to 'number'
```



**Type is structural**

>  *duck typing* is a first class language construct

```ts
interface Point2D {
    x: number;
		y: number; 
}
interface Point3D {
    x: number;
    y: number;
    z: number; 
}
var point2D: Point2D = { x: 0, y: 10 }
var point3D: Point3D = { x: 0, y: 10, z: 20 }
function iTakePoint2D(point: Point2D) { /* do something */ }

iTakePoint2D(point2D); // exact match okay 
iTakePoint2D(point3D); // extra information okay 
iTakePoint2D({ x: 0 }); // Error: missing information `y`
```

위 코드에서 `iTakePoint2D` 함수는 자신이 필요로 하는 값(`x`,`y`)을 가지기만 했다면, 무엇이든 받아들일 수 있다.

---

## 목차

- [1.JavaScript](./1.JavaScript.md)
- [2.Future JavaScript](./2.Future-JavaScript.md)


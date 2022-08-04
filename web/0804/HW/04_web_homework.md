# 04_web_homework

## 1. CSS flex-direction

Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.

- row - 가로로 나열
- column - 세로로 나열
- row-reverse - 가로 거꾸로  나열
- column-reverse - 세로 거꾸로 나열

## 2. Bootstrap flex-direction

flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

- row - `flex-row`
- column - `flex-column`
- row-reverse - `flex-row-reverse`
- column-reverse - `flex-column-reverse`

## 3. align-items

align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

- flex-start - 위
- flex-end - 아래
- center - 가운데
- stretch - 컨테이너를 가득 채움
- baseline - 텍스트를 baseline에 맞춤

## 4. flex-flow

flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.  (1)번

(1) flex-direction, flex-wrap
(2) flex-direction, align-items
(3) justify-content, flex-wrap
(4) justify-content, align-items

```jsx
<div class=" (a) ">
    <div class=" (b) ">
        <div class="col- (c) - (d) "></div>
    </div>
</div>
```

## 5. Bootstrap Grid System

상단 코드에 Bootstrap Grid System을 적용시키고자한다.
(a), (b) 각각에 입력해야 할 클래스 이름을 작성하시오.

(a) = container

(b) = row

## 6. Breakpoint prefix (5번 문제 연계)

Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

1. (c) 에 들어갈 수 있는 값들과 그 값들이 가지는 의미를 작성하시오.
2. (d) 에 들어갈 수 있는 값들과 그 값들이 가지는 의미를 작성하시오.

(c) - 적지않으면 기본값 xs, sm(576이상), md(768이상), lg(992이상), xl(1200이상), xxl(1400이상)    컨테이너의 크기에 따라 그리드가 변경됨

(d) - 숫자 화면의 크기가 size 이상일 경우row칸을 차지하는 갯수
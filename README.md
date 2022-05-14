# README

## 참여자: 김범종 최인호

### 목표

+ 족보 확인할 수 있는 함수 만들기
+ 게임 진행할 수 있도록 구현
+ ai 만들기
  + 기본적인 스타일은 타이트한 플레이어로 가는 게 좋을 것 같음.
  + 블러핑을 섞을 수 있도록 구현



### 1주차

#### 주요 목표

+ git 생성 및 사용법 익히기

+ 카드 족보 구현

#### 카드 족보 구현

각각의 족보를 구현시킨 후에, 가장 족보가 높은 loyal straight flush 부터 확인을 하면서 조건을 좁혀나갔기 때문에, 낮은 족보로 갈수록 구현이 간단해졌다.



### 2주차

#### 주요 목표

+ Poker Helper 만들기

#### Poker Helper 구현

hero와 villain의 hands가 공개 되었을 때, 승패 여부를 판정할 수 있게 됨.

#### rankings 보수 작업

승패를 확인하기 위해, 각 족보에 대한 return의 양식을 통일시킴.

=> 승패 판단이 가능해짐.

#### 상대경로 import 문제

```bash
ImportError: attempted relative import with no known parent package
```

상대 경로로 ranking의 모듈을 import 하는 과정에서 부모 패키지를 찾을수 없다는 에러가 발생하여 환경 변수에 상대경로로 경로를 지정해줘서 해결함.



### 3주차

#### 주요 목표

+ betting 구현
+ bank roll 관리
+ betting까지 가능한 온전한 포커 게임기 완성!

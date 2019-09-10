# 190909 Git

`git log --oneline`

`git checkout 264a387` : head가 264a387인 커밋 순간을 확인

`git checkout master` : 원상복구



## branch

**"Branch는 일회용품이다!"**

`git branch` : 현재 가지고 있는 branch들의 정보들을 알려줌. (초록 글씨 + '*' -> 현재 내가 있는 branch)

`git branch [브랜치이름]` : 새로운 branch 생성

`git checkout [브랜치이름]` : 다른 브랜치로 이동

`git switch [브랜치이름]` : 다른 브랜치로 이동 (최신버전)

`git branch -d [브랜치이름]` : 브랜치 삭제

`git checkout -b [브랜치이름]` : 브랜치 만들면서 이동

`git switch -c [브랜치이름]` : 브랜치 만들면서 이동

- 새로 만든 branch에서 commit을 찍는 순간, 평행세계가 만들어짐

![git1](./img/git1.jpg)

- `git switch master`를 통해 master branch로 이동할 경우, 마지막에 develop branch에서 커밋한 내용이 사라지는 것을 확인할 수 있다. (다시 `git switch develop`할 경우 복구됨)

`git merge [브랜치이름]` : **현재 Branch**에서 특정 Branch를 병합 (지금 내가 어느 Branch에 있는지 알고 있는 것이 중요하다. 합병의 주인이 누구인지를 항상 remind하자)



- git 시각화 툴 

  https://git-school.github.io/visualizing-git/



### 병합의 3가지 시나리오

1. fast forward merge

   분기되기 전 새로운 커밋이 없을 때 (줄기~ 가지 구분이 없을 때, 전부다 줄기라고 퉁치자)

   master에서 develop을 branch해서 develop branch에만 커밋을 해 왔을 때, (master의 내용은 변화가 없음) master의 head를 develop의 head로 옮기는 병합과정

![ffmerge1](./img/ffmerge1.jpg)

병합 전

![ffmerge2](./img/ffmerge2.jpg)

병합 후



2. auto merge

   master, 분기된 branch 각각 커밋이 있을 때. master에서 작업한 작업물과 branch의 작업물을 그대로 합쳐도 아무런 충돌(conflict)이 발생하지 않을 때 하는 병합.

![automerge1](./img/automerge1.jpg)

병합 전

![automerge2](./img/automerge2.jpg)

병합 후

![automerge3](./img/automerge3.jpg)



3. merge with conflict

   master에서 작업한 작업물과 branch의 작업물에 충돌이 발생할 때

![conflict1](./img/conflict1.jpg)

- vscode가 지원하는 기능을 이용하여 변경사항을 적용할 수 있지만, 아래와 같이 텍스트 편집기로 직접 열어 필요한 내용만 남길 수 도 있다.

![conflict2](./img/conflict2.jpg)

- conflict 해결 후 `add`, `commit` 하면 merge 완료
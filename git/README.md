# Git

`git log --oneline`

`git checkout 264a387` : head가 264a387인 커밋 순간을 확인

`git checkout master` :  master branch로 이동



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
  
  https://learngitbranching.js.org/



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

- merge [브랜치이름] : [브랜치이름]을 병합한다.
- rebase [브랜치이름] : ~를 [브랜치이름]에 갖다붙인다.



## Pull Request scenario (Fork & Pull request)

1. A가 repository 생성, 프로젝트 push
2. B가 A의 repository fork
3. fork한 repository를 B의 local에 clone
4. B가 clone한 프로젝트를 수정하여 fork했던 repository에 push
5. B : github > [fork한 repository] > [New pull request]
6. A : pull request 승인



- 수정된 프로젝트를 B가 받아가는 방법

  ```bash
  git remote -v
  git remote add upstream https://github.com/sspy21/nhaeng.git
  git remote -v #upstream 추가된 것 확인
  git fetch upstream
  git merge upstream/master
  
  git add .
  git commit -m "fix merge conflict"
  ```



## Branching & Pull request

- 현실 협업 모델
- contributor들이 각각 clone한 뒤, branch를 만들어 프로젝트를 수정.
- 수정된 프로젝트를 push ` git push origin kuhnhee`
- 내가 수정한 branch에 대한 pull request 요청
- reviewer들이 pull request를 검증



- merge된 master를 나의 local로 받아오기 (**반드시 master에서 해야한다.**)

  ```bash
  git checkout master
  git pull
  git branch -d kuhnhee
  ```

- 다시 내 이름으로 branch를 깐 뒤, 프로젝트 작업

  ```bash
  git checkout -b kuhnhee
  ```

  



## 추가 정리

**Scenario 1**

- Github에 프로젝트 저장소가 있고, A, B, C가 프로젝트에 참여한다 가정

- A, B, C는 각각 프로젝트를 fork한 뒤, 이를 자신의 로컬로 clone하여 작업한다.

  - 이 경우, A가 fork해 소유하고 있는 저장소는 origin이며, 프로젝트 저장소는 upstream이 된다.

- 작업한 branch를 origin에 push한다.

  ```bash
  $ git push origin [branch-name]
  ```

- uptream에 PR를 올린다.



**Scenario 2**

- Github에 프로젝트 저장소가 있고, A, B, C가 프로젝트에 참여한다 가정

- A, B, C는 프로젝트를 자신의 로컬로 clone한 뒤, 작업한다.

  - 이 경우, Github의 프로젝트 저장소는 origin이자 upstream이다.

- 작업한 branch를 push한다.

  ```bash 
  $ git push origin [branch-name]
  ```

- PR을 올린다.



**Branch 전략**

- master: 배포 단계

- develop: 개발 단계

  - develop에서 feature별로 branch를 파생시킨다.

  -  `feat/[feature-name]` 의 형태를 자주 사용한다.

  - naming convention은 kebab case를 따른다.

    e.g) feat/login-page, feat/kanban-task-component

  - feature개발이 완료되면 develop branch로 merge한다.



**실패한 branch 전략 예시**

- master: 배포 단계
- develop: 개발 단계
  - **fe** : fe개발 관련 feature branch들의 중간 베이스
    - `feat/[fe-feature-name]`
  - **be** : be개발 관련 feature branch들의 중간 베이스
    - `feat/[be-feature-name]`

> 왜 좋지 않은 전략인가?
>
> fe 관련 feature들을 개발하여 fe branch로 merge하고, be 관련 feature들을 개발하여 be branch로 merge하기까지는 문제 없었다.
>
> 하지만 개발 중간 단계에서 fe branch와 be branch를 develop branch로 merge하여 코드의 동작을 확인한 뒤, 이후 개발을 이어 나갈 때 문제가 발생한다.
>
> 다시 fe branch로 돌아간 뒤, 각각의 feature branch로 돌아가 작업을 이어 나가야 하는데, 이 모든 branch들을 develop branch로 rebase 시켜야 한다.(그렇지 않을 경우 be branch의 코드들이 반영되지 않은 상태이므로 제대로된 테스트를 할 수 없다.) 이후에도 매번 테스트를 할때마다 be, fe branch를 합쳐야 하고, 모든 branch의 rebase까지 해야하므로 여간 귀찮은 일이 아니다.
>
> 결론) develop branch에서 fe, be 구분 없이 feature 단위로만 branch를 파생시키는 게 가장 효율적이라고 생각된다.



**Branch tree 한 눈에 보고싶어?**

- Sourcetree 추천
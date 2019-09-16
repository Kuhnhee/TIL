# python basic (190725)

## git, 협업

- 협업 시 github 관리자를 정해야 함. (초기 프로젝트는 한 사람이 생성)
- README.md 파일을 생성
- 동시에 작업하지 않는다는 단순한 시나리오



#### 팀장 시점

1. ```shell
   mkdir git_practice
   cd git_practice
   code .
   
   README.md 생성
   ```

2. ```
   (README.md)
   # 협업 프로젝트
   github 'README.md' 같이 만들기
   ```

3. ```
   github organization 생성하여 팀원 초대
   repository 생성
   ```

4. ```shell
   git init
   git add .
   git commit -m "start collab project"
   git remote add origin https://github.com/ssafy-artists/collabo.git
   git push
   ```

- 팀원이 해당 repository를 clone하여 파일을 수정한 뒤, add/commit/push



#### 컨플릭트

- 동일한 내용을 동시에 수정하고자 할 경우, 두 개의 버전(A가 바꾼 버전, B가 바꾼 버전) 중에서 하나를 선택해야 한다.

- 컨플릭트가 발생한 뒤 vscode로 파일을 열어보면, 어떤 버전으로 결정할지 옵션을 선택할 수 있다.
- 컨플릭트 발생할만한 요소가 없다면, 두 사람이 동시에 작업 했더라도 auto-merge한다.



#### 협업 시 지켜야 할 것

- **동일 file을 동시간에 건들지 않는다.**
- **소통**
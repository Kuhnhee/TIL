## Visitor Pattern

**의도**

연산을 적용할 원소의 클래스를 변경하지 않고도 새로운 연산을 정의할 수 있다.

**동기**

여러 노드 시스템에 대하여, 유지보수&변경 작업을 편리하게 하기 위함.

방문자 패턴을 사용하면 두 개의 클래스 계통이 정의된다. 하나는 연산이 적용되는 원소에 대한 **클래스 계통**이고, 또 하나는 그 원소에 대해 적용할 연산을 정의하는 **방문자 클래스 계통**이다. 새로운 연산을 추가하려면 방문자 클래스 계통에 새로운 서브 c클래스를 추가하면 된다. 

 

- 적용 전

  ```python
  class Node:
      def TypeCheck()
      def GenerateCode()
      def PrettyPrint()
      
  class VariableRefNode extends Node:
      def TypeCheck()
      def GenerateCode()
      def PrettyPrint()
      
  class AssignmentNode extends Node:
      def TypeCheck()
      def GenerateCode()
      def PrettyPrint()
  ```

- 적용 후
  Visitor 클래스

  ```python
  class NodeVisitor:
      def VisitAssignment(AssignmentNode)
      def VisitVariableRef(VariableRefNode)
      
  class TypecheckingVisitor extends NodeVisitor:
      def VisitAssignment(AssignmentNode)
      def VisitVariableRef(VariableRefNode)
      
  class CodeGeneratingVisitor extends NodeVisitor:
      def VisitAssignment(AssignmentNode)
      def VisitVariableRef(VariableRefNode)
  ```


  Node 클래스

  ```python
  class Node:
      def Accept(NodeVisitor)
  
  class AssignmentNode extends Node:
      def Accept(NodeVisitor v):
  		v.VisitAssignment(this)
          
  class VariableRefNode extends Node:
      def Accept(NodeVisitor v):
          v.VisitVariableRef(this)
  ```

  

**활용성**

방문자 패턴은 다음과 같은 경우 사용한다.

- 다른 인터페이스를 가진 클래스가 객체 구조에 포함되어 있으며, 구체 클래스에 따라 달라진 연산을 이들 클래스의 객체에 대해 수행하고자 할 때

- 각각 특징이 있고, 관련되지 않은 많은 연산이 한 객체 구조에 속해있는 객체들에 대해 수행될 필요가 있으며, 연산으로 클래스들을 "더럽히고" 싶지 않을 때. Visitor 클래스는 관련된 모든 연산을 하나의 클래스 안에다 정의해 놓음으로써 관련된 연산이 함께 있을 수 있게 해 준다.

  어떤 객체 구조가 많은 응용프로그램으로 공유될 때, Visitor 클래스를 사용하면 이 객체 구조가 필요한 응용프로그램에만 연산을 둘 수 있다.

- 객체 구조가 자주 변경될 때는 해당 연산을 클래스에 정의하는 것이 비용 절감에 효과적이다.



**결과(장단점)**

1. 새로운 연산을 쉽게 추가한다.

   복잡한 객체를 구성하는 요소에 속한 연산을 쉽게 추가할 수 있다. 새로운 방문자를 추가하면 객체 구조에 대한 새로운 연산을 추가한 것이 된다. (이 때, 객체 구조는 계층적 형태를 띈다.) 방문자 없이 필요한 기능이 여러 클래스에 분산되어 있다면, 새로운 연산 추가를 위해 각 관련 클래스를 모두 수정해야 한다.

   

2. 방문자를 통해 관련된 연산들을 한 군데로 모으고 관련되지 않은 연산을 떼어낼 수 있다.

   서로 간 연관성이 있는(관계된) 행동들이 객체 구조를 정의하는 클래스에 분산되지 않게 되며, 방문자 클래스로 모이게 된다. 관련되지 않은 행동들은 그 자신의 방문자 서브클래스로 나뉜다. 이는 원소를 정의하는 클래스 및 방문자에 정의되어 있는 알고리즘 모두를 간단하게 합니다. 알고리즘에 특화된 자료 구조는 어떤 것이든 방문자 속에 숨겨집니다.

   

3. 새로운 ConcreteElement(=Node를 상속받은 클래스)를 추가하기 어렵다.

   방문자 패턴을 사용할 경우, Element(=Node) 클래스에 대한 새로운 서브클래스를 추가하기 어렵다. 새로운 ConcreteElement를 생성할 때마다, Visitor 클래스에 대한 새로운 추상 연산 및 모든 하위 ConcreteVisitor(=Visitor 클래스를 상속받은 클래스) 클래스에 그 연산에 대응하는 구현을 제공해야 한다.

   따라서 방문자 패턴을 적용하기 전, **객체의 구조에 적용될 알고리즘이 자주 변하는가**, 혹은 객체 **구조를 구성하는 클래스에 변화가 자주 발생하는가**를 고려해야 한다.

   

4. 반복자 패턴의 반복자와 달리, 방문하는 클래스의 제약이 없다.

   방문자는 동일한 부모 클래스가 없는 객체들도 방문할 수 있으며, Visitor 인터페이스에 어떤 객체의 타입이라도 추가할 수 있다.

   

5. 상태를 누적할 수 있다.

   객체 구조 내 각 원소들을 방문하며서 상태를 누적할 수 있다. 만일 방문자가 없다면, 이 상태는 별도의 다른 인자로서 순회를 담당하는 연산에 전달된다든지, 아니면 전역 변수로 존재해야 한다.

   

6. 데이터 은닉을 깰 수 있다.

   방문자 패턴은 ConcreteElement(=Node) 인터페이스가 방문자에게 필요한 작업을 수행시킬 만큼 충분히 강력하다는 가정을 전제로 한다. 이에 따라, 이 패턴을 사용할 경우 원소의 내부 상태에 접근하는데 필요한 연산들을 모두 공개 인터페이스로 만들 수밖에 없는데, 이는 **캡슐화 전략을 위배**하는 것이다.



**이슈**

- **이중 디스패치**

  실행되는 연산이 요청의 종류와 두 수신자의 타입에 따라 달라진다.

- 객체 구조 순회의 책임은 누가?





- 참고자료: [GoF의 디자인 패턴](http://www.yes24.com/Product/Goods/17525598)
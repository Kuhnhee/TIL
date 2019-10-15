## Visitor Pattern

**의도**

연산을 적용할 원소의 클래스를 변경하지 않고도 새로운 연산을 정의할 수 있다.

**동기**

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













- 참고자료: [GoF의 디자인 패턴](http://www.yes24.com/Product/Goods/17525598)
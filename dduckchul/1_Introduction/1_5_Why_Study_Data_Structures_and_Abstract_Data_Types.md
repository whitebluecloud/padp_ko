# 원문
## 1.5. Why Study Data Structures and Abstract Data Types?
* To manage the complexity of problems and the problem-solving process, computer scientists use abstractions to allow them to focus on the “big picture” without getting lost in the details. By creating models of the problem domain, we are able to utilize a better and more efficient problem-solving process. These models allow us to describe the data that our algorithms will manipulate in a much more consistent way with respect to the problem itself.

* Earlier, we referred to procedural abstraction as a process that hides the details of a particular function to allow the user or client to view it at a very high level. We now turn our attention to a similar idea, that of data abstraction. An abstract data type, sometimes abbreviated ADT, is a logical description of how we view the data and the operations that are allowed without regard to how they will be implemented. This means that we are concerned only with what the data is representing and not with how it will eventually be constructed. By providing this level of abstraction, we are creating an encapsulation around the data. The idea is that by encapsulating the details of the implementation, we are hiding them from the user’s view. This is called information hiding.

* Figure 2 shows a picture of what an abstract data type is and how it operates. The user interacts with the interface, using the operations that have been specified by the abstract data type. The abstract data type is the shell that the user interacts with. The implementation is hidden one level deeper. The user is not concerned with the details of the implementation.

* The implementation of an abstract data type, often referred to as a data structure, will require that we provide a physical view of the data using some collection of programming constructs and primitive data types. As we discussed earlier, the separation of these two perspectives will allow us to define the complex data models for our problems without giving any indication as to the details of how the model will actually be built. This provides an implementation-independent view of the data. Since there will usually be many different ways to implement an abstract data type, this implementation independence allows the programmer to switch the details of the implementation without changing the way the user of the data interacts with it. The user can remain focused on the problem-solving process.

# 번역
## 1.5. 왜 데이터 구조와 추상 데이터 타입을 공부해야 하는가?
* 문제의 복잡성과 문제 해결 과정을 다루기 위해, 컴퓨터 과학자들은 추상화를 사용하여 세부 사항은 놓치지 않으며, 중요한 로직에 집중 할 수 있도록 한다.  
도메인의 문제를 해결하는 모델을 만들때, 우리는 좀더 좋고 효율적인 방법을 사용할 수 있다.  
이러한 모델은 우리의 알고리즘이 문제해결과 관련해 일관적으로 우리의 데이터를 다룰것이다.  

* 앞서, 우리는 절차적인 추상화가 특정 펑션의 세부사항을 숨김으로써, 유저나 클라이언트가 펑션을 높은 레벨에서 다룰수 있다는걸 알았다.  
이제 우리는 비슷한 아이디어인 데이터 추상화에 대해 알아볼 때이다.  
추상 데이터 타입 (ADT라고 줄여 말하기도 함) 은 우리가 어떻게 데이터를 보는가, 그것이 어떻게 구현되었느냐와는 관련없이 동작하는 것에 대한 논리적인 설명이다.  
추상 데이터 타입은 이것이 어떻게 구성되어있느냐는 신경 쓸 필요없고, 어떻게 데이터가 보여지고 있느냐만 신경쓰면 된다는것을 의미한다.  
이 추상화 단계를 제공함으로써, 데이터를 캡슐화 할수 있다.  
이 아이디어는 구현하는 세부사항을 캡슐화 함으로써, 유저 측면에서 그것들을 보이지 않게 감추는 것이다.  
이것은 *Information Hiding* 이라고 불린다.  

* 2번은 추상화 데이터의 그림과 어떻게 동작하는지에 대해 나타내고있다.  
유저는 인터페이스와 상호작용하고, 추상 데이터 타입에 의해 명시된 오퍼레이션을 사용한다.  
추상 데이터 타입은 유저가 상호작용하는 껍질과 같다.  
구현체는 한 단계 깊게 숨겨져있다. 유저는 이 구현체의 동작에 대해선 신경쓰지 않아도 된다.  

* 추상 데이터의 구현은 종종 데이터 구조라고 일컬어 진다.  
데이터 구조는 프로그래밍 구조체와 원시 데이터 타입으로 이뤄져 있다.  
이전에 다루었던것 처럼, 두 관점이 분리된 것들은 문제를 해결하기 위해 좀더 복잡한 데이터 모델을 만들수 있도록 도와준다.
(이 모델이 실제로 어떻게 구현 되었는지는 알지 못해도 상관없기 때문)  
이것은 데이터의 측면에서 구현 독립적임을 제공해 준다.  
추상 데이터 타입을 구현하는 데는 수많은 방법이 있으므로, 구현 독립적인것은 프로그래머가 유저의 상호작용과는 상관없이 내부 구현을 마음대로 변경할 수 있게 해준다.  
따라서, 사용자는 문제 해결 과정에만 집중 할 수 있다.
# 원문
## 1.3. What Is Computer Science?
* Computer science is often difficult to define. This is probably due to the unfortunate use of the word “computer” in the name. As you are perhaps aware, computer science is not simply the study of computers. Although computers play an important supporting role as a tool in the discipline, they are just that–tools.

* Computer science is the study of problems, problem-solving, and the solutions that come out of the problem-solving process. Given a problem, a computer scientist’s goal is to develop an algorithm, a step-by-step list of instructions for solving any instance of the problem that might arise. Algorithms are finite processes that if followed will solve the problem. Algorithms are solutions.

* Computer science can be thought of as the study of algorithms. However, we must be careful to include the fact that some problems may not have a solution. Although proving this statement is beyond the scope of this text, the fact that some problems cannot be solved is important for those who study computer science. We can fully define computer science, then, by including both types of problems and stating that computer science is the study of solutions to problems as well as the study of problems with no solutions.

* It is also very common to include the word computable when describing problems and solutions. We say that a problem is computable if an algorithm exists for solving it. An alternative definition for computer science, then, is to say that computer science is the study of problems that are and that are not computable, the study of the existence and the nonexistence of algorithms. In any case, you will note that the word “computer” did not come up at all. Solutions are considered independent from the machine.

* Computer science, as it pertains to the problem-solving process itself, is also the study of abstraction. Abstraction allows us to view the problem and solution in such a way as to separate the so-called logical and physical perspectives. The basic idea is familiar to us in a common example.

* Consider the automobile that you may have driven to school or work today. As a driver, a user of the car, you have certain interactions that take place in order to utilize the car for its intended purpose. You get in, insert the key, start the car, shift, brake, accelerate, and steer in order to drive. From an abstraction point of view, we can say that you are seeing the logical perspective of the automobile. You are using the functions provided by the car designers for the purpose of transporting you from one location to another. These functions are sometimes also referred to as the interface.

* On the other hand, the mechanic who must repair your automobile takes a very different point of view. She not only knows how to drive but must know all of the details necessary to carry out all the functions that we take for granted. She needs to understand how the engine works, how the transmission shifts gears, how temperature is controlled, and so on. This is known as the physical perspective, the details that take place “under the hood.”

* The same thing happens when we use computers. Most people use computers to write documents, send and receive email, surf the web, play music, store images, and play games without any knowledge of the details that take place to allow those types of applications to work. They view computers from a logical or user perspective. Computer scientists, programmers, technology support staff, and system administrators take a very different view of the computer. They must know the details of how operating systems work, how network protocols are configured, and how to code various scripts that control function. They must be able to control the low-level details that a user simply assumes.

* The common point for both of these examples is that the user of the abstraction, sometimes also called the client, does not need to know the details as long as the user is aware of the way the interface works. This interface is the way we as users communicate with the underlying complexities of the implementation. As another example of abstraction, consider the Python math module. Once we import the module, we can perform computations such as

```python
import math
math.sqrt(16)
4.0
```

* This is an example of procedural abstraction. We do not necessarily know how the square root is being calculated, but we know what the function is called and how to use it. If we perform the import correctly, we can assume that the function will provide us with the correct results. We know that someone implemented a solution to the square root problem but we only need to know how to use it. This is sometimes referred to as a “black box” view of a process. We simply describe the interface: the name of the function, what is needed (the parameters), and what will be returned. The details are hidden inside (see Figure 1).

# 번역
## 1.3. 컴퓨터 과학이란?
* 컴퓨터 과학은 종종 정의하기 어렵다. 이것은 아마 컴퓨터 과학 이란 이름에서 _"컴퓨터"_ 의 잘못된 사용때문 일 것이다.  
당신도 아마 주의하고 있드시, 컴퓨터 과학은 단순히 컴퓨터에 대한 연구만 있는것이 아니다.  
비록 컴퓨터가 이 과목에서 중요한 부분을 담당하고있지만, 이것은 단지 도구일 뿐이다.

* 컴퓨터 과학은 문제, 문제해결, 문제해결 과정에서 나오는 해결법들을 다루는 학문이다.  
주어진 문제를 해결하기 위해 컴퓨터 과학자들의 목표는 *알고리즘*을 개발하는 것이다.  
알고리즘은 어떤 문제가 일어나던지 문제를 해결할수 있는, 단계별로 나눠진 명령들의 리스트이다.  
알고리즘은 그것을 따르게 되면 문제를 해결할수 있는 유한한 과정들이다. 알고리즘이 해결책인 것이다.  

* 컴퓨터 과학은 알고리즘의 학문이라고 생각할수도 있다.  
그러나, 우리는 몇몇 해결책이 없는 문제들도 있다는것을 유의해야한다.  
비록 이것을 증명하는 것이 여기 주제에서 벗어나 있지만, 컴퓨터 과학을 공부하는 사람들에게 어떤 문제들은 풀 수 없다는것이 중요할떄도 있다.  
우리는 컴퓨터 과학이 문제를 해결하는 학문이자, 해결책이 없는 문제들을 연구하는 학문이라는 것으로 정의할 수 있다.  

* 컴퓨팅 할수있다라는 단어를 문제를 설명할때나 해결책에서 넣는것은 흔한일이다.  
우리는 문제를 컴퓨팅 할 수 있다라는 단어를 그것을 푸는 알고리즘이 있을때 사용한다.  
컴퓨터 과학에 대한 다른 정의로는, 알고리즘이 존재하는지 존재하지 않는지에 대한 학문이다.  
어느 쪽이든, 당신은 _컴퓨터_ 라는 단어가 나오지 않는다는것을 알수 있을것이다.  
해결책들은 기계와는 독립적인 것이라고 생각된다.  

* 컴퓨터 과학은, 추상화에 대한 학문이라고도 할 수 있다.  
추상화는 문제와 해결책을 논리적이고, 물리적인 측면에서 분리되게 볼 수 있게 해준다.
이 기초적인 개념은 친숙한 예제를 들어 설명할 수 있다.  

* 당신이 출근이나 통학에 사용했던 차를 생각해봐라.  
운전자로써, 당신은 차를 의도대로 사용하기 위해 몇몇 상호작용을 했을것이다.  
운전을 하기위해 당신은 차를 타고, 키를 꼽고, 시동을걸고, 변속, 브레이크, 엑셀, 스티어링을 한다.  
추상화의 관점에서는, 이것을 자동차를 논리적인 관점에서 바라보고 있다고 할 수 있다.  
당신은 자동차 디자이너들이 운송수단으로써 제공하는 기능을 사용하고있다.  
이러한 기능들은 *인터페이스*라는 이름으로 언급된다. 

* 반면에, 당신의 차를 고쳐야하는 정비공들은 다른 관점을 가지고 있다.  
그녀는 운전 하는 것 뿐만 아니라, 움직이기 위한 모든 자세한 기능들을 알아햐 한다.  
그녀는 엔진이 어떻게 동작하는지, 트랜스미션이 어떻게 기어를 변속하는지, 어떻게 온도가 조절되는지 등을 모두 알아야 한다.  
이 후드 아래서 벌어지는 자세한 일들을 물리적인 관점이라고 말할수 있다. 

* 동일한 일들이 컴퓨터를 사용할 때 일어난다.  
대부분의 사람들은 컴퓨터를 문서 작성하거나, 이메일 주고받기, 인터넷서핑, 음악감상, 이미지 저장, 게임하기 등을 하는데 사용한다.  
이런 어플리케이션들을 사용하는데는 정확히 어떤 일이 일어나는지에 대한 지식이 없어도 실행할 수 있다.  
일반 사용자들은 컴퓨터를 논리적인 측면 (사용자 측면) 에서 바라본다.  
컴퓨터 과학자들, 프로그래머, 기술 지원 스탭, 시스템 관리자들은 매우 다른 측면에서 컴퓨터를 바라본다.  
그들은 반드시 OS가 어떻게 작동하는지, 네트워크 프로토콜이 어떻게 구성되어있는지, 코드 기능들을 어떻게 제어할지 들을 알아야 한다.  
그들은 유저가 단순히 생각한대로 사용하도록 로우 레벨에서 컨트롤 되어야 한다.

* 두 예제들의 공통된 점은, 추상화를 사용하는 사람들 (클라이언트) 은 인터페이스가 어떻게 동작하는지 알 필요가 없다는 것이다.  
인터페이스는 복잡한 부분을 감춘채 유저와 커뮤니케이션 할수 있는 방법이다.  
추상화의 다른 예제로, 파이썬의 *math* 모듈을 들수 있다.  
우리가 모듈을 임포트하면 아래와 같은 계산을 할 수 있다.  

```python
import math
math.sqrt(16)
4.0
```

* 이것은 절차적인 추상화의 예이다. 우리는 제곱근이 어떻게 계산되는지는 알 필요가 없지만, 펑션이 어떤것인지, 어떻게 사용하는지 정도는 알아야 한다.  
우리는 펑션이 정확한 결과를 줄것이라고 예상한다.  
우리는 누군가가 제곱근 문제를 사용할 수 있게 만들었다는 것을 알고있기 때문에, 어떻게 쓰는지만 알면 된다.  
이것은 과정이 블랙박스 처리 되었다고 말해진다.  
*우리는 인터페이스란 펑션의 이름, 어떤 파라미터가 필요한지, 그리고 어떤값이 리턴되는지로 설명 할 수 있다*
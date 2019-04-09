# Problem Solving with Algorithms and Data Structures using Python
1. 소개
  - [Part1. 목표](#part1)
  - [Part2. 시작하기](#part2)
  - [Part3. 컴퓨터과학이란](#part3)
  - [Part4. 프로그래밍이란](#part4)
  - [Part5. 데이터 구조와 추상화 데이터타입을 학습해야하는 이유](#part5)
  - [Part6. 알고리즘을 학습해야하는 이유](#part6)
  - [Part7. 파이썬 기본](#part7)
  - [Part8. 데이터를 활용해 시작하기](#part8)
    - [1.8.1. 기본형 데이터 타입](#part8-1)
    - [1.8.2. 컬렉션 데이터 타입](#part8-2)

## Part1
### 목표
  To review the ideas of computer science, programming, and problem-solving.
  ~~~
  컴퓨터 과학, 프로그래밍, 문제해결의 생각을 검토하기 위함
  ~~~
  To understand abstraction and the role it plays in the problem-solving process.
  ~~~
  추상화를 이해하고 그 역할(문제해결과정에서의 수행)을 이해하기 위함
  ~~~
  To understand and implement the notion of an abstract data type.
  ~~~
  추상적인 자료형의 개념을 이해하고 구현하기 위함
  ~~~
  To review the Python programming language.
  ~~~
  파이썬 프로그래밍 언어를 검토하기 위함
  ~~~

## Part2
### 시작하기
  The way we think about programming has undergone many changes in the years since the first electronic computers required patch cables and switches to convey instructions from human to machine.
  ~~~
  프로그래밍에 관해 우리가 생각하는 방식은 수년간 많은 변화들을 겪어왔다. 최초의 전자 컴퓨터가 패치 케이블과 스위치들(사람으로부터 기계까지 명령을 전달하는)을 필요한 이후로
  ~~~
  As is the case with many aspects of society, changes in computing technology provide computer scientists with a growing number of tools and platforms on which to practice their craft.
  ~~~
  사회의 여러측면들에서 그러듯, 컴퓨팅 기술에서의 변화들은 컴퓨터 과학자들에게 더욱 많아지는 도구와 플랫폼(그들의 기술을 연습할 수 있는)들을 제공한다.
  ~~~
  Advances such as faster processors, high-speed networks, and large memory capacities have created a spiral of complexity through which computer scientists must navigate.
  ~~~
  더욱 빠른 프로세서들, 높은 속도의 네트워크 그리고 큰 메모리 용량들과 같은 발전은 복잡성의 소용돌이(컴퓨터 과학자들이 반드시 찾아야 하는)를 만들어왔다.
  ~~~
  Throughout all of this rapid evolution, a number of basic principles have remained constant. The science of computing is concerned with using computers to solve problems.

  You have no doubt spent considerable time learning the basics of problem-solving and hopefully feel confident in your ability to take a problem statement and develop a solution. You have also learned that writing computer programs is often hard. The complexity of large problems and the corresponding complexity of the solutions can tend to overshadow the fundamental ideas related to the problem-solving process.

  This chapter emphasizes two important areas for the rest of the text. First, it reviews the framework within which computer science and the study of algorithms and data structures must fit, in particular, the reasons why we need to study these topics and how understanding these topics helps us to become better problem solvers. Second, we review the Python programming language. Although we cannot provide a detailed, exhaustive reference, we will give examples and explanations for the basic constructs and ideas that will occur throughout the remaining chapters.

## Part8
### 1.8 Getting Started with Data (데이터를 활용해 시작하기)
  We stated above that Python supports the object-oriented programming paradigm.
  ~~~
  우리는 위에서 파이썬이 객체지향프로그래밍 패러다임을 지지한다고 말했다.
  ~~~
  This means that Python considers data to be the focal point of the problem-solving process.
  ~~~
  이것은 파이썬이 데이터가 문제해결과정의 초점으로 여겨져야한다는 것을 의미한다.
  ~~~
  In Python, as well as in any other object-oriented programming language, we define a class to be a description of what the data look like (the state) and what the data can do (the behavior).
  ~~~
  파이썬에서뿐만 아니라, 어떤 다른 객체 지향 프로그래밍 언어에서도, 우리는 한 클래스를 데이터가 어떤건지 (상태) 그리고 그 데이터로 무엇을 할 수 있는지(동작)에 대한 설명이 되도록 정의한다.
  ~~~
  Classes are analogous to abstract data types because a user of a class only sees the state and behavior of a data item. Data items are called objects in the object-oriented paradigm. An object is an instance of a class.
  ~~~
  클래스는 추상적인 데이터 타입들과 유사하다 왜냐하면 클래스의 사용자는 오직 데이터 항목에 대한 상태와 동작을 보기 때문이다. 데이터 항목들은 객체 지향 패러다임에서 오브젝트(객쳬)라고 불린다.
  하나의 오브젝트는 한 클래스에 대한 하나의 인스턴스이다.
  ~~~
#### part8-1
#### 1.8.1 Built-in Atomic Data Types (기본형 데이터 타입)
We will begin our review by considering the atomic data types.
~~~
우리는 기본형 데이터 타입들을 고려함으로써 검토를 시작할 것이다.
~~~
Python has two main built-in numeric classes that implement the integer and floating point data types.
~~~
파이썬은 2개의 주된 내장된 숫자 클래스들(정수와 부동 소수점 데이터 타입들을 구현한)을 가지고 있다.
~~~
These Python classes are called int and float. The standard arithmetic operations, +, -, *, /, and ** (exponentiation), can be used with parentheses forcing the order of operations away from normal operator precedence.
~~~
이런 파이썬 클래스들은 int와 float라 불린다.
표준 산술 연산들 +, -, *, / 그리고 **(거듭제곱)은 괄호들(표준 연산자 우선순위로 부터 벗어나도록 하는)와 함께 사용될 수 있습니다.
~~~
Other very useful operations are the remainder (modulo) operator, %, and integer division, //.
~~~
다른 매우 유용한 연산자들은 나머지 연산자, %, 그리고 정수 나누기, // 이다.
~~~
Note that when two integers are divided, the result is a floating point.
~~~
두 정수를 나눌 때, 그 결과는 부동 소수점이라는 것을 주의하라
~~~
The integer division operator returns the integer portion of the quotient by truncating any fractional part.
~~~
정수 나누기 연산자는 일정 분수 부분을 잘라냄으로써 정수부분의 몫을 리턴한다.
~~~
The boolean data type, implemented as the Python bool class, will be quite useful for representing truth values. The possible state values for a boolean object are True and False with the standard boolean operators, and, or, and not.
~~~
파이썬 bool 클래스로써 구현된 boolean 데이터 유형은 진리 값을 표현하는데에 있어 꽤 유용할 것이다.
boolean 객체에 대한 가능한 상태 값들은 표준 boolean 연산자들(and, or, not)과 함께 True와 False 이다
~~~
Boolean data objects are also used as results for comparison operators such as equality (==) and greater than (>)
~~~
Boolean 데이터 객체는 또한 ==, > 과 같은 비교 연산자들의 결과로써 사용된다.
~~~
In addition, relational operators and logical operators can be combined together to form complex logical questions. [Table1](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-relational) shows the relational and logical operators with examples shown in the session that follows.
~~~
게다가, 관계 연산자와 논리 연산자는 복잡한 논리 질문을 만들 수 있도록 서로 결합할 수 있다.
Table 1에서는 다음 세션에서 보여지는 예제들과 함께 관계 연산자와 논리 연사자를 보여준다
~~~
Identifiers are used in programming languages as names. In Python, identifiers start with a letter or an underscore (_), are case sensitive, and can be of any length.
~~~
식별자는 프로그래밍 언어에서 이름으로써 사용된다.
파이썬에서 식별자는 문자 또는 밑줄(_)로 시작하고 대소문자를 구분하고 어떤 길이도 될 수 있다.
~~~
Remember that it is always a good idea to use names that convey meaning so that your program code is easier to read and understand.
~~~
기억해라! 너의 프로그램 코드가 읽고 이해하기에 더욱 쉽도록 의미를 전달하는 이름을 사용하는 것이 항상 좋은 생각이라는 것을
~~~
A Python variable is created when a name is used for the first time on the left-hand side of an assignment statement. Assignment statements provide a way to associate a name with a value. The variable will hold a reference to a piece of data and not the data itself. Consider the following session:
~~~
파이썬 변수는 생성된다. (이름이 대입문의 왼쪽에 처음으로 사용되어질때)
대입문은 이름과 값을 연관시키는 방법을 제공한다
변수는 데이터 자체가 아닌 데이터의 조각에 대한 참조를 담고 있을 것이다.
~~~
The assignment statement theSum = 0 creates a variable called theSum and lets it hold the reference to the data object 0 (see Figure 3). In general, the right-hand side of the assignment statement is evaluated and a reference to the resulting data object is “assigned” to the name on the left-hand side.
~~~
대입문 (theSum = 0 )은 theSum 이라는 변수를 생성한다. 그리고 그것이 데이터 객체 0에 대한 참조를 유지하도록 한다. (그림 3) 일반적으로 대입문의 오른쪽은 값이 매겨지고 결과 데이터 객체에 대한 참조가 왼쪽의 이름에 “할당” 된다.
~~~
At this point in our example, the type of the variable is integer as that is the type of the data currently being referred to by theSum. If the type of the data changes (see Figure 4), as shown above with the boolean value True, so does the type of the variable (theSum is now of the type boolean).
~~~
우리의 예에서 이 시점에, 변수의 유형은 정수이고 theSum에 의해 현재 참조되어지는 데이터의 유형이다.
만약 그 데이터의 타입이 위에서 보여진 boolean 값 true로 바뀐다면, 변수의 유형도 바뀐다.(theSum은 이제 boolean 타입이다)
~~~
The assignment statement changes the reference being held by the variable. This is a dynamic characteristic of Python. The same variable can refer to many different types of data.
~~~
대입문은 변수에 의해 보유되어진 참조를 바꾼다.
이것은 파이썬의 역동적인 특징이다.
동일한 변수는 많은 다른 유형들의 데이터를 참조할 수 있다.
~~~

#### part8-2
#### 1.8.2 Built-in Atomic Data Types (기본형 데이터 타입)

In addition to the numeric and boolean classes, Python has a number of very powerful built-in collection classes. Lists, strings, and tuples are ordered collections that are very similar in general structure but have specific differences that must be understood for them to be used properly. Sets and dictionaries are unordered collections.
~~~
숫자, boolean 클래스 외에도 파이썬은 많은 매우 파워풀한 내장 컬랙션 클래스들을 가지고 있다.
Lists, String, 튜플은 정돈된 수집들이다 (일반적인 구조에서는 매우 유사하지만 특정한 차이들을 가지고 있는)
(적절히 사용되어지기 위해서 그것들을 반드시 이해해야만 하는) Set과 Dictionary는 정돈되지 않은 수집이다.
~~~
A list is an ordered collection of zero or more references to Python data objects. Lists are written as comma-delimited values enclosed in square brackets. The empty list is simply [ ].
~~~
List는 파이썬 데이터 객체들에 대한 0개 또는 그 이상의 참조의 정돈된 수집이다.
List는 대괄호로 쌓여진 콤마로 구분된 값으로 쓰여진다.
빈 List는 단순히 []이다.
~~~
Lists are heterogeneous, meaning that the data objects need not all be from the same class and the collection can be assigned to a variable as below. The following fragment shows a variety of Python data objects in a list.
~~~
List는 여러 다른 종류로 이뤄지고, 이것은 데이터 객체가 모두 같은 클래스일 필요가 없으며, 수집이 아래처럼 변수에 할당될 수 있음을 의미한다.
다음 부분은 한 리스트에서 다양한 파이썬 데이터 객체를 보여준다.

>>> [1,3,True,6.5]
[1, 3, True, 6.5]
>>> myList = [1,3,True,6.5]
>>> myList
[1, 3, True, 6.5]
~~~
Note that when Python evaluates a list, the list itself is returned. However, in order to remember the list for later processing, its reference needs to be assigned to a variable.
~~~
주목해라 파이썬이 list를 평가할 때, 그 list는 그자체로 리턴된다. 하지만, 나중에 처리하기위해 그 리스트를 기억하기 위해서, 그 자체의 참조가 변수에 할당되어질 필요가 있다.
~~~
Since lists are considered to be sequentially ordered, they support a number of operations that can be applied to any Python sequence. [Table2](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-sequence) reviews these operations and the following session gives examples of their use.
~~~
list는 순차적으로 정돈되어지는 것으로 여겨지기때문에, list는 파이썬 순서에 적용될 수 있는 다양한 연산자를 지원한다.
테이블2는 이러한 연산자들을 검토하고 다음 세션은 그것들의 사용의 예들을 준다.
~~~
Note that the indices for lists (sequences) start counting with 0. The slice operation, myList[1:3], returns a list of items starting with the item indexed by 1 up to but not including the item indexed by 3.
~~~
List에 대한 인덱스(시퀀스)는 0으로 시작한다는 것을 주의하라.
slice 연산자, myList[1:3]은 1까지 인덱스된 항목으로 시작하는 항목의 list는 리턴하지만, 3에 의해 인덱스된 항목은 포함하지 않는다.
~~~
Sometimes, you will want to initialize a list. This can quickly be accomplished by using repetition. For example,
~~~
때때로, 너는 리스트를 초기화하기를 원할것이다.
이것은 반복을 사용함으로써 빠르게 이뤄질 수 있다.

>>> myList = [0] * 6
>>> myList
[0, 0, 0, 0, 0, 0]
~~~
One very important aside relating to the repetition operator is that the result is a repetition of references to the data objects in the sequence. This can best be seen by considering the following session:
~~~
반복 연산자와 관련된 한가지 가장 중요한 면은 그 결과는 그 순서 안의 데이터 객체에 대한 참조의 반복이다.
이것은 다음 세션을 고려해봄으로써 가장 잘 알수있다.

myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)

-> 결과
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
~~~
The variable A holds a collection of three references to the original list called myList. Note that a change to one element of myList shows up in all three occurrences in A.
~~~
변수 A는 myList라 불리는 기존의 List에 대한 3개의 참조의 수집을 담고 있다.
myList의 한 요소의 변경이 A 안의 3가지 모든 경우에 나타난다는 것을 유의해라
~~~
Lists support a number of methods that will be used to build data structures. [Table3](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-listmethods) provides a summary. Examples of their use follow.
~~~
List는 데이터 구조를 만드는데 사용되어지는 많은 메소드를 지원한다.
[테이블3]은 요약을 제공한다.
이거들의 사용 예는 다음과 같다.
~~~

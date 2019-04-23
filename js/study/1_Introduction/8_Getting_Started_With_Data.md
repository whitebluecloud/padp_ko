# Problem Solving with Algorithms and Data Structures using Python
  - [Part8. 데이터를 활용해 시작하기](#part8)
    - [1.8.1. 기본형 데이터 타입](#part8-1)
    - [1.8.2. 컬렉션 데이터 타입](#part8-2)

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

myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

->
[1024, 3, True, 6.5, False]
[1024, 3, 4.5, True, 6.5, False]
False
[1024, 3, 4.5, True, 6.5]
3
[1024, 4.5, True, 6.5]
[1024, 4.5, 6.5]
[4.5, 6.5, 1024]
[1024, 6.5, 4.5]
1
2
[1024, 4.5]
[4.5]
~~~

You can see that some of the methods, such as pop, return a value and also modify the list. Others, such as reverse, simply modify the list with no return value. pop will default to the end of the list but can also remove and return a specific item. The index range starting from 0 is again used for these methods. You should also notice the familiar “dot” notation for asking an object to invoke a method.myList.append(False) can be read as “ask the object myList to perform its append method and send it the value False.” Even simple data objects such as integers can invoke methods in this way.
~~~
너는 pop과 같은 일부 메소드들이 값을 리턴하고 또한 리스트를 수정하는 것을 볼 수 있다. 반대로 다른것들은 단순히 값을 리턴하지 않고 리스트를 수정한다.
pop은 리스트의 끝으로 디폴트되지만, 특정 항목을 제거하고 리턴할 수 있다.
이러한 방법에 대해서 0부터 시작하는 인덱스 범위가 다시 사용된다. 너는 또한 method.myList.append(False)를 호출하는 객체를 요청하는 것에 대해 익숙한 “dot(점)” 표기법을 “객체 myList에 추가 메소드를 수행하여 False로 보내도록 요청”으로 읽을 수 있다.
정수와 같은 단순한 데이터 객체라도 이런 식으로 메소드를 호출 할 수 있다.

>>> (54).__add__(21)
75
>>>
~~~
In this fragment we are asking the integer object 54 to execute its add method (called __add__ in Python) and passing it 21 as the value to add. The result is the sum, 75. Of course, we usually write this as 54+21. We will say much more about these methods later in this section.
~~~
이러한 부분에서 우리는 정수 객체 54에 add 메소드 (파이썬에서 __add__라 불리는)를 실행하고, 그것을 21을 더하기 위한 값으로 전달하도록 요청한다. 그 결과는 합 75이다.
물론 우리는 보통 이것을 54+21로서 쓴다.
우리는 이 섹션의 나중에 이러한 방법들에 대해서 더 많은 것을 이야기할 것이다.
~~~
One common Python function that is often discussed in conjunction with lists is the range function. range produces a range object that represents a sequence of values. By using the list function, it is possible to see the value of the range object as a list. This is illustrated below.
~~~
종종 list와 함께 묶여 논의되는 하나의 흔한 파이썬 함수는 범위 함수이다.
범위는 일련의 값들을 나타내는 범위 객체를 생성한다.
리스트 함수를 사용함으로써, 범위 객체의 값을 리스트로써 볼 수있다.
이것은 아래에 설명되어진다.

>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(5,10)
range(5, 10)
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(5,10,2))
[5, 7, 9]
>>> list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>>
~~~
The range object represents a sequence of integers. By default, it will start with 0. If you provide more parameters, it will start and end at particular points and can even skip items. In our first example,range(10), the sequence starts with 0 and goes up to but does not include 10. In our second example, range(5,10) starts at 5 and goes up to but not including 10. range(5,10,2) performs similarly but skips by twos (again, 10 is not included).
~~~
범위 객체는 일련의 정수를 나타낸다.
기본적으로 그것은 0에서 시작할 것이다.
만약 너가 더 많은 파라미터들을 제공한다면, 그것은 특정한 지점에서 시작하고 끝날 것이다. 그리고 심지어 항목을 뛰어 넘을 수 있다.
우리의 첫번째에서, range(10), 순서는 0에서 시작하고 10으로 올라가지만 10으로 포함하지 않는다.
우리의 두번째에서 range(5,10)는 5에서 시작하고 10까지 올라가지만 10은 포함하지 않는다.
range(5,10,2)는 유사하게 수행하지만, 2단계씩 스킵한다(10은 포함하지 않음)
~~~
Strings are sequential collections of zero or more letters, numbers and other symbols. We call these letters, numbers and other symbols characters. Literal string values are differentiated from identifiers by using quotation marks (either single or double).
~~~
String은 0개 또는 그 이상의 문자, 숫자 그리고 다른 기호들의 순차적인 수집들이다.
우리는 이러한 문자, 숫자 그리고 다른 기호 문자들을 부른다.
문자열 값은 따옴표(단일이나 이중)를 사용함으로써 식별자와 구별된다.

>>> "David"
'David'
>>> myName = "David"
>>> myName[3]
'i'
>>> myName*2
'DavidDavid'
>>> len(myName)
5
>>>
~~~
Since strings are sequences, all of the sequence operations described above work as you would expect. In addition, strings have a number of methods, some of which are shown in [Table4](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-stringmethods). For example,
~~~
String은 순서가 있기 때문에, 모든 순서 연산 (위에서 설명된)은 너가 예상한것처럼 작동한다.
게다가 String은 다양한 메소드를 가지는데, 그중 일부는 Table4에 보여진다. 예를들면,

>>> myName
'David'
>>> myName.upper()
'DAVID'
>>> myName.center(10)
'  David   '
>>> myName.find('v')
2
>>> myName.split('v')
['Da', 'id']
~~~
Of these, split will be very useful for processing data. split will take a string and return a list of strings using the split character as a division point. In the example, v is the division point. If no division is specified, the split method looks for whitespace characters such as tab, newline and space.
~~~
이중에서, split은 데이터를 처리에 있어 매우 유용할 것이다.
split은 문자열을 가지고 분할지점으로써 분할 문자를 사용하여 문자열 목록을 리턴할 것이다.
예에서는 v가 분할지점이다. 만약 분할 지점이 지정되어있지 않다면, split 메소드는 탭, 엔터 그리고 스페이스와 같은 공백문자를 검색한다.
~~~
A major difference between lists and strings is that lists can be modified while strings cannot. This is referred to as mutability. Lists are mutable; strings are immutable. For example, you can change an item in a list by using indexing and assignment. With a string that change is not allowed.
~~~
리스트와 문자열의 주요한 차이점은 리스트는 수정될 수 있다. 문자열이 수정할 수 없는 동안에
이것은 변하기 쉬움으로써 언급된다.
리스트는 변형이 가능하고, 문자열은 변형이 불가능하다.
예를들어, 너는 리스트에서 인덱싱과 할당을 사용함으로써 항목을 바꿀 수 있다.
문자열 변경은 허용되지 않는다.

>>> myList
[1, 3, True, 6.5]
>>> myList[0]=2**10
>>> myList
[1024, 3, True, 6.5]
>>>
>>> myName
'David'
>>> myName[0]='X'

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in -toplevel-
    myName[0]='X'
TypeError: object doesn't support item assignment
>>>
~~~
Tuples are very similar to lists in that they are heterogeneous sequences of data. The difference is that a tuple is immutable, like a string. A tuple cannot be changed. Tuples are written as comma-delimited values enclosed in parentheses. As sequences, they can use any operation described above. For example,
~~~
튜플은 여러종류로 이루어진 데이터의 순서라는 점에서 리스트와 매우 유사하다.
차이점은 튜블은 문자열처럼 불변이다.
튜플은 바뀔수 없다. 튜플은 괄호로 묶여진 쉼표값으로써 쓰여진다.
순서로써, 그것들은 위에서 설명한 어떠한 연산자도 사용할 수 있다. 예를 들면,

>>> myTuple = (2,True,4.96)
>>> myTuple
(2, True, 4.96)
>>> len(myTuple)
3
>>> myTuple[0]
2
>>> myTuple * 3
(2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
>>> myTuple[0:2]
(2, True)
>>>
~~~
However, if you try to change an item in a tuple, you will get an error. Note that the error message provides location and reason for the problem.
~~~
하지만, 만약 너가 튜플에서 항목을 바꾸려고 한다면, 너는 에러를 받을 것이다. 오류 메시지는 문제에 대한 위치와 이유를 제공한다는 것을 유념하라

>>> myTuple[1]=False

Traceback (most recent call last):
  File "<pyshell#137>", line 1, in -toplevel-
    myTuple[1]=False
TypeError: object doesn't support item assignment
>>>
~~~
A set is an unordered collection of zero or more immutable Python data objects. Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces. The empty set is represented by set(). Sets are heterogeneous, and the collection can be assigned to a variable as below.
~~~
Set은 0개 또는 그 이상의 불변의 파이썬 데이터 객체의 순서 없는 수집이다. Set는 중복을 허용하지 않고 중괄호 안에 묶여있는 콤마로 구분된 값으로 쓰여진다.
빈 Set은 set()로 표현되어진다.
Set은 여러 다른 종류로 이루어지며, 수집은 아래와 같이 변수에 할당할 수 있다.

>>> {3,6,"cat",4.5,False}
{False, 4.5, 3, 6, 'cat'}
>>> mySet = {3,6,"cat",4.5,False}
>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>>
~~~
Even though sets are not considered to be sequential, they do support a few of the familiar operations presented earlier. [Table 5](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-setops) reviews these operations and the following session gives examples of their use.
~~~
Set이 순차적으로 간주되지 않음에도 불구하고, 그것들은 앞에서 제시한 몇몇 친숙한 연산자들을 지원한다.
테이블5는 이런 연산자들을 리뷰하고 다음 세션에서 그것들의 사용에 대한 예제를 제공한다.

>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>> len(mySet)
5
>>> False in mySet
True
>>> "dog" in mySet
False
>>>
~~~
Sets support a number of methods that should be familiar to those who have worked with them in a mathematics setting. [Ta[ble6](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-setmethods) provides a summary. Examples of their use follow. Note that union,intersection, issubset, and difference all have operators that can be used as well.
~~~
Set은 수학적인 설정에서 그것들을 함께 작업한 사람들에게 친숙해야 하는 다양한 메소드들을 지원한다.
Table6은 요약을 제공한다.
그것들의 사용의 예는 다음과 같다.
union, intersection, issubset 그리고 difference 모두 사용할 수 있는 연산자를 가지고 있음을 유의해라

>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>> yourSet = {99,3,100}
>>> mySet.union(yourSet)
{False, 4.5, 3, 100, 6, 'cat', 99}
>>> mySet | yourSet
{False, 4.5, 3, 100, 6, 'cat', 99}
>>> mySet.intersection(yourSet)
{3}
>>> mySet & yourSet
{3}
>>> mySet.difference(yourSet)
{False, 4.5, 6, 'cat'}
>>> mySet - yourSet
{False, 4.5, 6, 'cat'}
>>> {3,100}.issubset(yourSet)
True
>>> {3,100}<=yourSet
True
>>> mySet.add("house")
>>> mySet
{False, 4.5, 3, 6, 'house', 'cat'}
>>> mySet.remove(4.5)
>>> mySet
{False, 3, 6, 'house', 'cat'}
>>> mySet.pop()
False
>>> mySet
{3, 6, 'house', 'cat'}
>>> mySet.clear()
>>> mySet
set()
>>>
~~~
Our final Python collection is an unordered structure called a dictionary. Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. This key-value pair is typically written as key:value. Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. For example,
~~~
우리의 마지막 파이썬 컬렉션은 순서가 없는 구조물이라 불리는 Dictionary이다.
Dictionary는 키와 값으로 구성된 쌍의 수집이다.
이러한 키-값 쌍은 일반적으로 키:값으로써 쓰여진다.
Dictionary는 중괄호로 묶여진 키:값 쌍으로 콤마로 구분되어져있다. 예를 들면,

>>> capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
>>> capitals
{'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
>>>
~~~
We can manipulate a dictionary by accessing a value via its key or by adding another key-value pair. The syntax for access looks much like a sequence access except that instead of using the index of the item we use the key value. To add a new value is similar.
~~~
우리는 dictionary를 키로 접근하거나 다른 키-값 쌍을 추가함으로써 조작할 수 있다.
접근을 위한 구문은 순차접근과 매우 유사하다 (우리가 키 값을 사용하는 항목의 색을 사용하는 대신 그것을 제외하고)
새 값을 추가하는 것은 유사하다.

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)

->
DesMoines
{'Iowa': 'DesMoines', 'Wisconsin': 'Madison', 'Utah': 'SaltLakeCity'}
4
DesMoines  is the capital of  Iowa
Madison  is the capital of  Wisconsin
SaltLakeCity  is the capital of  Utah
Sacramento  is the capital of  California
~~~
It is important to note that the dictionary is maintained in no particular order with respect to the keys. The first pair added ('Utah': 'SaltLakeCity') was placed first in the dictionary and the second pair added ('California': 'Sacramento') was placed last. The placement of a key is dependent on the idea of “hashing,” which will be explained in more detail in Chapter 4. We also show the length function performing the same role as with previous collections.
~~~
키와 관련하여 Dictionary는 특정한 순서로 유지되지 않는다는 것을 유의하는게 중요하다.
추가된 첫 번째 쌍 ('Utah': 'SaltLakeCity’)는 dictionary에서 1위를, 추가된 두 번째 쌍 ('California': 'Sacramento') 는 마지막에 놓여졌다.
키의 배치는 해싱의 개념에 달려있고, 이 개념은 4장에서 더 자세히 설명될 것이다.
또한 이전의 컬렉션과 함께 동일한 역할을 수행하는 length 함수를 보여준다.
~~~
Dictionaries have both methods and operators. [Table7](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-dictopers) and [Table8](http://interactivepython.org/courselib/static/pythonds/Introduction/GettingStartedwithData.html#tab-dictmethods) describe them, and the session shows them in action. The keys, values, and items methods all return objects that contain the values of interest. You can use the list function to convert them to lists. You will also see that there are two variations on the get method. If the key is not present in the dictionary, get will return None. However, a second, optional parameter can specify a return value instead.
~~~
dictionary는 메소드와 연산자 둘다 가지고 있다.
테이블7, 테이블8은 모두 그것을 설명하고 세션은 그 행동을 보여준다.
키, 값, 항목 메소드 모두 객체(관심값?)를 리턴한다.
너는 그것들을 리스트로 바꾸기 위해서 리스트 함수를 사용할 수 있다.
너는 또한 get 메소드에 2가지 변형이 있다는 것을 알 것이다.
만약 키가 dictionary에 없다면, get은 none을 리턴한다.
하지만 두번째 선택적 파라미터는 리턴 값을 지정할 수 있다.

>>> phoneext={'david':1410,'brad':1137}
>>> phoneext
{'brad': 1137, 'david': 1410}
>>> phoneext.keys()
dict_keys(['brad', 'david'])
>>> list(phoneext.keys())
['brad', 'david']
>>> phoneext.values()
dict_values([1137, 1410])
>>> list(phoneext.values())
[1137, 1410]
>>> phoneext.items()
dict_items([('brad', 1137), ('david', 1410)])
>>> list(phoneext.items())
[('brad', 1137), ('david', 1410)]
>>> phoneext.get("kent")
>>> phoneext.get("kent","NO ENTRY")
'NO ENTRY'
>>>
~~~

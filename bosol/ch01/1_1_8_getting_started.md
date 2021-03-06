1.8. Getting Started with Data
=============
* We stated above that Python supports the object-oriented programming paradigm. 
- 파이썬은 객체지향프로그래밍 패러다임을 지원한다고 위에 언급했다.
* This means that Python considers data to be the focal point of the problem-solving process. 
- 이 의미는 파이썬은 데이터가 문제해결과정의 초점이 된다는 것을 고려한다.
* In Python, as well as in any other object-oriented programming language, we define a class to be a description of what the data look like (the state) and what the data can do (the behavior). 
- 파이썬과 다른 객체지형 프로그래밍 언어에서 class가 어떤 형태인지 어떤 역할을 하는지에 대한 설명을 보다 잘 정의한다.
* Classes are analogous to abstract data types because a user of a class only sees the state and behavior of a data item. 
- 클래스에 유저는 데이터 아이템의 상태와 행동을 오직 볼수만있기때문에 클래스들은 추상데이터 타입과 유사하다.
* Data items are called objects in the object-oriented paradigm. 
- 객체지향 패러다임에서 데이터 아이템들은 오브젝트로 불린다.
* An object is an instance of a class.
- 하나의 오브젝트는 클래스의 하나의 인스턴스이다.

1.8.1. Built-in Atomic Data Types
=============

* We will begin our review by considering the atomic data types. 
- 우리는 원자데이터 유형을 고려하여 리뷰를 시작했다.
* Python has two main built-in numeric classes that implement the integer and floating point data types. 
- 파이썬은 정수형과 실수형 포인트 데이터 유형을 구현하는 2개의 내장 숫자 클래스들을 갖고 있다.  
* These Python classes are called int and float. 
- 이 파이썬 클래스들은 int와 float으로 불린다.
* The standard arithmetic operations, +, -, *, /, and ** (exponentiation), can be used with parentheses forcing the order of operations away from normal operator precedence. 
- 표준 산수 연산자들은 +,-,*,/, **(지수화),  괄호와 함께 사용하면 일반적인 상위 연산보다 멀리떨어져서 연산의 순서를 강제할 수 있다.
* Other very useful operations are the remainder (modulo) operator, %, and integer division, //. 
- 다른 아주 유용한 연산들은 나머지 연산 % , 그리고 정수형 나누기 //
* Note that when two integers are divided, the result is a floating point. 
- 유의사항은 2개의 정수를 나눌때 결과값은 실수형 이다.
* The integer division operator returns the integer portion of the quotient by truncating any fractional part.
- 정수형 나누기 연산은 결과로 정수값의 일부 분수 부분을 버린다.
* The boolean data type, implemented as the Python bool class, will be quite useful for representing truth values. 
- 파이썬 bool 클래스로 이행된  boolean 데이터 유형은, 사실값을 표현하기에 아주 유용할 것이다.
* The possible state values for a boolean object are True and False with the standard boolean operators, and, or, and not.
- boolean 객체의 가능한 상태 값은  표준 boolean 연산, and, or, and not과 함께 True와 False 이다.
* Boolean data objects are also used as results for comparison operators such as equality (==) and greater than (>). 
- Boolean 데이터 객체들은 또한 동등(==)과 크기(>) 비교 연산 결과로써 유용하다.
* In addition, relational operators and logical operators can be combined together to form complex logical questions. 
- 게다가, 관계형 연산과 논리 연산은 복잡한 논리적인 질문들을 결합 할 수있다.
* Table 1 shows the relational and logical operators with examples shown in the session that follows.
- 테이블 1은 관계와 논리 연산에 대한 예제와 함께   보여준다 

| Operation Name  | <center>Operator</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
|less than | < | Less than operator |
| greater than | \> | Greater than operator |
| less than or equal | <= | Less than or equal to operator |
| greater than or equal | \>= | Greater than or equal to operator|
| equal	| == |	Equality operator |
| not equal	| != |	Not equal operator |
| logical and |	and	| Both operands True for result to be True |
|logical or	| or |	One or the other operand is True for the result to be True |
| logical not |	not	| Negates the truth value, False becomes True, True becomes False |

* Identifiers are used in programming languages as names. 
- 식별자들은 프로그래밍언어에서 이름으로 사용된다.
* In Python, identifiers start with a letter or an underscore (_), are case sensitive, and can be of any length. 
- 파이썬에서 식별자들은 문자 혹은 밑줄로 시작되며, 대소문자를 구분하고, 길이 제한할 수 없다.
* Remember that it is always a good idea to use names that convey meaning so that your program code is easier to read and understand.
- 이것은 당신의 프로그래밍 코드가 쉽게 읽고 이해할수 있는 게 이름을 사용하는 것이 항상 좋은 아이디어라는것을 기억해라.
* A Python variable is created when a name is used for the first time on the left-hand side of an assignment statement.
-  파이썬은 첫번째 왼쪽 할당 문으로 이름을 사용할 때 변하기 쉽게 만들어졌다.
* Assignment statements provide a way to associate a name with a value. 
- 할당문은 이름과 값을 연결하는 방법을 제공한다. 
* The variable will hold a reference to a piece of data and not the data itself. 
-  변수는 데어타 자신이 아닌 데이터 조각에 대한 연결을 유지한다.
* Consider the following session:
- 다음 세션을 고려해봐라 :
```buildoutcfg
>>> theSum = 0
>>> theSum
0
>>> theSum = theSum + 1
>>> theSum
1
>>> theSum = True
>>> theSum
True
```
* The assignment statement theSum = 0 creates a variable called theSum and lets it hold the reference to the data object 0 (see Figure 3). 
- theSum = 0 할당문은 변수가 'theSum'을 호출하고 0 데이터 객체를 참조하고 유지하도록 만든다.
* In general, the right-hand side of the assignment statement is evaluated and a reference to the resulting data object is “assigned” to the name on the left-hand side. 
- 일반적으로, 오른쪽 할당문은 평가되고 결과 객체 참조에는 왼쪽에 있는 이름에 할당된다.
* At this point in our example, the type of the variable is integer as that is the type of the data currently being referred to by theSum. 
- 이 예제의 포인트는, 변수의 형태가 정수이며 theSum에 의해 언급된 데이터 유형이다.
* If the type of the data changes (see Figure 4), as shown above with the boolean value True, so does the type of the variable (theSum is now of the type boolean). 
- 만약 데이터 유형이 변경된다면, boolean 값인 True로 보여지고, 변수의 유형도 변경된다.
* The assignment statement changes the reference being held by the variable. 
- 선언문이 변수가 가리키는 참조를 변경한다.
* This is a dynamic characteristic of Python. 
- 이것은 동적 파이썬의 특성이다. 
* The same variable can refer to many different types of data.
- 같은 변수는 많은 다른 데이터 유형을 참조 할 수 있다.

1.8.2. Built-in Collection Data Types
=============

* In addition to the numeric and boolean classes, Python has a number of very powerful built-in collection classes. 
- 숫자와 boolean 클래스들 외에도, 파이썬은 많은 강력한 내장 콜렉션 클래스들을 갖고 있다.
* Lists, strings, and tuples are ordered collections that are very similar in general structure but have specific differences that must be understood for them to be used properly.
- Lists, string, tuples들은 일반적인 구조에서 매우 비슷한하지만 그것들을 정확히 사용하려면 특별하고 다른 것을 이해해야하만 하는 정렬된 콜렉션이다 
* Sets and dictionaries are unordered collections.
- Sets와 dictionaries는 순서가 없는 콜렉션들이다.
* A list is an ordered collection of zero or more references to Python data objects. 
- list는 0이나 그이상의 파이썬 데이터 객체를 참조하는 정렬된 컬렉션이다.
* Lists are written as comma-delimited values enclosed in square brackets. 
- list는 대괄호안에 콤마로 구분된 값들로 씌어진다.
* The empty list is simply [ ]. 
- 빈 list는 간단히 [] 이다.
* Lists are heterogeneous, meaning that the data objects need not all be from the same class and the collection can be assigned to a variable as below. 
- 리스트는 이기종이다. 데이터 객체가 모두 같은 클래스에 속할 필요는 없으며 콜렉션을 아래와 같이 변수에 할당 할 수 있습니다
* The following fragment shows a variety of Python data objects in a list.
- 다음 단편은 다양한 파이썬 데이터 객체가 list 안에 있는 것을 보여준다.
```buildoutcfg
>>> [1,3,True,6.5]
[1, 3, True, 6.5]
>>> myList = [1,3,True,6.5]
>>> myList
[1, 3, True, 6.5]
```
* Note that when Python evaluates a list, the list itself is returned. 
- 파이썬 리스트를 평가할때, 리스트 자체가 리턴된다.
* However, in order to remember the list for later processing, its reference needs to be assigned to a variable.
- 그러나, 나중에 처리하는 리스트를 기억하기 위해서, 이 참조는 변수에 할당할 필요가 있다.
* Since lists are considered to be sequentially ordered, they support a number of operations that can be applied to any Python sequence. 
- list는 순차적으로 정렬된 것으로 고려되기 때문에, 어떤 파이썬 시퀀스에도 적용될수 있는 많은 연산들을 제공한다.
* Table 2 reviews these operations and the following session gives examples of their use.

| Operation Name  | <center>Operator</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
|indexing |	[ ]	| Access an element of a sequence |
| concatenation	 | + | Combine sequences together |
| repetition | * | Concatenate a repeated number of times |
| membership | in |	Ask whether an item is in a sequence |
| length | len | Ask the number of items in the sequence |
| slicing |	[ : ] |	Extract a part of a sequence |

* Note that the indices for lists (sequences) start counting with 0. 
- list는 0부터 시작한다.
* The slice operation, myList[1:3], returns a list of items starting with the item indexed by 1 up to but not including the item indexed by 3.
- myList[1:3] slice 연산 myList[1:3]은 list의 인덱스 1부터 item을 포함해 시작해서  3으로 인덱스된 item을 포함하지 않은 것 까지 리턴한다.
* Sometimes, you will want to initialize a list. 
- 때때로, 초기화된 list를 원할때가 있다.
* This can quickly be accomplished by using repetition. 
- 이것은 반복을 사용해서 뛰어나고 빠르게 할 수있다.
For example,
```buildoutcfg
myList = [0] * 6
myList
[0, 0, 0, 0, 0, 0]
```
* One very important aside relating to the repetition operator is that the result is a repetition of references to the data objects in the sequence. 
- 반복 연산자와 관련하여 매우 중요한 점 중 하나는 결과가 시퀀스의 데이터 객체에 대한 참조를 반복한다는 것입니다
* This can best be seen by considering the following session:
- 다음의 세션은 가장 고려된 것으로 보여진다.
```buildoutcfg
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
```

* The variable A holds a collection of three references to the original list called myList. 
- 변수A는 MyList로 불리는 원조 list를 참조하는 3개의 콜렉션을 갖고있다.
* Note that a change to one element of myList shows up in all three occurrences in A.
- myList의 요소 하나를 변경한것이 A 안의 3개 모두에게 반영된것을 보여준다.
* Lists support a number of methods that will be used to build data structures. 
- List는 데이터 구조를 만드는데 사용되는 많은 메소드들을 제공한다.
* Table 3 provides a summary. Examples of their use follow.

| Method Name  | <center>Operator</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
| append | alist.append(item) |	Adds a new item to the end of a list |
| insert |	alist.insert(i,item) |	Inserts an item at the ith position in a list |
| pop |	alist.pop()	| Removes and returns the last item in a list |
| pop |	alist.pop(i) |	Removes and returns the ith item in a list |
| sort | alist.sort() |	Modifies a list to be sorted |
| reverse |	alist.reverse()	| Modifies a list to be in reverse order |
| del |	del alist[i] |	Deletes the item in the ith position |
| index | alist.index(item) |	Returns the index of the first occurrence of item |
| count | alist.count(item) |	Returns the number of occurrences of item |
| remove | alist.remove(item) |	Removes the first occurrence of item |

* You can see that some of the methods, such as pop, return a value and also modify the list. 
- 당신은 팝과같은 값을 리턴하고 list를 수정하는 몇몇 메소드를 볼수 있다.
* Others, such as reverse, simply modify the list with no return value. 
- reverse와 같은 다른것들은  반환 값 없이 list를 간단히 수정한다. 
* pop will default to the end of the list but can also remove and return a specific item. 
- pop은 기본적으로 list의 마지막이고 또한 삭제와 item을 반환한다.
* The index range starting from 0 is again used for these methods. 
- 이러한 메소드들을 위해 0부터 인덱스 범위의 스타팅은 재사용된다.
* You should also notice the familiar “dot” notation for asking an object to invoke a method. 
- 당신은 메소드를 호출하도록 객체에 요청하는 친숙한 dot 표기법을 주의해야한다.
* myList.append(False) can be read as “ask the object myList to perform its append method and send it the value False.” Even simple data objects such as integers can invoke methods in this way.
- myList.append (False)는 "append 메소드를 수행하여 값을 False로 보내도록 객체 myList에 요청하십시오."정수와 같은 간단한 데이터 객체조차도이 방법으로 메소드를 호출 할 수 있다.
```buildoutcfg
>>> (54).__add__(21)
75
>>>
```
* In this fragment we are asking the integer object 54 to execute its add method (called __add__ in Python) and passing it 21 as the value to add. 
- 이 파편안에서 우리는 정수 객체 54를 add 메소드를 실행하고 추가할 값으로 21을 전달하도록 요청한다.
* The result is the sum, 75. Of course, we usually write this as 54+21.
- 이 합계 결과는 75. 물론 우리는  보통 54+21 이라고 쓴다.
* We will say much more about these methods later in this section.
- 우리는 이번 섹션 이후에 이러한 메소드들에 대해서 더 많이 얘기할것이다.

* One common Python function that is often discussed in conjunction with lists is the range function. 
- list와 함께 조종 논의되는 일반적인 파이썬 함수 하나는 범위 함수다.
* range produces a range object that represents a sequence of values. 
- range는 값들의 순서를 표현하는 범위 객체를 생산하다.
* By using the list function, it is possible to see the value of the range object as a list. 
- list 함수 사용에 의해 이것은 범위함수의 값을 list로 보는것이 가능하다.
* This is illustrated below.
- 아래에 예시가 있다.
* The range object represents a sequence of integers. 
- 범위 객체는 숫자의 순서를 표현한다. 
* By default, it will start with 0.
- 기본적으로, 이것은 0으로 시작한다.
* If you provide more parameters, it will start and end at particular points and can even skip items.
-  만약 더 많은 파라미터를 제공한다면, 이것은  특이점에서 시작과 끝을 할 수 있고 items를 건너뛸 수 있다.
* In our first example, range(10), the sequence starts with 0 and goes up to but does not include 10. 
- 첫번째 예시로, range(10) 시작 순서는 0부터 10을 포함하지 않는 곳까지 간다.
* In our second example, range(5,10) starts at 5 and goes up to but not including 10.
- 두번째 예시로, range(5,10) 는 5부터 시작하여 10을 포함하지 않는 곳까지 간다.
* range(5,10,2) performs similarly but skips by twos (again, 10 is not included).
- range(5,10,2) 는 비슷하게 수행하지만 2개를 건너뛴다.
* Strings are sequential collections of zero or more letters, numbers and other symbols.
- Strings는 잇달아 일어나는 0이거나 문자, 숫자, 기타등등 컬렉션이다.  
* We call these letters, numbers and other symbols characters. 
- 우리는 이 문자, 숫자 기타등등 문자들을 호출한다.
* Literal string values are differentiated from identifiers by using quotation marks (either single or double).
- Literal string 값들은 따옴표 사용하여 식별자와 구분된다.
* Since strings are sequences, all of the sequence operations described above work as you would expect.
-  strings는 순서화되기 때문에, 위에 기술된 순서화된 모든 연산들은 예상대로 동작한다.
* In addition, strings have a number of methods, some of which are shown in Table 4. For example,
- 게다가, strings많은 메소드들을 갖고 있고, 이루는 테이블4와 같이 보여진다.
```buildoutcfg
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
```
* Of these, split will be very useful for processing data. 
- 이것들 중 split은 데이터 프로세싱하기에 매우 유용하다.  
* split will take a string and return a list of strings using the split character as a division point.
- split은 string과 분리포인트로 스플릿문자를 사용하여 strings 리스트 결과를 가져올 수 있다.
* In the example, v is the division point. If no division is specified, the split method looks for whitespace characters such as tab, newline and space.
- 예시로 v는 분할점이다. 만약 분할이 지정되지 않는다면, split 메소드는 탭, 개행 공백과 같은 공백 캐릭터를 찾다.

| Method Name  | <center>Operator</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
| center |	astring.center(w) |	Returns a string centered in a field of size w |
| count |	astring.count(item)	| Returns the number of occurrences of item in the string |
| ljust |	astring.ljust(w) |	Returns a string left-justified in a field of size w |
| lower |	astring.lower() |	Returns a string in all lowercase |
| rjust |	astring.rjust(w) |	Returns a string right-justified in a field of size w |
| find	| astring.find(item) |	Returns the index of the first occurrence of item |
| split |	astring.split(schar) |	Splits a string into substrings at schar |

* A major difference between lists and strings is that lists can be modified while strings cannot.
-  list와 strings의 주된 차이점은 list는 수정할 수있고 strings는 할수 없다는 것 이다.
* This is referred to as mutability. Lists are mutable; strings are immutable. 
- 이것은 가변성에 대한 것 이다. list는 가변적, Strings는 불변이다.
* For example, you can change an item in a list by using indexing and assignment. 
- 예를들어 당신은  할당과 인덱싱을 사용하여 list안에 한 item을 바꿀 수 있다.
* With a string that change is not allowed.
- string 변경은 허용되지 않는다.
* Tuples are very similar to lists in that they are heterogeneous sequences of data. 
- 튜플은 이기종의 데이터 순서와 list는 매우 비슷하다.
* The difference is that a tuple is immutable, like a string. 
- 차이점은 string과 같이 튜플은 불변이라는 것이다.
* A tuple cannot be changed. 
- 튜플은 바꿀 수 없다.
* Tuples are written as comma-delimited values enclosed in parentheses.
- 튜플은 괄호안에 쉼표로 구분된 값들로 쓰여진다. 
* As sequences, they can use any operation described above. 
- 시퀀스로서, 그것들은 위에 기술된 어떤 연산을 사용 할 수 있다.
* For example, 
```buildoutcfg
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
```
* However, if you try to change an item in a tuple, you will get an error. 
- 그러나, 만약 당신이 튜플안의 item을 변경을 시도한다면, 당신은 error를 확인 할 수있다.
* Note that the error message provides location and reason for the problem.
- error 메시지는 문제에 대한 위치와 이유 제공한다.
```buildoutcfg
>>> myTuple[1]=False

Traceback (most recent call last):
  File "<pyshell#137>", line 1, in -toplevel-
    myTuple[1]=False
TypeError: object doesn't support item assignment
>>>
```
* A set is an unordered collection of zero or more immutable Python data objects.
- set는 0과 불변의 파이썬 데이터 객체의 순서가매겨지지않은 컬렉션 이다.
* Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces.
- set는 중복허용이 안되고 중괄호 안에 콤마로 구분된 값들로 쓰여진다.
* The empty set is represented by set(). Sets are heterogeneous, and the collection can be assigned to a variable as below.
- 공백 set는 set()로 표현된다. set는 이기종이고, 콜렉션에 아래와 같이 변수에 할당된다.
```buildoutcfg
>>> {3,6,"cat",4.5,False}
{False, 4.5, 3, 6, 'cat'}
>>> mySet = {3,6,"cat",4.5,False}
>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>>
```
* Even though sets are not considered to be sequential, they do support a few of the familiar operations presented earlier. 
- 심지어 set는 순서가 고려되지 않는다, 그것들은 이전에 표현된 익숙한 연산의 일부를 지원한다.
* Table 5 reviews these operations and the following session gives examples of their use.
- 테이블5는 연산들을 보여주고 다음 세션은 예시와 그들의 사용법을 준다.

| Operation Name  | <center>Operator</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
| membership |	in	| Set membership |
| length |	len |	Returns the cardinality of the set |
|        |  aset  otherset |	Returns a new set with all elements from both sets |
| &	aset & otherset |	Returns a new set with only those elements common to both sets |
| -	aset - otherset |	Returns a new set with all items from the first set not in second |
| \<= |	aset <= otherset |	Asks whether all elements of the first set are in the second |

```buildoutcfg
>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>> len(mySet)
5
>>> False in mySet
True
>>> "dog" in mySet
False
>>>
```

* Sets support a number of methods that should be familiar to those who have worked with them in a mathematics setting. Table 6 provides a summary. 
- set는 수학적 셋팅에서 그들과 함께 일한 사람들에게 익숙하 많은 메소드들을 지원한다. 테이블6는 서머리를 제공한다.
* Examples of their use follow. Note that union, intersection, issubset, and difference all have operators that can be used as well.
- 그 사용예시는 아래와 같다. union, intersection, issubset, difference 모두 연산자를 사용할 수 있다.

| Method Name  | <center>Operator</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
| union	| aset.union(otherset) |	Returns a new set with all elements from both sets |
| intersection |	aset.intersection(otherset)	| Returns a new set with only those elements common to both sets |
| difference |	aset.difference(otherset) |	Returns a new set with all items from first set not in second |
| issubset |	aset.issubset(otherset) |	Asks whether all elements of one set are in the other |
| add |	aset.add(item) |	Adds item to the set |
| remove |	aset.remove(item) |	Removes item from the set |
| pop |	aset.pop()	| Removes an arbitrary element from the set |
| clear |	aset.clear() |	Removes all elements from the set |

```buildoutcfg
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
```

* Our final Python collection is an unordered structure called a dictionary. 
- 마지막으로 파이썬 컬렉션은 순서화되지 않는 구조 사전이이라고 불려진다. 
* Dictionaries are collections of associated pairs of items where each pair consists of a key and a value.
- 사전들은 연결된 item 쌍의 컬레션이고 키와 값 구성된다.
* This key-value pair is typically written as key:value. 
- 이 키값 쌍은 전형적으로 key:value로 쓰여진다.
* Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. For example,
- 사전들은 중괄호 안에 쉼표구분자로 key:value 쌍으로 쓰여진다. 예시로ㅡ
 
```buildoutcfg
>>> capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
>>> capitals
{'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
>>>
```

* We can manipulate a dictionary by accessing a value via its key or by adding another key-value pair. 
- 우리는 키를 통해 값에 접근하거나 다른 키값 쌍을 추가하여 사전을 다룰 수 있다.
* The syntax for access looks much like a sequence access except that instead of using the index of the item we use the key value.
- 이 접근 구문은 item 이 키 값을 사용하고 인덱스를 사용을 대신한다는것 외에 순차접과 비슷하다. (이해가 잘 안되는 부분????)
* To add a new value is similar.
- 추가적으로 새로은 값은 비슷하다.
* It is important to note that the dictionary is maintained in no particular order with respect to the keys.
- 사전이 키와 관련하여 특별한 순서 없이 유지된다는 점을 주의해야 한다.
* The first pair added ('Utah': 'SaltLakeCity') was placed first in the dictionary and the second pair added ('California': 'Sacramento') was placed last.
- 추가된 첫번째 쌍 ('Utah': 'SaltLakeCity')은 첫번째로 사전안에 위치 되었고  추가된 두번째 쌍 ('California': 'Sacramento')은 마지막에 위치되었다.
* The placement of a key is dependent on the idea of “hashing,” which will be explained in more detail in Chapter 4. 
- 키의 위치는 "hashing" 아이디에 의해 독립된고 자세한 내용은 챕터4에서 설명한다.
* We also show the length function performing the same role as with previous collections.
- 우리는 또한 length 함수 이전의 콜렉션들과 같은 규칙으로 수행하는것을 볼수있다.
* Dictionaries have both methods and operators. 
- 사전은 메소드와 연산을 갖고 있다.
* Table 7 and Table 8 describe them, and the session shows them in action.
- 테이블7,8은 그것들을 성명하고 섹셕은 그들의 행동을 보여준다.
* The keys, values, and items methods all return objects that contain the values of interest.
- 키, 값들, 그리고 item 메소드들 모두 관심갖는 값들을 포함한 객체를 반환한다.
* You can use the list function to convert them to lists.
- 당신은 그것들을 list로 변환하는 list함수를 사용할 수있다.
* You will also see that there are two variations on the get method.
- 당신은 또한 get 메소드에 2개의 변형을 볼 수있다. 
* If the key is not present in the dictionary, get will return None. 
- 만약 키가 사전에 표현되지 않는다면, 리턴은 아무것도 없다.
* However, a second, optional parameter can specify a return value instead.
- 그러나 두번째 선택가능한 파라미터는 관심있는 값 리턴을 지정 할 수 있다.

| Operator  | <center>Use</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
| [] |	myDict[k] |	Returns the value associated with k, otherwise its an error |
| in |	key in adict |	Returns True if key is in the dictionary, False otherwise |
| del |	del adict[key] |	Removes the entry from the dictionary |
```buildoutcfg
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
```

| Method Name  | <center>Use</center> | <center>Explanation</center> |
|:--------:|:--------:|:--------:|
| keys |	adict.keys() |	Returns the keys of the dictionary in a dict_keys object |
| values |	adict.values() |	Returns the values of the dictionary in a dict_values object |
| items |	adict.items() |	Returns the key-value pairs in a dict_items object |
| get |	adict.get(k) |	Returns the value associated with k, None otherwise |
| get |	adict.get(k,alt) |	Returns the value associated with k, alt otherwise |
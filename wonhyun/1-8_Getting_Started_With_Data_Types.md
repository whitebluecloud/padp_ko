We stated above that Python supports the object-oriented programming paradigm. 

우리는 파이썬이 객체지향적 프로그래밍 모델을 지원한다고 언급했다.

This means that Python considers data to be the focal point of the problem-solving process. 

이것은 파이썬이 데이터를 문제 해결 과정의 초점이라고 간주한다는 것을 의미한다.

In Python, as well as in any other object-oriented programming language, we define a class to be a description of what the data look like (the state) and what the data can do (the behavior). 

파이썬에서는, 다른 객체지향 프로그래밍 언어에서 처럼, 데이터가 무엇처럼 보이는지와 무엇을 할 수 있는지를 묘사하는 클래스를 정의한다.

Classes are analogous to abstract data types because a user of a class only sees the state and behavior of a data item. Data items are called objects in the object-oriented paradigm. 

클래스들은 추상 데이터 타입과 유사하다. 왜냐하면 클래스의 사용자는 오직 상태와 데이터 항목의 행동만 볼 수 있기 때문이다. 데이터 아이템은 객체지향 모델에서  오브젝트라고 불린다.

An object is an instance of a class.

오브젝트는 클래스의 인스턴스이다.

*1.8.1. Built-in Atomic Data Types

We will begin our review by considering the atomic data types.

우리는 원자 데이터 타입을 고려함으로써 리뷰를 시작할 것이다.

Python has two main built-in numeric classes that implement the integer and floating point data types. 

파이썬은 정수와 실수 포인트 데이터 타입을 구현하는 두가지 대표 내장 숫자 클래스를 가지고 있다.

These Python classes are called int and float.

이 파이썬 클래스들은 int와 float이라고 불린다.

The standard arithmetic operations, +, -, *, /, and \** (exponentiation), can be used with parentheses forcing the order of operations away from normal operator precedence. 

기본 산술연산자들은 보통의 연산 우선순위를 떠나 연산자들의 순서를 정할 수 있는 괄호와 함께 사용될 수 있다.

Other very useful operations are the remainder (modulo) operator, %, and integer division, //. 
다른 매우 유용한 연산자는 나머지 연산자와 정수 나누기 연산자 이다.

Note that when two integers are divided, the result is a floating point. 
두 정수가 나누어질때 결과는 부동 소수점이걸 유의하라.

The integer division operator returns the integer portion of the quotient by truncating any fractional part.
정수 나누기 연산자는 소수 부분은 버림으로써 몫의 정수 부분을 리턴한다.

<pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kc">True</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="kc">False</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="kc">False</span> <span class="ow">or</span> <span class="kc">True</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="ow">not</span> <span class="p">(</span><span class="kc">False</span> <span class="ow">or</span> <span class="kc">True</span><span class="p">)</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="kc">True</span> <span class="ow">and</span> <span class="kc">True</span>
<span class="go">True</span>
</pre>

The boolean data type, implemented as the Python bool class, will be quite useful for representing truth values. 

파이썬의 bool 클래스로 구현되는 불 연산자 데이터 타입은 참 값을 표현하는데 꽤 유용하다. 

The possible state values for a boolean object are True and False with the standard boolean operators, and, or, and not

불 객체에 가능한 상태 값은 True와 False이고, 기본 불 연산자 인 and, or, not과 사용될 수 있다.

Boolean data objects are also used as results for comparison operators such as equality (==) and greater than (>). 

불 데이터 오브젝트는 등호나 부등호 같은 비교 연산자의 결과로서도 사용될 수 있다.

In addition, relational operators and logical operators can be combined together to form complex logical questions. 

게다가, 관계 연산자와 논리 연산자는 복잡한 논리 질문을 형성하기위해 결합이 가능하다.

Table 1 shows the relational and logical operators with examples shown in the session that follows.

테이블1은 다음 세션에서 보여주는 예시에서 관계와 논리 연산자를 보여준다.

<table border="0" class="table" id="id1">
<caption><span class="caption-text"><strong>Table 1: Relational and Logical Operators</strong></span><a class="headerlink" href="#id1" title="Permalink to this table">¶</a></caption>
<colgroup>
<col width="25%">
<col width="13%">
<col width="61%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head"><strong>Operation Name</strong></th>
<th class="head"><strong>Operator</strong></th>
<th class="head"><strong>Explanation</strong></th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>less than</td>
<td><</td>
<td>미만</td>
</tr>
<tr class="row-odd"><td>greater than</td>
<td>></td>
<td>초과</td>
</tr>
<tr class="row-even"><td>less than or equal</td>
<td><=</td>
<td>이하</td>
</tr>
<tr class="row-odd"><td>greater than or equal</td>
<td>>=</td>
<td>이상</td>
</tr>
<tr class="row-even"><td>equal</td>
<td>==</td>
<td>같은</td>
</tr>
<tr class="row-odd"><td>not equal</td>
<td>!=</td>
<td>같지 않은</td>
</tr>
<tr class="row-even"><td>logical and</td>
<td>and</td>
<td>둘다 참이어야 참</td>
</tr>
<tr class="row-odd"><td>logical or</td>
<td>or</td>
<td>하나라도 참이면 참</td>
</tr>
<tr class="row-even"><td>logical not</td>
<td>not</td>
<td>거짓은 참으로, 참은 거짓으로</td>
</tr>
</tbody>
</table>

Identifiers are used in programming languages as names. 

프로그래밍 언어에서 식별자는 이름으로 사용된다.

In Python, identifiers start with a letter or an underscore (\_), are case sensitive, and can be of any length. 

파이썬에서 식별자는 문자나  \_으로 시작한다.

Remember that it is always a good idea to use names that convey meaning so that your program code is easier to read and understand.

의미를 전달하는 이름을 사용하여 너의 프로그램 코드를 읽기 더 쉽고 이해하기 쉽게 하는 것은 항상 좋은 아이디어라는 것을 기억해라.

A Python variable is created when a name is used for the first time on the left-hand side of an assignment statement. 

파이썬 변수는 이름이 대입문의 왼쪽에 사용될 때 처음 만들어진다.

Assignment statements provide a way to associate a name with a value. 

대입문은 이름과 값을 연결하는데 사용된다.

The variable will hold a reference to a piece of data and not the data itself.

변수는 작은 데이터에 대한 참조를 가지고 있다.

Consider the following session:

두 세션을 보자.
<pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">theSum</span> <span class="o">=</span> <span class="mi">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">theSum</span>
<span class="go">0</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">theSum</span> <span class="o">=</span> <span class="n">theSum</span> <span class="o">+</span> <span class="mi">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">theSum</span>
<span class="go">1</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">theSum</span> <span class="o">=</span> <span class="kc">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">theSum</span>
<span class="go">True</span>
</pre>
The assignment statement theSum = 0 creates a variable called theSum and lets it hold the reference to the data object 0 (see Figure 3).

theSum=0 대입문은 theSum이라는 변수를 만들고 데이터 객체 0의 참조를 가지게 한다.

In general, the right-hand side of the assignment statement is evaluated and a reference to the resulting data object is “assigned” to the name on the left-hand side. 

일반적으로, 대입문의 오른쪽은 평가된다. 결과 데이터 객체

At this point in our example, the type of the variable is integer as that is the type of the data currently being referred to by theSum.
If the type of the data changes (see Figure 4), as shown above with the boolean value True, so does the type of the variable (theSum is now of the type boolean). 

데이터 변화의 유형이

The assignment statement changes the reference being held by the variable. 

대입문은 변수가 지닌 참조를 바꾼다.

This is a dynamic characteristic of Python.

이것은 파이썬의 동적인 특징이다.

The same variable can refer to many different types of data.

같은 변수는 다양한 다른 종류의 데이터 타입을 나타낼 수 있다.

*1.8.2. Built-in Collection Data Types

In addition to the numeric and boolean classes, Python has a number of very powerful built-in collection classes.

숫자와 불 클래스 외에 파이썬은 많은 매우 강력한 내장 집합 클래스들을 가지고 있다.

Lists, strings, and tuples are ordered collections that are very similar in general structure but have specific differences that must be understood for them to be used properly. 

리스트, 스트링, 튜플은 일반적인 구조에서 매우 비슷하지만, 적절하게 사용되기 위해 꼭 이해되어야 하는 특정한 차이가 있는 순서가 있는 집합이다.

Sets and dictionaries are unordered collections.

셋은 순서가 없는 딕셔너리이다.

A list is an ordered collection of zero or more references to Python data objects. 

리스트는 파이썬 데이터 객체로 0개나 그 이상의 참조가 있는 순서가 있는 집합이다.

Lists are written as comma-delimited values enclosed in square brackets. 

리스트는 대괄호 안에서 콤마로 나뉘는 값이다.

The empty list is simply [ ]. 

빈 리스트는 간단히 []이다.

Lists are heterogeneous, meaning that the data objects need not all be from the same class and the collection can be assigned to a variable as below.

리스트는 여러 다른 종류로 이루어져 있으며 이것은 데이터 객체가 모두 같은 클래스일 필요는 없다는 것을 의미한다.

The following fragment shows a variety of Python data objects in a list.

Note that the indices for lists (sequences) start counting with 0. 

리스트의 인덱스(시퀀스)는 0부터 시작한다는 것을 유의해라.

The slice operation, myList[1:3], returns a list of items starting with the item indexed by 1 up to but not including the item indexed by 3.

myList[1:3] 과 같은 slice 연산자는 인덱스1로 시작는 요소부터 리턴하고, 인덱스3을 가진 요소는 포함하지 않는다.

Sometimes, you will want to initialize a list. This can quickly be accomplished by using repetition. For example,

때때로, 너는 리스트를 초기화하기를 원할 것이다. 이것은 반복을 통해 행해질 수 있다. 예를 들어, 

One very important aside relating to the repetition operator is that the result is a repetition of references to the data objects in the sequence. This can best be seen by considering the following session:

반복 연산자에 관해서 한가지 가장 중요한 점은 결과가 순서로 이루어진 데이터 참조의 반복이라는 것이다. 이것은 다음 세션에서 확인할 수 있다.

The variable A holds a collection of three references to the original list called myList. Note that a change to one element of myList shows up in all three occurrences in A.

A라는 변수는 myList라고 불리는 원본 리스트에 대한 3개의 참조의 집합을 가지고 있다. myList 중 하나의 요소의 변화가 A의 모든 3개의 경우에서 나타나고 있다는 것을 유의하라. 

Lists support a number of methods that will be used to build data structures. Table 3 provides a summary. Examples of their use follow.

리스트는 데이터구조를 형성할 때 사용될 수 있는 다양한 방법을 지원한다. 테이블3은 요약을 제공한다. 그것들(다양한 방법들)의 사용 예시이다.

You can see that some of the methods, such as pop, return a value and also modify the list. 

너는 리스트의 값을 리턴하거나 수정할 수 있는 pop과 같은 방법들 중 몇개를 볼수 있다. 

Others, such as reverse, simply modify the list with no return value. 

다른 것들, reverse와 같은 것들은 리턴하는 값 없이 간단하게 리스트를 수정한다.

pop will default to the end of the list but can also remove and return a specific item. 

pop은 리스트의 마지막 값을 리턴하는 것이 기본이지만 특정 요소를 제거하거나 리턴할 수 있다.

The index range starting from 0 is again used for these methods. 

0부터 시작하는 인덱스의 범위는 이 방법에서 다시 사용된다.

You should also notice the familiar “dot” notation for asking an object to invoke a method.

너는 또한 주의해야만 한다. dot 노테이션이

myList.append(False) can be read as “ask the object myList to perform its append method and send it the value False.” 

myList.append(False)는 myList에게 append method를 요청하고 False 값을 보내라고 읽혀질 수 있다.

Even simple data objects such as integers can invoke methods in this way.

interger와 같은 간단한 데이터객체조차도 이 방법으로 명령어를 실행할 수 있다.

In this fragment we are asking the integer object 54 to execute its add method (called __add__ in Python) and passing it 21 as the value to add. 

이 부분에서 우리는 정수 54에게 add 메써드를 실행하도록 요청하고, 더해질 값으로 21을 넘겼다.

The result is the sum, 75. Of course, we usually write this as 54+21. We will say much more about these methods later in this section.

덧셈의 결과는 75이다. 물론, 우리는 이것을 보통 54 + 21으로 작성한다. 우리는 이러한 다른 method들에 대해서 이번 섹션에 더 많은 것을 알아볼 것이다.

One common Python function that is often discussed in conjunction with lists is the range function. range produces a range object that represents a sequence of values. 

리스트의 결합에서 종종 논의되는 하나의 일반적인 파이썬의 함수는 range 함수

By using the list function, it is possible to see the value of the range object as a list. This is illustrated below.

리스트의 함수를 사용함으로써, 리스트같은 객체의 range 값을 보는 것이 가능하다. 이것은 아래에 나타나고 있다.

The range object represents a sequence of integers. 

range 객체는 정수의 연속을 나타낸다.

By default, it will start with 0. 

기본적으로 이것은 0부터 시작한다.

If you provide more parameters, it will start and end at particular points and can even skip items. 

몇 가지 파라미터를 더 제공한다면, 그것은 특정 점 부터 시작하고 끝난다. 또한 건너뛰는 것도 가능하다.

In our first example, range(10), the sequence starts with 0 and goes up to but does not include 10.

첫 번째 예처럼 range(10) 0부터 시작하여 순서대로 올라간다. 10에 해당하는 요소는 포함하지 않는다.

In our second example, range(5,10) starts at 5 and goes up to but not including 10. 

두 번째 예인 range(5,10)은 5에서 시작하고 10은 포함하지 않는다.

range(5,10,2) performs similarly but skips by twos (again, 10 is not included).

range(5,10,2)는 비슷하게 동작하지만 2번째 마다 값을 건너 뛴다.

Strings are sequential collections of zero or more letters, numbers and other symbols. 

String은 공집합이나 더 많은 문자들, 숫자, 기호의 연속적인 집합이다.

We call these letters, numbers and other symbols characters. 

우리는 이것들을 문자들, 숫자들, 그리고 다른 기호들이라고 부른다.

Literal string values are differentiated from identifiers by using quotation marks (either single or double).
(?)

Since strings are sequences, all of the sequence operations described above work as you would expect. 

스트링이 연속이기 때문에, 위에서 묘사된 연속적인 연산자 모두는 당신이 예상했듯이 동작한다.

In addition, strings have a number of methods, some of which are shown in Table 4. For example,

게다가, 스트링은 많은 method들을 가지고 있다. 몇가지는 Table4에 나와있다.

Of these, split will be very useful for processing data.

여기서, split는 데이터를 가공하는 데 매우 유용할 것이다.

split will take a string and return a list of strings using the split character as a division point. In the example, v is the division point.

split는 스트링을 받고 split 문자를 구분자로 사용하여 스트링의 리스트를 반환한다. 예에서는, v가 구분자이다.

If no division is specified, the split method looks for whitespace characters such as tab, newline and space.

구분자가 특정되지 않았다면, split method는 tab이나 줄바꿈, 스페이스와 같은 공백을 찾게 된다.

A major difference between lists and strings is that lists can be modified while strings cannot. 

리스트와 스트링의 주요한 차이는 스트링과는 달리 리스트는 수정이 가능하다는 점이다.

This is referred to as mutability. 

이것은 변동성이라고 불린다.

Lists are mutable; strings are immutable. 

리스트는 변동하고, 문자는 불변하다.

For example, you can change an item in a list by using indexing and assignment. 

예를들어, 너는 인덱싱과 assignment를 사용하여 리스트의 요소를 바꿀 수 있다.

With a string that change is not allowed.

스트링을 바꾸는 것을 허용되지 않는다.

Tuples are very similar to lists in that they are heterogeneous sequences of data. 

튜플은 이질적인 데이터의 연속이라는 점에서 리스트와 매우 유사하다.

The difference is that a tuple is immutable, like a string. 

차이점은 튜플은 스트링처럼 불변하다는 것이다.

A tuple cannot be changed. 

튜플은 바뀔 수가 없다.

Tuples are written as comma-delimited values enclosed in parentheses.

튜플은 괄호 내의 콤마로 분리된 값으로 쓰여진다.

As sequences, they can use any operation described above. For example,

결론적으로, 튜플은 위에서 묘사된 어떤 연산자들도 사용이 가능하다. 예를 들어,

However, if you try to change an item in a tuple, you will get an error. 

하지만, 만약에 너가 튜플 내의 요소를 바꾸려고 시도한다면 에러를 얻을 것이다.

Note that the error message provides location and reason for the problem.

에러 메세지는 문제의 위치와 원인을 제공한다.

A set is an unordered collection of zero or more immutable Python data objects. 

set은 0또는 파이썬의 불변 객체들의 순서가 없는 집합이다.

Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces. 

set은 복사하는 것을 허가하지 않고, 중괄호 내에 콤마로 분리한 값으로 쓰여진다.

The empty set is represented by set(). 

빈 셋은 set()으로 표현된다.

Sets are heterogeneous, and the collection can be assigned to a variable as below.

set은 이질적이다. 그리고 집합은 아래처럼 변수에 할당될 수 있다.

Even though sets are not considered to be sequential, they do support a few of the familiar operations presented earlier. 

비록 set이 순차적이지 않더라도 set은 위에서 말한 몇가지 친숙한 연산자들을 지원한다.

Table 5 reviews these operations and the following session gives examples of their use.

Table5 는 이러한 연산자들을 리뷰하고, 다음 세션은 그것들의 예를 보여준다.

Sets support a number of methods that should be familiar to those who have worked with them in a mathematics setting. 

set은 수학 계열에서 일하는 사람들에게 친숙해야 하는 다양한 method들을 지원한다.

Table 6 provides a summary. 

Table 6은 요약을 제공한다.

Examples of their use follow. 

그것들의 예가 나온다.

Note that union, intersection, issubset, and difference all have operators that can be used as well.

union, intersection, issubset, 그리고 difference는 모두 마찬가지로 사용될 수 있는 연산자를 가진다는 것을 유의해라.

Our final Python collection is an unordered structure called a dictionary. 

파이썬의 마지막 집합은 dictionary라고 불리는 순서가 없는 구조이다.

Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. 

dictionary는 각 쌍이 키와 값으로 구성되어 있는 관련 항목 쌍의 집합이다. 

This key-value pair is typically written as key:value. 

이러한 key-value 쌍은 일반적으로 key:value 형태로 쓰여진다.

Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. For example,

dictionary는 콤마로 구분되고, 중괄호로 묶인 key:value 쌍이다. 예를 들어,

It is important to note that the dictionary is maintained in no particular order with respect to the keys. 

key와 관련하여 dictionary는 특정한 순서로 유지되지 않는다는 것을 유의하는 것이 중요하다.  

The first pair added ('Utah': 'SaltLakeCity') was placed first in the dictionary and the second pair added ('California': 'Sacramento') was placed last. 
('Utah': 'SaltLakeCity') 첫번째 쌍은 dictionary의 첫 번째에 위치하였고, 두번째 쌍인 ('California': 'Sacramento')는 마지막에 위치한다.

The placement of a key is dependent on the idea of “hashing,” which will be explained in more detail in Chapter 4. 

키의 배치는 Chapter4에서 자세히 소개 할 hashing 아이디어에 의존한다.

We also show the length function performing the same role as with previous collections.

우리는 또한 이전의 집합들에서와 같은 역할을 하는 length function을 보여준다.

Dictionaries have both methods and operators. 

dictionary는 method와 연산자를 둘 다 가진다.

Table 7 and Table 8 describe them, and the session shows them in action. 

Table 7과 8은 그것들을 묘사하고, 이 세션은 결과를 보여준다.

The keys, values, and items methods all return objects that contain the values of interest. 

키와 값, 항목과 모든 method는 모두 관심 값을 포함하는 객체를 리턴한다.

You can use the list function to convert them to lists. 

너는 그것들을 리스트로 전환할 수 있는 리스트 함수를 사용할 수 있다.

You will also see that there are two variations on the get method. 

너는 또한 get method에서 두 변화를 볼 수 있다.

If the key is not present in the dictionary, get will return None. 

만약 키가 dictionary에서 찾을 수 없다면 get은 None을 리턴할 것 이다.

However, a second, optional parameter can specify a return value instead.

하지만, 두번째, 선택적인 파라미터는 대신 리턴 값을 특정할 수 있다.

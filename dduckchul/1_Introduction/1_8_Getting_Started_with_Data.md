# 원문
## 1.8. Getting Started with Data
* We stated above that Python supports the object-oriented programming paradigm. This means that Python considers data to be the focal point of the problem-solving process. In Python, as well as in any other object-oriented programming language, we define a class to be a description of what the data look like (the state) and what the data can do (the behavior). Classes are analogous to abstract data types because a user of a class only sees the state and behavior of a data item. Data items are called objects in the object-oriented paradigm. An object is an instance of a class.

### 1.8.1. Built-in Atomic Data Types
* We will begin our review by considering the atomic data types. Python has two main built-in numeric classes that implement the integer and floating point data types. These Python classes are called int and float. The standard arithmetic operations, +, -, *, /, and ** (exponentiation), can be used with parentheses forcing the order of operations away from normal operator precedence. Other very useful operations are the remainder (modulo) operator, %, and integer division, //. Note that when two integers are divided, the result is a floating point. The integer division operator returns the integer portion of the quotient by truncating any fractional part.

```python
print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)

#Basic Arithmetic Operators (intro_1)
```

* The boolean data type, implemented as the Python bool class, will be quite useful for representing truth values. The possible state values for a boolean object are True and False with the standard boolean operators, and, or, and not.

```python
>>> True  
True  
>>> False  
False  
>>> False or True  
True  
>>> not (False or True)  
False  
>>> True and True  
True
```

* Boolean data objects are also used as results for comparison operators such as equality (==) and greater than (>). In addition, relational operators and logical operators can be combined together to form complex logical questions. Table 1 shows the relational and logical operators with examples shown in the session that follows.

| Operation Name        | Operator | Explanation                                                     |
|-----------------------|----------|-----------------------------------------------------------------|
| less than             | <        | Less than operator                                              |
| greater than          | >        | Greater than operator                                           |
| less than or equal    | <=       | Less than or equal to operator                                  |
| greater than or equal | >=       | Greater than or equal to operator                               |
| equal                 | ==       | Equality operator                                               |
| not equal             | !=       | Not equal operator                                              |
| logical and           | and      | Both operands True for result to be True                        |
| logical or            | or       | One or the other operand is True for the result to be True      |
| logical not           | not      | Negates the truth value, False becomes True, True becomes False |
```python
print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))
```
​
* Basic Relational and Logical Operators (intro_2)

* Identifiers are used in programming languages as names. In Python, identifiers start with a letter or an underscore (_), are case sensitive, and can be of any length. Remember that it is always a good idea to use names that convey meaning so that your program code is easier to read and understand.

* A Python variable is created when a name is used for the first time on the left-hand side of an assignment statement. Assignment statements provide a way to associate a name with a value. The variable will hold a reference to a piece of data and not the data itself. Consider the following session:

```python
>>> theSum = 0  
>> theSum  
0
>>> theSum = theSum + 1  
>>> theSum  
1  
>>> theSum = True  
>>> theSum  
True  
```

* The assignment statement theSum = 0 creates a variable called theSum and lets it hold the reference to the data object 0 (see Figure 3). In general, the right-hand side of the assignment statement is evaluated and a reference to the resulting data object is “assigned” to the name on the left-hand side. At this point in our example, the type of the variable is integer as that is the type of the data currently being referred to by theSum. If the type of the data changes (see Figure 4), as shown above with the boolean value True, so does the type of the variable (theSum is now of the type boolean). The assignment statement changes the reference being held by the variable. This is a dynamic characteristic of Python. The same variable can refer to many different types of data.

### 1.8.2. Built-in Collection Data Types
* In addition to the numeric and boolean classes, Python has a number of very powerful built-in collection classes. Lists, strings, and tuples are ordered collections that are very similar in general structure but have specific differences that must be understood for them to be used properly. Sets and dictionaries are unordered collections.

* A list is an ordered collection of zero or more references to Python data objects. Lists are written as comma-delimited values enclosed in square brackets. The empty list is simply [ ]. Lists are heterogeneous, meaning that the data objects need not all be from the same class and the collection can be assigned to a variable as below. The following fragment shows a variety of Python data objects in a list.

```python
>>> [1,3,True,6.5]  
1, 3, True, 6.5]  
>>> myList = [1,3,True,6.5]  
>>> myList  
[1, 3, True, 6.5]  
```
* Note that when Python evaluates a list, the list itself is returned. However, in order to remember the list for later processing, its reference needs to be assigned to a variable.

* Since lists are considered to be sequentially ordered, they support a number of operations that can be applied to any Python sequence. Table 2 reviews these operations and the following session gives examples of their use.

| Operation Name | Operator | Explanation                             |
|----------------|----------|-----------------------------------------|
| indexing       | [ ]      | Access an element of a sequence         |
| concatenation  | +        | Combine sequences together              |
| repetition     | *        | Concatenate a repeated number of times  |
| membership     | in       | Ask whether an item is in a sequence    |
| length         | len      | Ask the number of items in the sequence |
| slicing        | [ : ]    | Extract a part of a sequence            |
* Note that the indices for lists (sequences) start counting with 0. The slice operation, myList[1:3], returns a list of items starting with the item indexed by 1 up to but not including the item indexed by 3.

* Sometimes, you will want to initialize a list. This can quickly be accomplished by using repetition. For example,

```python
>>> myList = [0] * 6  
>>> myList  
[0, 0, 0, 0, 0, 0]  
```
* One very important aside relating to the repetition operator is that the result is a repetition of references to the data objects in the sequence. This can best be seen by considering the following session:

```python
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
```

* The variable A holds a collection of three references to the original list called myList. Note that a change to one element of myList shows up in all three occurrences in A.

* Lists support a number of methods that will be used to build data structures. Table 3 provides a summary. Examples of their use follow.

| Method Name | Use                  | Explanation                                       |
|-------------|----------------------|---------------------------------------------------|
| append      | alist.append(item)   | Adds a new item to the end of a list              |
| insert      | alist.insert(i,item) | Inserts an item at the ith position in a list     |
| pop         | alist.pop()          | Removes and returns the last item in a list       |
| pop         | alist.pop(i)         | Removes and returns the ith item in a list        |
| sort        | alist.sort()         | Modifies a list to be sorted                      |
| reverse     | alist.reverse()      | Modifies a list to be in reverse order            |
| del         | del alist[i]         | Deletes the item in the ith position              |
| index       | alist.index(item)    | Returns the index of the first occurrence of item |
| count       | alist.count(item)    | Returns the number of occurrences of item         |
| remove      | alist.remove(item)   | Removes the first occurrence of item              |

```python
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
​
#Examples of List Methods (intro_5)
```

* You can see that some of the methods, such as pop, return a value and also modify the list. Others, such as reverse, simply modify the list with no return value. pop will default to the end of the list but can also remove and return a specific item. The index range starting from 0 is again used for these methods. You should also notice the familiar “dot” notation for asking an object to invoke a method. myList.append(False) can be read as “ask the object myList to perform its append method and send it the value False.” Even simple data objects such as integers can invoke methods in this way.

```python
>>> (54).__add__(21)  
75  
>>>
```

* In this fragment we are asking the integer object 54 to execute its add method (called __add__ in Python) and passing it 21 as the value to add. The result is the sum, 75. Of course, we usually write this as 54+21. We will say much more about these methods later in this section.

* One common Python function that is often discussed in conjunction with lists is the range function. range produces a range object that represents a sequence of values. By using the list function, it is possible to see the value of the range object as a list. This is illustrated below.

```python
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
```

* The range object represents a sequence of integers. By default, it will start with 0. If you provide more parameters, it will start and end at particular points and can even skip items. In our first example, range(10), the sequence starts with 0 and goes up to but does not include 10. In our second example, range(5,10) starts at 5 and goes up to but not including 10. range(5,10,2) performs similarly but skips by twos (again, 10 is not included).

* Strings are sequential collections of zero or more letters, numbers and other symbols. We call these letters, numbers and other symbols characters. Literal string values are differentiated from identifiers by using quotation marks (either single or double).

```python
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
```

* Since strings are sequences, all of the sequence operations described above work as you would expect. In addition, strings have a number of methods, some of which are shown in Table 4. For example,

```python
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

* Of these, split will be very useful for processing data. split will take a string and return a list of strings using the split character as a division point. In the example, v is the division point. If no division is specified, the split method looks for whitespace characters such as tab, newline and space.

| Method Name | Use                  | Explanation                                             |
|-------------|----------------------|---------------------------------------------------------|
| center      | astring.center(w)    | Returns a string centered in a field of size w          |
| count       | astring.count(item)  | Returns the number of occurrences of item in the string |
| ljust       | astring.ljust(w)     | Returns a string left-justified in a field of size w    |
| lower       | astring.lower()      | Returns a string in all lowercase                       |
| rjust       | astring.rjust(w)     | Returns a string right-justified in a field of size w   |
| find        | astring.find(item)   | Returns the index of the first occurrence of item       |
| split       | astring.split(schar) | Splits a string into substrings at schar                |

* A major difference between lists and strings is that lists can be modified while strings cannot. This is referred to as mutability. Lists are mutable; strings are immutable. For example, you can change an item in a list by using indexing and assignment. With a string that change is not allowed.

```python
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
```

* Tuples are very similar to lists in that they are heterogeneous sequences of data. The difference is that a tuple is immutable, like a string. A tuple cannot be changed. Tuples are written as comma-delimited values enclosed in parentheses. As sequences, they can use any operation described above. For example,

```python
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

* However, if you try to change an item in a tuple, you will get an error. Note that the error message provides location and reason for the problem.

```python
>>> myTuple[1]=False

Traceback (most recent call last):
  File "<pyshell#137>", line 1, in -toplevel-
    myTuple[1]=False
TypeError: object doesn't support item assignment
>>>
```
* A set is an unordered collection of zero or more immutable Python data objects. Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces. The empty set is represented by set(). Sets are heterogeneous, and the collection can be assigned to a variable as below.

```python
>>> {3,6,"cat",4.5,False}
{False, 4.5, 3, 6, 'cat'}
>>> mySet = {3,6,"cat",4.5,False}
>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>>
```

* Even though sets are not considered to be sequential, they do support a few of the familiar operations presented earlier. Table 5 reviews these operations and the following session gives examples of their use.

| Operation Name | Operator         | Explanation                                                       |
|----------------|------------------|-------------------------------------------------------------------|
| membership     | in               | Set membership                                                    |
| length         | len              | Returns the cardinality of the set                                |
| |              | aset | otherset  | Returns a new set with all elements from both sets                |
| &              | aset & otherset  | Returns a new set with only those elements common to both sets    |
| -              | aset - otherset  | Returns a new set with all items from the first set not in second |
| <=             | aset <= otherset | Asks whether all elements of the first set are in the second      |

```python
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
* Sets support a number of methods that should be familiar to those who have worked with them in a mathematics setting. Table 6 provides a summary. Examples of their use follow. Note that union, intersection, issubset, and difference all have operators that can be used as well.

| Method Name  | Use                         | Explanation                                                    |
|--------------|-----------------------------|----------------------------------------------------------------|
| union        | aset.union(otherset)        | Returns a new set with all elements from both sets             |
| intersection | aset.intersection(otherset) | Returns a new set with only those elements common to both sets |
| difference   | aset.difference(otherset)   | Returns a new set with all items from first set not in second  |
| issubset     | aset.issubset(otherset)     | Asks whether all elements of one set are in the other          |
| add          | aset.add(item)              | Adds item to the set                                           |
| remove       | aset.remove(item)           | Removes item from the set                                      |
| pop          | aset.pop()                  | Removes an arbitrary element from the set                      |
| clear        | aset.clear()                | Removes all elements from the set                              |

```python
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

* Our final Python collection is an unordered structure called a dictionary. Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. This key-value pair is typically written as key:value. Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. For example,

```python
>>> capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
>>> capitals
{'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
>>>
```
* We can manipulate a dictionary by accessing a value via its key or by adding another key-value pair. The syntax for access looks much like a sequence access except that instead of using the index of the item we use the key value. To add a new value is similar.

```python
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)
​
# Using a Dictionary (intro_7)
```

* It is important to note that the dictionary is maintained in no particular order with respect to the keys. The first pair added ('Utah': 'SaltLakeCity') was placed first in the dictionary and the second pair added ('California': 'Sacramento') was placed last. The placement of a key is dependent on the idea of “hashing,” which will be explained in more detail in Chapter 4. We also show the length function performing the same role as with previous collections.

* Dictionaries have both methods and operators. Table 7 and Table 8 describe them, and the session shows them in action. The keys, values, and items methods all return objects that contain the values of interest. You can use the list function to convert them to lists. You will also see that there are two variations on the get method. If the key is not present in the dictionary, get will return None. However, a second, optional parameter can specify a return value instead.

| Operator | Use            | Explanation                                                 |
|----------|----------------|-------------------------------------------------------------|
| []       | myDict[k]      | Returns the value associated with k, otherwise its an error |
| in       | key in adict   | Returns True if key is in the dictionary, False otherwise   |
| del      | del adict[key] | Removes the entry from the dictionary                       |

```python
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

| Method Name | Use              | Explanation                                                  |
|-------------|------------------|--------------------------------------------------------------|
| keys        | adict.keys()     | Returns the keys of the dictionary in a dict_keys object     |
| values      | adict.values()   | Returns the values of the dictionary in a dict_values object |
| items       | adict.items()    | Returns the key-value pairs in a dict_items object           |
| get         | adict.get(k)     | Returns the value associated with k, None otherwise          |
| get         | adict.get(k,alt) | Returns the value associated with k, alt otherwise           |

# 번역
## 1.8. 데이터 시작하기
* 우리는 앞서 파이썬이 객체지향 패러다임을 갖고있다고 배웠다.  
이것은 파이썬이 데이터를 문제해결에 초점을 두고있다고 생각할수 있다.  
파이썬에서는 다른 객체지향 프로그램 언어와 마찬가지로, 데이터가 어떻게 생겼고, 데이터가 어떤 역할을 할수있는지 클래스로 정의 할 수 있다.  
클래스는 사용자가 데이터의 상태와 데이터의 역할만 볼수 있다는 점에서 추상 데이터 유형과 비슷하다  
데이터 아이템들은 객체 지향 프로그래밍에서 오브젝트로 불린다. 오브젝트는 클래스의 인스턴트이다.  

### 1.8.1. 빌트인 원시 데이터 타입
* 우리는 원시 데이터 타입으로 첫 설명을 시작할 것이다.  
파이썬은 정수형과 소숫점 데이터 타입을 구현한 두가지 주요 숫자형 클래스가 있다.  
이 파이썬 클래스들은 int와 float으로 불린다.  
일반적인 수학적 연산 기호인 +,-,*,/와 **(지수)들은 괄호와 함꼐 사용하여 연산의 순서를 정할수 있다.  
또 다른 유용한 연산자는 나머지 연산자 %(모듈러)와 정수형 나누기인 // 이다.  
두개의 정수가 나눠질때, 결과값은 소수점 자료형임을 명심해라.  
정수형 나눗셈 연산자는 소숫점을 버리고 정수 부분만을 반환한다.

```python
print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)

#Basic Arithmetic Operators (intro_1)
```

* 불린 데이터 타입 (파이썬에서 bool 클래스로 구현되었음) 은 참인 값을 표현하기 유용한 클래스이다.  
불린 객체의 값은 True와 False이고, 불린 연산자인 and, or, not을 사용할 수 있다.

```python
>>> True  
True  
>>> False  
False  
>>> False or True  
True  
>>> not (False or True)  
False  
>>> True and True  
True
```

* 불린 데이터 객체들은 ==(같다), >(보다 큰) 등의 비교 연산자의 결과값을 위해 사용되기도 한다.  
추가적으로 관계적 연산자와 논리 연산자들도 함께 사용하여 복잡한 논리적 문제들을 표현할 수 있다.  
아래 표에서 관계적, 논리적 연산자들을 볼수 있다.

| Operation Name        | Operator | Explanation                                                     |
|-----------------------|----------|-----------------------------------------------------------------|
| 보다 적은 | <        | Less than operator                                              |
| 보다 큰 | \>        | Greater than operator                                           |
| 작거나 같다 | \<=       | Less than or equal to operator                                  |
| 크거나 같다 | \>=       | Greater than or equal to operator                               |
| 같다 | ==       | Equality operator                                               |
| 같지 않다 | !=       | Not equal operator                                              |
| 논리 and 연산 | and      | 비교하는 대상 두개가 참일때 참을 반환 |
| 논리 or 연산 | or       | 둘중 하나의 대상이 참일때 참을 반환 |
| 논리 not 연산 | not      | 값의 반대를 반환한다. 참이 거짓, 거짓이 참이 된다 |

```python
print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

# Basic Relational and Logical Operators (intro_2)
```

* 식별자들은 프로그래밍 언어에서 이름으로 사용한다.  
파이썬에서 식별자들은 영문자나, 언더스코어(_)로 시작하고, 대소문자를 구분하며, 몇글자든지 가능하다.  
의미를 가진 이름을 사용하는것이 당신의 코드를 가독성있고, 쉽게 이해할수 있게 만든다는 것을 기억해라.

* 파이썬 변수들은 처음으로 좌측에 할당되었을때 만들어진다  
할당은 변수의 이름과 값을 연결하기 위한 방법이다.  
변수는 데이터의 레퍼런스를 갖고 있을 뿐이지 데이터를 갖고있지는 않다.  
아래의 세션을 보자.

```python
>>> theSum = 0  
>> theSum  
0
>>> theSum = theSum + 1  
>>> theSum  
1  
>>> theSum = True  
>>> theSum  
True  
```

* theSum = 0 의 할당문이 theSum이라는 변수를 만들어 생성하고 0 이라는 데이터 객체의 레퍼런스를 가지게 한다.  
일반적으로 할당문에서 오른쪽이 왼쪽의 변수명에 레퍼런스로 들어간다고 여겨진다.  
우리의 예제에서, 변수의 타입은 현재 theSum의 레퍼런스인 정수형이다.  
만약 참조하고 있는 데이터 타입이 바뀐다면 (위에서 처럼 True값으로 바뀐다면), 변수의 데이터 유형도 달라진다.
할당문이 변수의 레퍼런스를 바꾸는 것이다. 이것은 파이썬의 동적인 특징을 나타내준다.  
같은 변수가 많은 유형의 데이터로 변할 수 있는 것이다.

### 1.8.2. 빌트인 컬렉션 데이터 유형
* 숫자형과, 불린 클래스들에 이어, 파이썬은 몇개의 강력한 컬렉션 클래스를 가지고 있다.  
리스트, 스트링, 튜플들은 일반적으로 순서가 있는 데이터로 유사한 구조를 가지고 있다.  
그러나 이것들을 적절히 사용하기 위해서는 그 특징들을 잘 알아야 한다.  
셋과 딕셔너리형은 순서가 없는 컬렉션들이다.

* 리스트 형은 순서가 있는 컬렉션으로써, 파이썬 데이터 객체들이 0개이거나 그 이상이 있을 수 있다.  
리스트는 쉼표로 값을 구분하고, 중괄호로 감싸진 형태로 쓰여진다.  
리스트들은 여러 다른 종류로 이루어질수 있어서, 리스트 안에 쓰여진 모든 데이터 유형들이 같은 클래스가 아니어도 된다.  
또한 컬렉션을 변수로 할당할 수 있다. 아래의 코드는 파이썬의 리스트 자료형이 얼마나 다양하게 쓰일수 있는지 보여준다.

```python
>>> [1,3,True,6.5]  
1, 3, True, 6.5]  
>>> myList = [1,3,True,6.5]  
>>> myList  
[1, 3, True, 6.5]  
```
* 파이썬에서 리스트형을 사용하면, 그 리스트가 반환된다. 그러나 추후 연산을 위해서는 리스트를 변수에 할당 해주어야 한다.

* 리스트들이 순차적으로 정렬되어있으므로, 파이썬에서 순차적인 연산들을 할수 있도록 제공해준다.  
아래의 테이블에서 이런 기능들과 어떻게 사용하는지를 나타내준다

| Operation Name | Operator | Explanation                             |
|----------------|----------|-----------------------------------------|
| indexing       | [ ]      | 순차적인 요소에 접근 할수 있게 한다 |
| concatenation  | +        | 순차적 요소들을 합친다 |
| repetition     | *        | 수만큼 반복하여 연결시킨다 |
| membership     | in       | 해당하는 아이템이 안에 있는지 찾는다 |
| length         | len      | 순차적 요소들이 몇개나 있는지 묻는다 |
| slicing        | [ : ]    | 순차적 요소들의 부분을 추출한다 |

* 리스트의 인덱스가 0부터 시작하는것을 기억해두어라.  
슬라이스 연산 myList[1:3]은 인덱스 1부터 3이전까지의 리스트를 반환해 준다.

* 가끔, 리스트를 초기화 하고싶을때 반복을 사용해 쉽게 초기화 할수 있다.

```python
>>> myList = [0] * 6  
>>> myList  
[0, 0, 0, 0, 0, 0]  
```
* 반복 연산자의 중요한 점은 순차적 데이터 객체에서도 레퍼런스를 반복할수도 있다는 것이다 
아래 코드로 확인해 보자

```python
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
```

* 변수 A는 3개의 myList란 이름의 3개의 레퍼런스를 가진 형태의 컬렉션이다.  
myList의 하나의 요소가 바뀌었을때 A 안의 모든 3개의 레퍼런스에서 변동한것을 볼 수 있다.


* 리스트형은 데이터 구조를 만들기 위해 몇개의 메소드를 제공한다. 아래 표에서 그것들의 사용법을 나타낸다.

| Method Name | Use                  | Explanation                                       |
|-------------|----------------------|---------------------------------------------------|
| append      | alist.append(item)   | 리스트의 끝에 새로운 아이템을 추가한다 |
| insert      | alist.insert(i,item) | i번째 위치에 새로운 아이템을 리스트에 추가한다 |
| pop         | alist.pop()          | 리스트의 마지막 아이템을 지우고 그 값을 반환한다 |
| pop         | alist.pop(i)         | i번째 위치에 있는 아이템을 지우고 그 값을 반환한다 |
| sort        | alist.sort()         | 리스트를 정렬한다 |
| reverse     | alist.reverse()      | 리스트를 역으로 정렬한다 |
| del         | del alist[i]         | i번째 위치에 있는 아이템을 삭제한다 |
| index       | alist.index(item)    | 처음으로 아이템이 위치한 인덱스를 반환한다 |
| count       | alist.count(item)    | 아이템이 몇번이나 있는지 갯수를 반환한다 |
| remove      | alist.remove(item)   | 첫번째로 위치한 아이템을 삭제한다 |

```python
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
​
#Examples of List Methods (intro_5)
```

* 여기서 볼 수 있드시, pop 같은 메소드들은 값을 반환하며, 리스트를 변경하는 것을 볼 수 있다.  
reverse 같은 메소드들은 반환 값 없이 리스트만 변경하는 것을 알 수 있다.  
pop은 기본적으로 리스트의 마지막 요소를 대상으로 하고있지만, 몇번째 요소를 pop 시킬시 지정할 수도 있다.  
인덱스 범위가 0 부터 시작하는것은 이 메소드들에도 사용된다.  
또한 dot을 사용해 객체에서 메소드를 실행할수 있다는것을 볼 수 있다.  
myList.append(False) 는 객체인 myList에 append 메소드를 실행하여 False 값을 추가해라 라는 뜻이다.
심지어 단순한 데이터 객체인 integer에서도 이와같이 실행할 수 있다.

```python
>>> (54).__add__(21)  
75  
>>>
```

* 위에서 보듯이 정수형 객체인 54에서 add 메소드를 호출하여 21을 전달하면 결과값인 75가 나온다.  
물론 우리는 보통 54+21로 사용하지만, 이런 메소드들을 추후에 좀더 다룰 것이다.  

* 파이썬의 기능중에 리스트와 흔히 사용되는 기능은 range 펑션이다.  
range는 순차적인 값들이 있는 range 객체를 만든다.  
리스트와 함께 사용한다면, 리스트 형태의 range 객체들의 값을 볼수 있을것이다.  
아래의 코드를 보자

```python
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
```

* range 객체가 순차적인 정수들을 갖고있다. 기본값으로 range는 0부터 시작한다  
만약 파라미터를 더 추가한다면, 시작점과 끝점, 그리고 아이템을 스킵할 수도 있다.
첫번째 예제인 range(10)에서는, 순차적으로 0부터 시작하여 10전 까지 올라간다.  
우리의 두번쨰 예제인 range(5,10)에서는 5부터 시작하여 10 전까지의 리스트를 보여준다.  
range(5,10,2)는 비슷한 역할을 하지만 2씩 스킵한다(마찬가지로 10은 제외)

* 스트링은 0개나 그 이상의 문자가 있는 순차적인 컬렉션이다.  
문자들이란 숫자나 다른 특수문자들도 포함하는 것이다.  
스트링 값들은 따옴표('나 ")를 사용해 다른 값들과 다른 식별자로 표시한다.  

```python
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
```

* 스트링은 순차적이기 때문에, 위에서 봤던 순차적 연산들을 모두 사용할 수 있다.  
또한 아래의 표와 같은 메소드 들도 사용할 수 있다. 예를 들어,

```python
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

* 이런 것들이 있는데, split이 데이터를 처리하는데 매우 유용할 것이다.  
split은 해당하는 스트링에서 스플릿 문자를 이용해 스트링의 리스트를 반환한다.  
위 예제에서는 v가 나뉘는 지점으로 사용되었다.  
만약 나누는 위치가 지정되지 않으면, split 메소드는 \n, 탭, 스페이스등의 공백문자를 사용하여 나눈다.

| Method Name | Use                  | Explanation                                             |
|-------------|----------------------|---------------------------------------------------------|
| center      | astring.center(w)    | w사이즈 만큼의 가운데 정렬된 스트링을 반환한다 |
| count       | astring.count(item)  | 스트링 안의 item이 나타난 횟수를 반환한다 |
| ljust       | astring.ljust(w)     | w사이즈 만큼의 왼쪽 정렬된 스트링을 반환한다 |
| lower       | astring.lower()      | 모두 소문자로된 문자열을 반환한다 |
| rjust       | astring.rjust(w)     | w사이즈 만큼의 오른쪽 정렬된 스트링을 반환한다 |
| find        | astring.find(item)   | 처음 나타난 아이템의 인덱스를 반환한다 |
| split       | astring.split(schar) | schar로 문자열을 나눈다 |

* 리스트와 스트링의 가장 주요한 차이는 리스트는 수정할수 있는 반면에 스트링은 수정할 수 없다는 것이다.  
이것을 변동성이라고 말한다. 리스트는 mutable하지만, 스트링은 immutable하다.  
예를들어, 리스트는 인덱스를 사용하여 안의 아이템을 바꿀수 있지만, 스트링은 그럴 수 없다.

```python
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
```

* 튜플은 다양한 순차적인 데이터로 이루어져 있다는 점에서 리스트와 비슷하다.  
그러나 튜플은 스트링처럼 immutable 하다. 튜플은 변경할 수 없다.  
튜플은 값을 쉼표로 구분하며, 소괄호로 묶인 형태로 쓰여있다.  
순차적인 데이터 이므로, 마찬가지로 순차적 연산을 할 수 있다.

```python
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

* 그러나, 튜플 안에 있는 아이템을 바꾸려고 할 때. 에러가 나올것이다.  
에러 메시지의 위치와 문제의 이유를 잘 살펴 보아라.

```python
>>> myTuple[1]=False

Traceback (most recent call last):
  File "<pyshell#137>", line 1, in -toplevel-
    myTuple[1]=False
TypeError: object doesn't support item assignment
>>>
```
* set은 0개 혹은 그 이상의 파이썬 데이터 오브젝트가 있는 비순차적 컬렉션이다.  
셋은 중복을 허용하지 않고, 컴마로 값을 구분하며 대괄호로 감싸져 있다.  
빈 셋은 set()으로 나타낸다.  
셋 또한 다양한 데이터로 이루어져 있으며, 아래처럼 변수로 할당할 수 있다.

```python
>>> {3,6,"cat",4.5,False}
{False, 4.5, 3, 6, 'cat'}
>>> mySet = {3,6,"cat",4.5,False}
>>> mySet
{False, 4.5, 3, 6, 'cat'}
>>>
```

* 셋은 순차적이지 않지만, 위와 언급된것과 비슷한 기능을 하는 연산자들을 제공한다.  
아래 표에 이 연산들과 사용법을 정리해 놓았다

| Operation Name | Operator         | Explanation                                                       |
|----------------|------------------|-------------------------------------------------------------------|
| membership     | in               | Set membership                                                    |
| length         | len              | set의 크기를 반환한다 |
| |              | aset | otherset  | 두 개 셋에 있는 엘리먼트를 모두 포함한 새로운 셋을 반환한다 |
| &              | aset & otherset  | 두 개 셋 중에 중복되는 엘리먼트만 가지고 있는 새로운 셋을 반환한다 |
| -              | aset - otherset  | 첫번째 셋에 있지만 두번째 셋에는 없는 엘리먼트로 이루어진 새로운 셋을 반환한다 |
| <=             | aset <= otherset | 첫번째 셋의 모든 엘리먼트들이 두번째 셋에 있는지 확인한다 |

```python
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
* 셋은 수학적인 연산들을 해본 사람들에게 친숙한 몇개의 메소드들을 제공하고 있다.  
아래표는 그것들의 사용법을 표시하고있다.  
union, intersection, issubset, difference들은 위의 연산자로도 할수 있다는것을 기억해두어라.  

| Method Name  | Use                         | Explanation                                                    |
|--------------|-----------------------------|----------------------------------------------------------------|
| union        | aset.union(otherset)        | |연산자 와 같은 기능 |
| intersection | aset.intersection(otherset) | & 연산자와 같은 기능 |
| difference   | aset.difference(otherset)   | - 연산자와 같은 기능 |
| issubset     | aset.issubset(otherset)     | <= 연산자와 같은 기능 |
| add          | aset.add(item)              | 셋에 아이템 추가 |
| remove       | aset.remove(item)           | 셋에 아이템 삭제 |
| pop          | aset.pop()                  | 셋에서 임의의 엘리먼트를 삭제한다 |
| clear        | aset.clear()                | 모든 엘리먼트를 삭제한다 |

```python
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

* 마지막으로 살펴볼 비순차적인 데이터 구조는 딕셔너리이다.  
딕셔너리는 키와 밸류 쌍으로 이루어진 컬렉션이다.  
키와 밸류 쌍은 일반적으로 키:밸류 로 쓰여진다.  
딕셔너리는 쉼표로 구분된 키:밸류 쌍들과 대괄호로 감싸져있다.  

```python
>>> capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
>>> capitals
{'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
>>>
```
* 딕셔너리는 키를 입력하거나, 다른 키:밸류 쌍을 추가하여 딕셔너리 데이터를 조작할 수 있다.  
접근하는 문법은 순차적 데이터를 접근할때 인덱스를 넣는것 처럼 키 값으로 접근하면 된다.  
새로운 값을 추가하는 것도 비슷하다.

```python
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)
​
# Using a Dictionary (intro_7)
```

* 딕셔너리는 키값만 있고 특별한 순서가 없다는것에 유의해라.  
첫번째 쌍인 'Utah':'SaltLakeCity'는 딕셔너리의 첫번째로 위치하고있고, 'California':'Sacramento'는 두번째로 추가되었지만 딕셔너리의 맨 마지막에 위치하고 있다.  
키의 위치는 해싱에 따라 결정되는데 챕터 4에서 이를 좀더 자세히 다룰 것이다.  
또한 length펑션은 이전 컬렉션들과 유사한 기능알 할것이다.  

* 딕셔너리 또한 메소드와 연산자를 지니고 있다. 아래의 표와 코드에서 기능을 나타내주고 있다.  
keys, values, items 메소드들은 모두 그것들이 가지고있는 값들을 반환한다.  
또한 list 기능을 사용해 리스트 형태로 변환할 수 있다.  
또한 get 메소드가 두가지 형태로 존재한다는 것을 알수 있을 것이다.  
키가 현재 딕셔너리에 존재하지 않는다면, get은 None을 리턴해줄 것이다.  
그러나 옵션 파라미터를 추가하면 None대신 할 리턴값을 지정할 수 있다

| Operator | Use            | Explanation                                                 |
|----------|----------------|-------------------------------------------------------------|
| []       | myDict[k]      | 키 k와 연관된 값 반환, 없을시 에러 |
| in       | key in adict   | 딕셔너리에 키가 존재하면 true, 없으면 false |
| del      | del adict[key] | 딕셔너리의 해당하는 키 밸류쌍을 지운다 |

```python
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

| Method Name | Use              | Explanation                                                  |
|-------------|------------------|--------------------------------------------------------------|
| keys        | adict.keys()     | 딕셔너리의 키들을 반환한다 |
| values      | adict.values()   | 딕셔너리의 밸류들을 반환한다 |
| items       | adict.items()    | 딕셔너리의 키:밸류 쌍들을 반환한다 |
| get         | adict.get(k)     | 키값 k의 밸류를 반환하고 없으면 None을 반환 |
| get         | adict.get(k,alt) | 키값 k의 밸류를 반환하고 없으면 대체값을 반환 |
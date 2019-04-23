# 1.13. Object-Oriented Programming in Python: Defining Classes

파이썬의 객체지향 프로그래밍 :  클래스 정의하기

We stated earlier that Python is an object-oriented programming language. 

우리는 이전에 파이썬은 객체지향언어라고 언급 했었다. 

So far, we have used a number of built-in classes to show examples of data and control structures. 

지금까지 우리는 데이터와 구조체들을 다루기는 예제를 보여주기 위해  몇개의 내장된 클래스를 사용했다. 

One of the most powerful features in an object-oriented programming language is the ability to allow a programmer (problem solver) to create new classes that model data that is needed to solve the problem.

객체지향프로그래밍 언어의 가장 강력한 특징은 프로그래머에게 문제해결을 위해 필요한 데이터를 만드는 새로운 클래스를 생성할 수 있다는 것이다. 

Remember that we use abstract data types to provide the logical description of what a data object looks like (its state) and what it can do (its methods). 

우리는 추상데이터 타입을 사용함으로서 데이터 객체가 어떻게 생겼는지(상태) 그것이 뭘 할수 있는지(메서드) 를 논리적으로 설명할 수 있다는걸 기억하라.

By building a class that implements an abstract data type, a programmer can take advantage of the abstraction process and at the same time provide the details necessary to actually use the abstraction in a program. 

추상데이터타입을 사용하는 클래스를 만들어서 프로그래머는 추상화의 장점을 취할 수 있고 동시에 프로그램에 추상화를 실제로 사용하기 위해 필요한 세부사항을 제공할 수 있다. 

Whenever we want to implement an abstract data type, we will do so with a new class.

너가 추상데이터타입을 구현하기 원할때 마다 새로운 클래스를 만들면 된다. 

## 1.13.1. A Fraction Class 분수클래스

A very common example to show the details of implementing a user-defined class is to construct a class to implement the abstract data type Fraction. 

사용자 정의 클래스의 구현세부사항을 보여주는 매우 흔한 예는 추상데이터타입인 분수를 구현한 클래스를 만드는 것이다. 

We have already seen that Python provides a number of numeric classes for our use. 

우리는 이미 파이썬이 몇개의 숫자클래스들을 제공하는걸 봤다. 

There are times, however, that it would be most appropriate to be able to create data objects that “look like” fractions.

그러나, 분수처럼 "보이는" 데이터 객체를 생성하는것이 가장 적절할 때가 있다.

A fraction such as 3/5 consists of two parts. 

3/5 같이 분수는 두 부분으로 구성돼있다.

The top value, known as the numerator, can be any integer. 

분자라고 알려진 윗 부분은 어떤 정수도 가능하다.

The bottom value, called the denominator, can be any integer greater than 0 (negative fractions have a negative numerator). 

분모라고 불리는 아랫부분은 0보다 큰 어떤 정수도 가능하다.(음수분수는 음수분자를 가진다.)

Although it is possible to create a floating point approximation for any fraction, in this case we would like to represent the fraction as an exact value

비록 어떤 분수도 부동소수점 추정을 만들 수 있지만, 이 경우에서 우리는 분수를 정확한 값 그대로 나타내고 싶다. 

The operations for the Fraction type will allow a Fraction data object to behave like any other numeric value. 

분수타입을 위한 연산들은 분사객체가 다른 어떤 숫자값처럼 쓰일수 있도록 한다.

We need to be able to add, subtract, multiply, and divide fractions. 

우리는 분수의 덧셈, 뺄셈, 곱셈, 나눗셈이 가능해야 한다.

We also want to be able to show fractions using the standard “slash” form, for example 3/5.

3/5 처럼 우리는 일반적인 분수 표현인 슬래시 형태를 사용했으면 좋겠다. 

 In addition, all fraction methods should return results in their lowest terms so that no matter what computation is performed, we always end up with the most common form.

추가적으로, 모든 분수메서드들은 가장 작은 값으로 결과를 반환해서 ,어떤 연산이 수행됐던지 항상 가장 일반적인 형태로 끝나야 한다.

In Python, we define a new class by providing a name and a set of method definitions that are syntactically similar to function definitions. For this example,

파이썬에서 우리는 함수 정의와 유사한 문법으로 이름과 메서드정의를 제공해 클래스를 정의한다. 예를들어,

    class Fraction:
    
       #the methods go here

provides the framework for us to define the methods. 

위는 우리에게 메서드를 정의하기 위한 프레임워크를 제공한다. 

The first method that all classes should provide is the constructor. 

모든 클래스가 제공해야하는 첫번째 메서드는 생성자이다. 

The constructor defines the way in which data objects are created. 

생성자는 어떤 데이터객체가 생성될지를 정의한다. 

To create a Fraction object, we will need to provide two pieces of data, the numerator and the denominator.

분수객체를 생성하기 위해서 우리는 분모,분자의  두 데이터를 제공해야 한다.

 In Python, the constructor method is always called **init** (two underscores before and after init) and is shown in Listing 2.

 Listing 2 에서 보이는것 처럼 파이썬에서 생성자는 항상 초기화를 호출한다.(초기화 전후의 두 밑줄)

 Listing 2

    class Fraction:
    
        def __init__(self,top,bottom):
    
            self.num = top
            self.den = bottom

Notice that the formal parameter list contains three items (`self`, `top`, `bottom`). 

파라미터가 self, top, bottom을 가지고 있는걸 봐라.

`self` is a special parameter that will always be used as a reference back to the object itself. 

`self`  는 객체 자체로 참조로 항상 사용될 특별한 파라미터 이다. 

It must always be the first formal parameter; however, it will never be given an actual parameter value upon invocation.

그것은 항상 첫번째 파리미터여야 한다. 그러나 호출로 실제 값을 주진 않는다.

 As described earlier, fractions require two pieces of state data, the numerator and the denominator. 

앞서 말했듯이 분수는 분자 와 분모 두가지 종류의 데이터가 필요하다.

The notation `self.num` in the constructor defines the `fraction` object to have an internal data object called `num` as part of its state. 

생성자에서  `self.num` 구문은 분수객체가 그것의 상태로 num이라 불리는 내부데이터를 가진다는걸 정의한다.

Likewise, `self.den` creates the denominator. 

마찬가지로  `self.den` 는 분모를 만든다.

The values of the two formal parameters are initially assigned to the state, allowing the new `fraction` object to know its starting value.

두 파라미터 값은 처음에 상테에 할당왜서 새로운 분수 객체가 그것의 시작값을 알 수 있게 한다. 

To create an instance of the `Fraction` class, we must invoke the constructor. 

분수클래스의 인스턴스 생성을 위해 우리는 생성자를 호출해야 한다.

This happens by using the name of the class and passing actual values for the necessary state (note that we never directly`invoke __init__`). For example,

클래스명과 필수 state 실제값을 넘겨서 발생한다.( 절대 직접`invoke __init__`를 호출하지 않는다.)

    myfraction = Fraction(3,5)

creates an object called myfraction representing the fraction 35 (three-fifths). 

3/5 (오분의삼) 을 나타내는 myfraction이라고 불리는 분수 객체  를 생성한다.

Figure 5 shows this object as it is now implemented.

그림 5는 객체가 이제 구현됐단걸 보여준다.

![](Untitled-16bca5ee-bc4b-4f48-9540-b198a0d657fa.png)

The next thing we need to do is implement the behavior that the abstract data type requires. 

다음으로 해야하는 일은 추상데이터타입이 요구하는 행동을 구현하는것이다.

To begin, consider what happens when we try to print a Fraction object.

먼저, 분수객체를 출력하려할때 어떻게 될지 생각해보자.

    >>> myf = Fraction(3,5)
    >>> print(myf)
    <__main__.Fraction instance at 0x409b1acc>

The `fraction` object, `myf`, does not know how to respond to this request to print. 

fraction객체인 myf 은 출력요청에 어떻게 반응해야하는지 모른다. 

The `print` function requires that the object convert itself into a string so that the string can be written to the output. 

print 함수는 객체가 자신을 결과물로 쓰일 수 있는 문자열로 바꾸는걸 요구한다.

The only choice `myf` has is to show the actual reference that is stored in the variable (the address itself). 

변수가 저장하고 있는 진짜 참조값(자신의 주소)을 보여주는게 myf가 가진 유일한 선택이다.

This is not what we want.

이건 우리가 원하는 바가 아니다.

There are two ways we can solve this problem. 

이 문제를 해결하기 위해 2가지 방법이 있다. 

One is to define a method called `show` that will allow the `Fraction` object to print itself as a string. 

첫번째는 show라는 메서드를 정의해서 fraction객체자신을 문자열로 출력하도록 하는것이다. 

We can implement this method as shown in [Listing 3](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-showmethod). 

우린 Listing 3에서 보이는것 같이 구현할 수 있다. 

If we create a `Fraction` object as before, we can ask it to show itself, in other words, print itself in the proper format.

우리가 Fraction 객체를 전처럼 만든다면 우린 객체에게 적당한 형식으로 출력되게 요청할 수 있다.

 Unfortunately, this does not work in general.

안타깝게도, 이것은 일반적으로 잘 동작하지 않는다. 

 In order to make printing work properly, we need to tell the `Fraction` class how to convert itself into a string.

알맞게 출력되기 위해선 Fraction 클래스에게 자신을 어떻게 문자열로 변환해야하는지 알려줘야 한다.

 This is what the `print` function needs in order to do its job.

이것이 print함수가 그 동작을 하기위해 필요한 것이다. 

**Listing 3**

    def show(self):
         print(self.num,"/",self.den)

    >>> myf = Fraction(3,5)
    >>> myf.show()
    3 / 5
    >>> print(myf)
    <__main__.Fraction instance at 0x40bce9ac>
    >>>

In Python, all classes have a set of standard methods that are provided but may not work properly. 

파이썬에서 모든 클래스는 제공하지만 제대로 동작하지 않는 메서드들을 가지고 있다.

One of these, `__str__`, is the method to convert an object into a string. 

그중 하나가  `__str__` 인데, 객체를 문자열로 바꿔준다.

The default implementation for this method is to return the instance address string as we have already seen. 

이 메서드의 기본 구현은 앞서 본것처럼 주소문자열을 반환하는 것이다. 

What we need to do is provide a “better” implementation for this method. 

우리에게 필요한건 이 메서드의 좀 더 나은 구현이다. 

We will say that this implementation **overrides** the previous one, or that it redefines the method’s behavior.

우리는 이전구현사항을 오버라이드 했다 또는  메서드의 동작을 재 정의 했다라고 한다.

To do this, we simply define a method with the name `__str__` and give it a new implementation as shown in [Listing 4](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-str). 

이렇게 하기 위해선 우리는 단순히  `__str__` 이름의 메서드를 정의하고 Listing4처럼 새로운 구현을 하면 된다.

This definition does not need any other information except the special parameter`self`. 

이 정의에는 self라는 특별한 파라미터 외에는 다른 정보는 필요하지 않는다. 

In turn, the method will build a string representation by converting each piece of internal state data to a string and then placing a `/` character in between the strings using string concatenation. 

그리고 그 메서드는 문자열 연결을 이용해서 내부상태데이터를 문자열로 바꾸고 사이에 /를 넣어 문자열 표현식을 만들것이다. 

The resulting string will be returned any time a `Fraction` object is asked to convert itself to a string.

결과 문자열은 Fraction객체가 자신을 문자열로 바꾸길 원할때마다 반환될 것이다.

 Notice the various ways that this function is used.

이 함수가 사용되는 다양한 방식을 봐라. 

**Listing 4**

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    >>> myf = Fraction(3,5)
    >>> print(myf)
    3/5
    >>> print("I ate", myf, "of the pizza")
    I ate 3/5 of the pizza
    >>> myf.__str__()
    '3/5'
    >>> str(myf)
    '3/5'
    >>>

We can override many other methods for our new `Fraction` class. 

우리의 Fraction 클래스를 위해 다른 많은 메서드를 오버라이드 할 수 있다. 

Some of the most important of these are the basic arithmetic operations. 

이것들중 가장 중요한 것은 기본적인 산술연산이다. 

We would like to be able to create two `Fraction` objects and then add them together using the standard “+” notation. 

우리는 두개의  `Fraction` 객체를 만들어서 표준인 +연산자를 이용해 더하고 싶다.

At this point, if we try to add two fractions, we get the following:

이시점에서  두 분수를 더하려 한다면 우린 다음과 같이 한다.

    >>> f1 = Fraction(1,4)
    >>> f2 = Fraction(1,2)
    >>> f1+f2
    
    Traceback (most recent call last):
      File "<pyshell#173>", line 1, in -toplevel-
        f1+f2
    TypeError: unsupported operand type(s) for +:
              'instance' and 'instance'
    >>>

If you look closely at the error, you see that the problem is that the “+” operator does not understand the `Fraction` operands.

에러를 자세하게 본다면 +연산자가  `Fraction` 연산을 이해하지 못하는 문제를 볼 수 있다. 

We can fix this by providing the `Fraction` class with a method that overrides the addition method. 

 `Fraction` 클래스에 더하기 메서드를 오버라이드 함으로서 이 문제를 고칠 수 있다.

In Python, this method is called `__add__` and it requires two parameters. 

파이썬에서 메서드 __add__ 는 두개의 파라미터를 필요로 한다.

The first, `self`, is always needed, and the second represents the other operand in the expression. For example,

첫번째로 self는 항상 필요한것이고 두번째는 표현의 다른 피연산함수를 나타낸다. 예를들어

    f1.__add__(f2)

would ask the `Fraction` object `f1` to add the `Fraction` object `f2` to itself. 

 `Fraction` 객체f1 에게  `Fraction` 객체인 f2를 더하라고 할 수 있다.

This can be written in the standard notation, `f1+f2`.

이건 표준적인 표기법인 f1+f2로 쓰일 수 있다. 

Two fractions must have the same denominator to be added.

분수가 더해지기 위해선 같은 분모를 가지고 있어야 한다. 

 The easiest way to make sure they have the same denominator is to simply use the product of the two denominators as a common denominator so that ab+cd=adbd+cbbd=ad+cbbdab+cd=adbd+cbbd=ad+cbbd The implementation is shown in [Listing 5](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-addmethod). 

그들이 같은 분모를 가지게 하기위한 가장 쉬은 방법은 Listing5에 보이는것처럼 단순히 두 문모의 곱을 공통분모로 사용하는 것이다. 

The addition function returns a new `Fraction` object with the numerator and denominator of the sum. 

더하기 함수는 합계의 분모 분자를 가지는  새로운  `Fraction` 객체를 반환한다.

We can use this method by writing a standard arithmetic expression involving fractions, assigning the result of the addition, and then printing our result.

우리는 분수에 관련된 표준연산기호를 써서 덧셈의 결과를 결과에 할당하고 그 결과를 출력하는 이 메서드를 사용할 수 있다.

**Listing 5**

    def __add__(self,otherfraction):
    
         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
    
         return Fraction(newnum,newden)

    >>> f1=Fraction(1,4)
    >>> f2=Fraction(1,2)
    >>> f3=f1+f2
    >>> print(f3)
    6/8
    >>>

The addition method works as we desire, but one thing could be better. 

덧셈메서드는 우리가 바라는 대로 동작하지만 더 좋아질 수 있다. 

Note that 6/8 is the correct result (1/4+1/2) but that it is not in the “lowest terms” representation. 

6/8은 맞는 결과이지만 기약분수는 아니다.

The best representation would be 3/4. 

가장 좋은 표현은 3/4 일 것이다.

In order to be sure that our results are always in the lowest terms, we need a helper function that knows how to reduce fractions.

결과가 항상 기약분수이기 위해서는 분수를 약분하는 helper함수가 필요하다.

 This function will need to look for the greatest common divisor, or GCD. 

이 함수는 최대공약수 즉 GCD를 찾아야 한다.

We can then divide the numerator and the denominator by the GCD and the result will be reduced to lowest terms.

우리는 분자,분모를 최대공약수로 나눠서 결과를 기약분수로 만들 수 있다. 

The best-known algorithm for finding a greatest common divisor is Euclid’s Algorithm, which will be discussed in detail in Chapter 8. 

최대공약수를 구하는 가장 잘 알려진 알고리즘은 Euclid’s  알고리즘인데, 자세한것은 8장에서 다룰것이다.

Euclid’s Algorithm states that the greatest common divisor of two integers m and n is n if n divides m evenly.

두 정수 m 과 n 가운데 만약 n이 m을 딱 떨어지게 나눈다면 n 이 두 정수의 최대공약수이다.

However, if n does not divide m evenly, then the answer is the greatest common divisor of n and the remainder of m divided by n. 

그러나, n이 m을 딱 떨어지게 못나눈다면 n과 m을 n으로 나눈 나머지의 최대공약수가 답이다.

 We will simply provide an iterative implementation here (see [ActiveCode 1](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-gcd)). 

우리는 간단하게 반복 구현을 제공했다 .(ActiveCode 1을 보라)

Note that this implementation of the GCD algorithm only works when the denominator is positive.

GCD알고리즘의 구현은 분모가 양수일때만 동작한다는걸 유념해라.

 This is acceptable for our fraction class because we have said that a negative fraction will be represented by a negative numerator.

이 점은 음의 분수는 음의 분자로 표현된다고 전에 말했으니  우리의 분수클래스에서 괜찮다.

Now we can use this function to help reduce any fraction. 

이제 우리는 이 함수를 이용해서 어떤 분수도 약분할 수 있다. 

To put a fraction in lowest terms, we will divide the numerator and the denominator by their greatest common divisor. 

기약분수로 만들기 위해 우리는 분모분자를 그들의 최대공약수로 나눌것이다.

So, for the fraction 6/8, the greatest common divisor is 2. 

따라서 분수6/8 이 최대공약수인 2로 나뉜다.

Dividing the top and the bottom by 2 creates a new fraction, 3/4 (see [Listing 6](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-newaddmethod)).

분모 분자를 2로 나눠서 새로운 분수인 3/4로 만들었다. (Listing6 참고)

**Listing 6**

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    >>> f1=Fraction(1,4)
    >>> f2=Fraction(1,2)
    >>> f3=f1+f2
    >>> print(f3)
    3/4
    >>>

![](Untitled-696e51a1-5089-4bd6-99a9-f03af83ca0ce.png)

Our `Fraction` object now has two very useful methods and looks like [Figure 6](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-fraction2). 

우리의  `Fraction` 객체는 그림 6에서 보이는것같이 매우 유용한 두개의 메서드를 가졌다.

An additional group of methods that we need to include in our example `Fraction` class will allow two fractions to compare themselves to one another. 

우리의 예제 `Fraction` 클래스에서 추가적으로 포함할 메서드들은 두 분수를 서로 비교하는것이다.

Assume we have two `Fraction` objects, `f1` and `f2`.

f1,f2두   `Fraction` 객체가 있다고 가정해보자.

 `f1==f2` will only be `True` if they are references to the same object.

f1==f2는 두 객체가 같은값을 참조할 때만 참 일것이다.

 Two different objects with the same numerators and denominators would not be equal under this implementation. 

이런 구현으로는 분모 분자가 같은 두 객체는 equal이 아닐것이다.

This is called **shallow equality** (see [Figure 7](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-fraction3)).

이것은 얕은균등이라고 한다.

![](http://interactivepython.org/courselib/static/pythonds/_images/fraction3.png)

We can create **deep equality** (see [Figure 7](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-fraction3))–equality by the same value, not the same reference–by overriding the `__eq__` method.

우리는 __eq __메서드를 오버라이딩 함으로서 같은참조가 가 아니라 같은 값으로 동등을 판단하는 깊은 동등 만들 수 있다. 

 The `__eq__` method is another standard method available in any class. 

__eq __는 모든 클래스에서 사용가능한 표준 메서드 이다.

The `__eq__` method compares two objects and returns `True` if their values are the same, `False`otherwise.

__eq __ 는 두 객체의 값이 같으면 참을 아니면 거짓을 반환한다. 

In the `Fraction` class, we can implement the `__eq__` method by again putting the two fractions in common terms and then comparing the numerators (see [Listing 7](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-cmpmethod)).

이 클래스에서 우리는 두 분수를 공통분모로 놓고 분자를 비교해서__eq __ 를 구현 할 수 있다. (listing 7)

 It is important to note that there are other relational operators that can be overridden.

여기서 오버라이드 도리 수있는 다른 관련 연산자가 있다는걸 아는게 중요하다. 

 For example, the `__le__` method provides the less than or equal functionality.

예를들어  `__le__` 메서드는 작거나 같다 기능을 수행한다. 

**Listing 7**

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum == secondnum

The complete Fraction class, up to this point, is shown in ActiveCode 2. 

지금까지의 완성된 분수 클래스는 ActiveCode 2. 에서 볼 수 있다. 

We leave the remaining arithmetic and relational methods as exercises.

나머지 산술, 비교 메서드는 연습으로 남겨놨다. 

**Self Check**

To make sure you understand how operators are implemented in Python classes, and how to properly write methods, write some methods to implement `*, /,` and `-` . Also implement comparison operators > and <

파이썬 클래스들에서 어떻게 연산이 동작하는지 이해하기 위해서, 그리고 적절하게 메서드를 작성하기 위해서 곱하기, 나누기, 빼기 메서드를 구현하라. 또한 비교 연산자인 >,< 도 구현해라.

# **1.13.2. Inheritance: Logic Gates and Circuits**

상속 : 논리게이트 와 순회

Our final section will introduce another important aspect of object-oriented programming. 

우리의 마지막장은 객체지향프로그래밍의 또다른 중요한 측면을 소개할것이다.

**Inheritance** is the ability for one class to be related to another class in much the same way that people can be related to one another.

상속은 사람이 다른 사람과 연관된 방식같이 하나의 클래스를 다른 클래스와 연관하는 것이다.

 Children inherit characteristics from their parents.

아이들은 그들의 부모의 특성을 상속받는다.

Similarly, Python child classes can inherit characteristic data and behavior from a parent class. 

유사하게, 파이썬 자식 클래스는 부모 클래스의 특징적인 데이터와 행동을 상속받을 수 있다.

These classes are often referred to as **subclasses** and **superclasses**.

이런 클래스들은 서브클래스 와 슈퍼클래스로 종종 불린다.

[Figure 8](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-inherit1) shows the built-in Python collections and their relationships to one another. 

그림 8 은 내장된 파이썬 콜랙션과 서로의 관계를 보여준다.

We call a relationship structure such as this an **inheritance hierarchy**. 

우린 이런 관계구조를 상속계층이라고 부른다.

For example, the list is a child of the sequential collection.

예를들어 리스트는 순차적인컬렉션의 자식이다.

 In this case, we call the list the child and the sequence the parent (or subclass list and superclass sequence). 

이런 경우에 우리는 리스트를 자식 그리고 시퀀스을 부모라고 부른다.(또는 리스트를 서브클래스 시퀀스를 슈퍼클래스라고 한다.)

This is often referred to as an `IS-A Relationship` (the list **IS-A** sequential collection).

이것은 종종 IS-A 관계로도 불린다.

 This implies that lists inherit important characteristics from sequences, namely the ordering of the underlying data and operations such as concatenation, repetition, and indexing.

이것은 리스트가  내제된데이터의 정렬 그리고 연결, 반복, 인덱싱 연산 같은  시퀀스의 중요한 특징들을 상속받고있다는걸 내포한다.

![](http://interactivepython.org/courselib/static/pythonds/_images/inheritance1.png)

Lists, tuples, and strings are all types of sequential collections. 

리스트, 튜블 그리고 문자열을 시퀀셜컬렉션 타입니다.

They all inherit common data organization and operations.

그들은 모두 공통된 데이터 구조와 연산을 상속받는다.

 However, each of them is distinct based on whether the data is homogeneous and whether the collection is immutable. 

그러나 각각은 데이터가 동종인지와 그 콜렉션이 불변한가에 따라 구분된다.

The children all gain from their parents but distinguish themselves by adding additional characteristics.

자식들은 모두 그들의 부모로 부터 생성됐지만 추가적인 특징을 가지며 구분된다.

By organizing classes in this hierarchical fashion, object-oriented programming languages allow previously written code to be extended to meet the needs of a new situation.

이런 상속적인 방법으로 클래스들을 만들면, 객체지향언어들은 새로운 상황의 필요성에 맞게 기존 코드를 확장할수있다.

 In addition, by organizing data in this hierarchical manner, we can better understand the relationships that exist. 

더불어, 이런 상속방식으로 데이터를 만들어서 관계를 더 잘 이해할 수 있다.

We can be more efficient in building our abstract representations.

To explore this idea further, we will construct a **simulation**, an application to simulate digital circuits. 

이 개념을 더 잘 이해하기위해 우리는 디지털 회로 시뮬레이션을 만들것이다.

The basic building block for this simulation will be the logic gate. 

이 시뮬레이션은 논리게이트를 만드는것이다.

These electronic switches represent boolean algebra relationships between their input and their output. 

이 전자기적 스위치는 인풋과 아웃풋간의 연산대수학관계를 나타낸다.

In general, gates have a single output line. 

일반적으로 게이트는 하나의 결과 라인을 갖는다.

The value of the output is dependent on the values given on the input lines.

이 아웃풋은 주어진 인풋값에 달려있다.

AND gates have two input lines, each of which can be either 0 or 1 

AND게이트는 0또는1의 두 인풋을 갖는다.

(representing `False` or `True`, repectively). 

(각각 참 또는 거짓을 나타낸다.)

If both of the input lines have the value 1, the resulting output is 1.

두 인풋이 모두 1이면 결과는 1이다.

 However, if either or both of the input lines is 0, the result is 0. 

그러나 하나 또는 두 인풋이 0이면 결과는 0이다.

OR gates also have two input lines and produce a 1 if one or both of the input values is a 1.

OR게이트 역시 두개의 인풋을 받아서 하나 또는 두개의 인풋값이 1이면 1을 생산한다.

 In the case where both input lines are 0, the result is 0.

이 경우에서 둘다 0을 받으면 결과는 0이다. 

NOT gates differ from the other two gates in that they only have a single input line. 

NOT게이트는 앞선 두 게이트와는 다르게 하나의 인풋을 가진다.

The output value is simply the opposite of the input value.

아웃풋은 단순히 인풋값의 반대값이다.

 If 0 appears on the input, 1 is produced on the output.

0이 들어오면 1이 아웃풋이다.

Similarly, 1 produces 0. 

비슷하게 1은 0을 결과로 갖는다.

[Figure 9](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-truthtable) shows how each of these gates is typically represented. 

그림9는 이 게이트들이 전형적으로 나타내는것을 보여준다.

Each gate also has a **truth table** of values showing the input-to-output mapping that is performed by the gate.

각 게이트는 게이트를 통해 수행되는 인풋과 아웃풋의 매핑값을 보여주는 진리표를 갖는다.

![](http://interactivepython.org/courselib/static/pythonds/_images/truthtable.png)

By combining these gates in various patterns and then applying a set of input values, we can build circuits that have logical functions. 

이 게이트들은 다양항 형식과 인풋값들로 으로 조합하해서, 우린 논리적 기능을 가지는 회로를 만들 수 있다. 

[Figure 10](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-circuit1) shows a circuit consisting of two AND gates, one OR gate, and a single NOT gate. 

그림10은 두개의AND 하나의 OR 그리고 하나의 NOT으로 구성된 회로이다.

The output lines from the two AND gates feed directly into the OR gate, and the resulting output from the OR gate is given to the NOT gate. 

두개의 AND게이트의 결과는 즉시 OR 게이트로 들어가고 그 결과는 NOT게이트로 들어간다.

If we apply a set of input values to the four input lines (two for each AND gate), the values are processed and a result appears at the output of the NOT gate.

만약 우리가 4개의 인풋라인을 적용한다면 (두 AND게이트를 위한) NOT게이트를 통해서 하나의 결과값으로 처리된다.

 [Figure 10](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-circuit1) also shows an example with values.

그림 10은 값들의 예시이다.

![](http://interactivepython.org/courselib/static/pythonds/_images/circuit1.png)

In order to implement a circuit, we will first build a representation for logic gates. 

이 회로를 구현하기 위해서는 우리는 먼저 논리게이트를 만들어야 한다.

Logic gates are easily organized into a class inheritance hierarchy as shown in [Figure 11](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-gates).

논리게이트는 그림 11에서 보이는것처럼 상속을받는 클래스를 통해 쉽게 구현할 수 있다.

 At the top of the hierarchy, the `LogicGate` class represents the most general characteristics of logic gates: namely, a label for the gate and an output line. 

계층의 가장 윗부분에서, `LogicGate` 클래스는 논리게이트의 가장 일반적인 특성을 나타낸다 : 즉 라벨과 결과라인이다.

The next level of subclasses breaks the logic gates into two families, those that have one input line and those that have two. 

다음단계의 서브클래스에서는 로직게이트를 하나의 인풋 또는 두개의 인풋을 갖는두개의  가족으로 나뉜다.

Below that, the specific logic functions of each appear.

아래에 보면, 각각의 특정한 논리기능들을 볼 수 있다. 

![](http://interactivepython.org/courselib/static/pythonds/_images/gates.png)

We can now start to implement the classes by starting with the most general, `LogicGate`. 

우리는 가장일반적인 `LogicGate` 클래스를 구현함으로서 시작할 수 있다. 

As noted earlier, each gate has a label for identification and a single output line.

이전에 언급했듯이, 각 게이트는 식별을 위한 라벨과 하나의 결과라인을 가진다.

 In addition, we need methods to allow a user of a gate to ask the gate for its label.

더불어, 우리는 그 게이트의 라벨을 붙이는 메서드가 필요하다.

The other behavior that every logic gate needs is the ability to know its output value. 

또 모든 로직게이트가 필요로 하는 기능은 그것의 결과값을 알리는거다.

This will require that the gate perform the appropriate logic based on the current input. 

현재 인풋을 기반으로 게이트의 적당한 논리를 수행하는것이 필요하다.

In order to produce output, the gate needs to know specifically what that logic is.

결과를 산출하기 위해선, 게이트는 그 논리가 무엇인지 자세하게 알아야 한다.

 This means calling a method to perform the logic computation. 

논리를 연산하기위해 수행할 메서드를 호출함을 의미한다.

The complete class is shown in [Listing 8](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-logicgateclass).

온전한 클래스는 리스팅 8과 같다.

**Listing 8**

    class LogicGate:
    
        def __init__(self,n):
            self.label = n
            self.output = None
    
        def getLabel(self):
            return self.label
    
        def getOutput(self):
            self.output = self.performGateLogic()
            return self.output

At this point, we will not implement the `performGateLogic` function.

지금시점에서는 우린  `performGateLogic`  함수를 구현하지 않을것이다.

 The reason for this is that we do not know how each gate will perform its own logic operation. 

왜냐하면 우리는 각 게이트의 고유한 논리연산이 무엇인지 모르기 때문이다.

Those details will be included by each individual gate that is added to the hierarchy.

이런 세부사항은 각 게이트가 계층에 추가될때 포함될 것이다.

 This is a very powerful idea in object-oriented programming. 

이것은 객체지향프로그래밍의 매우 중요한 개념이다.

We are writing a method that will use code that does not exist yet. 

우리는 아직 존재하지 않지만 곧 사용될 메서드를 작성한다.

The parameter `self` is a reference to the actual gate object invoking the method. 

 `self` 파라미터는 메서드를 호출하는 실제 객체를 참조이다.

Any new logic gate that gets added to the hierarchy will simply need to implement the `performGateLogic` function and it will be used at the appropriate time. 

계층에 추가되는 어떤 새로운 논리게이트라도 단순히  `performGateLogic` 함수를 구현하면 되고 그것은 적절히 사용될것이다.

Once done, the gate can provide its output value. 

그게 되면 게이트는 결과값을 제공할 수 있다. 

This ability to extend a hierarchy that currently exists and provide the specific functions that the hierarchy needs to use the new class is extremely important for reusing existing code.

존재하는 계층을 확장하고 새로운 클래스에서 사용할 특정 함수를 제공하는것은 이미 존재하는 코드를 재사용함에 있어서 매우 중요하다. 

We categorized the logic gates based on the number of input lines.

우리는 인풋의 개수로 논리게이트를 구분했다.

 The AND gate has two input lines. The OR gate also has two input lines. 

AND ,OR게이트는 2개의 인풋라인을 갖는다.

NOT gates have one input line. 

NOT게이트는 하나의 인풋라인을 갖는다.

The `BinaryGate` class will be a subclass of `LogicGate` and will add two input lines. 

이원게이트는 2개의 인풋을 갖는데 LogicGate 의 하위 클래스가 될것이다.

The `UnaryGate` class will also subclass `LogicGate`but will have only a single input line.

단일게이트 또한 LogicGate의 하위 클래스인데 하나의 인풋라인을 갖을것이다.

 In computer circuit design, these lines are sometimes called “pins” so we will use that terminology in our implementation.

컴퓨터회로에서 이 라인들은 pins이라고 불리기도 하는데 이것을 우리 구현의 용어로 사용할거다.

**Listing 9**

    class BinaryGate(LogicGate):
    
        def __init__(self,n):
            LogicGate.__init__(self,n)
    
            self.pinA = None
            self.pinB = None
    
        def getPinA(self):
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
    
        def getPinB(self):
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))

**Listing 10**

    class UnaryGate(LogicGate):
    
        def __init__(self,n):
            LogicGate.__init__(self,n)
    
            self.pin = None
    
        def getPin(self):
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

[Listing 9](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-logicgateclass) and [Listing 10](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-logicgateclass) implement these two classes.

9,10 은 두 클래스를 구현했다.

The constructors in both of these classes start with an explicit call to the constructor of the parent class using the parent’s `__init__` method. 

두 클래스들의 생성자는 부모의 init메서드를 이용해 부모의 생성자를 호출한다.

When creating an instance of the `BinaryGate` class, we first want to initialize any data items that are inherited from`LogicGate`. 

이원게이트 클래스의 인스턴스를 생성할때, 우리는 논리게이트에서 상속받은 데이터로 초기화 되길 원한다.

In this case, that means the label for the gate.

이 경우에선 게이트의 라벨을 의미한다.

 The constructor then goes on to add the two input lines (`pinA` and `pinB`). 

생성자는 두 인풋라인인 pinA, pinB를 추가한다.

This is a very common pattern that you should always use when building class hierarchies. 

이것은 당신이 클래스계층을 구현할때 항상 사용한 매우 일반적인 방식이다. 

Child class constructors need to call parent class constructors and then move on to their own distinguishing data.

자식클래스 생성자는 부모클래스 생성자를 호출해야하고 그들고유의 데이트로 옮겨진다.

Python also has a function called `super` which can be used in place of explicitly naming the parent class.

파이썬 역시 super라고 불리는 함수가 있는데 부모클래스의 명시적인 이름 대신에 사용할 수 있다. 

 This is a more general mechanism, and is widely used, especially when a class has more than one parent. 

이것은 더 일반적인 구조이고 특히 클래스가 하나 이상의 부모를 가질때 널리 사용된다.

But, this is not something we are going to discuss in this introduction. 

하지만, 이것은 우리가 이 소개부분에서 다룰 내용이 아니다.

For example in our example above`LogicGate.__init__(self,n)` could be replaced with `super(UnaryGate,self).__init__(n)`.

위의 `LogicGate.__init__(self,n)` 부분은  `super(UnaryGate,self).__init__(n)` 로 대체될 수 있다.

The only behavior that the `BinaryGate` class adds is the ability to get the values from the two input lines.

이항게이트가 추가한 유일한 기능은 두개의 인풋라인을 받는것이다.

 Since these values come from some external place, we will simply ask the user via an input statement to provide them. 

이 값들은 외부에서 받을것이기 때문에 우리는 단순히 input 구문을 사용해서 사용자에게 요청할 수 있다.

The same implementation occurs for the `UnaryGate` class except that there is only one input line.

단일게이트 클래스도 인풋라인이 하나라는것만 빼면 동일하다.

Now that we have a general class for gates depending on the number of input lines, we can build specific gates that have unique behavior. 

이제 인풋의 개수에 따라 두개의 일반적인 게이트 클래스가 있으니 , 우리는 각각의 고유의 기능을 만들면 된다.

For example, the `AndGate` class will be a subclass of `BinaryGate`since AND gates have two input lines. 

예를들어 AND게이트 클래스는 2개의 인풋을 가지니 이항게이트의 자식클래스가 될것이다.

As before, the first line of the constructor calls upon the parent class constructor (`BinaryGate`), which in turn calls its parent class constructor (`LogicGate`).

전에 썼던것처럼 생성자의 첫줄은 부모클래스인 이항연산자클래스의 생성자를 호출할것이고 차례로 그 부모인 논리게이트 생성자를 호출할 것이다. 

 Note that the `AndGate` class does not provide any new data since it inherits two input lines, one output line, and a label.

AND게이트는 두개의 인풋라인, 하나의 결과라인 그리고 라벨 외에 새로운 데이터를 받지 못했다.

**Listing 11**

    class AndGate(BinaryGate):
    
        def __init__(self,n):
            BinaryGate.__init__(self,n)
    
        def performGateLogic(self):
    
            a = self.getPinA()
            b = self.getPinB()
            if a==1 and b==1:
                return 1
            else:
                return 0

The only thing `AndGate` needs to add is the specific behavior that performs the boolean operation that was described earlier. 

AND게이트가 필요한 유일한 것은 이전에 설명했던 불의연산을 수행하는 특정기능을 추가하는것이다.

This is the place where we can provide the `performGateLogic` method. 

여기가  `performGateLogic` 를 제공할 시점이다.

For an AND gate, this method first must get the two input values and then only return 1 if both input values are 1. 

AND게이트에서는 꼭 두개의 인풋을 받고 두 인풋이 모두1일때만 1을 반환한다.

The complete class is shown in [Listing 11](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-andgateclass).

완성된 클래스가 11에 있다. 

We can show the `AndGate` class in action by creating an instance and asking it to compute its output. 

우리는 인스턴스를 생성하고 결과를 계산하게 요청해서 AND게이트의 동작을 확인할 수 있다. 

The following session shows an `AndGate` object, `g1`, that has an internal label `"G1"`. 

AND게이트 객체인 g1은 내부적으로 G1이라는 라벨을 가지고 있다.

When we invoke the `getOutput` method, the object must first call its `performGateLogic` method which in turn queries the two input lines.

우리가 getOutput메서드를 호출하면 객체는 두개의 인풋라인을 요구하는   `performGateLogic` 함수를 먼저 호출한다.

 Once the values are provided, the correct output is shown.

값이 제공되면 정확한 결과가 보인다. 

    >>> g1 = AndGate("G1")
    >>> g1.getOutput()
    Enter Pin A input for gate G1-->1
    Enter Pin B input for gate G1-->0
    0

The same development can be done for OR gates and NOT gates.

OR , NOT게이트도 같은 방식으로 구현할 수 있다. 

 The `OrGate` class will also be a subclass of `BinaryGate` and the `NotGate` class will extend the `UnaryGate` class. 

OR게이트는 마찬가지로 이항게이트의 자식클래스일것이고 NOT게이트는 단항게이트 클래스의 자식일것이다.

Both of these classes will need to provide their own `performGateLogic` functions, as this is their specific behavior.

이 두 클래스들도 그들 고유의 기능을 제공하는  `performGateLogic` 가 필요하다.

We can use a single gate by first constructing an instance of one of the gate classes and then asking the gate for its output (which will in turn need inputs to be provided). 

우리는 게이트 클래스들 중에서 하나의 게이트 인스턴스를 생성해서 그것에게 결과를 요청할 수있다. (그러기 위해선 인풋값을 필요로 한다.)

For example:

예를들어

    >>> g2 = OrGate("G2")
    >>> g2.getOutput()
    Enter Pin A input for gate G2-->1
    Enter Pin B input for gate G2-->1
    1
    >>> g2.getOutput()
    Enter Pin A input for gate G2-->0
    Enter Pin B input for gate G2-->0
    0
    >>> g3 = NotGate("G3")
    >>> g3.getOutput()
    Enter Pin input for gate G3-->0
    1

Now that we have the basic gates working, we can turn our attention to building circuits. 

이제 우린 기본적인 게이트들의 동작을 알았고 이젠 회로를 만드는게 집중해보자. 

In order to create a circuit, we need to connect gates together, the output of one flowing into the input of another. 

회로를 만들기 위해 게이트들을 연결해서 결과물이 다른게이트의 인풋이 되게 해야한다.

To do this, we will implement a new class called `Connector`.

그러기 위해 연결자라고 불리는 새로운 클래스를 구현할 것이다. 

The `Connector` class will not reside in the gate hierarchy.

연결자 클래스는 게이트 계층에 포함되지 않는다. 

 It will, however, use the gate hierarchy in that each connector will have two gates, one on either end (see [Figure 12](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#fig-connector)). 

그러나, 각 연결자는 양 끝에 하나씩 두개의 게이트를 다는데 게이트계층을 사용할것이다. 

This relationship is very important in object-oriented programming. 

이 관계를 객체지향 프로그래밍에서 매우 중요하다. 

It is called the **HAS-A Relationship**. 

**HAS-A 관계라고 부른다.**

Recall earlier that we used the phrase “IS-A Relationship” to say that a child class is related to a parent class, for example `UnaryGate` IS-A `LogicGate`.

앞서서 언급한 단항게이트 IS-A 논리 게이트 같이 자식클래스는 부모클래스와 연관있다는 IS-A관계를 기억해 봐라.

![](http://interactivepython.org/courselib/static/pythonds/_images/connector.png)

Now, with the `Connector` class, we say that a `Connector` HAS-A `LogicGate` meaning that connectors will have instances of the `LogicGate` class within them but are not part of the hierarchy. 

이제 연결자 클래스를 통해서 연결자가 로직게이트를 '가지고'있다는것의 의미가 연결자 내부에 논리게이트의 인스터스를 가지고 있지만 그것은 계층구조가 아니라고 할 수 잇다. 

When designing classes, it is very important to distinguish between those that have the IS-A relationship (which requires inheritance) and those that have HAS-A relationships (with no inheritance).

클래스를 만들때 IS-A(상속필요) 와 HAS-A(상속불필요) 간이 차이를 구분하는것은 매우 중요하다. 

[Listing 12](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-connectorclass) shows the `Connector` class. 

12는 연결자 클래스를 보여준다. 

The two gate instances within each connector object will be referred to as the `fromgate` and the `togate`, recognizing that data values will “flow” from the output of one gate into an input line of the next.

하나의 연결자 내부의 두개의 게이트 객체는 fromGate, toGate로 불리는데 한 게이트의 결과물이 다음 게이트의 인풋으로 흐르는걸 알 수 있다. 

 The call to `setNextPin` is very important for making connections (see [Listing 13](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-setpin)).

 `setNextPin` 를 호출하는것은 연결을 만드는데 있어 매우 중요하다. 

 We need to add this method to our gate classes so that each `togate` can choose the proper input line for the connection.

우린 게이트 클래스에 이 메서드를 추가해서 togate가 연결에서 적당한 input라인을 고르게 해야한다.

**Listing 12**

    class Connector:
    
        def __init__(self, fgate, tgate):
            self.fromgate = fgate
            self.togate = tgate
    
            tgate.setNextPin(self)
    
        def getFrom(self):
            return self.fromgate
    
        def getTo(self):
            return self.togate

In the `BinaryGate` class, for gates with two possible input lines, the connector must be connected to only one line. 

두개의 인풋라인이 가능한 이항게이트 클래스에서 연결자는 꼭 한 라인에만 연결되야 한다.

If both of them are available, we will choose `pinA` by default. 

두개가 가능하면 우리는 pinA를 기본으로 선택한다.

If `pinA` is already connected, then we will choose `pinB`.

pinA가 이미 연결됐다면 pinB를 선택한다.

 It is not possible to connect to a gate with no available input lines.

사용가능한 인풋라인이 없는 게이트에 연결하는건 불가능하다.

**Listing 13**

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
               raise RuntimeError("Error: NO EMPTY PINS")

Now it is possible to get input from two places: externally, as before, and from the output of a gate that is connected to that input line. 

이제 두곳에서 인풋을 받기 가능해졌다 : 외부에서 그리고 게이트의 아웃픗으로 부터 인풋라인에 연결된다.

This requires a change to the `getPinA` and `getPinB` methods (see [Listing 14](http://interactivepython.org/courselib/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-newgetpin)). 

getPinA, getPinB함수에 수정이 필요하다.(14참고)

If the input line is not connected to anything (`None`), then ask the user externally as before. 

인풋라인에 아무것도 연결되지 않았으면 전처럼 사용자에게 입력받는다.

However, if there is a connection, the connection is accessed and `fromgate`’s output value is retrieved. 

단, 접속이 있으면 접속하여 from게이트의 출력값을 이 된다.

This in turn causes that gate to process its logic. 

그것은 결국 게이트가 로직을 처리하게 만든다. 

This continues until all input is available and the final output value becomes the required input for the gate in question. 

모든 인풋이 사용가능하고 최종결과값이 게이트의 필요한 입력값이 될때 까지 계속된다.

In a sense, the circuit works backwards to find the input necessary to finally produce output.

즉  회로는 최종결과값을 산출하기 위한 입력값을 찾기위해 앞에서 뒤로 동작한다. 

**Listing 14**

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getName()+"-->")
        else:
            return self.pinA.getFrom().getOutput()

The following fragment constructs the circuit shown earlier in the section:

다음은 이 장 초반에 다뤘던 회로를 구성한것이다.

    >>> g1 = AndGate("G1")
    >>> g2 = AndGate("G2")
    >>> g3 = OrGate("G3")
    >>> g4 = NotGate("G4")
    >>> c1 = Connector(g1,g3)
    >>> c2 = Connector(g2,g3)
    >>> c3 = Connector(g3,g4)

The outputs from the two AND gates (`g1` and `g2`) are connected to the OR gate (`g3`) and that output is connected to the NOT gate (`g4`). 

g1 ,g2 두 AND게이트의 결과물은 OR게이트( g3)에 연결되고 그 결과문은 NOT게이트 g4에 연결된다.

The output from the NOT gate is the output of the entire circuit. For example:

NOT게이트의 결과물은 이 회로 전체의 결과물이다. 예를들어 :

    **>>>** g4.getOutput()
    Pin A input for gate G1-->0
    Pin B input for gate G1-->1
    Pin A input for gate G2-->1
    Pin B input for gate G2-->1
    0

Try it yourself using ActiveCode 4.

**Self Check**

Create a two new gate classes, one called NorGate the other called NandGate. 

NOR, Nand 게이트라 ㄹ불리는 두개의 새로운 게이트 클래스를 만들어봐라. 

NandGates work like AndGates that have a Not attached to the output. 

Nand게이트는 결과물에 NOT을 붙인 AND게이트처럼 동작한다.

 NorGates work lake OrGates that have a Not attached to the output.

NOR게이트는 OR게이트 결과에 NOT을 붙인것과 같다. 

Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D). 

게이트들을 만들어서  NOT (( A and B) or (C and D))  가 NOT( A and B ) and NOT (C and D) 와 같다는걸 증명하라.

Make sure to use some of your new gates in the simulation.

너의 게이트를 시뮬레이션에서 사용해라.
# 1.12. Defining Function

The earlier example of procedural abstraction called upon a Python function called sqrt from the math module to compute the square root.

이전 절차적인 추상화 예제에서 제곱근을 구하기위해 math모듈의 sqrt 라는 파이썬 함수를 호출했다. 

 In general, we can hide the details of any computation by defining a function.

일반적으로, 우리는 함수를 정의 함으로서 연산의 세부사항을 숨긴다.

 A function definition requires a name, a group of parameters, and a body. 

함수선언에는 이름, 파라미터들 그리고 본문이 필요하다.

It may also explicitly return a value. 

또한 명시적으로 값을 반환할 수 있다. 

For example, the simple function defined below returns the square of the value you pass into it.

예를들어, 아래에 정의된 간단한 함수는 입력받은 값의 제곱을 반환한다. 

    >>> def square(n):
    ...    return n**2
    ...
    >>> square(3)
    9
    >>> square(square(3))
    81
    >>>

The syntax for this function definition includes the name, square, and a parenthesized list of formal parameters.

이 함수정의 문법에는 square 라는 함수명 괄호 리스트안에 정규 파라미터를 포함하고 있다. 

 For this function, n is the only formal parameter, which suggests that square needs only one piece of data to do its work. 

이 함수에서는 n이 유일한 정규 파라미터인데, 이것은 square는 동작하기 위해 오직 하나의 데이터만이 필요하다는것을 의미한다. 

The details, hidden “inside the box,” simply compute the result of n**2 and return it. 

"박스안에" 순겨진 세부사항이 단순히 n의 제곱을 계산해서 리턴한다. 

We can invoke or call the square function by asking the Python environment to evaluate it, passing an actual parameter value, in this case, 3. 

우리는 파이썬 환경에게 이 함수를 평가를 요청함으로서 실제 파라미터값인, 이경우에선 3인 값을 전달해서 square 함수를  호출할 수 있다.  

Note that the call to square returns an integer that can in turn be passed to another invocation.

square 에서 리턴한 정수는 또 다른 호출에 넘겨질 수 있다는것을 기억해라.

We could implement our own square root function by using a well-known technique called “Newton’s Method.” 

우리는 Newton’s Method 라고 불리는 잘 알려진 기법을 사용해서 우리만의 제곱근 함수를 구현할 수 있다. 

Newton’s Method for approximating square roots performs an iterative computation that converges on the correct value. 

가까운 제곱근을 구하기 위한 Newton’s Method 는 정확한 값에 수렴하는 반복연산을 수행한다. 

The equation newguess=12∗(oldguess+noldguess) takes a value n and repeatedly guesses the square root by making each newguess the oldguess in the subsequent iteration. 

그 연산은 n값을 받아서 각 newguess를 바로 다음 반복의  oldguess로 만들면서 반복적으로 제곱근을 추정한다.

The initial guess used here is n/2. 

여기서 초기추정으로 사용된건 n/2이다.

Listing 1 shows a function definition that accepts a value n and returns the square root of n after making 20 guesses.

Listing 1  은  변수n을 받아서 20번의 추정을 거친 뒤 제곱근을 반환하는 함수의 정의이다.  

 Again, the details of Newton’s Method are hidden inside the function definition and the user does not have to know anything about the implementation to use the function for its intended purpose. 

다시한번, Newton’s Method의 세부사항은 함수정의 내부에 숨겨져있고 사용자는 의도된 목적의 함수를 사용하기 위해선 내부의 구현을 하나도 알 필요가 없다. 

Listing 1 also shows the use of the # character as a comment marker.

Listing 1 은 또한 #문자가 주석으로 사용되는것도 보여준다. 

 Any characters that follow the # on a line are ignored.

해당 라인에서 #뒤로 따라오는 모든 문자는 무시된다.

    def squareroot(n):
        root = n/2    #initial guess will be 1/2 of n
        for k in range(20):
            root = (1/2)*(root + (n / root))
    
        return root

    >>>squareroot(9)
    3.0
    >>>squareroot(4563)
    67.549981495186216
    >>>

셀프체크

Here’s a self check that really covers everything so far. 

여기 지금까지 다뤘던 모든걸 아우르는 셀프체크이다. 

You may have heard of the infinite monkey theorem? 

무한 원숭이 법칙을 들어봤는가? 

The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. 

그 이론은 원숭이가 키보드자판을 무한한 시간동안 무작위로 두드렸을때 , 거의 확실하게 윌리엄 셰익스피어의 작품 같은 주어진 글을 칠수 있다는 것이다. 

Well, suppose we replace a monkey with a Python function. 

이 원숭이를 파이썬 함수로 대체한다고 가정해보자. 

How long do you think it would take for a Python function to generate just one sentence of Shakespeare? 

파이썬 함수가 셰익스피어의 딱 한 문장을 만드는데 얼마나 걸릴것 같은가?

The sentence we’ll shoot for is: “methinks it is like a weasel”

우리가 도전해볼 문장은 “methinks it is like a weasel” 이다. 

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE.

너는 이 브라우저 내에서 이걸 동작해보는걸 원치 않을거니 너가 제일 좋아하는 파이썬 IDE를 열어라.

 The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. 

우리가 이것을 해볼 방법은 알파벳26글자+공백 중 무작위로 글자를 골라서  총 27 자리 문자열을 생성하는 함수를 작성하는것이다.

We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

우린 목표와 생성된 문자열을 비교해  점수를 매기는 또다른 함수도 작성할 것이다. 

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. 

세번째로 반복적으로 생성과 점수 함수를 호출해서 100% 일치한 글자이면 끝나는 함수다.

If the letters are not correct then we will generate a whole new string.

만약 문자열이 틀리면 완전 새로운 문자열을 생성한다.

To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.

너의 프로그램의 진행을 따라기기 쉽게 하기 위해서, 이 세번째 함수는 1000번의 시도 마다 가장 잘 생성된 문자열을 출력한다. 

**Self Check Challenge 셀프체크 도전** 

See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. 

지금까지의 최고의 문자열에서 맞는 다른 글자는 유지하고 한 문자만 변경하는 방식으로 너의 프로그램을 발전시킬수 있는지 봐라.

This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.

이것은 이전 보다 나은 결과일때만 결과를 유지하는 hill climbing 알고리즘 같은 유형이다
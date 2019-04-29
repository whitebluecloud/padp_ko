def gcd(m, n):
    m = abs(m)
    n = abs(n)

    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:
    def __init__(self, top, bottom):
        # Exercise 5
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError()

        # Exercise 6
        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)

        elif bottom < 0:
            top = -top
            bottom = abs(bottom)

        # Exercise 2
        common = gcd(top, bottom)

        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    # Exercise 3
    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    # Exercise 4
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum >= secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum <= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum != secondnum

    # Exercise 7
    def __radd__(self, other):  # right-side add
        return self.__add__(other)

    # Exercise 8
    def __iadd__(self, other):  # 
        return self.__add__(other)

    # Exercise 1
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)

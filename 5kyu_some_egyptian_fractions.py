from fractions import *
import math
def decompose(n):
    # Egyptian Fraction using Fibonacci's algorithm
    if n.split('/')[0] == '0':
        return []

    decomposed = []

    if Fraction(n).denominator == 1:
        return [str(Fraction(n).numerator)]

    n = Fraction(n)
    #print(n)
    numerator = n.numerator
    denominator = n.denominator

    if denominator == 0 or numerator < 0:
        raise ValueError

    if numerator > denominator:
        wholeNum = int(numerator/denominator)

        decomposed.append(str(wholeNum))
        numerator -= denominator * wholeNum

        if numerator % denominator == 0:
            return decomposed

    fraction = Fraction(numerator, denominator)

    startDen = 0

    while fraction.numerator != Fraction(0):
            # denominator of the largest fraction you can subtract from
            # a fraction is d = ceil(denominator / numerator)
            # e.g. 4/5 -> ceil(5/4) = ceil(1.25) = 2 -> 1/2
            startDen = math.ceil(fraction.denominator / fraction.numerator)
            fraction -= Fraction(1,startDen)
            decomposed.append('1/' + str(startDen))


    return decomposed

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(decompose('0'), [])
        test.assert_equals(decompose('3/4'), ["1/2", "1/4"])
        test.assert_equals(decompose('4/5'), ["1/2", "1/4", "1/20"])
        test.assert_equals(decompose('0.66'), ["1/2", "1/7", "1/59", "1/5163", "1/53307975"])
        test.assert_equals(decompose('75/3'), ["25"])
def make_negative( number ):
    return -(abs(number))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(make_negative(42), -42)
        test.assert_equals(make_negative(-9), -9)
        test.assert_equals(make_negative(0), 0)
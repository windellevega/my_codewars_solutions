def reverse_number(n):
    if n < 0:
        return -int(str(abs(n))[::-1])
    return int(str(abs(n))[::-1])

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_number(123), 321)
        test.assert_equals(reverse_number(-123), -321, 'Negative Numbers should be preserved')
        test.assert_equals(reverse_number(1000), 1)
        test.assert_equals(reverse_number(4321234), 4321234)
        test.assert_equals(reverse_number(5), 5)
        test.assert_equals(reverse_number(0), 0)
        test.assert_equals(reverse_number(98989898), 89898989)

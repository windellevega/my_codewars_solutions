def high_and_low(numbers):
    numbers = [int(n) for n in numbers.split(' ')]
    return str(max(numbers)) + ' ' + str(min(numbers))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
        test.assert_equals(high_and_low("1 -1"), "1 -1");
        test.assert_equals(high_and_low("1 1"), "1 1");
        test.assert_equals(high_and_low("-1 -1"), "-1 -1");
        test.assert_equals(high_and_low("1 -1 0"), "1 -1");
        test.assert_equals(high_and_low("1 1 0"), "1 0");
        test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
        test.assert_equals(high_and_low("42"), "42 42");
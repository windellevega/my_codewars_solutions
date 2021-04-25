def basic_op(operator, value1, value2):
    switcher = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }

    return switcher.get(operator)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(basic_op('+', 4, 7), 11)
        test.assert_equals(basic_op('-', 15, 18), -3)
        test.assert_equals(basic_op('*', 5, 5), 25)
        test.assert_equals(basic_op('/', 49, 7), 7)
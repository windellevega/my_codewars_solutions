def add_binary(a,b):
    return bin(a + b).replace('0b', '')

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(add_binary(1, 1), "10")
        test.assert_equals(add_binary(0, 1), "1")
        test.assert_equals(add_binary(1, 0), "1")
        test.assert_equals(add_binary(2, 2), "100")
        test.assert_equals(add_binary(51, 12), "111111")
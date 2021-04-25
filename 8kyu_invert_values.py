def invert(lst):
    return [x * -1 for x in lst]

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
        test.assert_equals(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
        test.assert_equals(invert([]), [])
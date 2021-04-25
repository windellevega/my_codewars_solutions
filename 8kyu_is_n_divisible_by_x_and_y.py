def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_divisible(3, 2, 2), False)
        test.assert_equals(is_divisible(3, 3, 4), False)
        test.assert_equals(is_divisible(12, 3, 4), True)
        test.assert_equals(is_divisible(8, 3, 4), False)
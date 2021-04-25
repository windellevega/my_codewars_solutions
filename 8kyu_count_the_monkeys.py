def monkey_count(n):
    return [i for i in range(1, n + 1)]

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(monkey_count(5), [1, 2, 3, 4, 5])
        test.assert_equals(monkey_count(3), [1, 2, 3])
        test.assert_equals(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        test.assert_equals(monkey_count(20), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

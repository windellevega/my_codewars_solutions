def get_sum(a, b):
    return sum(range(min([a,b]), max([a, b]) + 1))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_sum(0, 1), 1)
        test.assert_equals(get_sum(0, -1), -1)
        test.assert_equals(get_sum(1, 1), 1)
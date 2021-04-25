def positive_sum(arr):
    sum = 0
    for num in arr:
        if num > 0:
            sum += num

    return sum

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(positive_sum([1, 2, 3, 4, 5]), 15)
        test.assert_equals(positive_sum([1, -2, 3, 4, 5]), 13)
        test.assert_equals(positive_sum([-1, 2, 3, 4, -5]), 9)
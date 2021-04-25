def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(odd_or_even([0, 1, 2]), "odd")
        test.assert_equals(odd_or_even([0, 1, 3]), "even")
        test.assert_equals(odd_or_even([1023, 1, 2]), "even")
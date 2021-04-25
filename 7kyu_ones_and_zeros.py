def binary_array_to_number(arr):
    return int(''.join(str(x) for x in arr), 2)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(binary_array_to_number([0, 0, 0, 1]), 1)
        test.assert_equals(binary_array_to_number([0, 0, 1, 0]), 2)
        test.assert_equals(binary_array_to_number([1, 1, 1, 1]), 15)
        test.assert_equals(binary_array_to_number([0, 1, 1, 0]), 6)

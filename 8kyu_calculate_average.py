def find_average(numbers):
    return sum(numbers) / len(numbers)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_average([1, 2, 3]), 2)
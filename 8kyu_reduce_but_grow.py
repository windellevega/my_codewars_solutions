from functools import reduce
def grow(arr):
    return reduce((lambda x, y: x * y), arr)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            [6, [1, 2, 3]],
            [16, [4, 1, 1, 1, 4]],
            [64, [2, 2, 2, 2, 2, 2]],
        ]

        for exp, inp in tests:
            test.assert_equals(grow(inp), exp)
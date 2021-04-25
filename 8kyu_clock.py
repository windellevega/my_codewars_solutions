def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(past(0, 1, 1), 61000)
        test.assert_equals(past(1, 1, 1), 3661000)
        test.assert_equals(past(0, 0, 0), 0)
        test.assert_equals(past(1, 0, 1), 3601000)
        test.assert_equals(past(1, 0, 0), 3600000)
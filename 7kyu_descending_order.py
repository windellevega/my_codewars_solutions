def descending_order(num):
    if num < 10:
        return num
    num = str(num)
    num = list(num)
    num = sorted(num, reverse=True)
    return int(''.join(num))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(descending_order(0), 0)
        test.assert_equals(descending_order(15), 51)
        test.assert_equals(descending_order(123456789), 987654321)
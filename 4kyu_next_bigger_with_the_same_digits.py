import itertools
def next_bigger(number):
    digits = list(str(number))

    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            temp = digits[i:]
            m = min(filter(lambda x: x > temp[0], temp))
            temp.remove(m)
            temp.sort()
            digits[i:] = [m] + temp
            return int("".join(digits))
    return -1

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(next_bigger(12), 21)
        test.assert_equals(next_bigger(513), 531)
        test.assert_equals(next_bigger(2017), 2071)
        test.assert_equals(next_bigger(414), 441)
        test.assert_equals(next_bigger(144), 414)
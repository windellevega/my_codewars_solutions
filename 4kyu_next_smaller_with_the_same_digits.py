def next_smaller(number):
    digits = list(str(number))
    i = j = len(digits) - 1
    while i > 0 and digits[i - 1] <= digits[i]:
        i -= 1
    if i <= 0:
        return -1
    while digits[j] >= digits[i - 1]:
        j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = reversed(digits[i:])
    if digits[0] == '0':
        return -1
    return int(''.join(digits))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(next_smaller(907), 790)
        test.assert_equals(next_smaller(531), 513)
        test.assert_equals(next_smaller(135), -1)
        test.assert_equals(next_smaller(2071), 2017)
        test.assert_equals(next_smaller(414), 144)
        test.assert_equals(next_smaller(123456798), 123456789)
        test.assert_equals(next_smaller(123456789), -1)
        test.assert_equals(next_smaller(1234567908), 1234567890)
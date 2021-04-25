import math
def buddy(start, limit):
    sums = []

    for i in range(start, limit):
        sumn = get_sum_divisors(i)
        if sumn > i + 1:
            summ = get_sum_divisors(sumn - 1)
            if i == summ - 1:
                return [i, sumn - 1]

    return 'Nothing'

def get_sum_divisors(n):
    sum = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            if n / i == i:
                sum += i
            else:
                sum += i + n / i
    return int(sum - n)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(buddy(10, 50), [48, 75])
        test.assert_equals(buddy(2177, 4357), "Nothing")
        test.assert_equals(buddy(57345, 90061), [62744, 75495])
        test.assert_equals(buddy(1071625, 1103735), [1081184, 1331967])
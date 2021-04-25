def persistence(n):
    #code here
    ctr = 0

    while n >= 10:
        prod = 1
        for d in str(n):
            prod *= int(d)
        n = prod
        ctr += 1

    return ctr

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)
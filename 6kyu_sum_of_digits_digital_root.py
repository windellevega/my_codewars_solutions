def digital_root(n):
    # ...
    #code here
    ctr = 0
    sum = n
    while n >= 10:
        sum = 0
        for d in str(n):
            sum += int(d)
        n = sum
        ctr += 1

    return sum

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)
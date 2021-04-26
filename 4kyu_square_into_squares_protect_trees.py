def decompose(n):
    return decompose_yield(n, n ** 2)

def decompose_yield(n, rem):
    if rem < 0:
        return None
    if rem == 0:
        return []

    i = n - 1
    while i > 0:
        diff = rem - i ** 2
        res = decompose_yield(i, diff)

        if res != None:
            res.append(i)
            return res

        i -= 1

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(decompose(5), [3, 4])
        test.assert_equals(decompose(8), None)
        test.assert_equals(decompose(12), [1, 2, 3, 7, 9])
        test.assert_equals(decompose(11), [1, 2, 4, 10])
        test.assert_equals(decompose(50), [1, 3, 5, 8, 49])
        test.assert_equals(decompose(4502467), [1, 3, 4, 5, 11, 69, 3000, 4502466])
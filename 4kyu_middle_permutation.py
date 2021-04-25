import math

def middle_permutation(string):
    ans, tmp = '', sorted(list(string))
    dividend = math.factorial(len(tmp)) // 2 - 1
    for i in range(len(tmp)):
        perms = math.factorial(len(tmp)) // len(tmp)
        if len(tmp) == 1:
            ans += tmp[0]
            break
        letter = tmp[dividend // perms]
        ans += letter
        tmp.remove(letter)
        dividend -= perms * (dividend // perms)
    return ans

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(middle_permutation("abc"), "bac")
        test.assert_equals(middle_permutation("abcd"), "bdca")
        test.assert_equals(middle_permutation("abcdx"), "cbxda")
        test.assert_equals(middle_permutation("abcdxg"), "cxgdba")
        test.assert_equals(middle_permutation("abcdxgz"), "dczxgba")
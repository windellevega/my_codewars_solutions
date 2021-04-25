def solution(s):
    splits = []

    if len(s) == 1:
        splits.append(s + '_')

    for x in range(0, len(s) - 1, 2):
        splits.append(s[x] + s[x+1])
        if x == len(s) - 3:
            splits.append(s[x + 2] + '_')

    return splits

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(solution('asdf'), ['as', 'df'])
        test.assert_equals(solution('asdfg'), ['as', 'df', 'g_'])
        test.assert_equals(solution('asdfgasd'), ['as', 'df', 'ga', 'sd'])
        test.assert_equals(solution(''), [])
        test.assert_equals(solution('a'), ['a_'])
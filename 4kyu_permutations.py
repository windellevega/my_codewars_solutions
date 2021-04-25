from itertools import permutations as perm


def permutations(string):
    if len(string) == 1:
        return [string]
    string = perm(string)
    perms = []
    for strs in string:
        perms.append(''.join(strs))

    return list(set(perms))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sorted(permutations('a')), ['a']);
        test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
        test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
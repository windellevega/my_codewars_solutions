from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode_rail_fence_cipher(s, n):
    p = rail_pattern(n)

    return ''.join(sorted(s, key=lambda i: next(p)))


def decode_rail_fence_cipher(s, n):
    p = rail_pattern(n)
    indexes = sorted(range(len(s)), key=lambda i: next(p))
    result = [''] * len(s)
    for i, c in zip(indexes, s):
        result[i] = c
    return ''.join(result)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN");
        test.assert_equals(encode_rail_fence_cipher("Hello, World!", 3), "Hoo!el,Wrdl l");
        test.assert_equals(encode_rail_fence_cipher("Hello, World!", 4), "H !e,Wdloollr");
        test.assert_equals(encode_rail_fence_cipher("", 3), "");

        test.assert_equals(decode_rail_fence_cipher("H !e,Wdloollr", 4), "Hello, World!");
        test.assert_equals(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE");
        test.assert_equals(decode_rail_fence_cipher("", 3), "");
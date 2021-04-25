def position(alphabet):
    return 'Position of alphabet: ' + str('abcdefghijklmnopqrstuvwxyz'.index(alphabet.lower()) + 1)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            # [input, expected]
            ["a", "Position of alphabet: 1"],
            ["z", "Position of alphabet: 26"],
            ["e", "Position of alphabet: 5"],
        ]

        for inp, exp in tests:
            test.assert_equals(position(inp), exp)
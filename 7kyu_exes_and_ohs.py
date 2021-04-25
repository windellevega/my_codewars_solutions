def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.expect(xo('xo'), 'True expected')
        test.expect(xo('xo0'), 'True expected')
        test.expect(not xo('xxxoo'), 'False expected')

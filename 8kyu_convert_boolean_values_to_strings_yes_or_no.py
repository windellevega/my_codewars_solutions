def bool_to_word(boolean):
    # TODO
    if boolean:
        return 'Yes'
    return 'No'

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bool_to_word(True), 'Yes')
        test.assert_equals(bool_to_word(False), 'No')
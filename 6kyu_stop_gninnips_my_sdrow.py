def spin_words(sentence):
    return ' '.join([(x[::-1] if len(x) >=5 else x) for x in sentence.split(' ')])

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(spin_words("Welcome"), "emocleW")
def hello(name = None):
    if name == None or name == '':
        return 'Hello, World!'
    return 'Hello, ' + name.title() + '!'

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = (
            ("John", "Hello, John!"),
            ("aLIce", "Hello, Alice!"),
            ("", "Hello, World!"),
        )

        for inp, exp in tests:
            test.assert_equals(hello(inp), exp)

        test.assert_equals(hello(), "Hello, World!")
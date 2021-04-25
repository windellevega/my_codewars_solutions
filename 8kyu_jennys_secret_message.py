def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.describe("Jenny's greeting function")
        test.it("should greet some people normally")
        test.assert_equals(greet("James"), "Hello, James!")
        test.assert_equals(greet("Jane"), "Hello, Jane!")
        test.assert_equals(greet("Jim"), "Hello, Jim!")

        test.it("should greet Johnny a little bit more special")
        test.assert_equals(greet("Johnny"), "Hello, my love!")
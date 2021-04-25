def find_short(s):
    # your code here
    s = s.split(' ')
    return len(min((word for word in s if word), key=len))

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
            test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
            test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
            test.assert_equals(find_short("lets talk about javascript the best language"), 3)
            test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
            test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
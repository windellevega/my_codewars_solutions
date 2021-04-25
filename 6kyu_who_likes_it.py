def likes(names):
    length = len(names)
    if length == 0:
        return "no one likes this"
    elif length == 1:
        return names[0] + " likes this"
    elif length == 2:
        return names[0] + " and " + names[1] + " like this"
    elif length == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(length - 2) + " others like this"

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(likes([]), 'no one likes this')
        test.assert_equals(likes(['Peter']), 'Peter likes this')
        test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
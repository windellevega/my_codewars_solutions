def create_phone_number(n):
    phoneNumber = '('

    for x in range(len(n)):
        phoneNumber += str(n[x])
        if x == 2:
            phoneNumber += ') '
        elif x == 5:
            phoneNumber += '-'

    return phoneNumber

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
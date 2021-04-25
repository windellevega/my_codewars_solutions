def abbrev_name(name):
    name = name.split(' ')
    return name[0][0].upper() + '.' + name[1][0].upper()

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(abbrev_name("Sam Harris"), "S.H")
        test.assert_equals(abbrev_name("Patrick Feenan"), "P.F")
        test.assert_equals(abbrev_name("Evan Cole"), "E.C")
        test.assert_equals(abbrev_name("P Favuzzi"), "P.F")
        test.assert_equals(abbrev_name("David Mendieta"), "D.M")
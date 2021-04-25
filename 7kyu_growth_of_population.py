def nb_year(population, percent, additional, target):
    #code here
    percent = percent / 100
    ctr = 0
    while population < target:
        population += population * percent
        population += additional
        population = int(population)
        ctr += 1

    return ctr

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
        test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
        test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)
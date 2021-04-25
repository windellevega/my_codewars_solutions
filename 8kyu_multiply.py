def multiply(a, b):
  return a * b

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(multiply(2,1), 2)
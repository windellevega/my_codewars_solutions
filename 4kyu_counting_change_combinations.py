def count_change(money, coins):
    combinations = [0] * (money + 1)
    combinations[0] = 1
    for coin in coins:
        for j in range(coin, money + 1):
            combinations[j] += combinations[j - coin]
    return combinations[money]

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(3, count_change(4, [1, 2]))
        test.assert_equals(4, count_change(10, [5, 2, 3]))
        test.assert_equals(0, count_change(11, [5, 7]))
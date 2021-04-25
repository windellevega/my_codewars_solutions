def sum_for_list(lst):
    primeList = []
    finalList = []

    for n in lst:
        primeList = list(set(primeList).union(set(prime_factors(n))))

    primeList.sort()

    for n in primeList:
        sum = 0
        listN = [n]
        for m in lst:
            if m % n == 0:
                sum = sum + m

        listN.append(sum)

        finalList.append(listN)

    return finalList


def prime_factors(n):
    i = 2
    n = abs(n)
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        a = [12, 15]
        test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

        a = [15, 21, 24, 30, 45]
        test.assert_equals(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])
def snail(snail_map):
    n = len(snail_map)

    if snail_map == [[]]:
        return []

    path = []
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    direction = 0

    while (top <= bottom and left <= right):
        if direction == 0:
            for i in range(left, right + 1):
                path.append(snail_map[top][i])
            top += 1
            direction = 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                path.append(snail_map[i][right])
            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right, left - 1, -1):
                path.append(snail_map[bottom][i])
            bottom -= 1
            direction = 3

        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                path.append(snail_map[i][left])
            left += 1
            direction = 0
    return path

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        test.assert_equals(snail(array), expected)

        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test.assert_equals(snail(array), expected)

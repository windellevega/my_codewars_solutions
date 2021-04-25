sum = 0
DIRECT = {'A': set('BFEHD'), 'B': set('ACFIEGD'), 'C': set('BFHED'), 'D': set('ABCEIHG'),
          'E': set('ABCDFGHI'), 'F': set('ABCEGHI'), 'G': set('DBEFH'),
          'H': set('GDAECFI'), 'I': set('HDEBF')}
OVER = {'A': {'B': 'C', 'E': 'I', 'D': 'G'}, 'B': {'E': 'H'}, 'C': {'B': 'A', 'E': 'G', 'F': 'I'}, 'D': {'E': 'F'},
        'F': {'E': 'D'}, 'G': {'D': 'A', 'E': 'C', 'H': 'I'}, 'G': {'D': 'A', 'E': 'C', 'H': 'I'},
        'H': {'E': 'B'}, 'I': {'H': 'G', 'E': 'A', 'F': 'C'}, 'E': {}}

def re(count, point, element, path):
    global sum
    element = element.replace(point, '')

    if count == 0:
        sum += 1
    else:
        for i in DIRECT[point]:
            if i in element:
                re(count - 1, i, element, path + i)
            else:
                if i in OVER[point] and OVER[point][i] in element:
                    re(count - 1, OVER[point][i], element, path + point)

def count_patterns_from(firstPoint, length):

    global sum
    sum = 0
    element = 'ABCDEFGHI'
    if length < 1 or length > 9 or firstPoint not in element:
        return 0
    else:
        re(length - 1, firstPoint, element, firstPoint)
        return sum

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_patterns_from('A', 10), 0)
        test.assert_equals(count_patterns_from('A', 0), 0)
        test.assert_equals(count_patterns_from('E', 14), 0)
        test.assert_equals(count_patterns_from('B', 1), 1)
        test.assert_equals(count_patterns_from('C', 2), 5)
        test.assert_equals(count_patterns_from('E', 2), 8)
        test.assert_equals(count_patterns_from('E', 4), 256)
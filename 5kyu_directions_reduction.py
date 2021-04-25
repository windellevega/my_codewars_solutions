def dirReduc(arr):
    opposites = ['NORTH,SOUTH', 'SOUTH,NORTH', 'WEST,EAST', 'EAST,WEST', 'NORTH, SOUTH', 'SOUTH, NORTH', 'WEST, EAST',
                 'EAST, WEST']

    arr = ','.join(arr)
    arr = arr.upper()

    # print(directions)

    while True:
        arr = arr.replace(',,', ',')
        check = 0
        for opposite in opposites:
            if opposite in arr:
                arr = arr.replace(opposite, '')
                arr = arr.replace(',,', ',')
                check += 1

        if check == 0:
            # print(directions)
            arr = arr.rstrip(',')
            arr = arr.lstrip(',')
            if arr == '':
                return []
            return arr.split(',')

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        test.assert_equals(dirReduc(a), ['WEST'])
        u = ["NORTH", "WEST", "SOUTH", "EAST"]
        test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
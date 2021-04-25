def maskify(card_number):
    temp = ''
    if(len(card_number) < 4):
        return card_number
    for i in range(0, len(card_number) - 4):
        temp += '#'
    return temp + card_number[len(card_number) - 4:len(card_number)]

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        cc = ''
        r = maskify(cc)
        test.describe("masking: {0}".format(cc))
        test.it("{0}  matches  {1}".format(cc, r))
        test.assert_equals(r, cc)

        cc = '123'
        r = maskify(cc)
        test.describe("masking: {0}".format(cc))
        test.it("{0}  matches  {1}".format(cc, r))
        test.assert_equals(r, cc)

        cc = 'SF$SDfgsd2eA'
        r = maskify(cc)
        test.describe("masking: {0}".format(cc))
        test.it("{0}  matches  {1}".format('########d2eA', r))
        test.assert_equals(r, '########d2eA')
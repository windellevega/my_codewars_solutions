def remove_consecutive_duplicates(string):
    str_arr = string.split(' ')
    ulist = [str_arr[0]]
    temp = str_arr[0]
    for word in str_arr:
        if temp != word:
            ulist.append(word)
            temp = word

    return ' '.join(ulist)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_consecutive_duplicates(
            'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'),
                           'alpha beta gamma delta alpha beta gamma delta');
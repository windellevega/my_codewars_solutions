def pig_it(text):
    text = text.split(' ')
    result = []
    for i in text:
        if i in ['.', '!', '?']:
            result.append(i)
        else:
            result.append(i[1:len(i)] + i[0] + 'ay')
    return ' '.join(result)

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        test.assert_equals(pig_it('This is my string'), 'hisTay siay ymay tringsay')
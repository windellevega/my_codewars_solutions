def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    startPos = alphabet.find(chars[0].lower())

    for char in chars:
        if char.lower() != alphabet[startPos]:
            if char.isupper():
                return alphabet[startPos].upper()
            else:
                return alphabet[startPos]
        startPos += 1

    return ''

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.describe("kata tests")
        test.it("example tests")
        test.assert_equals(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        test.assert_equals(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')

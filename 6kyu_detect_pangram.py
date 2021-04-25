import string

def is_pangram(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for l in s:
        if l.lower() in alphabet:
            alphabet.remove(l.lower())
    if len(alphabet) == 0:
           return True
    return False

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        pangram = "The quick, brown fox jumps over the lazy dog!"
        test.assert_equals(is_pangram(pangram), True)
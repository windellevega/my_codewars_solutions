import re
def validate_pin(pin):
    if re.match('^\d{4}\Z', pin) or re.match('^\d{6}\Z', pin):
        return True
    return False

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(validate_pin("1"), False, "Wrong output for '1'")
        test.assert_equals(validate_pin("12"), False, "Wrong output for '12'")
        test.assert_equals(validate_pin("123"), False, "Wrong output for '123'")
        test.assert_equals(validate_pin("12345"), False, "Wrong output for '12345'")
        test.assert_equals(validate_pin("1234567"), False, "Wrong output for '1234567'")
        test.assert_equals(validate_pin("-1234"), False, "Wrong output for '-1234'")
        test.assert_equals(validate_pin("-12345"), False, "Wrong output for '-12345'")
        test.assert_equals(validate_pin("1.234"), False, "Wrong output for '1.234'")
        test.assert_equals(validate_pin("00000000"), False, "Wrong output for '00000000'")

    @test.it("should return False for pins which contain characters other than digits")
    def _():
        test.assert_equals(validate_pin("a234"), False, "Wrong output for 'a234'")
        test.assert_equals(validate_pin(".234"), False, "Wrong output for '.234'")

    @test.it("should return True for valid pins")
    def _():
        test.assert_equals(validate_pin("0000"), True, "Wrong output for '0000'")
        test.assert_equals(validate_pin("1111"), True, "Wrong output for '1111'")
        test.assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("098765"), True, "Wrong output for '098765'")
        test.assert_equals(validate_pin("000000"), True, "Wrong output for '000000'")
        test.assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
        test.assert_equals(validate_pin("090909"), True, "Wrong output for '090909'")
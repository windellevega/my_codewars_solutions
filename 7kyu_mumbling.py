def accum(sequence):
    if not sequence.isalpha():
        return ""
    ctr = 0
    mumbled = ""
    for char in enumerate(sequence):
        mumbled += char[1].upper()
        for idx in range(ctr):
            mumbled += char[1].lower()
        if char[0] < len(sequence) -1:
            mumbled += "-"
        ctr += 1

    return mumbled

from test_framework import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.describe("Basic tests")

    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(accum("ZpglnRxqenU"),
                           "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        test.assert_equals(accum("NyffsGeyylB"),
                           "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        test.assert_equals(accum("MjtkuBovqrU"),
                           "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
        test.assert_equals(accum("EvidjUnokmM"),
                           "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
        test.assert_equals(accum("HbideVbxncC"),
                           "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")